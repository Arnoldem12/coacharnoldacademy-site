from shared import shell, ld, page_hero, SITE

# ----------------------------------------------------------------- TEAMS
teams_body = page_hero("Teams", "Academy teams",
  "Academy-affiliated teams for youth players and adults. Rosters, tactics and private announcements stay behind a login.",
  '<a class="btn" href="join-team.html">Apply to a team</a><a class="btn ghost" href="obsidian-ac.html">Obsidian AC</a>') + """
<section>
  <div class="wrap">
    <div class="grid g3" id="team-list"></div>
    <div class="notice" style="margin-top:2rem"><strong>How joining works.</strong>
      <p>Send an application, Coach Arnold reviews it, and suitable players are invited to train with the squad before anyone commits. There is no fee to apply and no obligation after a trial session.</p></div>
  </div>
</section>

<section class="paper">
  <div class="wrap">
    <div class="head"><span class="rule"></span><h2>What team members get</h2></div>
    <div class="grid g3">
      <div class="feature"><h3>A secure team area</h3><p>Roster, tactics, lineups and documents visible only to approved members who are signed in.</p></div>
      <div class="feature"><h3>Match availability</h3><p>Mark yourself available, unavailable, maybe or injured for every fixture, and get a nudge if you forget.</p></div>
      <div class="feature"><h3>Announcements</h3><p>Schedule changes and match information by email, with a WhatsApp group for the day-to-day.</p></div>
      <div class="feature"><h3>Coaching, not just games</h3><p>A planned training session every week, not a kickabout before kick-off.</p></div>
      <div class="feature"><h3>Video and analysis</h3><p>Clips from matches with specific coaching points for individual players.</p></div>
      <div class="feature"><h3>Player safeguarding</h3><p>Minors' details are never published. Photo use requires parental consent that can be withdrawn.</p></div>
    </div>
  </div>
</section>
"""

teams_js = """<script>
(function(){
  var C=window.CAA,D=C.D;
  document.getElementById('team-list').innerHTML=D.teams.map(function(t){
    return '<article class="tile"><div style="display:flex;gap:.9rem;align-items:center;margin-bottom:.9rem">'+
      '<span class="badge-crest">'+C.esc(t.crest)+'</span>'+
      '<div><h3 style="margin:0">'+C.esc(t.name)+'</h3><p class="meta" style="margin:0">'+C.esc(t.level)+' · '+C.esc(t.ages)+'</p></div></div>'+
      '<p>'+C.esc(t.blurb)+'</p>'+
      '<p class="meta">'+(t.recruiting?'<span class="chip ok">Recruiting</span> '+(t.needs.length?'Needs: '+C.esc(t.needs.join(', ')):''):'<span class="chip">Squad full for now</span>')+'</p>'+
      '<div class="foot"><a class="btn sm" href="'+(t.id==='obsidian-ac'?'obsidian-ac.html':'team.html?id='+t.id)+'">Team page</a>'+
      '<a class="btn sm dark-ghost" href="join-team.html?team='+t.id+'">Apply to join</a></div></article>';
  }).join('');
})();
</script>"""

shell("teams.html", "Soccer Teams Near Vancouver WA | Coach Arnold Academy",
      "Youth and adult soccer teams affiliated with Coach Arnold Academy in Camas and Vancouver, Washington. See who is recruiting and apply to join a squad.",
      teams_body, extra_js=teams_js)

# ----------------------------------------------------------------- TEAM DETAIL
team_body = """
<section class="page-hero" data-pitch>
  <div class="wrap inner">
    <nav class="crumbs"><a href="index.html">Home</a> / <a href="teams.html">Teams</a> / <span id="crumb">Team</span></nav>
    <div style="display:flex;gap:1.1rem;align-items:center;flex-wrap:wrap">
      <span class="badge-crest" id="t-crest" style="width:88px;height:88px;font-size:1.8rem"></span>
      <div><h1 id="t-name" style="margin-bottom:.15rem">Team</h1><p class="lede" id="t-meta" style="margin:0"></p></div>
    </div>
    <p class="lede" id="t-blurb" style="margin-top:1rem"></p>
    <div class="btn-row"><a class="btn" id="t-join" href="join-team.html">Apply to join</a>
      <a class="btn ghost" id="t-contact" href="#" target="_blank" rel="noopener">Contact the team</a></div>
  </div>
</section>
<section>
  <div class="wrap split">
    <div>
      <div class="head"><span class="rule"></span><h2>About the team</h2></div>
      <p id="t-history"></p>
      <h3 style="margin-top:2rem">Training schedule</h3>
      <ul id="t-train" style="padding-left:1.1rem"></ul>
      <h3 style="margin-top:2rem">Fixtures and results</h3>
      <div class="rows" id="t-fixtures"></div>
      <h3 style="margin-top:2rem">League standings</h3>
      <div id="t-standings"></div>
      <h3 style="margin-top:2rem">Team announcements</h3>
      <div id="t-news"></div>
    </div>
    <div>
      <div class="tile" style="margin-bottom:1.2rem">
        <h3>Squad</h3>
        <div id="t-roster"></div>
      </div>
      <div class="tile" style="margin-bottom:1.2rem">
        <h3>Members-only area</h3>
        <div id="t-private"></div>
      </div>
      <div class="tile">
        <h3>Photos and video</h3>
        <p class="meta">Match nights and training.</p>
        <div class="grid" style="grid-template-columns:1fr 1fr;gap:.5rem">
          <div style="aspect-ratio:1;background:var(--paper);border:2px dashed var(--line-d);border-radius:3px"></div>
          <div style="aspect-ratio:1;background:var(--paper);border:2px dashed var(--line-d);border-radius:3px"></div>
          <div style="aspect-ratio:1;background:var(--paper);border:2px dashed var(--line-d);border-radius:3px"></div>
          <div style="aspect-ratio:1;background:var(--paper);border:2px dashed var(--line-d);border-radius:3px"></div>
        </div>
        <p class="small muted" style="margin-top:.7rem">Photos of minors are published only with written parental consent. <a href="gallery.html">Full gallery</a>.</p>
      </div>
    </div>
  </div>
</section>
"""

