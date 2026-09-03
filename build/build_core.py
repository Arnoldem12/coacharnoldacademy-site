from shared import shell, ld, page_hero, LOCAL_BUSINESS, SITE

# ----------------------------------------------------------------- HOME
home_body = """
<section class="hero" data-pitch>
  <div class="glow"></div>
  <div class="wrap inner hero-anim">
    <span class="kicker"><i></i> US Soccer licensed coaching in Camas, Vancouver and Portland</span>
    <h1>Develop your skills. Build your confidence. Elevate your game.</h1>
    <p class="lede">Personalised soccer coaching, group training, team development and competitive playing opportunities for youth and adults.</p>
    <div class="btn-row">
      <a class="btn" href="book.html">Book a training session</a>
      <a class="btn ghost" href="teams.html">Join a team</a>
      <a class="btn ghost" href="contact.html">Contact Coach Arnold</a>
    </div>
    <p class="small" style="color:#8FA1C4;margin-top:1.2rem">First session includes a written baseline of where the player is now and what we work on next.</p>
  </div>
  <div class="hero-strip">
    <div class="wrap"><div class="grid" style="gap:1px">
      <div class="cell"><span class="n">10</span><span class="l">Coaching programs, from first touch to tactical work</span></div>
      <div class="cell"><span class="n">5+</span><span class="l">Ages five through adult, beginner through competitive</span></div>
      <div class="cell"><span class="n">1:1</span><span class="l">Private sessions, small groups capped at six</span></div>
      <div class="cell"><span class="n">4</span><span class="l">Cities served across Washington and Oregon</span></div>
    </div></div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="reveal">
      <div class="head"><span class="rule"></span><h2>A coach who plans the session before you arrive</h2></div>
      <p class="lede">Coach Arnold Academy exists to help players get measurably better and enjoy the game enough to keep playing it. That means proper technical work, tactical understanding taught in plain language, and an environment where a nervous eight-year-old and a thirty-five-year-old beginner both feel able to try something and get it wrong.</p>
      <p>Every player starts with a baseline session so we agree on what we're actually working on. From there you get a session plan, honest feedback and something specific to practise between sessions. Parents get a short written note at the end of each block rather than a vague thumbs up at the car park.</p>
      <div class="btn-row">
        <a class="btn" href="about.html">Meet Coach Arnold</a>
        <a class="btn dark-ghost" href="programs.html">Find the right program</a>
      </div>
    </div>
    <div class="reveal">
      <div class="tile">
        <h3>What you can expect</h3>
        <div class="feature" style="margin-bottom:1.1rem"><h3>Licensed and screened</h3><p>US Soccer coaching licences, SafeSport trained and background checked. Documentation available to parents on request.</p></div>
        <div class="feature" style="margin-bottom:1.1rem"><h3>Small numbers</h3><p>Private sessions are one player. Small groups stop at six. Nobody stands in a queue waiting for a turn.</p></div>
        <div class="feature" style="margin-bottom:1.1rem"><h3>Written feedback</h3><p>Two or three specific targets per player, revisited every session so progress is visible.</p></div>
        <div class="feature"><h3>Flexible scheduling</h3><p>Evenings and weekends, indoor through winter, and free rescheduling with 24 hours' notice.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="paper">
  <div class="wrap">
    <div class="head reveal"><span class="rule"></span><h2>Coaching programs</h2>
      <p>Ten programs covering technique, tactics, fitness and match preparation. Not sure which fits? Send a message and describe the player.</p></div>
    <div class="grid g3" id="home-programs"></div>
    <div class="btn-row"><a class="btn" href="programs.html">See all ten programs</a><a class="btn dark-ghost" href="contact.html">Ask which one fits</a></div>
  </div>
</section>

<section class="ink">
  <div class="wrap">
    <div class="head reveal"><span class="rule"></span><h2>Reasons to train here</h2></div>
    <div class="grid g2">
      <div class="feature reveal"><h3>Confidence is coached, not assumed</h3><p>Players who are afraid of making mistakes stop asking for the ball. Sessions are built so that trying something difficult is the point, not the risk.</p></div>
      <div class="feature reveal"><h3>Technique taught properly</h3><p>Body shape, plant foot, contact point, scanning before receiving. Details that hold up when the game speeds up.</p></div>
      <div class="feature reveal"><h3>The game explained in plain language</h3><p>Why we press here, why we drop there, what your run does for the player next to you. Understanding makes decisions faster.</p></div>
      <div class="feature reveal"><h3>Adults are genuinely welcome</h3><p>Beginners, returning players and league regulars train in dedicated adult sessions, not squeezed into a youth group.</p></div>
      <div class="feature reveal"><h3>A route into a team</h3><p>Players who want competitive minutes can apply to an academy team or to Obsidian AC, the adult indoor side.</p></div>
      <div class="feature reveal"><h3>Straightforward admin</h3><p>Book online, pay online or in person, get a confirmation email and add the session to your calendar in one tap.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="head reveal"><span class="rule"></span><h2>Upcoming sessions and matches</h2>
      <p>Open training slots and the next fixtures. Full calendar on the schedule page.</p></div>
    <div class="split">
      <div>
        <h3 style="font-size:1.2rem">Training with spaces</h3>
        <div class="rows" id="home-trainings"></div>
      </div>
      <div>
        <h3 style="font-size:1.2rem">Next matches</h3>
        <div class="rows" id="home-matches"></div>
      </div>
    </div>
    <div class="btn-row"><a class="btn" href="schedule.html">View upcoming matches</a><a class="btn dark-ghost" href="book.html">Book your first session</a></div>
  </div>
</section>

<section class="ink" id="obsidian">
  <div class="wrap split">
    <div class="reveal">
      <div class="head"><span class="rule"></span><h2>Obsidian AC</h2></div>
      <p class="lede">The academy's adult indoor side. Competitive league nights, a proper training session every Wednesday, and a squad that turns up.</p>
      <p>Obsidian AC is currently recruiting a goalkeeper, a centre back and a wide midfielder for the winter indoor season. Applications go through a short form, and suitable players are invited to train with the squad before committing to anything.</p>
      <div class="btn-row">
        <a class="btn" href="obsidian-ac.html">Apply for Obsidian AC</a>
        <a class="btn ghost" href="schedule.html?team=obsidian-ac">See the fixtures</a>
      </div>
    </div>
    <div class="reveal">
      <div class="tile">
        <div style="display:flex;gap:1rem;align-items:center;margin-bottom:1rem">
          <span class="badge-crest">OAC</span>
          <div><h3 style="margin:0">Obsidian AC</h3><p class="meta" style="margin:0">Adult co-ed indoor · Riverview Indoor Arena, Vancouver WA</p></div>
        </div>
        <div class="rows" id="obsidian-mini"></div>
        <div class="foot"><a class="btn sm ghost" href="obsidian-ac.html">Team page</a><a class="btn sm ghost" href="join-team.html?team=obsidian-ac">Apply to join</a></div>
      </div>
    </div>
  </div>
</section>

<section class="paper">
  <div class="wrap">
    <div class="head reveal"><span class="rule"></span><h2>Training videos</h2>
      <p>Short, specific drills you can run at home with one ball. New videos through the season on the academy YouTube channel.</p></div>
    <div class="grid g3" id="home-videos"></div>
    <div class="btn-row"><a class="btn" href="videos.html">Watch training videos</a>
      <a class="btn dark-ghost" id="yt-sub" href="#" target="_blank" rel="noopener">Subscribe on YouTube</a></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="head reveal"><span class="rule"></span><h2>What players and parents say</h2></div>
    <div class="grid g3" id="home-quotes"></div>
    <div class="btn-row"><a class="btn dark-ghost" href="testimonials.html">Read more</a></div>
  </div>
</section>

<section class="paper tight">
  <div class="wrap">
    <div class="head reveal"><span class="rule"></span><h2>Follow the academy</h2>
      <p>Session clips, match nights and announcements go out on Instagram and Facebook first.</p></div>
    <div class="grid g2">
      <div class="tile"><h3>Instagram</h3><p class="meta">@coacharnoldacademy</p>
        <p>Training clips, drill breakdowns and match-day photos.</p>
        <div class="foot"><a class="btn sm" id="ig-link" href="#" target="_blank" rel="noopener">Open Instagram</a></div>
        <p class="small muted" style="margin-top:.8rem">To embed the live feed here, add an Instagram Basic Display or third-party feed embed. See the README, section "Social embeds".</p></div>
      <div class="tile"><h3>Facebook</h3><p class="meta">Coach Arnold Academy</p>
        <p>Longer updates, registration windows and community news.</p>
        <div class="foot"><a class="btn sm" id="fb-link" href="#" target="_blank" rel="noopener">Open Facebook</a></div>
        <p class="small muted" style="margin-top:.8rem">The Facebook Page plugin iframe can be dropped straight into this card once the page URL is confirmed.</p></div>
    </div>
  </div>
</section>

<section class="ink">
  <div class="wrap" style="text-align:center">
    <div class="head" style="margin-inline:auto;text-align:center">
      <span class="rule" style="margin-inline:auto"></span>
      <h2>Start your development</h2>
      <p style="margin-inline:auto">Book a first session, apply to a team, or just send a message describing the player and Coach Arnold will tell you honestly where to start.</p>
    </div>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="book.html">Book your first session</a>
      <a class="btn ghost" href="join-team.html">Apply to a team</a>
      <a class="btn ghost" href="contact.html">Contact Coach Arnold</a>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap-n">
    <div class="tile">
      <h3>Announcements and newsletter</h3>
      <p class="meta">Session openings, registration windows and match news. Roughly two emails a month, no spam, unsubscribe any time.</p>
      <form class="form" data-form="newsletter" data-success-title="You're on the list"
            data-success="A confirmation email is on its way. If it doesn't arrive within a few minutes, check your spam folder and add the academy address to your contacts."
            data-toast="Subscribed to academy updates">
        <div class="msg" tabindex="-1"></div>
        <div class="fgrid">
          <div class="field"><label for="nl-name">Your name</label><input id="nl-name" name="name" required autocomplete="name"></div>
          <div class="field"><label for="nl-email">Email address</label><input id="nl-email" name="email" type="email" required autocomplete="email"></div>
        </div>
        <div class="field"><span class="lbl">What are you interested in?</span>
          <div class="opts">
            <label><input type="checkbox" name="interests" value="Youth coaching"> Youth coaching</label>
            <label><input type="checkbox" name="interests" value="Adult training"> Adult training</label>
            <label><input type="checkbox" name="interests" value="Teams and matches"> Teams and matches</label>
            <label><input type="checkbox" name="interests" value="Training videos"> Training videos</label>
          </div></div>
        <div class="check"><input id="nl-ok" type="checkbox" name="consent" required>
          <label for="nl-ok">I agree to receive email updates from Coach Arnold Academy and I've read the <a href="privacy.html">privacy policy</a>.</label></div>
        <div><button class="btn" type="submit">Sign up for updates</button></div>
      </form>
    </div>
  </div>
</section>
"""

