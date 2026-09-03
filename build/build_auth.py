from shared import shell, page_hero

# ----------------------------------------------------------------- LOGIN
login_body = """
<section class="page-hero" data-pitch>
  <div class="wrap inner">
    <nav class="crumbs"><a href="index.html">Home</a> / Log in</nav>
    <h1 id="login-h1">Log in</h1>
    <p class="lede" id="login-sub">Players, parents and coaches use the same login. What you see depends on your account type.</p>
  </div>
</section>
<section>
  <div class="wrap-n">
    <div class="tabs" id="auth-tabs">
      <button type="button" class="on" data-t="signin">Sign in</button>
      <button type="button" data-t="register">Create an account</button>
    </div>

    <div id="pane-signin">
      <form class="form" id="signin-form" novalidate>
        <div class="msg" id="si-msg" tabindex="-1"></div>
        <div class="field"><label for="si-email">Email address</label>
          <input id="si-email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="si-pass">Password</label>
          <input id="si-pass" type="password" autocomplete="current-password" required></div>
        <div class="check"><input id="si-remember" type="checkbox" checked><label for="si-remember">Keep me signed in on this device</label></div>
        <div><button class="btn" type="submit">Sign in</button></div>
        <p class="small"><a href="#" id="si-forgot">Forgotten your password?</a></p>
      </form>

      <div class="notice" style="margin-top:1.6rem">
        <strong>Demo accounts for testing.</strong>
        <p>This preview uses local accounts so every screen can be tested before a real login system is connected. Password for all three is <code>demo1234</code>.</p>
        <div class="btn-row" style="margin-top:.6rem">
          <button class="btn sm dark-ghost" type="button" data-demo="player@demo.test">Player demo</button>
          <button class="btn sm dark-ghost" type="button" data-demo="parent@demo.test">Parent demo</button>
          <button class="btn sm dark-ghost" type="button" data-demo="coach@demo.test">Coach and admin demo</button>
        </div>
      </div>
    </div>

    <div id="pane-register" style="display:none">
      <form class="form" id="register-form" novalidate>
        <div class="msg" id="rg-msg" tabindex="-1"></div>
        <div class="field"><span class="lbl">What kind of account do you need?</span>
          <div class="opts">
            <label><input type="radio" name="role" value="player" checked> Player, 18 or over</label>
            <label><input type="radio" name="role" value="parent"> Parent or guardian</label>
          </div>
          <p class="hint">Players under 18 do not get their own account. A parent or guardian registers and manages everything on their behalf.</p></div>
        <div class="fgrid">
          <div class="field"><label for="rg-name">Full name</label><input id="rg-name" autocomplete="name" required></div>
          <div class="field"><label for="rg-email">Email address</label><input id="rg-email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="rg-pass">Password</label><input id="rg-pass" type="password" autocomplete="new-password" required>
            <p class="hint">At least eight characters.</p></div>
          <div class="field"><label for="rg-pass2">Confirm password</label><input id="rg-pass2" type="password" autocomplete="new-password" required></div>
        </div>
        <div class="check"><input id="rg-terms" type="checkbox" required>
          <label for="rg-terms">I accept the <a href="terms.html" target="_blank">terms of use</a> and the <a href="privacy.html" target="_blank">privacy policy</a>.</label></div>
        <div><button class="btn" type="submit">Create account</button></div>
      </form>
    </div>

    <div class="grid g2" style="margin-top:2.4rem">
      <div class="tile"><h3>What players see</h3>
        <p>Your schedule, match availability, tactics and documents shared by the coach, announcements, and your training history.</p></div>
      <div class="tile"><h3>What parents see</h3>
        <p>Each child's schedule and forms, consent settings, invoices, availability responses, and a direct line to Coach Arnold.</p></div>
    </div>
  </div>
</section>
"""

