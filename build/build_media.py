from shared import shell, ld, page_hero, SITE

# ----------------------------------------------------------------- VIDEOS
videos_body = page_hero("Training videos", "Training videos",
  "Short, specific drills you can run at home with one ball. Organised by topic, with coaching points and related drills for each one.",
  '<a class="btn" id="yt-main" href="#" target="_blank" rel="noopener">Subscribe on YouTube</a><a class="btn ghost" href="book.html">Book a session</a>') + """
<section>
  <div class="wrap">
    <div class="tabs" id="vid-cats" role="tablist" aria-label="Video categories"></div>
    <div class="grid g3" id="vid-list"></div>
  </div>
</section>
<section class="paper tight">
  <div class="wrap-n">
    <div class="notice"><strong>Videos are placeholders until YouTube IDs are added.</strong>
      <p>Open <code>assets/js/data.js</code>, find the <code>videos</code> list, and paste each YouTube video's eleven-character ID into the <code>yt</code> field. The embed, thumbnail and share links then work automatically. This can also be done from the admin dashboard.</p></div>
  </div>
</section>
"""

videos_js = """<script>
(function(){
  var C=window.CAA,D=C.D,active='All';
  document.getElementById('yt-main').href=D.site.youtube;
  var cats=['All'].concat(D.videos.map(function(v){return v.cat;}).filter(function(v,i,a){return a.indexOf(v)===i;}));
  document.getElementById('vid-cats').innerHTML=cats.map(function(c,i){
    return '<button type="button" role="tab" class="'+(i===0?'on':'')+'">'+C.esc(c)+'</button>';}).join('');
  function render(){
    document.getElementById('vid-list').innerHTML=D.videos.filter(function(v){
      return active==='All'||v.cat===active;}).map(function(v){
      var thumb=v.yt?'<img src="https://img.youtube.com/vi/'+v.yt+'/hqdefault.jpg" alt="" loading="lazy" style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:6px">'
        :'<span class="play">&#9654;</span>';
      return '<article class="tile"><a class="vthumb" href="video.html?id='+v.id+'" aria-label="Open: '+C.esc(v.title)+'">'+thumb+'</a>'+
        '<h3 style="margin-top:1rem;font-size:1.15rem">'+C.esc(v.title)+'</h3>'+
        '<p class="meta">'+C.esc(v.cat)+' · '+C.esc(v.level)+'</p><p>'+C.esc(v.desc)+'</p>'+
        '<div class="foot"><a class="btn sm" href="video.html?id='+v.id+'">Open video</a></div></article>';
    }).join('');
  }
  C.$$('#vid-cats button').forEach(function(b){
    b.addEventListener('click',function(){
      C.$$('#vid-cats button').forEach(function(x){x.classList.remove('on');});
      b.classList.add('on'); active=b.textContent; render();});
  });
  render();
})();
</script>"""

shell("videos.html", "Soccer Training Videos &amp; Home Drills | Coach Arnold Academy",
      "Free soccer training videos: ball mastery, dribbling, passing, shooting, first touch, defending, goalkeeping, agility and tactics, with drills you can do at home.",
      videos_body, extra_js=videos_js)

# ----------------------------------------------------------------- VIDEO DETAIL
video_body = """
<section class="page-hero" data-pitch>
  <div class="wrap inner">
    <nav class="crumbs"><a href="index.html">Home</a> / <a href="videos.html">Training videos</a> / <span id="crumb">Video</span></nav>
    <h1 id="v-title">Video</h1>
    <p class="lede" id="v-desc"></p>
  </div>
</section>
<section>
  <div class="wrap split">
    <div>
      <div id="v-embed"></div>
      <h3 style="margin-top:1.8rem">Coaching points</h3>
      <ul id="v-points" style="padding-left:1.1rem"></ul>
      <h3 style="margin-top:1.8rem">Related drills</h3>
      <ul id="v-drills" style="padding-left:1.1rem"></ul>
      <div class="btn-row">
        <a class="btn" href="book.html">Book a session</a>
        <button class="btn dark-ghost" type="button" id="v-share">Copy share link</button>
        <a class="btn dark-ghost" id="v-wa" href="#" target="_blank" rel="noopener">Share on WhatsApp</a>
      </div>
    </div>
    <div>
      <div class="tile" style="margin-bottom:1.2rem">
        <h3>Details</h3>
        <div class="tablewrap"><table><tbody id="v-facts"></tbody></table></div>
      </div>
      <div class="tile">
        <h3>Related videos</h3>
        <div id="v-related"></div>
      </div>
    </div>
  </div>
</section>
"""