team_js = """<script>
(function(){
  var C=window.CAA,D=C.D,id=C.qs('id')||'caa-u12';
  var t=D.teams.find(function(x){return x.id===id;});
  if(!t){location.replace('teams.html');return;}
  if(t.id==='obsidian-ac'){location.replace('obsidian-ac.html');return;}
  document.title=t.name+' | Coach Arnold Academy';
  document.getElementById('crumb').textContent=t.name;
  document.getElementById('t-name').textContent=t.name;
  document.getElementById('t-crest').textContent=t.crest;
  document.getElementById('t-meta').textContent=t.level+' · '+t.ages+' · '+t.manager;
  document.getElementById('t-blurb').textContent=t.blurb;
  document.getElementById('t-history').textContent=t.history;
  document.getElementById('t-join').href='join-team.html?team='+t.id;
  document.getElementById('t-contact').href=C.waLink('Hi Coach Arnold, I have a question about '+t.name+': ');
  document.getElementById('t-train').innerHTML=t.trainings.map(function(x){return '<li>'+C.esc(x)+'</li>';}).join('');

  var fx=D.matches.filter(function(m){return m.team===t.id;});
  document.getElementById('t-fixtures').innerHTML=fx.length?fx.map(function(m){
    var d=C.dparse(m.date);
    return '<div class="row"><div class="date"><span class="d">'+d.getDate()+'</span><span class="m">'+
      ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'][d.getMonth()]+'</span></div>'+
      '<div><div class="t">'+C.esc(m.opponent)+'</div><div class="s">'+
      (m.status==='completed'?C.esc(m.score||'Result to follow'):C.fmtTime(m.kick)+' · '+C.esc(m.venue))+'</div></div>'+
      '<div class="act"><a class="btn sm dark-ghost" href="schedule.html#'+m.id+'">Details</a></div></div>';
  }).join('') : '<div class="empty"><h4>No fixtures listed</h4><p>The season schedule goes up here as soon as the league confirms it.</p></div>';

  var st=D.standings[t.id];
  document.getElementById('t-standings').innerHTML = st ? tableHTML(st) :
    '<div class="empty"><h4>No table for this team</h4><p>This squad plays friendlies and development fixtures rather than a league season.</p></div>';
  function tableHTML(s){
    return '<p class="meta">'+C.esc(s.league)+'</p><div class="tablewrap"><table><thead><tr><th>Team</th><th>P</th><th>W</th><th>D</th><th>L</th><th>GF</th><th>GA</th><th>Pts</th></tr></thead><tbody>'+
      s.rows.map(function(r){return '<tr'+(r.us?' style="font-weight:600;background:rgba(27,84,255,.07)"':'')+'><td>'+C.esc(r.team)+'</td><td>'+r.p+'</td><td>'+r.w+'</td><td>'+r.d+'</td><td>'+r.l+'</td><td>'+r.gf+'</td><td>'+r.ga+'</td><td>'+r.pts+'</td></tr>';}).join('')+
      '</tbody></table></div>';
  }

  document.getElementById('t-news').innerHTML=D.news.slice(0,2).map(function(n){
    return '<div class="feature" style="margin-bottom:1rem"><h3>'+C.esc(n.title)+'</h3><p class="meta">'+C.fmtDate(n.date)+'</p><p>'+C.esc(n.body)+'</p></div>';
  }).join('')+'<a class="btn sm dark-ghost" href="news.html">All announcements</a>';

  var u=C.auth.user(), roster=D.roster[t.id]||[];
  var lock='<svg viewBox="0 0 24 24"><path d="M12 1a5 5 0 0 0-5 5v3H6a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2h-1V6a5 5 0 0 0-5-5zm0 2a3 3 0 0 1 3 3v3H9V6a3 3 0 0 1 3-3z"/></svg>';
  if(u){
    document.getElementById('t-roster').innerHTML='<div class="tablewrap"><table><thead><tr><th>#</th><th>Player</th><th>Position</th></tr></thead><tbody>'+
      roster.map(function(p){return '<tr><td>'+C.esc(p.num)+'</td><td>'+C.esc(p.n)+'</td><td>'+C.esc(p.pos)+'</td></tr>';}).join('')+'</tbody></table></div>'+
      '<p class="small muted" style="margin-top:.6rem">Players under 18 are listed by first name and last initial only.</p>';
    document.getElementById('t-private').innerHTML='<p class="meta">You are signed in as '+C.esc(u.name)+'.</p>'+
      '<p>Tactics, lineups, documents and the team WhatsApp group are in your dashboard.</p>'+
      '<div class="foot"><a class="btn sm" href="dashboard.html">Open team dashboard</a></div>';
  }else{
    document.getElementById('t-roster').innerHTML='<div class="locked">'+lock+'<h4>Roster is private</h4>'+
      '<p class="small">Squad lists are visible to approved team members only. This protects players, particularly minors.</p>'+
      '<div class="btn-row" style="justify-content:center"><a class="btn sm" href="login.html">Log in</a></div></div>';
    document.getElementById('t-private').innerHTML='<div class="locked">'+lock+'<h4>Members only</h4>'+
      '<p class="small">Tactics, lineups, documents and the WhatsApp group link are behind the login.</p>'+
      '<div class="btn-row" style="justify-content:center"><a class="btn sm" href="login.html">Log in</a><a class="btn sm dark-ghost" href="join-team.html?team='+t.id+'">Apply</a></div></div>';
  }
})();
</script>"""