home_js = """<script>
(function(){
  var C=window.CAA, D=C.D;
  document.getElementById('ig-link').href=D.site.instagram;
  document.getElementById('fb-link').href=D.site.facebook;
  document.getElementById('yt-sub').href=D.site.youtube;

  var picks=['private','small-group','youth','adult','team','virtual'];
  document.getElementById('home-programs').innerHTML=picks.map(function(id){
    var p=D.programs.find(function(x){return x.id===id;});
    return '<article class="tile reveal"><h3>'+C.esc(p.name)+'</h3>'+
      '<p class="meta">'+C.esc(p.ages)+' · '+C.esc(p.duration)+' · '+C.esc(p.price)+'</p>'+
      '<p>'+C.esc(p.short)+'</p>'+
      '<div class="foot"><a class="btn sm" href="program.html?id='+p.id+'">Details</a>'+
      '<a class="btn sm dark-ghost" href="book.html?program='+p.id+'">Book now</a></div></article>';
  }).join('');

  var today=new Date(); today.setHours(0,0,0,0);
  var t=D.trainings.filter(function(x){return C.dparse(x.date)>=today;}).slice(0,4);
  document.getElementById('home-trainings').innerHTML = t.length? t.map(function(x){
    var d=C.dparse(x.date);
    return '<div class="row"><div class="date"><span class="d">'+d.getDate()+'</span><span class="m">'+
      ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'][d.getMonth()]+'</span></div>'+
      '<div><div class="t">'+C.esc(C.progName(x.program))+'</div><div class="s">'+C.fmtTime(x.time)+' · '+C.esc(C.locName(x.location))+
      ' · <span class="chip ok">'+x.spaces+' spaces</span></div></div>'+
      '<div class="act"><a class="btn sm dark-ghost" href="book.html?program='+x.program+'&date='+x.date+'&time='+x.time+'">Book</a></div></div>';
  }).join('') : '<div class="empty"><h4>No open sessions listed</h4><p>New slots go up every Sunday. Message Coach Arnold to be told first.</p></div>';

  var m=D.matches.filter(function(x){return x.status!=='completed';})
    .sort(function(a,b){return a.date<b.date?-1:1;}).slice(0,4);
  document.getElementById('home-matches').innerHTML=m.map(function(x){
    var d=C.dparse(x.date);
    return '<div class="row"><div class="date"><span class="d">'+d.getDate()+'</span><span class="m">'+
      ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'][d.getMonth()]+'</span></div>'+
      '<div><div class="t">'+C.esc(C.teamName(x.team))+' v '+C.esc(x.opponent)+'</div>'+
      '<div class="s">'+C.fmtTime(x.kick)+' · '+C.esc(x.venue)+' · '+(x.home?'Home':'Away')+'</div></div>'+
      '<div class="act"><a class="btn sm dark-ghost" href="schedule.html#'+x.id+'">Details</a></div></div>';
  }).join('');

  document.getElementById('obsidian-mini').innerHTML=D.matches.filter(function(x){
    return x.team==='obsidian-ac';}).slice(0,3).map(function(x){
    var d=C.dparse(x.date);
    return '<div class="row"><div class="date"><span class="d">'+d.getDate()+'</span><span class="m">'+
      ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'][d.getMonth()]+'</span></div>'+
      '<div><div class="t">'+C.esc(x.opponent)+'</div><div class="s">'+(x.status==='completed'?C.esc(x.score||'Result to follow'):C.fmtTime(x.kick)+' · '+(x.home?'Home':'Away'))+'</div></div></div>';
  }).join('');

  document.getElementById('home-videos').innerHTML=D.videos.slice(0,3).map(function(v){
    return '<article class="tile reveal"><a class="vthumb" href="video.html?id='+v.id+'" aria-label="Watch: '+C.esc(v.title)+'"><span class="play">&#9654;</span></a>'+
      '<h3 style="margin-top:1rem;font-size:1.15rem">'+C.esc(v.title)+'</h3>'+
      '<p class="meta">'+C.esc(v.cat)+' · '+C.esc(v.level)+'</p><p>'+C.esc(v.desc)+'</p>'+
      '<div class="foot"><a class="btn sm dark-ghost" href="video.html?id='+v.id+'">Open video</a></div></article>';
  }).join('');

  document.getElementById('home-quotes').innerHTML=D.testimonials.slice(0,3).map(function(q){
    return '<div class="tile reveal"><blockquote class="quote"><p>'+C.esc(q.q)+'</p><cite>'+C.esc(q.a)+' · '+C.esc(q.role)+'</cite></blockquote></div>';
  }).join('');

  C.wireReveal();
})();
</script>"""