video_js = """<script>
(function(){
  var C=window.CAA,D=C.D,id=C.qs('id')||'v1';
  var v=D.videos.find(function(x){return x.id===id;});
  if(!v){location.replace('videos.html');return;}
  document.title=v.title+' | Coach Arnold Academy';
  document.getElementById('crumb').textContent=v.cat;
  document.getElementById('v-title').textContent=v.title;
  document.getElementById('v-desc').textContent=v.desc;
  document.getElementById('v-embed').innerHTML = v.yt ?
    '<iframe class="vid" src="https://www.youtube-nocookie.com/embed/'+v.yt+'" title="'+C.esc(v.title)+'" loading="lazy" allowfullscreen allow="accelerometer;clipboard-write;encrypted-media;gyroscope;picture-in-picture"></iframe>'
    : '<div class="vthumb" style="cursor:default"><div style="text-align:center;padding:1.4rem"><span class="play" style="margin:0 auto .8rem"> &#9654;</span>'+
      '<p style="color:#C9D5EC;margin:0;font-size:.95rem">Video not linked yet. Add the YouTube ID for <strong>'+C.esc(v.id)+'</strong> in data.js.</p></div></div>';
  document.getElementById('v-points').innerHTML=v.points.map(function(p){return '<li>'+C.esc(p)+'</li>';}).join('');
  document.getElementById('v-drills').innerHTML=v.drills.map(function(p){return '<li>'+C.esc(p)+'</li>';}).join('');
  document.getElementById('v-facts').innerHTML=[['Category',v.cat],['Recommended level',v.level]].map(function(r){
    return '<tr><th scope="row">'+r[0]+'</th><td>'+C.esc(r[1])+'</td></tr>';}).join('');
  document.getElementById('v-related').innerHTML=D.videos.filter(function(x){
    return x.id!==v.id&&(x.cat===v.cat||Math.random()>.5);}).slice(0,4).map(function(x){
    return '<div class="feature" style="margin-bottom:.9rem"><h3 style="font-size:1rem"><a href="video.html?id='+x.id+'">'+C.esc(x.title)+'</a></h3><p>'+C.esc(x.cat)+'</p></div>';}).join('');
  document.getElementById('v-wa').href='https://wa.me/?text='+encodeURIComponent(v.title+' — '+location.href);
  document.getElementById('v-share').addEventListener('click',function(){
    navigator.clipboard.writeText(location.href).then(function(){C.toast('Link copied to your clipboard');},
      function(){C.toast('Copy failed. Copy the address from the browser bar instead.');});
  });
})();
</script>"""

shell("video.html", "Training video | Coach Arnold Academy",
      "Watch a Coach Arnold Academy training video with coaching points, related drills and a home practice plan.",
      video_body, extra_js=video_js, og_type="video.other")