shell("team.html", "Team page | Coach Arnold Academy",
      "Team information, training schedule, fixtures, results and standings for Coach Arnold Academy squads. Rosters and tactics require a member login.",
      team_body, extra_js=team_js)

# ----------------------------------------------------------------- OBSIDIAN AC
obs_body = """
<section class="hero" data-pitch>
  <div class="glow"></div>
  <div class="wrap inner hero-anim">
    <span class="kicker"><i></i> Adult indoor soccer, Vancouver WA</span>
    <h1>Obsidian AC</h1>
    <p class="lede">Coach Arnold's indoor side. A planned training session every Wednesday, a competitive league night, and a squad that shows up for both.</p>
    <div class="btn-row">
      <a class="btn" href="join-team.html?team=obsidian-ac">Apply for Obsidian AC</a>
      <a class="btn ghost" href="#fixtures">View upcoming matches</a>
      <a class="btn ghost" href="#tryout">Register for a tryout</a>
    </div>
  </div>
  <div class="hero-strip"><div class="wrap"><div class="grid" style="gap:1px" id="obs-stats"></div></div></div>
</section>

<section>
  <div class="wrap split">
    <div>
      <div class="head"><span class="rule"></span><h2>The team</h2></div>
      <p class="lede" id="obs-blurb"></p>
      <p id="obs-history"></p>
      <p>The squad is co-ed and open to adults of any background who can play at a reasonable standard and commit to a weekly league night. Obsidian AC is competitive without being unpleasant: players are expected to work, and expected to behave.</p>
      <h3 style="margin-top:2rem">Indoor league information</h3>
      <div class="grid g2">
        <div class="feature"><h3>Format</h3><p>Six-a-side indoor, running clock, rolling substitutions, walls in play.</p></div>
        <div class="feature"><h3>Season</h3><p>Winter league across roughly twelve weeks, one fixture per week on a weeknight.</p></div>
        <div class="feature"><h3>Home venue</h3><p>Riverview Indoor Arena, Vancouver WA. Free parking, spectators welcome.</p></div>
        <div class="feature"><h3>Fees</h3><p>Season fee per player covering league registration, referees and venue. Confirm current amount with Coach Arnold.</p></div>
      </div>
      <p class="small muted" style="margin-top:.8rem">League name, venue and fee figures are sample content. <strong>Replace with the real league details before launch.</strong></p>
    </div>
    <div>
      <div class="tile" style="margin-bottom:1.2rem">
        <h3>Recruitment</h3>
        <div id="obs-recruit"></div>
        <div class="foot"><a class="btn sm" href="join-team.html?team=obsidian-ac">Apply to join</a>
          <a class="btn sm dark-ghost" href="#tryout">Tryout registration</a></div>
      </div>
      <div class="tile" style="margin-bottom:1.2rem">
        <h3>Training</h3>
        <ul id="obs-train" style="padding-left:1.1rem"></ul>
        <p class="small muted">Training is open to trialists once an application has been reviewed.</p>
      </div>
      <div class="tile">
        <h3>Getting there</h3>
        <p class="meta">Riverview Indoor Arena, 1200 SE Riverview Way, Vancouver, WA</p>
        <p>Enter through the north doors. Changing rooms are to the left, the arena is straight ahead. Arrive thirty minutes before kick-off.</p>
        <div class="foot"><a class="btn sm dark-ghost" href="https://maps.google.com/?q=Vancouver+WA+indoor+soccer" target="_blank" rel="noopener">Open in maps</a></div>
      </div>
    </div>
  </div>
</section>

<section class="ink" id="fixtures">
  <div class="wrap">
    <div class="head"><span class="rule"></span><h2>Fixtures and results</h2>
      <p>Signed-in squad members can set their availability for each fixture.</p></div>
    <div class="split">
      <div><h3 style="font-size:1.2rem">Upcoming</h3><div class="rows" id="obs-next"></div></div>
      <div><h3 style="font-size:1.2rem">Recent results</h3><div class="rows" id="obs-past"></div></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div>
      <div class="head"><span class="rule"></span><h2>League standings</h2></div>
      <div id="obs-table"></div>
    </div>
    <div>
      <div class="head"><span class="rule"></span><h2>Squad</h2></div>
      <div id="obs-roster"></div>
    </div>
  </div>
</section>

<section class="paper" id="tryout">
  <div class="wrap-n">
    <div class="head"><span class="rule"></span><h2>Tryout registration</h2>
      <p>A short form to reserve a place at a Wednesday trial session. There's no fee to trial and no obligation afterwards.</p></div>
    <form class="form" data-form="tryouts" data-success-title="Tryout place reserved"
          data-success="Coach Arnold has your registration and will confirm the date, time and what to bring by email. Bring both a dark and a light shirt."
          data-toast="Tryout registration sent">
      <div class="msg" tabindex="-1"></div>
      <div class="fgrid">
        <div class="field"><label for="ty-name">Full name</label><input id="ty-name" name="name" required autocomplete="name"></div>
        <div class="field"><label for="ty-email">Email</label><input id="ty-email" name="email" type="email" required autocomplete="email"></div>
        <div class="field"><label for="ty-phone">Phone</label><input id="ty-phone" name="phone" type="tel" required autocomplete="tel"></div>
        <div class="field"><label for="ty-age">Age</label><input id="ty-age" name="age" type="number" min="18" max="70" required></div>
        <div class="field"><label for="ty-pos">Preferred position</label>
          <select id="ty-pos" name="position" required>
            <option value="">Choose one</option><option>Goalkeeper</option><option>Defender</option>
            <option>Midfielder</option><option>Forward</option></select></div>
        <div class="field"><label for="ty-date">Which Wednesday suits you?</label><input id="ty-date" name="date" type="date" required></div>
      </div>
      <div class="field"><label for="ty-exp">Playing experience</label>
        <textarea id="ty-exp" name="experience" required placeholder="Recent clubs or leagues, level, how often you currently play."></textarea></div>
      <div class="check"><input id="ty-waiver" type="checkbox" name="waiver" required>
        <label for="ty-waiver">I accept the <a href="waiver.html" target="_blank">liability waiver</a> and <a href="conduct.html" target="_blank">code of conduct</a>, and I'm 18 or over.</label></div>
      <div><button class="btn" type="submit">Reserve a tryout place</button></div>
    </form>
  </div>
</section>

<section class="ink">
  <div class="wrap">
    <div class="head"><span class="rule"></span><h2>Team announcements</h2></div>
    <div class="grid g3" id="obs-news"></div>
    <div class="split" style="margin-top:2.4rem">
      <div>
        <h3>Sponsors</h3>
        <p>Obsidian AC is looking for local sponsors for kit, arena fees and equipment. Sponsorship puts your business on the shirt, on this page and in match-night posts.</p>
        <div class="btn-row"><a class="btn" href="sponsorship.html">Sponsorship options</a></div>
        <div class="grid g4" style="margin-top:1.4rem">
          <div style="aspect-ratio:2/1;border:2px dashed var(--line);border-radius:3px;display:grid;place-items:center;font-size:.78rem;color:#8FA1C4">Sponsor logo</div>
          <div style="aspect-ratio:2/1;border:2px dashed var(--line);border-radius:3px;display:grid;place-items:center;font-size:.78rem;color:#8FA1C4">Sponsor logo</div>
          <div style="aspect-ratio:2/1;border:2px dashed var(--line);border-radius:3px;display:grid;place-items:center;font-size:.78rem;color:#8FA1C4">Available</div>
        </div>
      </div>
      <div>
        <h3>Team store</h3>
        <p>Training tops, match shirts and hoodies in the Obsidian AC colours. The store opens once the winter kit order is confirmed.</p>
        <div class="tile"><h3 style="font-size:1.1rem">Store opening soon</h3>
          <p class="meta">Placeholder section</p>
          <p>Connect a Shopify, Square or Printful storefront here, or link out to an external store. See the README, section "Team store".</p>
          <div class="foot"><a class="btn sm ghost" data-wa="Hi Coach Arnold, I'd like to know when the Obsidian AC store opens." href="#" target="_blank" rel="noopener">Tell me when it opens</a></div></div>
      </div>
    </div>
  </div>
</section>

<section class="paper tight">
  <div class="wrap-n">
    <div class="tile"><h3>Members-only dashboard</h3>
      <p>Squad members sign in for tactics, lineups, the availability list and the team WhatsApp group. The group link is never published on a public page.</p>
      <div class="foot"><a class="btn sm" href="login.html">Squad login</a><a class="btn sm dark-ghost" href="join-team.html?team=obsidian-ac">Apply to join</a></div></div>
  </div>
</section>
"""