shell("index.html",
      "Soccer Coach in Camas &amp; Vancouver WA | Coach Arnold Academy",
      "US Soccer licensed private and group soccer coaching for kids, teens and adults in Camas, Vancouver and Portland. Book a training session, join a team or apply for Obsidian AC.",
      home_body, jsonld=ld(LOCAL_BUSINESS), extra_js=home_js)

# ----------------------------------------------------------------- ABOUT
about_body = page_hero("About", "Coach Arnold",
  "Arnold Eoka Mambe is a US Soccer licensed coach working with youth and adult players across Camas, Vancouver, Washougal and the Portland metro area.",
  '<a class="btn" href="book.html">Book a session</a><a class="btn ghost" href="contact.html">Ask a question</a>') + """
<section>
  <div class="wrap split">
    <div>
      <div class="head"><span class="rule"></span><h2>Coaching philosophy</h2></div>
      <p class="lede">Confident players make better decisions. Everything else follows from that.</p>
      <p>A player who is worried about making a mistake will hide: they will take the safe pass, avoid the one against one, and stop asking for the ball in tight areas. No amount of technical work fixes that on its own. So sessions are designed so that attempting the difficult thing is the point, mistakes are expected out loud, and the coaching happens in the moment rather than as a lecture afterwards.</p>
      <p>On top of that foundation, the work is deliberately old-fashioned: technique repeated until it is reliable, tactical ideas explained in plain language and then played at speed, and standards for effort and behaviour that apply to a six-year-old and a thirty-year-old equally. Players are told the truth about where they are, and given something specific to do about it.</p>
      <p><strong>The six things every session is measured against:</strong></p>
      <div class="grid g2" style="margin:1.2rem 0 1.6rem">
        <div class="feature"><h3>Confidence</h3><p>Did the player try something they would normally avoid?</p></div>
        <div class="feature"><h3>Technical development</h3><p>Was there enough quality repetition to change a habit?</p></div>
        <div class="feature"><h3>Tactical understanding</h3><p>Can the player explain why, not just what?</p></div>
        <div class="feature"><h3>Discipline</h3><p>Punctuality, effort, respect for teammates and officials.</p></div>
        <div class="feature"><h3>Enjoyment</h3><p>Would they want to come back next week?</p></div>
        <div class="feature"><h3>Teamwork and growth</h3><p>Did they make the players around them better?</p></div>
      </div>
      <hr>

      <div class="head"><span class="rule"></span><h2>Playing experience</h2></div>
      <p class="notice"><strong>Coach Arnold, replace this section.</strong> Add your playing history here: clubs, levels, positions, countries and years. Two or three short paragraphs is plenty. Parents read this section closely, so specifics matter more than adjectives.</p>
      <p>Arnold grew up playing the game and continues to play competitively, which keeps the coaching grounded in what actually happens on a pitch rather than what looks tidy on a whiteboard.</p>
      <hr>

      <div class="head"><span class="rule"></span><h2>Coaching experience</h2></div>
      <p class="notice"><strong>Replace with your real history.</strong> List the clubs, schools, camps and age groups you have coached, with approximate years. Include adult and youth work separately.</p>
      <p>Coaching work spans youth development from age five, competitive youth teams, adult beginners returning to the game, and team-level sessions run alongside existing club staff. Arnold also manages Obsidian AC, the academy's adult indoor side.</p>
      <hr>

      <div class="head"><span class="rule"></span><h2>Working with youth and adults</h2></div>
      <p>Children and adults fail differently. A ten-year-old who loses the ball three times in a row usually needs the exercise adjusted so they can succeed and rebuild. An adult beginner usually needs to be told plainly that the technique is wrong, shown the fix, and then left alone to repeat it without an audience. Sessions are grouped by age and stage for exactly this reason, and adults never train inside a youth group.</p>
      <p>For minors, a parent or guardian completes registration, consent and medical information, and is welcome to watch any session. Communication about a minor always goes through the parent account.</p>
      <hr>

      <div class="head"><span class="rule"></span><h2>Mission and values</h2></div>
      <p class="lede">To help every player who walks onto the pitch leave more capable and more confident than when they arrived, and to make organised soccer available to families and adults who have been priced or intimidated out of it.</p>
      <ul>
        <li><strong>Honesty.</strong> Players are told where they actually are, kindly and clearly.</li>
        <li><strong>Preparation.</strong> Every session is planned before anyone arrives.</li>
        <li><strong>Safety.</strong> SafeSport standards, background screening, and concussion protocols that are followed rather than filed.</li>
        <li><strong>Access.</strong> Group pricing and blocks that keep quality coaching within reach.</li>
        <li><strong>Respect.</strong> For teammates, opponents, officials and the game.</li>
      </ul>
    </div>

    <div>
      <div class="tile" style="margin-bottom:1.2rem">
        <h3>Credentials</h3>
        <p class="meta">Verified with US Soccer. Documentation available to parents on request.</p>
        <ul style="padding-left:1.1rem;font-size:.96rem">
          <li>US Soccer licensed coach</li>
          <li>US Soccer Grassroots coaching education, 7v7 and 9v9 pathways</li>
          <li>SafeSport trained</li>
          <li>Background screened through US Soccer Learning Center</li>
          <li>Concussion and player safety certified</li>
          <li>First aid and CPR <span class="chip warn">confirm current date</span></li>
        </ul>
        <p class="small muted">Coach Arnold's US Soccer coaching ID is held on file and shown on request. It is deliberately not published on this website.</p>
      </div>

      <div class="tile" style="margin-bottom:1.2rem">
        <h3>Professional photos</h3>
        <p class="meta">Replace these three placeholders with real photography.</p>
        <div class="grid" style="grid-template-columns:1fr 1fr;gap:.6rem">
          <div style="aspect-ratio:1;background:var(--paper);border:2px dashed var(--line-d);border-radius:var(--r-sm);display:grid;place-items:center;font-size:.8rem;color:var(--muted-d);text-align:center;padding:.5rem">Coaching a session</div>
          <div style="aspect-ratio:1;background:var(--paper);border:2px dashed var(--line-d);border-radius:var(--r-sm);display:grid;place-items:center;font-size:.8rem;color:var(--muted-d);text-align:center;padding:.5rem">Portrait in academy kit</div>
          <div style="aspect-ratio:1;background:var(--paper);border:2px dashed var(--line-d);border-radius:var(--r-sm);display:grid;place-items:center;font-size:.8rem;color:var(--muted-d);text-align:center;padding:.5rem;grid-column:1/-1">On the touchline with a team</div>
        </div>
        <p class="small muted" style="margin-top:.7rem">Save images into <code>assets/img/</code> and swap the placeholder blocks for <code>&lt;img&gt;</code> tags.</p>
      </div>

      <div class="tile">
        <h3>Service area</h3>
        <p data-site-area></p>
        <div class="foot">
          <a class="btn sm" href="book.html">Book a session</a>
          <a class="btn sm dark-ghost" data-wa="Hi Coach Arnold, I read your about page and I'd like to ask about " target="_blank" rel="noopener" href="#">WhatsApp</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

person_ld = ld("""{
 "@context":"https://schema.org","@type":"Person","name":"Arnold Eoka Mambe",
 "jobTitle":"US Soccer licensed soccer coach",
 "worksFor":{"@type":"Organization","name":"Coach Arnold Academy"},
 "areaServed":"Camas, Vancouver, Washougal WA and Portland OR",
 "url":"%s/about.html"}""" % SITE)

shell("about.html", "About Coach Arnold | US Soccer Licensed Coach, Camas WA",
      "Arnold Eoka Mambe is a US Soccer licensed coach in Camas, Washington. Coaching philosophy, playing and coaching experience, licences and safety credentials.",
      about_body, jsonld=person_ld, og_type="profile")

# ----------------------------------------------------------------- PROGRAMS
programs_body = page_hero("Coaching programs", "Coaching programs",
  "Ten programs covering technique, tactics, fitness, position work and match preparation, for players from age five through adult.",
  '<a class="btn" href="book.html">Book a training session</a><a class="btn ghost" href="contact.html">Ask which program fits</a>') + """