# ----------------------------------------------------------------- NEWS
news_body = page_hero("News", "News and announcements",
  "Registration windows, schedule changes, match news and academy updates.") + """
<section>
  <div class="wrap split">
    <div id="news-list"></div>
    <div>
      <div class="tile" style="margin-bottom:1.2rem">
        <h3>Get announcements by email</h3>
        <p class="meta">Roughly two a month. Unsubscribe any time.</p>
        <form class="form" data-form="newsletter" data-success-title="You're subscribed"
              data-success="Check your inbox for a confirmation email." data-toast="Subscribed">
          <div class="msg" tabindex="-1"></div>
          <div class="field"><label for="n2-name">Name</label><input id="n2-name" name="name" required></div>
          <div class="field"><label for="n2-email">Email</label><input id="n2-email" name="email" type="email" required></div>
          <div class="check"><input id="n2-ok" type="checkbox" name="consent" required>
            <label for="n2-ok">I agree to the <a href="privacy.html">privacy policy</a>.</label></div>
          <button class="btn wide" type="submit">Subscribe</button>
        </form>
      </div>
      <div class="tile">
        <h3>Team announcements</h3>
        <p>Match-specific announcements, tactics and lineups go to squad members in the private team area rather than here.</p>
        <div class="foot"><a class="btn sm dark-ghost" href="login.html">Team login</a></div>
      </div>
    </div>
  </div>
</section>
"""

news_js = """<script>
(function(){
  var C=window.CAA,D=C.D;
  var extra=C.store.get('announcements',[]);
  var all=extra.concat(D.news);
  document.getElementById('news-list').innerHTML=all.map(function(n){
    return '<article style="border-bottom:1px solid var(--line-d);padding-bottom:1.6rem;margin-bottom:1.6rem">'+
      '<p class="meta">'+C.fmtDate(n.date,true)+'</p><h2 style="font-size:1.7rem">'+C.esc(n.title)+'</h2>'+
      '<p>'+C.esc(n.body)+'</p>'+
      '<a class="btn sm dark-ghost" href="'+C.waLink('Question about: '+n.title+' — ')+'" target="_blank" rel="noopener">Ask about this</a></article>';
  }).join('');
})();
</script>"""

shell("news.html", "Academy News &amp; Announcements | Coach Arnold Academy",
      "Registration windows, schedule changes, tryout dates and match news from Coach Arnold Academy in Camas and Vancouver, Washington.",
      news_body, extra_js=news_js)