obs_js = """<script>
(function(){
  var C=window.CAA,D=C.D,t=D.teams.find(function(x){return x.id==='obsidian-ac';});
  var MN=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'];
  document.getElementById('obs-blurb').textContent=t.blurb;
  document.getElementById('obs-history').textContent=t.history;
  document.getElementById('obs-train').innerHTML=t.trainings.map(function(x){return '<li>'+C.esc(x)+'</li>';}).join('');

  var st=D.standings['obsidian-ac'], us=st.rows.find(function(r){return r.us;});
  document.getElementById('obs-stats').innerHTML=
    '<div class="cell"><span class="n">'+us.pts+'</span><span class="l">Points from '+us.p+' league matches</span></div>'+
    '<div class="cell"><span class="n">'+us.gf+'</span><span class="l">Goals scored this season</span></div>'+
    '<div class="cell"><span class="n">'+t.needs.length+'</span><span class="l">Squad places currently open</span></div>'+
    '<div class="cell"><span class="n">Wed</span><span class="l">Weekly training, 8:00 pm</span></div>';

  document.getElementById('obs-recruit').innerHTML = t.recruiting ?
    '<p><span class="chip ok">Recruiting now</span></p><p class="meta">Positions needed</p><ul style="padding-left:1.1rem">'+
      t.needs.map(function(n){return '<li>'+C.esc(n)+'</li>';}).join('')+'</ul>'+
      '<p class="small">Outfield players in other positions are still welcome to apply and will be kept on the list.</p>'
    : '<p><span class="chip">Squad currently full</span></p><p class="small">Applications are still accepted and held for the next window.</p>';

  var fx=D.matches.filter(function(m){return m.team==='obsidian-ac';});
  function row(m){
    var d=C.dparse(m.date), done=m.status==='completed';
    return '<div class="row" id="'+m.id+'"><div class="date"><span class="d">'+d.getDate()+'</span><span class="m">'+MN[d.getMonth()]+'</span></div>'+
      '<div><div class="t">'+C.esc(m.opponent)+'</div><div class="s">'+
      (done?C.esc(m.score||'Result to follow'):C.fmtTime(m.kick)+' · arrive '+C.fmtTime(m.arrive)+' · '+C.esc(m.venue)+' · '+(m.home?'Home':'Away')+' · '+C.esc(m.kit))+
      '</div></div><div class="act">'+(done?'<span class="chip">Completed</span>':'<a class="btn sm ghost" href="schedule.html#'+m.id+'">Set availability</a>')+'</div></div>';
  }
  document.getElementById('obs-next').innerHTML=fx.filter(function(m){return m.status!=='completed';}).map(row).join('');
  document.getElementById('obs-past').innerHTML=fx.filter(function(m){return m.status==='completed';}).map(row).join('');

  document.getElementById('obs-table').innerHTML='<p class="meta">'+C.esc(st.league)+'</p><div class="tablewrap"><table>'+
    '<thead><tr><th>Team</th><th>P</th><th>W</th><th>D</th><th>L</th><th>GF</th><th>GA</th><th>Pts</th></tr></thead><tbody>'+
    st.rows.map(function(r){return '<tr'+(r.us?' style="font-weight:600;background:rgba(27,84,255,.07)"':'')+'><td>'+C.esc(r.team)+'</td><td>'+r.p+'</td><td>'+r.w+'</td><td>'+r.d+'</td><td>'+r.l+'</td><td>'+r.gf+'</td><td>'+r.ga+'</td><td>'+r.pts+'</td></tr>';}).join('')+'</tbody></table></div>';

  var u=C.auth.user();
  document.getElementById('obs-roster').innerHTML = u ?
    '<div class="tablewrap"><table><thead><tr><th>#</th><th>Player</th><th>Position</th></tr></thead><tbody>'+
      D.roster['obsidian-ac'].map(function(p){return '<tr><td>'+C.esc(p.num)+'</td><td>'+C.esc(p.n)+'</td><td>'+C.esc(p.pos)+'</td></tr>';}).join('')+
      '</tbody></table></div>'
    : '<div class="locked"><h4>Squad list is private</h4><p class="small">Sign in as a squad member to see the full roster, shirt numbers and contact details.</p>'+
      '<div class="btn-row" style="justify-content:center"><a class="btn sm" href="login.html">Log in</a></div></div>';

  document.getElementById('obs-news').innerHTML=D.news.map(function(n){
    return '<article class="tile"><h3 style="font-size:1.15rem">'+C.esc(n.title)+'</h3><p class="meta">'+C.fmtDate(n.date)+'</p><p>'+C.esc(n.body)+'</p></article>';
  }).join('');

  var d=new Date(); d.setDate(d.getDate()+((3-d.getDay()+7)%7||7));
  document.getElementById('ty-date').value=d.toISOString().slice(0,10);
  document.getElementById('ty-date').min=new Date().toISOString().slice(0,10);
})();
</script>"""