<section>
  <div class="wrap">
    <div class="tabs" id="prog-filter" role="tablist" aria-label="Filter programs"></div>
    <div class="grid g3" id="prog-list"></div>
    <div class="notice" style="margin-top:2rem"><strong>Not sure where to start?</strong>
      <p>Describe the player, their age and how much they have played, and Coach Arnold will recommend a program and be honest if a cheaper option would serve you better. <a href="contact.html">Send a message</a> or <a data-wa="Hi Coach Arnold, I'm trying to work out which program fits. The player is " href="#" target="_blank" rel="noopener">ask on WhatsApp</a>.</p></div>
  </div>
</section>

<section class="paper">
  <div class="wrap">
    <div class="head"><span class="rule"></span><h2>Packages and pricing</h2>
      <p>Single sessions are pay as you go. Blocks reduce the per-session rate and hold your regular slot.</p></div>
    <div class="grid g3">
      <div class="tile"><h3>Single session</h3><p class="meta">No commitment</p><p>Pay per session at the rate listed on each program. Useful for a first session or an occasional top-up.</p></div>
      <div class="tile"><h3>Five session block</h3><p class="meta">Around 10% lower per session</p><p>Five sessions to use within ten weeks, with a held slot each week and written progress notes at the end.</p></div>
      <div class="tile"><h3>Ten session block</h3><p class="meta">Around 15% lower per session</p><p>A full development block with a baseline assessment, mid-block review and a written plan for the next stage.</p></div>
      <div class="tile"><h3>Monthly membership</h3><p class="meta">Group programs only</p><p>Unlimited access to a nominated group program for a monthly fee, billed on the same date each month and cancellable with 30 days' notice.</p></div>
      <div class="tile"><h3>Team blocks</h3><p class="meta">Contact for pricing</p><p>Priced per session or per season depending on squad size, venue and how many sessions your staff want covered.</p></div>
      <div class="tile"><h3>Sibling and referral discounts</h3><p class="meta">Applied at checkout</p><p>Discount codes are issued for siblings training in the same block and for families who refer a new player.</p></div>
    </div>
    <p class="small muted" style="margin-top:1.2rem">Prices shown across the site are sample figures. <strong>Coach Arnold must confirm final pricing in <code>assets/js/data.js</code> or through the admin dashboard before launch.</strong></p>
  </div>