# ----------------------------------------------------------------- CONTACT
contact_body = page_hero("Contact", "Contact Coach Arnold",
  "Send a message, ask a question, or just describe the player and get an honest recommendation about where to start.") + """
<section>
  <div class="wrap split">
    <div>
      <form class="form" data-form="contacts" data-success-title="Message sent"
            data-success="Coach Arnold has your message. Most replies go out within 24 hours, and same day on weekdays."
            data-toast="Message sent to Coach Arnold">
        <div class="msg" tabindex="-1"></div>
        <div class="field"><label for="c-topic">What's this about?</label>
          <select id="c-topic" name="topic" required>
            <option value="">Choose a topic</option>
            <option>Private coaching</option><option>Group coaching</option><option>Team coaching</option>
            <option>Youth registration</option><option>Adult training</option><option>Joining Obsidian AC</option>
            <option>General question</option><option>Partnership or sponsorship</option>
          </select></div>
        <div class="fgrid">
          <div class="field"><label for="c-name">Your name</label><input id="c-name" name="name" required autocomplete="name"></div>
          <div class="field"><label for="c-email">Email</label><input id="c-email" name="email" type="email" required autocomplete="email"></div>
          <div class="field"><label for="c-phone">Phone or WhatsApp</label><input id="c-phone" name="phone" type="tel" autocomplete="tel"></div>
          <div class="field"><label for="c-city">City</label><input id="c-city" name="city" placeholder="Camas, Vancouver, Portland"></div>
        </div>
        <div class="field"><label for="c-msg">Your message</label>
          <textarea id="c-msg" name="message" required placeholder="Tell me about the player: age, experience, and what you'd like to work on."></textarea></div>
        <div class="field"><span class="lbl">How would you like to be contacted?</span>
          <div class="opts">
            <label><input type="radio" name="preferred" value="Email" checked> Email</label>
            <label><input type="radio" name="preferred" value="Phone call"> Phone call</label>
            <label><input type="radio" name="preferred" value="Text or WhatsApp"> Text or WhatsApp</label>
          </div></div>
        <div class="check"><input id="c-privacy" type="checkbox" name="privacy" required>
          <label for="c-privacy">I've read the <a href="privacy.html">privacy policy</a> and agree to my details being used to reply to this message.</label></div>
        <div><button class="btn" type="submit">Send message</button></div>
      </form>
    </div>
    <div>
      <div class="tile" style="margin-bottom:1.2rem">
        <h3>Faster options</h3>
        <p class="meta" data-site-area></p>
        <div class="btn-row" style="margin-top:.2rem;flex-direction:column;align-items:stretch">
          <a class="btn" data-wa="Hi Coach Arnold, I found you through the website and I'd like to ask about " href="#" target="_blank" rel="noopener">Message on WhatsApp</a>
          <a class="btn dark-ghost" data-mail="Coaching enquiry from the website" href="#">Send an email</a>
          <a class="btn dark-ghost" data-tel href="#"></a>
          <a class="btn dark-ghost" id="ig-dm" href="#" target="_blank" rel="noopener">Message on Instagram</a>
          <a class="btn dark-ghost" id="fb-msg" href="#" target="_blank" rel="noopener">Facebook Messenger</a>
        </div>
        <p class="small muted" style="margin-top:.9rem">Facebook Messenger opens the academy page. If the page isn't set up yet, use WhatsApp or email.</p>
      </div>
      <div class="tile" style="margin-bottom:1.2rem">
        <h3>Response time</h3>
        <p data-site-response></p>
        <p class="small muted">Messages sent during a session get answered afterwards. If it's urgent and match-related, WhatsApp is fastest.</p>
      </div>
      <div class="tile">
        <h3>Where sessions happen</h3>
        <div id="c-locs"></div>
      </div>
    </div>
  </div>
</section>

<section class="paper">
  <div class="wrap-n">
    <div class="head"><span class="rule"></span><h2>Common questions</h2></div>
    <div id="c-faq"></div>
    <div class="btn-row"><a class="btn dark-ghost" href="faq.html">All questions</a></div>
  </div>
</section>
"""

contact_js = """<script>
(function(){
  var C=window.CAA,D=C.D;
  document.getElementById('ig-dm').href=D.site.instagram;
  document.getElementById('fb-msg').href=D.site.facebook;
  C.$$('[data-site-response]').forEach(function(n){n.textContent=D.site.responseTime;});
  document.getElementById('c-locs').innerHTML=D.locations.map(function(l){
    return '<div class="feature" style="margin-bottom:.9rem"><h3 style="font-size:1rem">'+C.esc(l.name)+'</h3><p>'+C.esc(l.city)+'. '+C.esc(l.note)+'</p></div>';}).join('');
  document.getElementById('c-faq').innerHTML=D.faqs.slice(0,5).map(function(f,i){
    return '<div class="acc"><button type="button"><span>'+C.esc(f.q)+'</span><span class="pm">+</span></button>'+
      '<div class="body"><p>'+C.esc(f.a)+'</p></div></div>';}).join('');
  C.wireAccordions();
  var t=C.qs('topic'); if(t) document.getElementById('c-topic').value=t;
})();
</script>"""

shell("contact.html", "Contact Coach Arnold | Soccer Coaching in Camas &amp; Vancouver WA",
      "Contact Coach Arnold Academy by form, WhatsApp, email or phone about private coaching, group training, youth registration, adult sessions or joining Obsidian AC.",
      contact_body, extra_js=contact_js)