shell("obsidian-ac.html", "Obsidian AC | Indoor Soccer Team Near Vancouver WA",
      "Obsidian AC is Coach Arnold Academy's adult indoor soccer team in Vancouver, Washington. Fixtures, standings, recruitment, tryout registration and team news.",
      obs_body, extra_js=obs_js,
      jsonld=ld("""{"@context":"https://schema.org","@type":"SportsTeam","name":"Obsidian AC",
        "sport":"Indoor soccer","url":"%s/obsidian-ac.html",
        "coach":{"@type":"Person","name":"Arnold Eoka Mambe"},
        "memberOf":{"@type":"Organization","name":"Coach Arnold Academy"},
        "location":{"@type":"Place","name":"Riverview Indoor Arena","address":"Vancouver, WA"}}""" % SITE))

# ----------------------------------------------------------------- JOIN TEAM
join_body = page_hero("Apply to a team", "Team application",
  "One form to apply to any academy team. Coach Arnold reviews every application personally and replies whether the answer is yes or no.") + """
<section>
  <div class="wrap-n">
    <form class="form" data-form="applications" data-reset="no"
          data-success-title="Application received"
          data-success="Coach Arnold has your application and a confirmation is on its way to your email. Expect a reply within a few days. If the squad is full, you'll be told plainly rather than left waiting."
          data-toast="Application sent to Coach Arnold">
      <div class="msg" tabindex="-1"></div>

      <fieldset>
        <legend>Which team?</legend>
        <div class="field"><label for="a-team">Team</label><select id="a-team" name="team" required></select>
          <p class="hint" id="a-team-note"></p></div>
      </fieldset>

      <fieldset>
        <legend>About you</legend>
        <div class="fgrid">
          <div class="field"><label for="a-name">Full name</label><input id="a-name" name="fullName" required autocomplete="name"></div>
          <div class="field"><label for="a-dob">Date of birth</label><input id="a-dob" name="dob" type="date" required></div>
          <div class="field"><label for="a-email">Email</label><input id="a-email" name="email" type="email" required autocomplete="email"></div>
          <div class="field"><label for="a-phone">Phone</label><input id="a-phone" name="phone" type="tel" required autocomplete="tel"></div>
          <div class="field"><label for="a-wa">WhatsApp number</label><input id="a-wa" name="whatsapp" type="tel" placeholder="Used for the team group"></div>
          <div class="field"><label for="a-city">City</label><input id="a-city" name="city" required placeholder="Camas, Vancouver, Portland"></div>
        </div>
      </fieldset>

      <fieldset>
        <legend>Football details</legend>
        <div class="fgrid">
          <div class="field"><label for="a-pos1">Preferred position</label>
            <select id="a-pos1" name="position1" required><option value="">Choose one</option>
              <option>Goalkeeper</option><option>Centre back</option><option>Full back</option>
              <option>Defensive midfielder</option><option>Central midfielder</option><option>Attacking midfielder</option>
              <option>Winger</option><option>Striker</option></select></div>
          <div class="field"><label for="a-pos2">Secondary position</label>
            <select id="a-pos2" name="position2"><option value="">None</option>
              <option>Goalkeeper</option><option>Centre back</option><option>Full back</option>
              <option>Defensive midfielder</option><option>Central midfielder</option><option>Attacking midfielder</option>
              <option>Winger</option><option>Striker</option></select></div>
          <div class="field"><label for="a-club">Current or previous club</label><input id="a-club" name="club" placeholder="Club, school or league. Write none if this is your first team."></div>
          <div class="field"><label for="a-foot">Stronger foot</label>
            <select id="a-foot" name="foot"><option>Right</option><option>Left</option><option>Both</option></select></div>
        </div>
        <div class="field" style="margin-top:1rem"><label for="a-exp">Playing experience</label>
          <textarea id="a-exp" name="experience" required placeholder="How long you've played, what level, how often you play now, and what you're looking for from a team."></textarea></div>
        <div class="field"><span class="lbl">Availability</span>
          <div class="opts">
            <label><input type="checkbox" name="availability" value="Weekday evenings"> Weekday evenings</label>
            <label><input type="checkbox" name="availability" value="Weekday daytime"> Weekday daytime</label>
            <label><input type="checkbox" name="availability" value="Saturday"> Saturday</label>
            <label><input type="checkbox" name="availability" value="Sunday"> Sunday</label>
          </div>
          <p class="hint">Most teams need one training session and one fixture per week.</p></div>
      </fieldset>

      <fieldset>
        <legend>Safety and contact</legend>
        <div class="fgrid">
          <div class="field"><label for="a-em">Emergency contact name</label><input id="a-em" name="emergencyName" required></div>
          <div class="field"><label for="a-emp">Emergency contact phone</label><input id="a-emp" name="emergencyPhone" type="tel" required></div>
        </div>
        <div class="field" style="margin-top:1rem"><label for="a-inj">Injuries or medical information</label>
          <textarea id="a-inj" name="injuries" placeholder="Current or recent injuries, conditions the coach should know about, medication. Write none if there is nothing."></textarea></div>
      </fieldset>

      <fieldset id="a-guardian" style="display:none">
        <legend>Parent or guardian, for applicants under 18</legend>
        <div class="fgrid">
          <div class="field"><label for="a-gname">Parent or guardian name</label><input id="a-gname" name="guardianName"></div>
          <div class="field"><label for="a-grel">Relationship</label><input id="a-grel" name="guardianRelationship"></div>
          <div class="field"><label for="a-gemail">Parent email</label><input id="a-gemail" name="guardianEmail" type="email"></div>
          <div class="field"><label for="a-gphone">Parent phone</label><input id="a-gphone" name="guardianPhone" type="tel"></div>
        </div>
        <div class="check" style="margin-top:1rem"><input id="a-gconsent" type="checkbox" name="guardianConsent">
          <label for="a-gconsent">As parent or legal guardian I consent to this application and to my child training and playing with the team.</label></div>
      </fieldset>

      <fieldset>
        <legend>Optional extras</legend>
        <div class="fgrid">
          <div class="field"><label for="a-photo">Profile photo</label><input id="a-photo" name="photo" type="file" accept="image/*">
            <p class="hint">Used only on the private team roster. Never published without your permission.</p></div>
          <div class="field"><label for="a-video">Highlight video link</label><input id="a-video" name="video" type="url" placeholder="https://youtube.com/...">
            <p class="hint">Optional. Helpful but never required.</p></div>
        </div>
      </fieldset>

      <fieldset>
        <legend>Agreement</legend>
        <div class="check"><input id="a-policy" type="checkbox" name="policies" required>
          <label for="a-policy">I accept the <a href="conduct.html" target="_blank">code of conduct</a>, the <a href="waiver.html" target="_blank">liability waiver</a> and the team policies.</label></div>
        <div class="check"><input id="a-privacy" type="checkbox" name="privacy" required>
          <label for="a-privacy">I've read the <a href="privacy.html" target="_blank">privacy policy</a> and agree to my details being stored to process this application.</label></div>
        <div class="check"><input id="a-photoc" type="checkbox" name="photoConsent">
          <label for="a-photoc">I consent to team photos and video including me being used publicly. <span class="muted">Optional, and can be withdrawn at any time.</span></label></div>
      </fieldset>

      <div class="btn-row" style="margin-top:0"><button class="btn" type="submit">Send application</button>
        <a class="btn dark-ghost" href="teams.html">Back to teams</a></div>
    </form>
  </div>
</section>
"""

