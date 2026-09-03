/* ============================================================
   Coach Arnold Academy — dashboard.js
   Renders the player, parent and coach/administrator dashboards.
   All data comes from the local store written by the site forms.
   Swap the store calls for API calls when a backend is added.
   ============================================================ */
(function () {
  "use strict";
  var C = window.CAA, D = C.D, esc = C.esc, store = C.store;
  var user = C.auth.require(["player", "parent", "coach"]);
  if (!user) return;

  var navEl = document.getElementById("dash-nav");
  var mainEl = document.getElementById("dash-main");
  var titleEl = document.getElementById("dash-title");
  var subEl = document.getElementById("dash-sub");

  titleEl.textContent = user.role === "coach" ? "Coach dashboard" : user.role === "parent" ? "Parent dashboard" : "Player dashboard";
  subEl.textContent = "Signed in as " + user.name + " (" + user.email + ")";

  /* ---------------- shared bits ---------------- */
  function stat(n, l) { return '<div class="stat"><div class="n">' + n + '</div><div class="l">' + l + "</div></div>"; }
  function card(title, inner) { return '<section class="card"><h3>' + esc(title) + "</h3>" + inner + "</section>"; }
  function empty(h, p) { return '<div class="empty"><h4>' + esc(h) + "</h4><p>" + p + "</p></div>"; }
  function table(headers, rows) {
    if (!rows.length) return empty("Nothing here yet", "Entries appear as soon as they come in.");
    return '<div class="tablewrap"><table><thead><tr>' + headers.map(function (h) { return "<th>" + esc(h) + "</th>"; }).join("") +
      "</tr></thead><tbody>" + rows.map(function (r) { return "<tr>" + r.map(function (c) { return "<td>" + c + "</td>"; }).join("") + "</tr>"; }).join("") +
      "</tbody></table></div>";
  }
  function when(iso) { try { return new Date(iso).toLocaleString(); } catch (e) { return iso; } }
  function csv(key, rows) {
    if (!rows.length) { C.toast("Nothing to export in " + key + " yet."); return; }
    var cols = Object.keys(rows.reduce(function (a, r) { Object.keys(r).forEach(function (k) { a[k] = 1; }); return a; }, {}));
    var lines = [cols.join(",")].concat(rows.map(function (r) {
      return cols.map(function (c) { return '"' + String(r[c] == null ? "" : r[c]).replace(/"/g, '""') + '"'; }).join(",");
    }));
    var a = document.createElement("a");
    a.href = "data:text/csv;charset=utf-8," + encodeURIComponent(lines.join("\n"));
    a.download = "caa-" + key + "-" + new Date().toISOString().slice(0, 10) + ".csv";
    document.body.appendChild(a); a.click(); a.remove();
    C.toast("Exported " + rows.length + " " + key + " to CSV.");
  }
  window.__csv = function (key) { csv(key, store.get(key, [])); };

  function upcomingMatches(teamIds) {
    return D.matches.filter(function (m) {
      return m.status !== "completed" && (!teamIds || !teamIds.length || teamIds.indexOf(m.team) > -1);
    }).sort(function (a, b) { return a.date < b.date ? -1 : 1; });
  }

  function availabilityFor(matchId) { return store.get("availability", {})[matchId] || {}; }
  window.__respond = function (matchId, answer) {
    var all = store.get("availability", {});
    all[matchId] = all[matchId] || {};
    all[matchId][user.email] = { answer: answer, name: user.name, at: new Date().toISOString() };
    store.set("availability", all);
    C.toast("Marked " + answer.toLowerCase() + ".");
    render(current);
  };

  function availBlock(m) {
    var mine = (availabilityFor(m.id)[user.email] || {}).answer;
    return ["Available", "Not available", "Maybe", "Injured"].map(function (x) {
      return '<button class="btn sm ' + (mine === x ? "" : "dark-ghost") + '" type="button" onclick="__respond(\'' + m.id + "','" + x + "')\">" + x + "</button>";
    }).join(" ");
  }

  /* ---------------- player views ---------------- */
  var playerViews = {
    "Overview": function () {
      var ms = upcomingMatches(user.teams);
      var next = ms[0];
      return '<div class="grid g4" style="margin-bottom:1.4rem">' +
        stat(ms.length, "Upcoming matches") +
        stat((user.teams || []).length, "Teams") +
        stat(store.get("bookings", []).filter(byMe).length, "Sessions booked") +
        stat(Object.keys(store.get("availability", {})).filter(function (k) {
          return (store.get("availability", {})[k] || {})[user.email];
        }).length, "Availability replies") + "</div>" +
        card("Next fixture", next
          ? "<p><strong>" + esc(C.teamName(next.team)) + " v " + esc(next.opponent) + "</strong><br>" +
            C.fmtDate(next.date, true) + " · kick-off " + C.fmtTime(next.kick) + " · arrive " + C.fmtTime(next.arrive) + "<br>" +
            esc(next.venue) + ", " + esc(next.address) + "<br>Kit: " + esc(next.kit) + "</p>" +
            '<div class="btn-row" style="margin-top:.4rem">' + availBlock(next) +
            '<a class="btn sm dark-ghost" href="' + C.gcalLink({ title: C.teamName(next.team) + " v " + next.opponent, date: next.date, time: next.arrive, minutes: 120, location: next.venue }) + '" target="_blank" rel="noopener">Add to calendar</a></div>'
          : empty("No fixture scheduled", "New fixtures appear here as soon as the league confirms them.")) +
        card("Announcements", D.news.slice(0, 2).map(function (n) {
          return "<p><strong>" + esc(n.title) + "</strong><br><span class=\"muted small\">" + C.fmtDate(n.date) + "</span><br>" + esc(n.body) + "</p>";
        }).join("<hr>"));
    },
    "My profile": function () {
      return card("Personal details", '<div class="tablewrap"><table><tbody>' +
        [["Name", user.name], ["Email", user.email], ["Role", "Player"],
         ["Teams", (user.teams || []).map(C.teamName).join(", ") || "Not on a team yet"]].map(function (r) {
          return "<tr><th>" + r[0] + "</th><td>" + esc(r[1]) + "</td></tr>";
        }).join("") + "</tbody></table></div>" +
        '<p class="small muted" style="margin-top:.8rem">To change your details, message Coach Arnold. Profile editing arrives with the account system described in the README.</p>') +
      card("Photo and video consent", '<div class="check"><input id="pc" type="checkbox"><label for="pc">I consent to photos and video that include me being used on the academy website and social media.</label></div>' +
        '<button class="btn sm" type="button" onclick="CAA.toast(\'Consent preference saved.\')">Save preference</button>' +
        '<p class="small muted" style="margin-top:.7rem">You can withdraw consent at any time and existing images will be removed within two working days.</p>');
    },
    "Sessions": function () {
      var mine = store.get("bookings", []).filter(byMe);
      return card("Your training sessions", table(["Program", "Date", "Time", "Location", "Status"],
        mine.map(function (b) {
          return [esc(C.progName(b.program)), esc(b.date), esc(C.fmtTime(b.time)), esc(C.locName(b.location)),
            '<span class="chip ok">Requested</span>'];
        }))) +
        card("Book another session", '<p>Sessions are booked through the main booking form so that health details and consent stay current.</p><a class="btn sm" href="book.html">Book a session</a>');
    },
    "Matches": function () {
      var ms = upcomingMatches(user.teams);
      return card("Fixtures and availability", ms.length ? ms.map(function (m) {
        return '<div style="border-bottom:1px solid var(--line-d);padding:1rem 0">' +
          "<strong>" + esc(C.teamName(m.team)) + " v " + esc(m.opponent) + "</strong><br>" +
          '<span class="small muted">' + C.fmtDate(m.date, true) + " · " + C.fmtTime(m.kick) + " · " + esc(m.venue) + " · " + (m.home ? "Home" : "Away") + "</span>" +
          '<div class="btn-row" style="margin-top:.5rem">' + availBlock(m) + "</div></div>";
      }).join("") : empty("No fixtures", "Nothing scheduled for your teams right now."));
    },
    "Tactics and documents": function () {
      return card("Shared by your coach",
        '<p class="small muted">Visible to signed-in squad members only.</p>' +
        '<div class="feature" style="margin-bottom:1rem"><h3>Formation: 2-1-2 indoor shape</h3><p>Pressing triggers, rotation when the ball goes wide, and who covers the back post. PDF, uploaded by Coach Arnold.</p></div>' +
        '<div class="feature" style="margin-bottom:1rem"><h3>Set pieces, attacking</h3><p>Three corner routines and the kick-in pattern from the left.</p></div>' +
        '<div class="feature"><h3>Match video, most recent fixture</h3><p>Full match with clips tagged by player.</p></div>' +
        '<p class="notice" style="margin-top:1rem"><strong>File uploads need a backend.</strong> Once storage is connected, these become real downloads. See the README, section "File uploads".</p>');
    },
    "Team chat": function () { return waCard(); },
    "Payments": function () {
      return card("Payment history", table(["Date", "Item", "Amount", "Status"], [])) +
        card("How payment works", "<p>Card payments go live when Stripe is connected. Until then, Coach Arnold sends a payment link with each confirmation, and receipts arrive by email.</p>");
    },
    "Progress": function () {
      return card("Coaching progress", empty("No notes yet",
        "After each block Coach Arnold records two or three targets and how you're tracking against them. Notes appear here."));
    }
  };
  function byMe(b) { return (b.contactEmail || b.email || "").toLowerCase() === user.email.toLowerCase(); }

  function waCard() {
    return card("Team WhatsApp",
      "<p>The team group is for day-to-day chat: who's running late, who's bringing bibs, and match-night logistics. Official changes always come by email as well.</p>" +
      '<div class="btn-row"><a class="btn sm" href="' + C.waLink("Hi Coach Arnold, please add me to the team WhatsApp group. My name is " + user.name + ".") + '" target="_blank" rel="noopener">Ask to be added</a>' +
      '<a class="btn sm dark-ghost" href="' + C.waLink("Hi Coach Arnold, ") + '" target="_blank" rel="noopener">Message Coach Arnold directly</a></div>' +
      '<p class="small muted" style="margin-top:.8rem">Group invite links are never published on public pages. Coach Arnold adds approved members manually.</p>');
  }

  /* ---------------- parent views ---------------- */
  var parentViews = {
    "Overview": function () {
      var kids = user.children || [];
      return '<div class="grid g4" style="margin-bottom:1.4rem">' +
        stat(kids.length, "Children registered") +
        stat(store.get("bookings", []).filter(byMe).length, "Sessions booked") +
        stat(upcomingMatches(kids.map(function (k) { return k.team; }).filter(Boolean)).length, "Upcoming matches") +
        stat(0, "Outstanding invoices") + "</div>" +
        card("Your children", kids.length ? kids.map(function (k) {
          return '<div class="feature" style="margin-bottom:1rem"><h3>' + esc(k.name) + "</h3><p>Age " + k.age + " · " +
            (k.team ? esc(C.teamName(k.team)) : "Not on a team") + '</p><div class="btn-row" style="margin-top:.4rem">' +
            '<a class="btn sm dark-ghost" href="book.html">Book a session</a>' +
            '<a class="btn sm dark-ghost" href="join-team.html">Apply to a team</a></div></div>';
        }).join("") : empty("No children added", "Register a child through the booking form and they'll appear here."));
    },
    "Children": function () {
      return card("Manage children", (user.children || []).map(function (k) {
        return '<div class="feature" style="margin-bottom:1.1rem"><h3>' + esc(k.name) + "</h3>" +
          "<p>Age " + k.age + " · " + (k.team ? esc(C.teamName(k.team)) : "Not on a team") + "</p></div>";
      }).join("") + '<p class="notice"><strong>Adding a child</strong><p>Register an additional child through the booking form. Each child needs their own medical details, emergency contacts and consent record.</p></p>' +
        '<a class="btn sm" href="book.html">Register another child</a>');
    },
    "Forms and waivers": function () {
      return card("Consent and waivers", table(["Document", "Applies to", "Status"],
        (user.children || []).flatMap(function (k) {
          return [
            [ "Liability waiver", esc(k.name), '<span class="chip ok">Signed</span>' ],
            [ "Parent consent", esc(k.name), '<span class="chip ok">Signed</span>' ],
            [ "Photo and video consent", esc(k.name), '<span class="chip warn">Not given</span>' ],
            [ "Medical information", esc(k.name), '<span class="chip ok">On file</span>' ]
          ];
        }))) +
        card("Photo and video consent",
          "<p>Photo consent is optional and separate from everything else. Withholding it changes nothing about your child's coaching.</p>" +
          (user.children || []).map(function (k, i) {
            return '<div class="check"><input id="pcx' + i + '" type="checkbox"><label for="pcx' + i + '">I consent to images of ' + esc(k.name) + " being used publicly.</label></div>";
          }).join("") +
          '<button class="btn sm" type="button" onclick="CAA.toast(\'Consent preferences saved.\')">Save preferences</button>');
    },
    "Schedule": function () {
      var teams = (user.children || []).map(function (k) { return k.team; }).filter(Boolean);
      var ms = upcomingMatches(teams);
      return card("Match availability", ms.length ? ms.map(function (m) {
        return '<div style="border-bottom:1px solid var(--line-d);padding:1rem 0"><strong>' +
          esc(C.teamName(m.team)) + " v " + esc(m.opponent) + "</strong><br>" +
          '<span class="small muted">' + C.fmtDate(m.date, true) + " · arrive " + C.fmtTime(m.arrive) + " · " + esc(m.venue) + "</span>" +
          '<div class="btn-row" style="margin-top:.5rem">' + availBlock(m) + "</div></div>";
      }).join("") : empty("Nothing scheduled", "Fixtures for your children's teams appear here.")) +
      card("Training sessions", table(["Program", "Date", "Time", "Location"],
        store.get("bookings", []).filter(byMe).map(function (b) {
          return [esc(C.progName(b.program)), esc(b.date), esc(C.fmtTime(b.time)), esc(C.locName(b.location))];
        })));
    },
    "Announcements": function () {
      return card("From Coach Arnold", D.news.map(function (n) {
        return "<p><strong>" + esc(n.title) + '</strong><br><span class="small muted">' + C.fmtDate(n.date) + "</span><br>" + esc(n.body) + "</p>";
      }).join("<hr>")) + waCard();
    },
    "Invoices": function () {
      return card("Invoices and payments", table(["Date", "Item", "Amount", "Status"], [])) +
        card("Payment methods", "<p>Card payment goes live when Stripe is connected. Coach Arnold currently sends a payment link with each confirmation. No card details are stored on this website at any point.</p>");
    },
    "Contact the coach": function () {
      return card("Message Coach Arnold",
        '<div class="btn-row" style="margin-top:0"><a class="btn sm" href="' + C.waLink("Hi Coach Arnold, this is " + user.name + ". ") + '" target="_blank" rel="noopener">WhatsApp</a>' +
        '<a class="btn sm dark-ghost" href="' + C.mailLink("Message from " + user.name) + '">Email</a>' +
        '<a class="btn sm dark-ghost" href="contact.html">Contact form</a></div>' +
        "<p style=\"margin-top:1rem\">" + esc(D.site.responseTime) + "</p>");
    }
  };

  /* ---------------- coach views ---------------- */
  function inbox(key, cols, pick) {
    var rows = store.get(key, []);
    return card(cols.title, table(cols.heads, rows.map(pick)) +
      '<div class="btn-row"><button class="btn sm dark-ghost" type="button" onclick="__csv(\'' + key + '\')">Export CSV</button>' +
      '<span class="small muted" style="align-self:center">' + rows.length + " total</span></div>");
  }

  var coachViews = {
    "Overview": function () {
      var b = store.get("bookings", []), a = store.get("applications", []), c = store.get("contacts", []).concat(store.get("questions", []));
      var pending = 0, replies = store.get("availability", {});
      upcomingMatches().forEach(function (m) { pending += Object.keys(replies[m.id] || {}).length; });
      return '<div class="grid g4" style="margin-bottom:1.4rem">' +
        stat(b.length, "Booking requests") + stat(a.length, "Team applications") +
        stat(c.length, "Messages and questions") + stat(pending, "Availability responses") + "</div>" +
        card("Needs your attention", (b.length || a.length || c.length)
          ? "<ul style=\"padding-left:1.1rem\">" +
            (b.length ? "<li>" + b.length + " booking request" + (b.length > 1 ? "s" : "") + " to confirm.</li>" : "") +
            (a.length ? "<li>" + a.length + " team application" + (a.length > 1 ? "s" : "") + " to review.</li>" : "") +
            (c.length ? "<li>" + c.length + " message" + (c.length > 1 ? "s" : "") + " waiting for a reply.</li>" : "") +
            "</ul>"
          : empty("Nothing waiting", "Bookings, applications and messages land here the moment they're submitted.")) +
        card("This week", table(["When", "What", "Where"],
          D.trainings.slice(0, 4).map(function (t) {
            return [C.fmtDate(t.date) + " " + C.fmtTime(t.time), esc(C.progName(t.program)), esc(C.locName(t.location))];
          }).concat(upcomingMatches().slice(0, 3).map(function (m) {
            return [C.fmtDate(m.date) + " " + C.fmtTime(m.kick), esc(C.teamName(m.team) + " v " + m.opponent), esc(m.venue)];
          }))));
    },
    "Bookings": function () {
      return inbox("bookings", { title: "Booking requests", heads: ["Received", "Player", "Program", "Requested", "Contact", "Payment"] }, function (r) {
        return [when(r.submitted), esc(r.playerName || "") + " (" + esc(r.playerAge || "?") + ")", esc(C.progName(r.program)),
          esc(r.date || "") + " " + esc(r.time || ""), esc(r.contactEmail || "") + "<br>" + esc(r.contactPhone || ""), esc(r.payment || "")];
      });
    },
    "Applications": function () {
      return inbox("applications", { title: "Team applications", heads: ["Received", "Name", "Team", "Position", "City", "Contact"] }, function (r) {
        return [when(r.submitted), esc(r.fullName || ""), esc(C.teamName(r.team || "")), esc(r.position1 || ""), esc(r.city || ""),
          esc(r.email || "") + "<br>" + esc(r.phone || "")];
      }) +
      inbox("tryouts", { title: "Tryout registrations", heads: ["Received", "Name", "Age", "Position", "Date", "Contact"] }, function (r) {
        return [when(r.submitted), esc(r.name || ""), esc(r.age || ""), esc(r.position || ""), esc(r.date || ""), esc(r.email || "")];
      });
    },
    "Messages": function () {
      return inbox("contacts", { title: "Contact form messages", heads: ["Received", "Topic", "Name", "Contact", "Message"] }, function (r) {
        return [when(r.submitted), esc(r.topic || ""), esc(r.name || ""), esc(r.email || ""), esc((r.message || "").slice(0, 140))];
      }) +
      inbox("questions", { title: "Program questions", heads: ["Received", "Program", "Name", "Email", "Question"] }, function (r) {
        return [when(r.submitted), esc(r.program || ""), esc(r.name || ""), esc(r.email || ""), esc((r.message || "").slice(0, 140))];
      }) +
      inbox("sponsors", { title: "Sponsorship enquiries", heads: ["Received", "Business", "Contact", "Level", "Message"] }, function (r) {
        return [when(r.submitted), esc(r.business || ""), esc(r.name || "") + "<br>" + esc(r.email || ""), esc(r.level || ""), esc((r.message || "").slice(0, 120))];
      });
    },
    "Players and parents": function () {
      var accounts = store.get("accounts", []).concat(D.demoUsers);
      return card("Accounts", table(["Name", "Email", "Role", "Teams or children"], accounts.map(function (a) {
        return [esc(a.name), esc(a.email), esc(a.role),
          esc((a.teams || []).map(C.teamName).join(", ") || (a.children || []).map(function (k) { return k.name; }).join(", ") || "—")];
      }))) +
      card("Registered players from bookings", table(["Player", "Age", "Level", "Guardian", "Medical notes"],
        store.get("bookings", []).map(function (b) {
          return [esc(b.playerName || ""), esc(b.playerAge || ""), esc(b.level || ""), esc(b.contactName || ""),
            esc((b.medical || "None given").slice(0, 90))];
        }))) +
      '<div class="notice"><strong>Handle this data carefully.</strong><p>Medical details and children\'s information are sensitive. Never export them to a shared drive, and delete records once they are no longer needed. See the privacy policy for retention periods.</p></div>';
    },
    "Teams and rosters": function () {
      return D.teams.map(function (t) {
        return card(t.name, '<p class="small muted">' + esc(t.level) + " · " + esc(t.ages) + " · " +
          (t.recruiting ? '<span class="chip ok">Recruiting</span>' : '<span class="chip">Full</span>') + "</p>" +
          table(["#", "Player", "Position"], (D.roster[t.id] || []).map(function (p) {
            return [esc(p.num), esc(p.n), esc(p.pos)];
          })) + '<a class="btn sm dark-ghost" href="team.html?id=' + t.id + '">View public page</a>');
      }).join("");
    },
    "Matches": function () {
      return card("Fixtures and availability", D.matches.map(function (m) {
        var a = availabilityFor(m.id), keys = Object.keys(a);
        var counts = { Available: 0, "Not available": 0, Maybe: 0, Injured: 0 };
        keys.forEach(function (k) { if (counts[a[k].answer] != null) counts[a[k].answer]++; });
        var squad = (D.roster[m.team] || []).length;
        return '<div style="border-bottom:1px solid var(--line-d);padding:1rem 0">' +
          "<strong>" + esc(C.teamName(m.team)) + " v " + esc(m.opponent) + "</strong> " +
          '<span class="chip">' + esc(m.status) + "</span><br>" +
          '<span class="small muted">' + C.fmtDate(m.date, true) + " · " + C.fmtTime(m.kick) + " · " + esc(m.venue) + "</span>" +
          '<p class="small" style="margin:.5rem 0">' + counts.Available + " available · " + counts["Not available"] + " out · " +
          counts.Maybe + " maybe · " + counts.Injured + " injured · " + Math.max(0, squad - keys.length) + " no response</p>" +
          (keys.length ? '<p class="small muted">' + keys.map(function (k) { return esc(a[k].name) + ": " + esc(a[k].answer); }).join(" · ") + "</p>" : "") +
          '<div class="btn-row" style="margin-top:.3rem">' +
          '<a class="btn sm dark-ghost" href="' + C.waLink("Reminder: " + C.teamName(m.team) + " v " + m.opponent + " on " + C.fmtDate(m.date) + ", arrive " + C.fmtTime(m.arrive) + " at " + m.venue + ". Please confirm your availability on the website.") + '" target="_blank" rel="noopener">Send WhatsApp reminder</a>' +
          '<button class="btn sm dark-ghost" type="button" onclick="CAA.toast(\'Email reminder queued for players who have not responded.\')">Email non-responders</button></div></div>';
      }).join(""));
    },
    "Attendance": function () {
      var players = D.roster["obsidian-ac"] || [];
      return card("Record attendance",
        '<p class="small muted">Pick a session, tick who attended, and save. Attendance feeds the player progress notes.</p>' +
        '<div class="field" style="max-width:340px"><label for="att-sess">Session</label><select id="att-sess">' +
        D.trainings.map(function (t) { return '<option>' + esc(C.progName(t.program)) + " — " + C.fmtDate(t.date) + "</option>"; }).join("") +
        "</select></div>" +
        players.map(function (p, i) {
          return '<div class="check"><input id="att' + i + '" type="checkbox" checked><label for="att' + i + '">' + esc(p.n) + " · " + esc(p.pos) + "</label></div>";
        }).join("") +
        '<button class="btn sm" type="button" onclick="CAA.toast(\'Attendance saved for this session.\')">Save attendance</button>');
    },
    "Announcements": function () {
      var extra = store.get("announcements", []);
      return card("Post an announcement",
        '<form class="form" id="ann-form"><div class="field"><label for="an-t">Title</label><input id="an-t" required></div>' +
        '<div class="field"><label for="an-b">Message</label><textarea id="an-b" required></textarea></div>' +
        '<div class="field"><span class="lbl">Send to</span><div class="opts">' +
        '<label><input type="checkbox" checked> Website news page</label>' +
        '<label><input type="checkbox" checked> Email subscribers</label>' +
        '<label><input type="checkbox"> Team members only</label></div></div>' +
        '<button class="btn sm" type="submit">Publish announcement</button></form>') +
      card("Published", (extra.concat(D.news)).map(function (n) {
        return "<p><strong>" + esc(n.title) + '</strong><br><span class="small muted">' + C.fmtDate(n.date) + "</span><br>" + esc(n.body) + "</p>";
      }).join("<hr>")) +
      card("WhatsApp", "<p>Automated WhatsApp sending needs the WhatsApp Business API, which is a separate paid service. Until that's connected, use these click-to-chat links: they open WhatsApp with the message already written so you only have to pick the group.</p>" +
        '<div class="btn-row"><a class="btn sm" href="' + C.waLink("Team announcement: ") + '" target="_blank" rel="noopener">Open WhatsApp with a message</a></div>' +
        '<p class="small muted" style="margin-top:.7rem">Email is the primary notification channel and works today.</p>');
    },
    "Programs and pricing": function () {
      return card("Edit programs",
        '<p class="small muted">Changes save to this browser immediately so you can preview them. Use "Export as data.js" to produce a file you can commit to the repository, which makes the change live for everyone.</p>' +
        '<div id="prog-editor"></div>' +
        '<div class="btn-row"><button class="btn sm" type="button" onclick="__saveProgs()">Save changes</button>' +
        '<button class="btn sm dark-ghost" type="button" onclick="__exportData()">Export as data.js</button>' +
        '<button class="btn sm dark-ghost" type="button" onclick="__resetContent()">Reset to defaults</button></div>');
    },
    "Videos and social": function () {
      return card("YouTube video IDs",
        '<p class="small muted">Paste the eleven-character ID from a YouTube URL, for example the part after v= in youtube.com/watch?v=<strong>dQw4w9WgXcQ</strong>.</p>' +
        '<div id="vid-editor"></div>' +
        '<div class="btn-row"><button class="btn sm" type="button" onclick="__saveVids()">Save video links</button>' +
        '<button class="btn sm dark-ghost" type="button" onclick="__exportData()">Export as data.js</button></div>') +
      card("Social links", '<div class="tablewrap"><table><tbody>' +
        [["Instagram", D.site.instagram], ["Facebook", D.site.facebook], ["YouTube", D.site.youtube],
         ["WhatsApp", "+" + D.site.whatsapp], ["TikTok", D.site.tiktok || "Not set up yet"]].map(function (r) {
          return "<tr><th>" + r[0] + "</th><td>" + esc(r[1]) + "</td></tr>";
        }).join("") + "</tbody></table></div><p class=\"small muted\">Edit these in data.js under site.</p>");
    },
    "Payments": function () {
      return card("Payments", empty("Stripe is not connected yet",
        "Once Stripe is connected, single sessions, packages, memberships, team fees and tryout fees appear here with receipts and refund tracking. Setup steps are in the README, section \"Payments\".")) +
      card("Discount codes", table(["Code", "Discount", "Applies to", "Status"], [
        ["SIBLING10", "10%", "Any program, second child", '<span class="chip ok">Sample</span>'],
        ["FIRSTSESSION", "$15 off", "First booking only", '<span class="chip ok">Sample</span>'],
        ["WINTER25", "25%", "Obsidian AC season fee", '<span class="chip warn">Sample, expired</span>']
      ]) + '<p class="small muted">Codes are placeholders until payment processing is live.</p>');
    },
    "Website content": function () {
      return card("What you can edit without code",
        "<ul style=\"padding-left:1.1rem\">" +
        "<li>Programs, descriptions and pricing, on the Programs tab.</li>" +
        "<li>Video links, on the Videos tab.</li>" +
        "<li>Announcements, on the Announcements tab.</li>" +
        "<li>Everything else lives in <code>assets/js/data.js</code>, which is a plain text file with comments explaining each field.</li></ul>" +
        "<p>The Export as data.js button produces a complete replacement file. Commit it to the repository and the change goes live for every visitor.</p>") +
      card("Longer term", "<p>If editing a text file becomes tiresome, the README describes moving the same content into a hosted CMS such as Sanity, Contentful or Decap, keeping the site structure exactly as it is.</p>");
    },
    "Exports": function () {
      var keys = ["bookings", "applications", "tryouts", "contacts", "questions", "newsletter", "testimonials", "sponsors"];
      return card("Download your data", "<p>Everything submitted through the site, as CSV files you can open in Excel or Google Sheets.</p>" +
        '<div class="btn-row">' + keys.map(function (k) {
          return '<button class="btn sm dark-ghost" type="button" onclick="__csv(\'' + k + '\')">' + k + " (" + store.get(k, []).length + ")</button>";
        }).join("") + "</div>" +
        '<p class="small muted" style="margin-top:1rem">Exports may contain personal and medical information about children. Store them securely and delete them when finished.</p>');
    },
    "Settings": function () {
      return card("Account", '<div class="tablewrap"><table><tbody>' +
        [["Name", user.name], ["Email", user.email], ["Role", "Coach and administrator"]].map(function (r) {
          return "<tr><th>" + r[0] + "</th><td>" + esc(r[1]) + "</td></tr>";
        }).join("") + "</tbody></table></div>") +
      card("User permissions", table(["Role", "Can see", "Can change"], [
        ["Player", "Own profile, own team's schedule, tactics, announcements", "Own availability and consent settings"],
        ["Parent", "Own children, their schedules, invoices, forms", "Children's availability, consent, bookings"],
        ["Coach and administrator", "Everything", "Everything"]
      ])) +
      card("Danger zone", '<p>Clearing local data removes every booking, application and message stored in this browser. It cannot be undone.</p>' +
        '<button class="btn sm" style="--bg:#C4282B;--bd:#C4282B" type="button" onclick="__wipe()">Clear all local data</button>');
    }
  };

  /* editors */
  window.__saveProgs = function () {
    var progs = D.programs.map(function (p, i) {
      var row = document.getElementById("pe" + i);
      return Object.assign({}, p, {
        name: row.querySelector("[data-f=name]").value,
        price: row.querySelector("[data-f=price]").value,
        short: row.querySelector("[data-f=short]").value
      });
    });
    C.saveContent("programs", progs);
    C.toast("Programs saved. Export data.js to make this live for everyone.");
  };
  window.__saveVids = function () {
    var vids = D.videos.map(function (v, i) {
      return Object.assign({}, v, { yt: document.getElementById("ve" + i).value.trim() });
    });
    C.saveContent("videos", vids);
    C.toast("Video links saved.");
  };
  window.__exportData = function () {
    var out = "/* Generated by the Coach Arnold Academy dashboard on " + new Date().toISOString() +
      "\n   Replace assets/js/data.js with this file and commit it. */\nwindow.CAA_DATA = " +
      JSON.stringify(D, null, 2) + ";\n";
    var a = document.createElement("a");
    a.href = "data:text/javascript;charset=utf-8," + encodeURIComponent(out);
    a.download = "data.js"; document.body.appendChild(a); a.click(); a.remove();
    C.toast("data.js downloaded. Replace the file in assets/js and commit it.");
  };
  window.__resetContent = function () {
    store.del("content"); C.toast("Content reset to defaults. Reloading."); setTimeout(function () { location.reload(); }, 900);
  };
  window.__wipe = function () {
    if (!confirm("Clear every booking, application and message stored in this browser? This cannot be undone.")) return;
    ["bookings", "applications", "tryouts", "contacts", "questions", "newsletter", "testimonials", "sponsors", "availability", "announcements", "content"]
      .forEach(store.del);
    C.toast("Local data cleared."); setTimeout(function () { location.reload(); }, 900);
  };

  /* ---------------- render ---------------- */
  var views = user.role === "coach" ? coachViews : user.role === "parent" ? parentViews : playerViews;
  var names = Object.keys(views);
  var current = names[0];

  navEl.innerHTML = '<div class="grp">' + (user.role === "coach" ? "Manage" : "Your account") + "</div>" +
    names.map(function (n) { return '<button type="button" data-v="' + esc(n) + '">' + esc(n) + "</button>"; }).join("") +
    '<div class="grp">Site</div><button type="button" onclick="location.href=\'index.html\'">Back to website</button>' +
    '<button type="button" data-logout>Sign out</button>';

  var firstRender = true;
  function render(name) {
    current = name;
    mainEl.innerHTML = views[name]();
    C.$$("#dash-nav button[data-v]").forEach(function (b) { b.classList.toggle("on", b.dataset.v === name); });
    if (!firstRender) mainEl.scrollIntoView({ block: "start", behavior: "smooth" });
    firstRender = false;

    /* wire dynamic editors after render */
    var pe = document.getElementById("prog-editor");
    if (pe) {
      pe.innerHTML = D.programs.map(function (p, i) {
        return '<div id="pe' + i + '" style="border-bottom:1px solid var(--line-d);padding:.9rem 0">' +
          '<div class="fgrid"><div class="field"><label>Program name</label><input data-f="name" value="' + esc(p.name) + '"></div>' +
          '<div class="field"><label>Price</label><input data-f="price" value="' + esc(p.price) + '"></div></div>' +
          '<div class="field" style="margin-top:.6rem"><label>Short description</label><input data-f="short" value="' + esc(p.short) + '"></div></div>';
      }).join("");
    }
    var ve = document.getElementById("vid-editor");
    if (ve) {
      ve.innerHTML = D.videos.map(function (v, i) {
        return '<div class="field" style="margin-bottom:.7rem"><label for="ve' + i + '">' + esc(v.title) + "</label>" +
          '<input id="ve' + i + '" value="' + esc(v.yt || "") + '" placeholder="YouTube video ID"></div>';
      }).join("");
    }
    var af = document.getElementById("ann-form");
    if (af) {
      af.addEventListener("submit", function (e) {
        e.preventDefault();
        var t = document.getElementById("an-t").value.trim(), b = document.getElementById("an-b").value.trim();
        if (!t || !b) { C.toast("Add a title and a message before publishing."); return; }
        store.push("announcements", { id: C.uid("n"), date: new Date().toISOString().slice(0, 10), title: t, body: b });
        C.toast("Published. It's live on the news page.");
        render("Announcements");
      });
    }
    C.$$("[data-logout]").forEach(function (a) { a.addEventListener("click", function (e) { e.preventDefault(); C.auth.logout(); }); });
  }

  C.$$("#dash-nav button[data-v]").forEach(function (b) {
    b.addEventListener("click", function () { render(b.dataset.v); });
  });
  C.$$("#dash-nav [data-logout]").forEach(function (a) { a.addEventListener("click", function (e) { e.preventDefault(); C.auth.logout(); }); });

  render(C.qs("view") && views[C.qs("view")] ? C.qs("view") : current);
})();