# ----------------------------------------------------------------- FAQ
faq_body = page_hero("FAQ", "Frequently asked questions",
  "Sessions, pricing, cancellations, safety and joining a team. If your question isn't here, send it over.",
  '<a class="btn" href="contact.html">Ask a question</a>') + """
<section><div class="wrap-n"><div id="faq-all"></div>
  <div class="notice" style="margin-top:2rem"><strong>Still unsure?</strong>
    <p>Describe the player and Coach Arnold will tell you honestly whether the academy is the right fit. <a href="contact.html">Send a message</a>.</p></div>
</div></section>
"""
faq_js = """<script>
(function(){
  var C=window.CAA,D=C.D;
  document.getElementById('faq-all').innerHTML=D.faqs.map(function(f){
    return '<div class="acc"><button type="button"><span>'+C.esc(f.q)+'</span><span class="pm">+</span></button>'+
      '<div class="body"><p>'+C.esc(f.a)+'</p></div></div>';}).join('');
  C.wireAccordions();
})();
</script>"""

faq_ld = ld("""{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What ages do you coach?","acceptedAnswer":{"@type":"Answer","text":"Players from about age five through adults. Sessions are grouped by age and level, and adults train with adults."}},
{"@type":"Question","name":"Where do sessions take place?","acceptedAnswer":{"@type":"Answer","text":"Camas, Vancouver and Washougal in Washington, plus east Portland in Oregon."}},
{"@type":"Question","name":"How do I cancel or reschedule?","acceptedAnswer":{"@type":"Answer","text":"Reschedule free with at least 24 hours notice from your account or by replying to your confirmation email."}},
{"@type":"Question","name":"Are you licensed and background checked?","acceptedAnswer":{"@type":"Answer","text":"Coach Arnold holds US Soccer coaching licences and completes SafeSport training and background screening."}}]}""")

shell("faq.html", "Soccer Coaching FAQ | Coach Arnold Academy",
      "Answers about ages, locations, pricing, what to bring, weather, cancellations, coaching credentials and joining a team at Coach Arnold Academy.",
      faq_body, extra_js=faq_js, jsonld=faq_ld)

# ----------------------------------------------------------------- TESTIMONIALS
testi_body = page_hero("Testimonials", "What players and parents say",
  "Feedback from families and adult players. Names are shortened for privacy, and no minor is identified.") + """
<section><div class="wrap"><div class="grid g2" id="t-all"></div></div></section>
<section class="paper">
  <div class="wrap-n">
    <div class="head"><span class="rule"></span><h2>Share your experience</h2>
      <p>Trained with Coach Arnold? Feedback is welcome, including the critical kind.</p></div>
    <form class="form" data-form="testimonials" data-success-title="Thank you"
          data-success="Your feedback is with Coach Arnold. Nothing is published without asking you first."
          data-toast="Feedback sent">
      <div class="msg" tabindex="-1"></div>
      <div class="fgrid">
        <div class="field"><label for="ts-name">Your name</label><input id="ts-name" name="name" required></div>
        <div class="field"><label for="ts-role">Your connection to the academy</label>
          <select id="ts-role" name="role" required><option value="">Choose one</option>
            <option>Parent</option><option>Adult player</option><option>Youth player</option>
            <option>Team manager</option><option>Other</option></select></div>
      </div>
      <div class="field"><label for="ts-msg">Your feedback</label><textarea id="ts-msg" name="message" required></textarea></div>
      <div class="check"><input id="ts-ok" type="checkbox" name="publishConsent">
        <label for="ts-ok">You may publish this on the website with my first name and last initial. <span class="muted">Optional.</span></label></div>
      <div><button class="btn" type="submit">Send feedback</button></div>
    </form>
    <p class="small muted" style="margin-top:1rem">A parent may not submit a testimonial that identifies a child by full name. Reviews naming a minor are edited before publication.</p>
  </div>
</section>
"""
testi_js = """<script>
(function(){
  var C=window.CAA,D=C.D;
  document.getElementById('t-all').innerHTML=D.testimonials.map(function(q){
    return '<div class="tile"><blockquote class="quote"><p>'+C.esc(q.q)+'</p><cite>'+C.esc(q.a)+' · '+C.esc(q.role)+'</cite></blockquote></div>';}).join('');
})();
</script>"""
shell("testimonials.html", "Testimonials | Coach Arnold Academy Soccer Coaching",
      "Feedback from parents, youth players and adult beginners who train with Coach Arnold Academy in Camas and Vancouver, Washington.",
      testi_body, extra_js=testi_js)