</section>
"""

programs_js = """<script>
(function(){
  var C=window.CAA,D=C.D,cats=['All programs','Youth','Adult','Team','Online'];
  var active='All programs';
  function match(p){
    if(active==='All programs')return true;
    if(active==='Youth')return ['youth','small-group','technical','position','conditioning','private'].indexOf(p.id)>-1;
    if(active==='Adult')return ['adult','private','tactical','conditioning','position','technical'].indexOf(p.id)>-1;
    if(active==='Team')return ['team','tactical'].indexOf(p.id)>-1;
    if(active==='Online')return p.id==='virtual';
    return true;
  }
  function render(){
    document.getElementById('prog-list').innerHTML=D.programs.slice().sort(function(a,b){return a.order-b.order;})
      .filter(match).map(function(p){
      return '<article class="tile"><h3>'+C.esc(p.name)+'</h3>'+
        '<p class="meta">'+C.esc(p.ages)+' · '+C.esc(p.duration)+' · max '+C.esc(p.max)+'</p>'+
        '<p>'+C.esc(p.short)+'</p>'+
        '<p class="meta"><span class="chip">'+C.esc(p.price)+'</span> <span class="chip">'+C.esc(p.level)+'</span></p>'+
        '<div class="foot"><a class="btn sm" href="program.html?id='+p.id+'">Program details</a>'+
        '<a class="btn sm dark-ghost" href="book.html?program='+p.id+'">Book now</a></div></article>';
    }).join('');
  }
  document.getElementById('prog-filter').innerHTML=cats.map(function(c,i){
    return '<button type="button" role="tab" class="'+(i===0?'on':'')+'">'+c+'</button>';}).join('');
  C.$$('#prog-filter button').forEach(function(b){
    b.addEventListener('click',function(){
      C.$$('#prog-filter button').forEach(function(x){x.classList.remove('on');});
      b.classList.add('on'); active=b.textContent; render();
    });
  });
  render();
})();
</script>"""

shell("programs.html", "Soccer Coaching Programs | Youth &amp; Adult Training in Vancouver WA",
      "Private one-on-one coaching, small-group training, youth development, adult soccer, team sessions, goalkeeping, tactics and video analysis in Camas and Vancouver, WA.",
      programs_body, extra_js=programs_js)

# ----------------------------------------------------------------- PROGRAM DETAIL
program_body = """
<section class="page-hero" data-pitch>
  <div class="wrap inner">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / <a href="programs.html">Programs</a> / <span id="crumb">Program</span></nav>
    <h1 id="p-name">Program</h1>
    <p class="lede" id="p-short"></p>
    <div class="btn-row"><a class="btn" id="p-book" href="book.html">Book now</a>
      <a class="btn ghost" id="p-ask" href="#">Ask a question</a></div>
  </div>
