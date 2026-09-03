/* ============================================================
   Coach Arnold Academy — app.js
   Shared behaviour for every page: header, footer, forms,
   demo authentication, local data store, calendar links.
   ============================================================ */
(function () {
  "use strict";

  var D = window.CAA_DATA;

  /* ---------- storage (falls back to memory if blocked) ---------- */
  var mem = {};
  var LS = (function () {
    try {
      var k = "__caa"; window.localStorage.setItem(k, "1"); window.localStorage.removeItem(k);
      return window.localStorage;
    } catch (e) { return null; }
  })();
  var store = {
    get: function (k, dflt) {
      var raw = LS ? LS.getItem("caa." + k) : mem[k];
      if (raw == null) return dflt;
      try { return JSON.parse(raw); } catch (e) { return dflt; }
    },
    set: function (k, v) {
      var raw = JSON.stringify(v);
      if (LS) { try { LS.setItem("caa." + k, raw); } catch (e) { mem[k] = raw; } } else { mem[k] = raw; }
      return v;
    },
    push: function (k, v) { var a = store.get(k, []); a.unshift(v); store.set(k, a); return v; },
    del: function (k) { if (LS) LS.removeItem("caa." + k); delete mem[k]; }
  };

  /* content overrides written by the admin dashboard */
  var overrides = store.get("content", {});
  Object.keys(overrides).forEach(function (k) { if (D[k]) D[k] = overrides[k]; });

  /* ---------- small helpers ---------- */
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function el(tag, attrs, html) {
    var n = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) { n.setAttribute(k, attrs[k]); });
    if (html != null) n.innerHTML = html;
    return n;
  }
  function qs(name) { return new URLSearchParams(location.search).get(name); }
  function uid(p) { return (p || "id") + "_" + Date.now().toString(36) + Math.random().toString(36).slice(2, 7); }

  var MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  var DAY = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  function dparse(d) { var p = String(d).split("-"); return new Date(+p[0], +p[1] - 1, +p[2]); }
  function fmtDate(d, long) {
    var x = dparse(d);
    return long ? DAY[x.getDay()] + " " + x.getDate() + " " + MON[x.getMonth()] + " " + x.getFullYear()
                : x.getDate() + " " + MON[x.getMonth()] + " " + x.getFullYear();
  }
  function fmtTime(t) {
    if (!t) return "";
    var p = t.split(":"), h = +p[0], m = p[1];
    var ap = h >= 12 ? "pm" : "am"; h = h % 12 || 12;
    return h + ":" + m + " " + ap;
  }
  function locName(id) { var l = (D.locations || []).find(function (x) { return x.id === id; }); return l ? l.name + ", " + l.city : id; }
  function progName(id) { var p = (D.programs || []).find(function (x) { return x.id === id; }); return p ? p.name : id; }
  function teamName(id) { var t = (D.teams || []).find(function (x) { return x.id === id; }); return t ? t.name : id; }

  /* ---------- contact links ---------- */
  var S = D.site;
  function waLink(text) {
    return "https://wa.me/" + S.whatsapp + "?text=" + encodeURIComponent(text || "Hi Coach Arnold, I found you through the academy website and I'd like to ask about ");
  }
  function mailLink(subj) { return "mailto:" + S.email + (subj ? "?subject=" + encodeURIComponent(subj) : ""); }

  /* ---------- calendar ---------- */
  function pad(n) { return n < 10 ? "0" + n : "" + n; }
  function stamp(dateStr, timeStr, addMin) {
    var d = dparse(dateStr), t = (timeStr || "09:00").split(":");
    d.setHours(+t[0], +t[1] || 0, 0, 0);
    if (addMin) d.setMinutes(d.getMinutes() + addMin);
    return d.getFullYear() + pad(d.getMonth() + 1) + pad(d.getDate()) + "T" + pad(d.getHours()) + pad(d.getMinutes()) + "00";
  }
  function gcalLink(ev) {
    var p = new URLSearchParams({
      action: "TEMPLATE", text: ev.title,
      dates: stamp(ev.date, ev.time) + "/" + stamp(ev.date, ev.time, ev.minutes || 90),
      details: ev.details || "", location: ev.location || ""
    });
    return "https://calendar.google.com/calendar/render?" + p.toString();
  }
  function icsDownload(ev) {
    var body = [
      "BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Coach Arnold Academy//EN", "BEGIN:VEVENT",
      "UID:" + uid("caa") + "@coacharnoldacademy.com",
      "DTSTAMP:" + stamp(ev.date, ev.time),
      "DTSTART:" + stamp(ev.date, ev.time),
      "DTEND:" + stamp(ev.date, ev.time, ev.minutes || 90),
      "SUMMARY:" + ev.title,
      "DESCRIPTION:" + String(ev.details || "").replace(/\n/g, "\\n"),
      "LOCATION:" + (ev.location || ""), "END:VEVENT", "END:VCALENDAR"
    ].join("\r\n");
    var a = el("a");
    a.href = "data:text/calendar;charset=utf-8," + encodeURIComponent(body);
    a.download = ev.title.replace(/[^\w]+/g, "-").toLowerCase() + ".ics";
    document.body.appendChild(a); a.click(); a.remove();
  }

  /* ---------- toast ---------- */
  var toastEl;
  function toast(msg) {
    if (!toastEl) { toastEl = el("div", { class: "toast", role: "status", "aria-live": "polite" }); document.body.appendChild(toastEl); }
    toastEl.textContent = msg;
    toastEl.classList.add("show");
    clearTimeout(toastEl._t);
    toastEl._t = setTimeout(function () { toastEl.classList.remove("show"); }, 3800);
  }

  /* ---------- auth (front-end demo only) ---------- */
  var auth = {
    user: function () { return store.get("session", null); },
    login: function (email, pass, wantRole) {
      var accounts = store.get("accounts", []).concat(D.demoUsers || []);
      var u = accounts.find(function (a) {
        return a.email.toLowerCase() === String(email).toLowerCase() && a.pass === pass;
      });
      if (!u) return { ok: false, error: "That email and password combination isn't recognised. Check both, or create an account." };
      if (wantRole && wantRole !== "any" && u.role !== wantRole) {
        return { ok: false, error: "That account is registered as a " + u.role + " account. Use the " + u.role + " login instead." };
      }
      var sess = { email: u.email, role: u.role, name: u.name, teams: u.teams || [], children: u.children || [] };
      store.set("session", sess);
      return { ok: true, user: sess };
    },
    register: function (data) {
      var accounts = store.get("accounts", []);
      var all = accounts.concat(D.demoUsers || []);
      if (all.some(function (a) { return a.email.toLowerCase() === data.email.toLowerCase(); })) {
        return { ok: false, error: "An account already exists with that email address. Try signing in instead." };
      }
      accounts.push(data); store.set("accounts", accounts);
      var sess = { email: data.email, role: data.role, name: data.name, teams: [], children: data.children || [] };
      store.set("session", sess);
      return { ok: true, user: sess };
    },
    logout: function () { store.del("session"); location.href = "index.html"; },
    require: function (roles) {
      var u = auth.user();
      if (!u || (roles && roles.indexOf(u.role) === -1)) {
        location.href = "login.html?next=" + encodeURIComponent(location.pathname.split("/").pop() + location.search);
        return null;
      }
      return u;
    }
  };

  /* ---------- pitch line graphic ---------- */
  function pitchSVG() {
    return '<svg class="pitch" viewBox="0 0 1200 520" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">' +
      '<g fill="none" stroke="#5C8BFF" stroke-opacity=".28" stroke-width="2">' +
      '<circle cx="980" cy="260" r="128"/><line x1="980" y1="0" x2="980" y2="520"/>' +
      '<rect x="1130" y="120" width="150" height="280"/><rect x="1180" y="190" width="120" height="140"/>' +
      '<path d="M760 120 L760 400"/><circle cx="980" cy="260" r="5" fill="#5C8BFF" stroke="none"/>' +
      '<path d="M-60 470 L1260 470" stroke-opacity=".16"/><path d="M-60 40 L1260 40" stroke-opacity=".16"/>' +
      "</g></svg>";
  }

  /* ---------- header / footer ---------- */
  var NAV = [
    { href: "index.html", label: "Home" },
    { href: "about.html", label: "About" },
    { href: "programs.html", label: "Programs" },
    { href: "book.html", label: "Book" },
    { href: "teams.html", label: "Teams" },
    { href: "obsidian-ac.html", label: "Obsidian AC" },
    { href: "schedule.html", label: "Schedule" },
    { href: "videos.html", label: "Videos" },
    { href: "news.html", label: "News" },
    { href: "contact.html", label: "Contact" }
  ];

  function buildHeader() {
    var here = location.pathname.split("/").pop() || "index.html";
    var u = auth.user();
    var links = NAV.map(function (n) {
      return '<a href="' + n.href + '"' + (n.href === here ? ' aria-current="page"' : "") + ">" + n.label + "</a>";
    }).join("");

    var account = u
      ? '<div class="has-drop"><button type="button" aria-expanded="false">' + esc(u.name.split(" ")[0]) + ' ▾</button>' +
        '<div class="drop"><a href="dashboard.html">My dashboard</a><a href="schedule.html">Schedule</a>' +
        '<a href="#" data-logout>Sign out</a></div></div>' +
        '<a class="btn sm" href="book.html">Book a session</a>'
      : '<div class="has-drop"><button type="button" aria-expanded="false">Log in ▾</button>' +
        '<div class="drop"><a href="login.html?role=player">Player login</a><a href="login.html?role=parent">Parent login</a>' +
        '<a href="login.html?role=coach">Coach and admin login</a><a href="login.html?tab=register">Create an account</a></div></div>' +
        '<a class="btn sm" href="book.html">Book a session</a>';

    var h = el("header", { class: "topbar" });
    h.innerHTML =
      '<div class="wrap bar">' +
        '<a class="brand" href="index.html"><img src="assets/img/logo-512.png" alt="Coach Arnold Academy crest" width="40" height="40">' +
        '<b>Coach Arnold<span>Academy</span></b></a>' +
        '<button class="navtoggle" type="button" aria-expanded="false" aria-controls="mainnav">Menu</button>' +
        '<nav class="nav" id="mainnav" aria-label="Main">' + links + account + '</nav>' +
      "</div>";
    return h;
  }

  function buildFooter() {
    var f = el("footer", { class: "site" });
    var ig = '<svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.07 1.2.05 1.8.25 2.2.42.6.22 1 .48 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c0 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2 0-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c0-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.2A6.6 6.6 0 1 0 18.6 12 6.6 6.6 0 0 0 12 5.4zm0 10.9A4.3 4.3 0 1 1 16.3 12 4.3 4.3 0 0 1 12 16.3zm6.9-11.1a1.5 1.5 0 1 1-1.6-1.5 1.5 1.5 0 0 1 1.6 1.5z"/></svg>';
    var fb = '<svg viewBox="0 0 24 24"><path d="M13.5 21v-8h2.7l.4-3.1h-3.1V7.9c0-.9.25-1.5 1.55-1.5h1.65V3.6A22 22 0 0 0 14.3 3.5c-2.4 0-4 1.45-4 4.1v2.3H7.6V13h2.7v8z"/></svg>';
    var yt = '<svg viewBox="0 0 24 24"><path d="M21.6 7.2a2.5 2.5 0 0 0-1.75-1.75C18.25 5 12 5 12 5s-6.25 0-7.85.45A2.5 2.5 0 0 0 2.4 7.2 26 26 0 0 0 2 12a26 26 0 0 0 .4 4.8 2.5 2.5 0 0 0 1.75 1.75C5.75 19 12 19 12 19s6.25 0 7.85-.45a2.5 2.5 0 0 0 1.75-1.75A26 26 0 0 0 22 12a26 26 0 0 0-.4-4.8zM10 15V9l5.2 3z"/></svg>';
    var wa = '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm5.8 14.2c-.25.7-1.45 1.35-2 1.4-.5.05-1.15.1-3.4-.75-2.85-1.1-4.65-4-4.8-4.2-.15-.2-1.15-1.5-1.15-2.9s.75-2.05 1-2.35a1 1 0 0 1 .75-.35h.55c.2 0 .45-.05.7.5s.85 2.05.9 2.2a.5.5 0 0 1 0 .5c-.35.7-.75.65-.5 1.1a7.3 7.3 0 0 0 3.4 3c.4.2.6.15.85-.1s1-1.15 1.25-1.55.5-.3.8-.2 2 .95 2.3 1.1.55.25.65.4a2.9 2.9 0 0 1-.2 1.2z"/></svg>';

    f.innerHTML =
      '<div class="wrap">' +
        '<div class="cols">' +
          '<div>' +
            '<a class="brand" href="index.html" style="margin-bottom:.9rem"><img src="assets/img/logo-512.png" alt="" width="46" height="46"><b>Coach Arnold<span>Academy</span></b></a>' +
            '<p style="font-size:.94rem;max-width:34ch">Private, group and team soccer coaching for children, teenagers and adults across ' + esc(S.serviceArea) + '.</p>' +
            '<div class="social">' +
              '<a href="' + S.instagram + '" aria-label="Instagram" rel="noopener" target="_blank">' + ig + "</a>" +
              '<a href="' + S.facebook + '" aria-label="Facebook" rel="noopener" target="_blank">' + fb + "</a>" +
              '<a href="' + S.youtube + '" aria-label="YouTube" rel="noopener" target="_blank">' + yt + "</a>" +
              '<a href="' + waLink() + '" aria-label="WhatsApp" rel="noopener" target="_blank">' + wa + "</a>" +
            "</div>" +
          "</div>" +
          "<div><h4>Train</h4>" +
            '<a href="programs.html">All programs</a><a href="book.html">Book a session</a><a href="videos.html">Training videos</a>' +
            '<a href="schedule.html">Schedule</a><a href="gallery.html">Gallery</a></div>' +
          "<div><h4>Teams</h4>" +
            '<a href="teams.html">Team directory</a><a href="obsidian-ac.html">Obsidian AC</a><a href="join-team.html">Apply to a team</a>' +
            '<a href="news.html">News and announcements</a><a href="sponsorship.html">Sponsorship</a></div>' +
          "<div><h4>Help</h4>" +
            '<a href="contact.html">Contact</a><a href="faq.html">FAQ</a><a href="testimonials.html">Testimonials</a>' +
            '<a href="policies.html">Policies and waivers</a><a href="login.html">Log in</a></div>' +
        "</div>" +
        '<div class="base"><span>© <span data-year></span> Coach Arnold Academy. All rights reserved.</span>' +
          '<span><a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a> · <a href="accessibility.html">Accessibility</a> · <a href="safety.html">Player safety</a></span>' +
        "</div>" +
      "</div>";
    return f;
  }

  function buildStickyCTA() {
    var d = el("div", { class: "sticky-cta" });
    d.innerHTML = '<a class="btn sm" href="book.html">Book</a>' +
      '<a class="btn sm ghost" href="' + waLink() + '" target="_blank" rel="noopener">WhatsApp</a>' +
      '<a class="btn sm ghost" href="contact.html">Contact</a>';
    return d;
  }

  function cookieBanner() {
    if (store.get("cookies", null)) return;
    var c = el("div", { class: "cookie show", role: "region", "aria-label": "Cookie preferences" });
    c.innerHTML = '<p>This site uses essential cookies to keep you signed in, and optional analytics cookies to understand which pages are useful. You choose.</p>' +
      '<button class="btn sm" type="button" data-ck="all">Accept all</button>' +
      '<button class="btn sm dark-ghost" type="button" data-ck="essential">Essential only</button>' +
      '<a class="btn sm dark-ghost" href="privacy.html">Read the policy</a>';
    document.body.appendChild(c);
    $$("[data-ck]", c).forEach(function (b) {
      b.addEventListener("click", function () {
        store.set("cookies", { choice: b.dataset.ck, at: new Date().toISOString() });
        c.remove();
        toast(b.dataset.ck === "all" ? "Analytics cookies allowed. You can change this on the privacy page." : "Only essential cookies will be used.");
      });
    });
  }

  /* ---------- forms ---------- */
  function markError(field, msg) {
    field.setAttribute("aria-invalid", "true");
    var e = field.parentElement.querySelector(".err-msg");
    if (!e) { e = el("p", { class: "err-msg" }); field.parentElement.appendChild(e); }
    e.textContent = msg; e.classList.add("show");
  }
  function clearError(field) {
    field.removeAttribute("aria-invalid");
    var e = field.parentElement.querySelector(".err-msg");
    if (e) e.classList.remove("show");
  }
  function validate(form) {
    var bad = null;
    $$("input,select,textarea", form).forEach(function (f) {
      if (f.type === "hidden" || f.disabled) return;
      clearError(f);
      var v = (f.value || "").trim();
      if (f.required && ((f.type === "checkbox" && !f.checked) || (f.type !== "checkbox" && !v))) {
        markError(f, f.type === "checkbox" ? "You need to tick this to continue." : "This one is required.");
        bad = bad || f; return;
      }
      if (v && f.type === "email" && !/^[^@\s]+@[^@\s]+\.[a-z]{2,}$/i.test(v)) { markError(f, "Check the email address, something looks off."); bad = bad || f; }
      if (v && f.type === "tel" && v.replace(/\D/g, "").length < 7) { markError(f, "Add a full phone number including area code."); bad = bad || f; }
      if (v && f.type === "url" && !/^https?:\/\//i.test(v)) { markError(f, "Links need to start with http:// or https://"); bad = bad || f; }
    });
    return bad;
  }
  function formData(form) {
    var o = {};
    $$("input,select,textarea", form).forEach(function (f) {
      if (!f.name) return;
      if (f.type === "checkbox") {
        if (form.querySelectorAll('[name="' + f.name + '"]').length > 1) { o[f.name] = o[f.name] || []; if (f.checked) o[f.name].push(f.value); }
        else o[f.name] = f.checked;
      } else if (f.type === "radio") { if (f.checked) o[f.name] = f.value; }
      else o[f.name] = f.value;
    });
    return o;
  }

  /* Sends the form to Netlify Forms (works once the site is deployed on
     Netlify with a matching name="" + data-netlify="true" on the <form>;
     silently no-ops anywhere else, e.g. local file preview). */
  function netlifySubmit(form) {
    try {
      var body = new URLSearchParams(new FormData(form)).toString();
      return fetch("/", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: body
      });
    } catch (e) { return Promise.reject(e); }
  }

  /* Generic handler. data-form="bookings" data-success="..." */
  function wireForms() {
    $$("form[data-form]").forEach(function (form) {
      /* honeypot spam trap */
      if (!form.querySelector("[name=_trap]")) {
        var t = el("div", { style: "position:absolute;left:-9999px", "aria-hidden": "true" });
        t.innerHTML = '<label>Leave this empty<input type="text" name="_trap" tabindex="-1" autocomplete="off"></label>';
        form.appendChild(t);
      }
      form.addEventListener("submit", function (ev) {
        ev.preventDefault();
        var msg = form.querySelector(".msg") || (function () { var m = el("div", { class: "msg", role: "status", tabindex: "-1" }); form.prepend(m); return m; })();
        msg.className = "msg";
        if (form._trap && form._trap.value) { return; } /* silently drop bots */
        var bad = validate(form);
        if (bad) {
          msg.className = "msg bad show";
          msg.innerHTML = "<h4>That didn't send</h4><p>Some fields need attention. The first one is highlighted below.</p>";
          msg.focus(); bad.focus();
          return;
        }
        var rec = formData(form);
        delete rec._trap;
        rec.id = uid(form.dataset.form);
        rec.submitted = new Date().toISOString();
        rec.status = "new";
        store.push(form.dataset.form, rec);
        netlifySubmit(form); /* best-effort; local record above is the UI source of truth */

        msg.className = "msg ok show";
        msg.innerHTML = "<h4>" + esc(form.dataset.successTitle || "Sent") + "</h4><p>" +
          (form.dataset.success || "Coach Arnold has your message and will reply soon. A copy has been sent to your email address.") + "</p>";
        msg.focus();
        toast(form.dataset.toast || "Sent to Coach Arnold");
        if (form.dataset.reset !== "no") form.reset();
        if (form.dataset.after) { var fn = window[form.dataset.after]; if (typeof fn === "function") fn(rec, form, msg); }
        window.scrollTo({ top: msg.getBoundingClientRect().top + window.scrollY - 110, behavior: "smooth" });
      });
    });
  }

  /* ---------- reveal on scroll ---------- */
  function wireReveal() {
    var items = $$(".reveal");
    if (!items.length) return;
    if (!("IntersectionObserver" in window) || matchMedia("(prefers-reduced-motion: reduce)").matches) {
      items.forEach(function (i) { i.classList.add("in"); }); return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: .08 });
    items.forEach(function (i) { io.observe(i); });
  }

  /* ---------- accordions & tabs ---------- */
  function wireAccordions() {
    $$(".acc > button").forEach(function (b) {
      var box = b.parentElement;
      b.setAttribute("aria-expanded", box.classList.contains("open") ? "true" : "false");
      b.addEventListener("click", function () {
        var open = box.classList.toggle("open");
        b.setAttribute("aria-expanded", open ? "true" : "false");
      });
    });
  }

  /* ---------- init ---------- */
  function init() {
    var mount = $("[data-header]");
    if (mount) mount.replaceWith(buildHeader());
    var fmount = $("[data-footer]");
    if (fmount) fmount.replaceWith(buildFooter());
    if (!document.body.hasAttribute("data-no-sticky")) document.body.appendChild(buildStickyCTA());

    $$("[data-year]").forEach(function (n) { n.textContent = new Date().getFullYear(); });
    $$("[data-pitch]").forEach(function (n) { n.insertAdjacentHTML("afterbegin", pitchSVG()); });

    /* nav behaviour */
    var tog = $(".navtoggle"), nav = $(".nav");
    if (tog) tog.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      tog.setAttribute("aria-expanded", open ? "true" : "false");
      tog.textContent = open ? "Close" : "Menu";
    });
    $$(".has-drop > button").forEach(function (b) {
      b.addEventListener("click", function (e) {
        e.stopPropagation();
        var p = b.parentElement, open = p.classList.toggle("open");
        b.setAttribute("aria-expanded", open ? "true" : "false");
      });
    });
    document.addEventListener("click", function () { $$(".has-drop.open").forEach(function (p) { p.classList.remove("open"); }); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") { $$(".has-drop.open").forEach(function (p) { p.classList.remove("open"); }); } });
    $$("[data-logout]").forEach(function (a) { a.addEventListener("click", function (e) { e.preventDefault(); auth.logout(); }); });

    /* templated links */
    $$("[data-wa]").forEach(function (a) { a.href = waLink(a.dataset.wa); });
    $$("[data-mail]").forEach(function (a) { a.href = mailLink(a.dataset.mail); });
    $$("[data-tel]").forEach(function (a) { a.href = "tel:" + S.phone.replace(/[^\d+]/g, ""); if (!a.textContent.trim()) a.textContent = S.phone; });
    $$("[data-site-phone]").forEach(function (n) { n.textContent = S.phone; });
    $$("[data-site-email]").forEach(function (n) { n.textContent = S.email; });
    $$("[data-site-area]").forEach(function (n) { n.textContent = S.serviceArea; });

    wireForms(); wireReveal(); wireAccordions(); cookieBanner();
  }

  /* public API used by page scripts */
  window.CAA = {
    D: D, S: S, $: $, $$: $$, el: el, esc: esc, qs: qs, uid: uid, store: store, auth: auth,
    fmtDate: fmtDate, fmtTime: fmtTime, dparse: dparse, locName: locName, progName: progName, teamName: teamName,
    waLink: waLink, mailLink: mailLink, gcalLink: gcalLink, icsDownload: icsDownload, toast: toast,
    pitchSVG: pitchSVG, wireReveal: wireReveal, wireAccordions: wireAccordions, wireForms: wireForms,
    saveContent: function (key, value) { var o = store.get("content", {}); o[key] = value; store.set("content", o); D[key] = value; }
  };

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