join_js = """<script>
(function(){
  var C=window.CAA,D=C.D,sel=document.getElementById('a-team');
  sel.innerHTML='<option value="">Choose a team</option>'+D.teams.map(function(t){
    return '<option value="'+t.id+'">'+C.esc(t.name)+' — '+C.esc(t.ages)+(t.recruiting?'':' (squad full)')+'</option>';}).join('')+
    '<option value="any">Not sure, put me where I fit</option>';
  var pre=C.qs('team'); if(pre) sel.value=pre;
  function note(){
    var t=D.teams.find(function(x){return x.id===sel.value;});
    document.getElementById('a-team-note').textContent = t ?
      (t.recruiting ? 'Currently recruiting'+(t.needs.length?': '+t.needs.join(', '):'')+'.' : 'This squad is full, but applications are held for the next window.') : '';
  }
  sel.addEventListener('change',note); note();

  var dob=document.getElementById('a-dob');
  dob.addEventListener('change',function(){
    var age=(Date.now()-new Date(dob.value))/31557600000;
    var minor=age<18&&age>0;
    document.getElementById('a-guardian').style.display=minor?'block':'none';
    ['a-gname','a-gemail','a-gphone'].forEach(function(id){document.getElementById(id).required=minor;});
    document.getElementById('a-gconsent').required=minor;
  });
})();
</script>"""