</section>
<section>
  <div class="wrap split">
    <div>
      <div id="p-body"></div>
      <h3>What the player will learn</h3>
      <ul id="p-learn" style="padding-left:1.1rem"></ul>
      <h3 style="margin-top:2rem">Available dates and times</h3>
      <p class="muted" style="font-size:.95rem">Regular weekly slots. Exact availability is confirmed when you book, and one-off times can be arranged.</p>
      <div class="opts" id="p-slots" style="margin-bottom:1.4rem"></div>
      <div class="btn-row"><a class="btn" id="p-book2" href="book.html">Book this program</a>
        <a class="btn dark-ghost" href="programs.html">Compare other programs</a></div>
    </div>
    <div>
      <div class="tile" style="margin-bottom:1.2rem">
        <h3>At a glance</h3>
        <div class="tablewrap"><table><tbody id="p-facts"></tbody></table></div>
      </div>
      <div class="tile" style="margin-bottom:1.2rem">
        <h3>Training locations</h3>
        <div id="p-locs"></div>
      </div>
      <div class="tile">
        <h3>Questions before booking?</h3>
        <p class="meta">Coach Arnold answers these himself, usually within a day.</p>
        <form class="form" data-form="questions" data-success-title="Question sent"
              data-success="Coach Arnold has your question and will reply by email, usually within 24 hours."
              data-toast="Question sent to Coach Arnold">
          <div class="msg" tabindex="-1"></div>
          <input type="hidden" name="program" id="q-prog">
          <div class="field"><label for="q-name">Your name</label><input id="q-name" name="name" required autocomplete="name"></div>
          <div class="field"><label for="q-email">Email</label><input id="q-email" name="email" type="email" required autocomplete="email"></div>
          <div class="field"><label for="q-msg">Your question</label><textarea id="q-msg" name="message" required placeholder="Tell me about the player: age, how long they've played, and what you're hoping to work on."></textarea></div>
          <button class="btn wide" type="submit">Ask a question</button>
        </form>
      </div>
    </div>
  </div>
</section>
"""

program_js = """<script>
(function(){
  var C=window.CAA,D=C.D;
  var id=C.qs('id')||'private';
  var p=D.programs.find(function(x){return x.id===id;});
  if(!p){location.replace('programs.html');return;}
  document.title=p.name+' | Coach Arnold Academy';
  var md=document.querySelector('meta[name=description]'); if(md) md.content=p.short;
  document.getElementById('crumb').textContent=p.name;
  document.getElementById('p-name').textContent=p.name;
  document.getElementById('p-short').textContent=p.short;
  document.getElementById('p-body').innerHTML='<p class="lede">'+C.esc(p.body)+'</p>';
  document.getElementById('p-learn').innerHTML=p.learn.map(function(l){return '<li>'+C.esc(l)+'</li>';}).join('');
  document.getElementById('p-slots').innerHTML=p.slots.map(function(s){
    return '<label><input type="radio" name="slotview" value="'+C.esc(s)+'"> '+C.esc(s)+'</label>';}).join('');
  document.getElementById('p-facts').innerHTML=
    [['Recommended age',p.ages],['Skill level',p.level],['Session length',p.duration],
     ['Maximum players',p.max],['Price',p.price]].map(function(r){
      return '<tr><th scope="row">'+r[0]+'</th><td>'+C.esc(r[1])+'</td></tr>';}).join('');
  document.getElementById('p-locs').innerHTML=p.locations.map(function(lid){
    var l=D.locations.find(function(x){return x.id===lid;});
    return '<div class="feature" style="margin-bottom:.9rem"><h3>'+C.esc(l.name)+'</h3><p>'+C.esc(l.city)+'. '+C.esc(l.note)+'</p></div>';
  }).join('');
  document.getElementById('p-book').href='book.html?program='+p.id;
  document.getElementById('p-book2').href='book.html?program='+p.id;
  document.getElementById('p-ask').href=C.waLink("Hi Coach Arnold, I'd like to ask about "+p.name+": ");
  document.getElementById('q-prog').value=p.name;
})();
</script>"""

shell("program.html", "Program details | Coach Arnold Academy",
      "Full details for each Coach Arnold Academy coaching program: ages, session length, group size, what the player will learn, locations and pricing.",
      program_body, extra_js=program_js)

# ----------------------------------------------------------------- BOOK
book_body = page_hero("Book training", "Book a training session",
  "Pick a program, choose a time, tell Coach Arnold about the player, and you're done. Registration for anyone under 18 must be completed by a parent or legal guardian.") + """