login_js = """<script>
(function(){
  var C=window.CAA;
  var role=C.qs('role'), tab=C.qs('tab');
  if(role==='player'){document.getElementById('login-h1').textContent='Player login';}
  if(role==='parent'){document.getElementById('login-h1').textContent='Parent login';}
  if(role==='coach'){document.getElementById('login-h1').textContent='Coach and administrator login';
    document.getElementById('login-sub').textContent='Manage bookings, applications, teams, schedules, announcements and website content.';}

  function show(t){
    document.getElementById('pane-signin').style.display=t==='signin'?'block':'none';
    document.getElementById('pane-register').style.display=t==='register'?'block':'none';
    C.$$('#auth-tabs button').forEach(function(b){b.classList.toggle('on',b.dataset.t===t);});
  }
  C.$$('#auth-tabs button').forEach(function(b){b.addEventListener('click',function(){show(b.dataset.t);});});
  if(tab==='register') show('register');

  function fail(box,text){box.className='msg bad show';box.innerHTML='<h4>Sign in failed</h4><p>'+text+'</p>';box.focus();}

  document.getElementById('signin-form').addEventListener('submit',function(e){
    e.preventDefault();
    var box=document.getElementById('si-msg');
    var em=document.getElementById('si-email').value.trim(), pw=document.getElementById('si-pass').value;
    if(!em||!pw){fail(box,'Enter both your email address and your password.');return;}
    var r=C.auth.login(em,pw,role||'any');
    if(!r.ok){fail(box,C.esc(r.error));return;}
    box.className='msg ok show';box.innerHTML='<h4>Signed in</h4><p>Taking you to your dashboard.</p>';
    var next=C.qs('next')||'dashboard.html';
    setTimeout(function(){location.href=next;},550);
  });

  C.$$('[data-demo]').forEach(function(b){
    b.addEventListener('click',function(){
      document.getElementById('si-email').value=b.dataset.demo;
      document.getElementById('si-pass').value='demo1234';
      C.toast('Demo details filled in. Press sign in.');
    });
  });

  document.getElementById('si-forgot').addEventListener('click',function(e){
    e.preventDefault();
    var box=document.getElementById('si-msg');
    box.className='msg ok show';
    box.innerHTML='<h4>Password resets are not live yet</h4><p>Password reset needs the email service described in the README. For now, message Coach Arnold and he will reset it for you.</p>';
    box.focus();
  });

  document.getElementById('register-form').addEventListener('submit',function(e){
    e.preventDefault();
    var box=document.getElementById('rg-msg');
    var name=document.getElementById('rg-name').value.trim();
    var email=document.getElementById('rg-email').value.trim();
    var p1=document.getElementById('rg-pass').value, p2=document.getElementById('rg-pass2').value;
    var roleSel=document.querySelector('input[name=role]:checked').value;
    if(!name||!email){box.className='msg bad show';box.innerHTML='<h4>Check the form</h4><p>Name and email are both needed.</p>';box.focus();return;}
    if(p1.length<8){box.className='msg bad show';box.innerHTML='<h4>Password too short</h4><p>Use at least eight characters.</p>';box.focus();return;}
    if(p1!==p2){box.className='msg bad show';box.innerHTML='<h4>Passwords do not match</h4><p>Retype the confirmation to match the password above.</p>';box.focus();return;}
    if(!document.getElementById('rg-terms').checked){box.className='msg bad show';box.innerHTML='<h4>One more thing</h4><p>Tick the box to accept the terms and privacy policy.</p>';box.focus();return;}
    var r=C.auth.register({name:name,email:email,pass:p1,role:roleSel,children:[]});
    if(!r.ok){box.className='msg bad show';box.innerHTML='<h4>Could not create the account</h4><p>'+C.esc(r.error)+'</p>';box.focus();return;}
    box.className='msg ok show';box.innerHTML='<h4>Account created</h4><p>Welcome. Taking you to your dashboard.</p>';
    setTimeout(function(){location.href='dashboard.html';},650);
  });
})();
</script>"""

shell("login.html", "Player &amp; Parent Login | Coach Arnold Academy",
      "Sign in to your Coach Arnold Academy account to see schedules, confirm match availability, manage children's registrations and read team announcements.",
      login_body, extra_js=login_js)

# ----------------------------------------------------------------- DASHBOARD
dash_body = """
<section class="page-hero" data-pitch style="padding-block:0">
  <div class="wrap inner" style="padding-block:clamp(26px,4vw,44px)">
    <h1 id="dash-title" style="margin-bottom:.2rem">Dashboard</h1>
    <p class="lede" id="dash-sub" style="margin:0"></p>
  </div>
</section>
<div class="dash">
  <aside id="dash-nav" aria-label="Dashboard sections"></aside>
  <main id="dash-main"></main>
</div>
"""

shell("dashboard.html", "Your dashboard | Coach Arnold Academy",
      "Private dashboard for Coach Arnold Academy players, parents and coaches.",
      dash_body, extra_js='<script src="assets/js/dashboard.js"></script>')

print("auth pages built")