shell("join-team.html", "Apply to Join a Soccer Team | Coach Arnold Academy",
      "Apply to join an academy soccer team or Obsidian AC in Vancouver, WA. One short application covering position, experience, availability and emergency contacts.",
      join_body, extra_js=join_js)

# ----------------------------------------------------------------- SCHEDULE
sched_body = page_hero("Schedule", "Schedule",
  "Training sessions and match fixtures. Signed-in players and parents can set availability for every match.",
  '<a class="btn" href="book.html">Book a training session</a>') + """
<section>
  <div class="wrap">
    <div class="tabs" id="sched-tabs" role="tablist">
      <button type="button" class="on" data-view="matches">Matches</button>
      <button type="button" data-view="training">Training</button>
      <button type="button" data-view="results">Results</button>
    </div>
    <div class="fgrid" style="margin-bottom:1.6rem">
      <div class="field"><label for="f-team">Team</label><select id="f-team"></select></div>
      <div class="field"><label for="f-search">Search</label><input id="f-search" type="search" placeholder="Opponent, venue or program"></div>
    </div>
    <div id="sched-out"></div>
  </div>
</section>

<section class="paper tight">
  <div class="wrap-n">
    <div class="notice"><strong>Availability responses.</strong>
      <p>Availability is recorded against your account so Coach Arnold can see who is coming. Sign in to respond, and change your answer any time up to kick-off. Coach Arnold can send a reminder to anyone who hasn't replied.</p></div>
  </div>
</section>
"""