# ----------------------------------------------------------------- GALLERY
gallery_body = page_hero("Gallery", "Photo and video gallery",
  "Sessions, match nights and team moments. Photographs of players under 18 appear only with written parental consent.") + """
<section>
  <div class="wrap">
    <div class="tabs" id="g-tabs"><button class="on" type="button">Photos</button><button type="button">Video</button></div>
    <div id="g-photos" class="grid g3"></div>
    <div id="g-video" class="grid g3" style="display:none"></div>
    <div class="notice" style="margin-top:2rem"><strong>Replace these placeholders with real media.</strong>
      <p>Save images into <code>assets/img/gallery/</code> and list them in the gallery array, or upload them through the admin dashboard. Before publishing any image that includes a minor, confirm that photo consent is recorded on that player's registration.</p></div>
  </div>
</section>
<section class="paper tight">
  <div class="wrap-n"><div class="tile"><h3>Want a photo removed?</h3>
    <p>Any player, parent or guardian can ask for an image to be taken down, for any reason and without explaining why. Requests are actioned within two working days.</p>
    <div class="foot"><a class="btn sm" href="contact.html?topic=General%20question">Request a removal</a>
      <a class="btn sm dark-ghost" href="privacy.html">Privacy policy</a></div></div></div>
</section>
"""
gallery_js = """<script>
(function(){
  var C=window.CAA;
  var caps=['Small-group session, Lacamas Lake','Adult training, Heritage Park','Obsidian AC match night',
            'Youth development block','Goalkeeping session','Team huddle before kick-off',
            'Coaching education','Trophy night','Indoor arena warm-up'];
  document.getElementById('g-photos').innerHTML=caps.map(function(c){
    return '<figure style="margin:0"><div style="aspect-ratio:4/3;background:var(--paper);border:2px dashed var(--line-d);border-radius:6px;display:grid;place-items:center;color:var(--muted-d);font-size:.85rem;text-align:center;padding:1rem">Photo placeholder</div>'+
      '<figcaption class="small muted" style="margin-top:.4rem">'+C.esc(c)+'</figcaption></figure>';}).join('');
  document.getElementById('g-video').innerHTML=C.D.videos.slice(0,6).map(function(v){
    return '<article class="tile"><a class="vthumb" href="video.html?id='+v.id+'"><span class="play">&#9654;</span></a>'+
      '<h3 style="margin-top:.9rem;font-size:1.05rem">'+C.esc(v.title)+'</h3><p class="meta">'+C.esc(v.cat)+'</p></article>';}).join('');
  C.$$('#g-tabs button').forEach(function(b,i){
    b.addEventListener('click',function(){
      C.$$('#g-tabs button').forEach(function(x){x.classList.remove('on');});b.classList.add('on');
      document.getElementById('g-photos').style.display=i===0?'grid':'none';
      document.getElementById('g-video').style.display=i===1?'grid':'none';});
  });
})();
</script>"""
shell("gallery.html", "Photo &amp; Video Gallery | Coach Arnold Academy",
      "Photos and video from Coach Arnold Academy training sessions, youth development blocks and Obsidian AC match nights.",
      gallery_body, extra_js=gallery_js)