<section>
  <div class="wrap-n">
    <div class="steps" aria-hidden="true">
      <span class="on">1. Program</span><span class="on">2. Player</span><span class="on">3. Health and consent</span><span class="on">4. Payment</span>
    </div>

    <form class="form" id="booking" data-form="bookings" data-reset="no"
          data-success-title="Session requested"
          data-success="Your request is with Coach Arnold. You'll get a confirmation email with the exact field, what to bring and a calendar link. Sessions are confirmed rather than instant, so if the slot has gone you'll be offered the nearest alternative."
          data-toast="Booking request sent" data-after="afterBooking">
      <div class="msg" tabindex="-1"></div>

      <fieldset>
        <legend>1. Choose your session</legend>
        <div class="fgrid">
          <div class="field"><label for="b-prog">Coaching program</label>
            <select id="b-prog" name="program" required></select></div>
          <div class="field"><label for="b-type">Session type</label>
            <select id="b-type" name="sessionType" required>
              <option value="">Choose one</option>
              <option>Private, one player</option>
              <option>Group session</option>
              <option>Pair, two players sharing</option>
              <option>Team session</option>
            </select></div>
          <div class="field"><label for="b-date">Preferred date</label>
            <input id="b-date" name="date" type="date" required></div>
          <div class="field"><label for="b-time">Preferred time</label>
            <input id="b-time" name="time" type="time" required></div>
          <div class="field"><label for="b-loc">Training location</label>
            <select id="b-loc" name="location" required></select></div>
          <div class="field"><label for="b-alt">Backup time that also works</label>
            <input id="b-alt" name="altTime" placeholder="For example: Saturday morning"></div>
        </div>
        <p class="hint" id="b-prog-note" style="margin-top:.7rem"></p>
      </fieldset>

      <fieldset>
        <legend>2. Player details</legend>
        <div class="fgrid">
          <div class="field"><label for="b-pname">Player's full name</label><input id="b-pname" name="playerName" required></div>
          <div class="field"><label for="b-page">Player's age</label><input id="b-page" name="playerAge" type="number" min="4" max="80" required></div>
          <div class="field"><label for="b-level">Current skill level</label>
            <select id="b-level" name="level" required>
              <option value="">Choose one</option>
              <option>Complete beginner, never played</option>
              <option>Beginner, played a little</option>
              <option>Recreational or school team</option>
              <option>Club or select level</option>
              <option>Competitive or high school varsity</option>
              <option>Adult league</option>
            </select></div>
          <div class="field"><label for="b-pos">Usual position</label>
            <select id="b-pos" name="position">
              <option value="">Not sure yet</option>
              <option>Goalkeeper</option><option>Defender</option><option>Midfielder</option><option>Forward</option><option>Anywhere</option>
            </select></div>
        </div>
        <div class="field" style="margin-top:1rem"><label for="b-goals">What would you like to work on?</label>
          <textarea id="b-goals" name="goals" required placeholder="For example: first touch under pressure, confidence in games, getting fit for adult league, preparing for club tryouts."></textarea>
          <p class="hint">Be specific if you can. It shapes the first session plan.</p></div>
      </fieldset>

      <fieldset>
        <legend>3. Who is booking?</legend>
        <div class="field"><span class="lbl">Is the player under 18?</span>
          <div class="opts">
            <label><input type="radio" name="isMinor" value="yes" required> Yes, I'm the parent or legal guardian</label>
            <label><input type="radio" name="isMinor" value="no"> No, I'm booking for myself as an adult</label>
          </div></div>
        <div class="fgrid" style="margin-top:1rem">
          <div class="field"><label for="b-cname">Your full name</label><input id="b-cname" name="contactName" required autocomplete="name"></div>
          <div class="field"><label for="b-cemail">Email address</label><input id="b-cemail" name="contactEmail" type="email" required autocomplete="email"></div>
          <div class="field"><label for="b-cphone">Phone number</label><input id="b-cphone" name="contactPhone" type="tel" required autocomplete="tel"></div>
          <div class="field"><label for="b-cwa">WhatsApp number</label><input id="b-cwa" name="whatsapp" type="tel" placeholder="Optional, if different from your phone"></div>
        </div>
        <div id="guardian-block" style="display:none;margin-top:1rem">
          <div class="fgrid">
            <div class="field"><label for="b-rel">Relationship to the player</label><input id="b-rel" name="relationship" placeholder="Parent, guardian, grandparent"></div>
            <div class="field"><label for="b-em">Emergency contact name</label><input id="b-em" name="emergencyName"></div>
            <div class="field"><label for="b-emp">Emergency contact phone</label><input id="b-emp" name="emergencyPhone" type="tel"></div>
            <div class="field"><label for="b-em2">Second emergency contact</label><input id="b-em2" name="emergency2" placeholder="Name and phone, optional"></div>
          </div>
        </div>
      </fieldset>

      <fieldset>
        <legend>4. Health, injuries and accommodations</legend>
        <div class="field"><label for="b-med">Injuries, medical conditions, allergies or medication</label>
          <textarea id="b-med" name="medical" placeholder="Asthma and inhaler location, recent ankle sprain, ADHD, diabetes, allergies. Write none if there is nothing."></textarea>
          <p class="hint">Coach Arnold is the only person who sees this. It is stored so that the right decision can be made if something happens on the field.</p></div>
        <div class="field"><label for="b-accom">Accommodations that would help</label>
          <textarea id="b-accom" name="accommodations" placeholder="Optional. For example: clear one-step instructions, a quieter group, a break halfway through."></textarea></div>
      </fieldset>

      <fieldset>
        <legend>5. Consent and policies</legend>
        <div class="check"><input id="b-waiver" type="checkbox" name="waiver" required>
          <label for="b-waiver">I have read and accept the <a href="waiver.html" target="_blank">liability waiver</a> and the <a href="conduct.html" target="_blank">code of conduct</a>.</label></div>
        <div class="check"><input id="b-cancel" type="checkbox" name="cancellation" required>
          <label for="b-cancel">I understand the <a href="refunds.html" target="_blank">cancellation and refund policy</a>, including the 24-hour rescheduling window.</label></div>
        <div class="check"><input id="b-consent" type="checkbox" name="guardianConsent">
          <label for="b-consent">As parent or legal guardian, I consent to my child taking part in coaching sessions. <span class="muted">Required for players under 18.</span></label></div>
        <div class="check"><input id="b-photo" type="checkbox" name="photoConsent">
          <label for="b-photo">I consent to photos and video that may include the player being used on the academy website and social media. <span class="muted">Entirely optional. Saying no changes nothing about the coaching, and consent can be withdrawn at any time.</span></label></div>
        <div class="check"><input id="b-privacy" type="checkbox" name="privacy" required>
          <label for="b-privacy">I've read the <a href="privacy.html" target="_blank">privacy policy</a> and agree to my details being used to run this booking.</label></div>
      </fieldset>

      <fieldset>
        <legend>6. Payment</legend>
        <div class="field"><span class="lbl">How would you like to pay?</span>
          <div class="opts">
            <label><input type="radio" name="payment" value="Card online" required> Card online</label>
            <label><input type="radio" name="payment" value="Pay later"> Pay later, before the session</label>
            <label><input type="radio" name="payment" value="Use a package"> Use an existing package</label>
          </div></div>
        <div class="field" style="margin-top:1rem"><label for="b-code">Discount code</label>
          <input id="b-code" name="discount" placeholder="Optional"></div>
        <div class="notice" style="margin-top:1rem"><strong>Card payments are not live yet.</strong>
          <p>This form records your booking and your chosen payment method. Card checkout goes live when Stripe is connected. Until then, choose pay later and Coach Arnold will send a payment link with your confirmation. No card details are ever collected or stored by this website.</p></div>
      </fieldset>

      <div class="btn-row" style="margin-top:0">
        <button class="btn" type="submit">Confirm booking request</button>
        <a class="btn dark-ghost" href="programs.html">Back to programs</a>
      </div>
    </form>

    <div id="post-book" style="display:none;margin-top:1.6rem">
      <div class="tile">
        <h3>Add it to your calendar</h3>
        <p class="meta">A calendar invitation is also attached to your confirmation email.</p>
        <div class="btn-row" style="margin-top:.4rem">
          <a class="btn sm" id="cal-g" href="#" target="_blank" rel="noopener">Google Calendar</a>
          <button class="btn sm dark-ghost" id="cal-i" type="button">Apple Calendar or Outlook</button>
          <a class="btn sm dark-ghost" href="dashboard.html">See it in my dashboard</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="paper tight">
  <div class="wrap-n">
    <h2 style="font-size:1.6rem">Before your first session</h2>
    <div class="grid g2">
      <div class="feature"><h3>What to bring</h3><p>Boots or turf shoes, shin guards, water, and a ball if you have one. Spares are available.</p></div>
      <div class="feature"><h3>Arrive ten minutes early</h3><p>Enough time to meet, warm up properly and start on time.</p></div>
      <div class="feature"><h3>Parents are welcome to watch</h3><p>Stay for the whole session if you'd like. For younger players it often helps.</p></div>
      <div class="feature"><h3>Weather</h3><p>Sessions run in rain. If a field closes you'll be emailed and messaged, and rescheduled free.</p></div>
    </div>
  </div>