sched_js = """<script>
(function(){
  var C=window.CAA,D=C.D,view='matches',team=C.qs('team')||'all',q='';
  var MN=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'];
  var out=document.getElementById('sched-out');
  var ft=document.getElementById('f-team');
  ft.innerHTML='<option value="all">All teams</option>'+D.teams.map(function(t){
    return '<option value="'+t.id+'">'+C.esc(t.name)+'</option>';}).join('');
  ft.value=team;

  function avail(id){ return (C.store.get('availability',{})[id])||{}; }
  function setAvail(id,ans){
    var u=C.auth.user(); if(!u) return;
    var all=C.store.get('availability',{}); all[id]=all[id]||{};
    all[id][u.email]={answer:ans,name:u.name,at:new Date().toISOString()};
    C.store.set('availability',all);
    C.toast('Marked '+ans.toLowerCase()+' — Coach Arnold can see your response.');
    render();
  }
  window.__setAvail=setAvail;

  function statusChip(m){
    if(m.status==='completed')return '<span class="chip">Completed</span>';
    if(m.status==='canceled')return '<span class="chip err">Canceled</span>';
    if(m.status==='changed')return '<span class="chip warn">Time changed</span>';
    return '<span class="chip ok">Scheduled</span>';
  }

  function matchCard(m){
    var u=C.auth.user(), a=avail(m.id), mine=u?(a[u.email]||{}).answer:null;
    var counts={Available:0,'Not available':0,Maybe:0,Injured:0};
    Object.keys(a).forEach(function(k){ if(counts[a[k].answer]!=null) counts[a[k].answer]++; });
    var d=C.dparse(m.date);
    var ev={title:C.teamName(m.team)+' v '+m.opponent,date:m.date,time:m.arrive,minutes:120,
      location:m.venue+', '+m.address,details:'Arrive '+C.fmtTime(m.arrive)+'. Kick-off '+C.fmtTime(m.kick)+'. Kit: '+m.kit};
    var buttons = u ? ['Available','Not available','Maybe','Injured'].map(function(x){
        return '<button class="btn sm '+(mine===x?'':'dark-ghost')+'" type="button" onclick="__setAvail(\\''+m.id+'\\',\\''+x+'\\')">'+x+'</button>';}).join('')
      : '<a class="btn sm" href="login.html">Log in to set availability</a>';
    return '<article class="tile" id="'+m.id+'" style="margin-bottom:1rem">'+
      '<div style="display:flex;gap:1rem;align-items:flex-start;flex-wrap:wrap">'+
        '<div class="date" style="border-right:2px solid var(--blue);padding-right:1rem;font-family:var(--ff-d);text-align:center">'+
          '<span style="font-size:2rem;display:block;line-height:1">'+d.getDate()+'</span>'+
          '<span style="font-size:.85rem;color:var(--muted-d)">'+MN[d.getMonth()]+'</span></div>'+
        '<div style="flex:1 1 260px"><h3 style="margin-bottom:.2rem">'+C.esc(C.teamName(m.team))+' v '+C.esc(m.opponent)+'</h3>'+
          '<p class="meta" style="margin-bottom:.5rem">'+C.fmtDate(m.date,true)+' · kick-off '+C.fmtTime(m.kick)+
          ' · arrive '+C.fmtTime(m.arrive)+' · '+(m.home?'Home':'Away')+' '+statusChip(m)+'</p>'+
          '<p style="margin-bottom:.4rem"><strong>'+C.esc(m.venue)+'</strong><br>'+C.esc(m.address)+
          ' · <a href="https://maps.google.com/?q='+encodeURIComponent(m.venue+' '+m.address)+'" target="_blank" rel="noopener">Map and directions</a></p>'+
          '<p style="margin-bottom:.4rem">Kit: '+C.esc(m.kit)+(m.notes?'<br>Notes: '+C.esc(m.notes):'')+'</p>'+
          (m.score?'<p><strong>Final score: '+C.esc(m.score)+'</strong></p>':'')+
        '</div></div>'+
      (m.status==='completed'?'':'<div style="margin-top:1rem;border-top:1px solid var(--line-d);padding-top:1rem">'+
        '<p class="meta" style="margin-bottom:.5rem">Your availability'+(mine?': <span class="chip ok">'+C.esc(mine)+'</span>':'')+'</p>'+
        '<div class="btn-row" style="margin-top:0">'+buttons+
        '<a class="btn sm dark-ghost" href="'+C.gcalLink(ev)+'" target="_blank" rel="noopener">Add to Google Calendar</a>'+
        '</div>'+
        '<p class="small muted" style="margin-top:.6rem">Squad responses so far: '+counts.Available+' available, '+
        counts['Not available']+' out, '+counts.Maybe+' maybe, '+counts.Injured+' injured.</p></div>')+
      '</article>';
  }

  function trainCard(t){
    var d=C.dparse(t.date);
    var ev={title:'Training: '+C.progName(t.program),date:t.date,time:t.time,minutes:75,location:C.locName(t.location),
      details:'Coach Arnold Academy training session.'};
    return '<article class="tile" style="margin-bottom:1rem"><div style="display:flex;gap:1rem;flex-wrap:wrap;align-items:flex-start">'+
      '<div style="border-right:2px solid var(--blue);padding-right:1rem;font-family:var(--ff-d);text-align:center">'+
      '<span style="font-size:2rem;display:block;line-height:1">'+d.getDate()+'</span><span style="font-size:.85rem;color:var(--muted-d)">'+MN[d.getMonth()]+'</span></div>'+
      '<div style="flex:1 1 260px"><h3 style="margin-bottom:.2rem">'+C.esc(C.progName(t.program))+'</h3>'+
      '<p class="meta">'+C.fmtDate(t.date,true)+' at '+C.fmtTime(t.time)+' · '+C.esc(C.locName(t.location))+
      ' · <span class="chip ok">'+t.spaces+' spaces left</span></p>'+
      '<div class="btn-row" style="margin-top:.6rem"><a class="btn sm" href="book.html?program='+t.program+'&date='+t.date+'&time='+t.time+'">Book this session</a>'+
      '<a class="btn sm dark-ghost" href="'+C.gcalLink(ev)+'" target="_blank" rel="noopener">Add to calendar</a></div></div></div></article>';
  }

  function render(){
    var txt=q.toLowerCase();
    if(view==='training'){
      var t=D.trainings.filter(function(x){
        return (!txt||(C.progName(x.program)+C.locName(x.location)).toLowerCase().indexOf(txt)>-1);});
      out.innerHTML=t.length?t.map(trainCard).join(''):'<div class="empty"><h4>No sessions match</h4><p>Clear the search, or <a href="contact.html">ask Coach Arnold</a> about a time that suits you.</p></div>';
      return;
    }
    var list=D.matches.filter(function(m){
      if(team!=='all'&&m.team!==team)return false;
      if(view==='results'&&m.status!=='completed')return false;
      if(view==='matches'&&m.status==='completed')return false;
      if(txt&&(m.opponent+m.venue).toLowerCase().indexOf(txt)===-1)return false;
      return true;
    }).sort(function(a,b){return view==='results'?(a.date<b.date?1:-1):(a.date<b.date?-1:1);});
    out.innerHTML=list.length?list.map(matchCard).join(''):
      '<div class="empty"><h4>Nothing scheduled here yet</h4><p>Fixtures go up as soon as the league confirms them. <a href="news.html">Announcements</a> carry any changes.</p></div>';
    if(location.hash){var el=document.getElementById(location.hash.slice(1)); if(el) el.scrollIntoView({block:'center'});}
  }

  C.$$('#sched-tabs button').forEach(function(b){
    b.addEventListener('click',function(){
      C.$$('#sched-tabs button').forEach(function(x){x.classList.remove('on');});
      b.classList.add('on'); view=b.dataset.view; render();
    });
  });
  ft.addEventListener('change',function(){team=ft.value;render();});
  document.getElementById('f-search').addEventListener('input',function(e){q=e.target.value;render();});
  render();
})();
</script>"""

shell("schedule.html", "Match Schedule &amp; Training Calendar | Coach Arnold Academy",
      "Upcoming soccer matches, results and open training sessions in Camas and Vancouver, WA. Players and parents can confirm match availability online.",
      sched_body, extra_js=sched_js)

print("team pages built")