# ----------------------------------------------------------------- SPONSORSHIP
spon_body = page_hero("Sponsorship", "Sponsorship and partnerships",
  "Local sponsorship keeps coaching affordable for families and puts your business in front of players, parents and match-night crowds.",
  '<a class="btn" href="#spon-form">Talk about sponsorship</a>') + """
<section>
  <div class="wrap">
    <div class="head"><span class="rule"></span><h2>Where sponsorship goes</h2></div>
    <div class="grid g3">
      <div class="feature"><h3>Kit and equipment</h3><p>Match shirts, training tops, balls, bibs and goals for youth sessions.</p></div>
      <div class="feature"><h3>Arena and field fees</h3><p>Indoor arena time and field permits, the single biggest cost in running a season.</p></div>
      <div class="feature"><h3>Scholarship places</h3><p>Funded places for families who cannot cover coaching fees. These are allocated quietly and confidentially.</p></div>
    </div>
  </div>
</section>
<section class="paper">
  <div class="wrap">
    <div class="head"><span class="rule"></span><h2>Partnership levels</h2>
      <p>Sample tiers. Final amounts and benefits are agreed directly with Coach Arnold.</p></div>
    <div class="grid g3">
      <div class="tile"><h3>Community supporter</h3><p class="meta">Sample: $250 per season</p>
        <ul style="padding-left:1.1rem;font-size:.95rem"><li>Logo on the sponsorship page</li><li>Thank-you post on Instagram and Facebook</li><li>Named in match-night announcements</li></ul></div>
      <div class="tile"><h3>Team sponsor</h3><p class="meta">Sample: $750 per season</p>
        <ul style="padding-left:1.1rem;font-size:.95rem"><li>Logo on training tops</li><li>Logo on the team page and this page</li><li>Social posts across the season</li><li>Banner at home match nights</li></ul></div>
      <div class="tile"><h3>Principal partner</h3><p class="meta">Sample: contact to discuss</p>
        <ul style="padding-left:1.1rem;font-size:.95rem"><li>Logo on the front of match shirts</li><li>Named as the academy's principal partner</li><li>Funded scholarship places in your name</li><li>Presence at academy events</li></ul></div>
    </div>
    <p class="small muted" style="margin-top:1.2rem"><strong>Coach Arnold must confirm real amounts and benefits before this page goes live.</strong></p>
  </div>
</section>
<section id="spon-form">
  <div class="wrap-n">
    <div class="head"><span class="rule"></span><h2>Start a conversation</h2></div>
    <form class="form" data-form="sponsors" data-success-title="Enquiry received"
          data-success="Coach Arnold will be in touch to discuss what would work for your business."
          data-toast="Sponsorship enquiry sent">
      <div class="msg" tabindex="-1"></div>
      <div class="fgrid">
        <div class="field"><label for="s-biz">Business name</label><input id="s-biz" name="business" required></div>
        <div class="field"><label for="s-name">Contact name</label><input id="s-name" name="name" required></div>
        <div class="field"><label for="s-email">Email</label><input id="s-email" name="email" type="email" required></div>
        <div class="field"><label for="s-phone">Phone</label><input id="s-phone" name="phone" type="tel"></div>
        <div class="field"><label for="s-level">Interested in</label>
          <select id="s-level" name="level" required><option value="">Choose one</option>
            <option>Community supporter</option><option>Team sponsor</option><option>Principal partner</option>
            <option>In-kind support such as equipment or venue</option><option>Not sure yet</option></select></div>
        <div class="field"><label for="s-web">Website</label><input id="s-web" name="website" type="url" placeholder="https://"></div>
      </div>
      <div class="field"><label for="s-msg">What would you want out of it?</label><textarea id="s-msg" name="message" required></textarea></div>
      <div><button class="btn" type="submit">Send enquiry</button></div>
    </form>
  </div>
</section>
"""
shell("sponsorship.html", "Sponsorship &amp; Partnerships | Coach Arnold Academy",
      "Sponsor a local soccer academy in Camas and Vancouver, WA. Kit, arena fees and scholarship places for families, with logo placement and match-night presence.",
      spon_body)

print("media pages built")