</section>
"""

book_js = """<script>
function afterBooking(rec){
  var C=window.CAA;
  var ev={title:'Soccer training: '+rec.program,date:rec.date,time:rec.time,minutes:75,
    location:C.locName(rec.location),
    details:'Coach Arnold Academy session for '+rec.playerName+'. Arrive 10 minutes early with boots, shin guards and water.'};
  var box=document.getElementById('post-book'); box.style.display='block';
  document.getElementById('cal-g').href=C.gcalLink(ev);
  document.getElementById('cal-i').onclick=function(){C.icsDownload(ev);};
}
(function(){
  var C=window.CAA,D=C.D;
  var sel=document.getElementById('b-prog');
  sel.innerHTML='<option value="">Choose a program</option>'+D.programs.slice().sort(function(a,b){return a.order-b.order;})
    .map(function(p){return '<option value="'+p.id+'">'+C.esc(p.name)+' — '+C.esc(p.price)+'</option>';}).join('');
  document.getElementById('b-loc').innerHTML='<option value="">Choose a location</option>'+
    D.locations.map(function(l){return '<option value="'+l.id+'">'+C.esc(l.name)+', '+C.esc(l.city)+'</option>';}).join('');

  var pre=C.qs('program'); if(pre) sel.value=pre;
  var pd=C.qs('date'); if(pd) document.getElementById('b-date').value=pd;
  var pt=C.qs('time'); if(pt) document.getElementById('b-time').value=pt;
  var today=new Date(); document.getElementById('b-date').min=today.toISOString().slice(0,10);

  function note(){
    var p=D.programs.find(function(x){return x.id===sel.value;});
    document.getElementById('b-prog-note').textContent = p ?
      (p.duration+' · '+p.ages+' · maximum '+p.max+' · '+p.price+'. Usual times: '+p.slots.join(', ')) : '';
  }
  sel.addEventListener('change',note); note();

  C.$$('input[name=isMinor]').forEach(function(r){
    r.addEventListener('change',function(){
      var minor=r.value==='yes'&&r.checked;
      document.getElementById('guardian-block').style.display=minor?'block':'none';
      ['b-rel','b-em','b-emp'].forEach(function(id){document.getElementById(id).required=minor;});
      document.getElementById('b-consent').required=minor;
    });
  });
})();
</script>"""

shell("book.html", "Book Soccer Training in Camas &amp; Vancouver WA | Coach Arnold Academy",
      "Book private or group soccer training with Coach Arnold. Choose a program, date, time and location, register a child or yourself, and get an email confirmation.",
      book_body, extra_js=book_js)

print("core pages built")
