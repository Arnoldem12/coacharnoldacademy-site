/* ============================================================
   Coach Arnold Academy — site content
   ------------------------------------------------------------
   This file is the content source for the whole site. Anything
   Coach Arnold needs to change regularly lives here, and the
   admin dashboard writes changes back into this same shape.

   Lines marked  // REPLACE  hold sample content that must be
   swapped for real details before launch.
   ============================================================ */

window.CAA_DATA = {

  site: {
    name: "Coach Arnold Academy",
    tagline: "Youth and adult soccer coaching",
    coach: "Arnold Eoka Mambe",
    email: "coach@coacharnoldacademy.com",          // REPLACE
    phone: "+1 (360) 555-0142",                      // REPLACE
    whatsapp: "13605550142",                         // REPLACE digits only, no +
    instagram: "https://instagram.com/coacharnoldacademy",
    facebook: "https://facebook.com/coacharnoldacademy",   // REPLACE
    youtube: "https://youtube.com/@coacharnoldacademy",    // REPLACE
    tiktok: "",                                      // add later
    serviceArea: "Camas, Vancouver and Washougal, WA; Portland, OR and surrounding communities",
    baseCity: "Camas, Washington",
    responseTime: "Most messages get a reply within 24 hours, and same day on weekdays.",
    ga4: "G-XXXXXXXXXX",                             // REPLACE with Google Analytics 4 ID
    searchConsole: "REPLACE_WITH_VERIFICATION_TOKEN"
  },

  locations: [
    { id:"lacamas",  name:"Lacamas Lake Fields",      city:"Camas, WA",      note:"Outdoor turf and grass. Free parking on the north lot." },       // REPLACE
    { id:"heritage", name:"Heritage Park Turf",       city:"Vancouver, WA",  note:"Lit turf, available year round." },                              // REPLACE
    { id:"indoor",   name:"Riverview Indoor Arena",   city:"Vancouver, WA",  note:"Home venue for Obsidian AC league nights." },                     // REPLACE
    { id:"portland", name:"Portland east side fields",city:"Portland, OR",   note:"Field assigned when your session is confirmed." },                // REPLACE
    { id:"virtual",  name:"Online session",           city:"Video call",     note:"Zoom or Google Meet link sent with your confirmation." }
  ],

  programs: [
    {
      id:"private", name:"One-on-one private coaching", order:1,
      short:"A full hour built around one player, one plan and measurable goals.",
      ages:"Ages 6 to adult", duration:"60 minutes", max:"1 player",
      level:"Beginner to advanced", price:"$75 per session", locations:["lacamas","heritage","portland"],
      body:"Private sessions move fastest because every repetition belongs to one player. The first session is a baseline: first touch under pressure, both feet, body shape when receiving, decision speed in small spaces. From there Coach Arnold sets two or three targets and returns to them every week so progress is visible rather than assumed.",
      learn:["Clean first touch with both feet and away from pressure","Change of direction and beating a defender one against one","Passing weight, angle and timing under game speed","Finishing technique from inside and outside the box","Scanning before receiving so the next decision is already made"],
      slots:["Mon 4:00 pm","Tue 5:30 pm","Wed 4:00 pm","Thu 5:30 pm","Sat 9:00 am","Sat 10:30 am"]
    },
    {
      id:"small-group", name:"Small-group training", order:2,
      short:"Two to six players. Private-session detail with the competition of real opponents.",
      ages:"Ages 7 to 18", duration:"75 minutes", max:"6 players",
      level:"Beginner to advanced", price:"$35 per player, per session", locations:["lacamas","heritage"],
      body:"Small groups keep the coaching detailed while adding what a private session cannot: a real opponent. Sessions run technical work first, then small-sided games where the technique has to hold up against pressure. Bring a friend or teammate, or ask to be placed in a group at a similar level.",
      learn:["Combination play in tight areas","Defending one against one and recovery runs","Speed of play in two-touch and one-touch games","Competing for a loose ball without fouling","Communication and simple leadership habits"],
      slots:["Tue 4:30 pm","Thu 4:30 pm","Sat 11:30 am","Sun 10:00 am"]
    },
    {
      id:"youth", name:"Youth player development", order:3,
      short:"A season-long pathway for young players, built on confidence before complexity.",
      ages:"Ages 5 to 14", duration:"60 minutes weekly", max:"12 players",
      level:"New players welcome", price:"$180 per 6-week block", locations:["lacamas","heritage"],
      body:"Younger players learn best when they touch the ball constantly and are allowed to try things without fear. Sessions are short, active and game-based. Parents receive a brief written note after each block covering what improved and what to practise at home.",
      learn:["Ball mastery patterns children can repeat at home","Dribbling with the head up","Comfortable receiving under light pressure","Fair play, effort and how to lose well","Enjoying the game enough to keep playing"],
      slots:["Mon 5:00 pm","Wed 5:00 pm","Sat 9:00 am"]
    },
    {
      id:"adult", name:"Adult soccer training", order:4,
      short:"For adults returning to the game, starting it late, or preparing for league nights.",
      ages:"Ages 18+", duration:"75 minutes", max:"10 players",
      level:"Complete beginner to league standard", price:"$30 per session", locations:["heritage","indoor"],
      body:"Plenty of adults want to play but do not want to be the least confident person on the pitch. These sessions fix that in private, at a sensible intensity, with technique taught properly rather than assumed. Beginners and returning players train in the same group and are given different targets within the same exercise.",
      learn:["Striking a ball correctly without straining the ankle or knee","Receiving and turning in small indoor spaces","Positional basics for six-a-side and seven-a-side","Fitness that carries through a full match","Playing at pace without panicking on the ball"],
      slots:["Tue 7:30 pm","Thu 7:30 pm","Sun 6:00 pm"]
    },
    {
      id:"team", name:"Team training", order:5,
      short:"Full-squad sessions for clubs, school teams and rec teams that want structure.",
      ages:"All ages", duration:"90 minutes", max:"22 players",
      level:"Rec through competitive", price:"Contact for pricing", locations:["lacamas","heritage","portland"],
      body:"Coach Arnold plans and runs the session with your existing coaching staff, or takes it entirely. The work is built from what your team actually struggles with, whether that is building out from the back, pressing as a unit, or simply having a warm-up that prepares players properly. Available as a one-off or a block across a season.",
      learn:["A repeatable session structure your staff can reuse","Pressing triggers the whole team recognises","Building out from the goalkeeper under pressure","Set-piece routines for and against","Standards for training intensity and behaviour"],
      slots:["By arrangement"]
    },
    {
      id:"position", name:"Position-specific coaching", order:6,
      short:"Detail work for goalkeepers, defenders, midfielders and forwards.",
      ages:"Ages 10 to adult", duration:"60 minutes", max:"4 players",
      level:"Intermediate to advanced", price:"$75 private, $40 in pairs", locations:["lacamas","heritage"],
      body:"Every position has its own problems to solve. A centre back needs different feet, different scanning habits and a different first touch than a winger. These sessions strip the game down to the demands of one role and drill them until they hold under pressure.",
      learn:["Goalkeeping: handling, set position, distribution, dealing with crosses","Full backs: overlapping, defending the touchline, recovery angles","Centre backs: heading, body position, stepping out with the ball","Midfielders: receiving on the half turn, screening, switching play","Forwards: movement in the box, finishing first time, pressing from the front"],
      slots:["Wed 6:30 pm","Fri 4:30 pm","Sun 11:30 am"]
    },
    {
      id:"technical", name:"Technical skills training", order:7,
      short:"Pure repetition on the four techniques the game is built from.",
      ages:"Ages 8 to adult", duration:"60 minutes", max:"8 players",
      level:"All levels", price:"$30 per session", locations:["lacamas","heritage"],
      body:"Touch, turn, pass, strike. Sessions are high-volume and deliberately repetitive, because technique becomes reliable through repetition and nothing else. Players leave with a short home routine that takes fifteen minutes and needs only a ball and a wall.",
      learn:["Ball mastery: sole rolls, chops, drag backs, laces control","Receiving across the body to open the pitch","Driven, lofted and disguised passing","Striking through the ball for power and placement","A fifteen-minute home routine that actually works"],
      slots:["Mon 6:00 pm","Wed 6:00 pm","Sat 12:30 pm"]
    },
    {
      id:"tactical", name:"Tactical learning and game understanding", order:8,
      short:"Classroom and pitch work on why the game happens the way it does.",
      ages:"Ages 11 to adult", duration:"75 minutes", max:"12 players",
      level:"Intermediate to advanced", price:"$35 per session", locations:["heritage","virtual"],
      body:"Players who understand the game make faster decisions with less effort. Sessions combine a short whiteboard segment with pitch work on the same idea, so the concept is seen, walked through and then played at speed. Formations, pressing structure, transitions and game management are covered across a rolling cycle.",
      learn:["Reading the shape of the opposition","When to press and when to hold","Playing forward, backward and sideways with purpose","Roles inside 4-3-3, 4-4-2 and 3-5-2","Managing a match: game state, tempo, time"],
      slots:["Tue 6:30 pm","Sun 4:00 pm"]
    },
    {
      id:"conditioning", name:"Speed, agility and conditioning", order:9,
      short:"Soccer-specific movement, acceleration and match fitness.",
      ages:"Ages 12 to adult", duration:"55 minutes", max:"10 players",
      level:"All levels", price:"$28 per session", locations:["lacamas","heritage"],
      body:"Conditioning built for soccer, not for a track. Work focuses on the first three steps, changing direction without losing balance, and repeating high-intensity efforts across ninety minutes. Every session includes a proper warm-up and a cool-down, with movement quality prioritised over exhaustion.",
      learn:["Acceleration mechanics over the first five yards","Decelerating and cutting without losing the ball","Repeat sprint capacity for match demands","Warm-up and recovery habits worth keeping","Injury-reduction work for ankles, knees and hips"],
      slots:["Mon 7:00 pm","Thu 6:00 pm","Sat 8:00 am"]
    },
    {
      id:"virtual", name:"Online video analysis and virtual coaching", order:10,
      short:"Send match or training footage and get it broken down clip by clip.",
      ages:"Ages 10 to adult", duration:"45 minutes live, plus written notes", max:"1 player",
      level:"Intermediate to advanced", price:"$50 per analysis", locations:["virtual"],
      body:"Upload a full match or a set of clips, and Coach Arnold returns a marked-up breakdown covering decisions, positioning and technique, followed by a live call to talk through it. Useful for players away from the area, players preparing for a trial, and anyone who wants to see what they actually do rather than what they think they do.",
      learn:["What your positioning looks like from outside your own head","Decision patterns that repeat, good and bad","Two or three specific fixes to work on next","A follow-up plan tied to your next match","How to review your own footage without a coach"],
      slots:["Thu 8:30 pm","Sun 7:00 pm","By arrangement"]
    }
  ],

  teams: [
    {
      id:"obsidian-ac", name:"Obsidian AC", crest:"OAC", featured:true,
      level:"Adult indoor, co-ed", ages:"18+", manager:"Coach Arnold",
      blurb:"The academy's indoor side. Competitive, disciplined, and built for players who want a serious league night without a full outdoor commitment.",
      home:"indoor", recruiting:true, needs:["Goalkeeper","Centre back","Wide midfielder"],
      trainings:["Wednesdays 8:00 pm, Riverview Indoor Arena"],
      history:"Obsidian AC was formed in 2024 out of the academy's adult sessions, when a group of players wanted somewhere to put the work they had been doing on Tuesday nights. The squad plays in the winter indoor league and trains through the season."   // REPLACE with real founding details
    },
    {
      id:"caa-u12", name:"CAA Development U12", crest:"U12",
      level:"Recreational and select development", ages:"U11 to U12", manager:"Coach Arnold",
      blurb:"A development squad focused on technical growth and regular game time for every player.",
      home:"lacamas", recruiting:true, needs:["Outfield players"],
      trainings:["Mondays 5:00 pm, Lacamas Lake Fields","Saturdays 9:00 am, Lacamas Lake Fields"],
      history:"Formed to give younger players a competitive but low-pressure route into organised soccer."   // REPLACE
    },
    {
      id:"caa-u15", name:"CAA Development U15", crest:"U15",
      level:"Select development", ages:"U14 to U15", manager:"Coach Arnold",
      blurb:"For players preparing to step into high school and club soccer with a stronger technical base.",
      home:"heritage", recruiting:false, needs:[],
      trainings:["Wednesdays 6:00 pm, Heritage Park Turf"],
      history:"Built around the academy's small-group players who wanted a regular team environment."   // REPLACE
    }
  ],

  /* Fixtures. status: scheduled | changed | canceled | completed */
  matches: [
    { id:"m1", team:"obsidian-ac", opponent:"Riverside FC", date:"2026-09-09", kick:"20:30", arrive:"20:00",
      venue:"Riverview Indoor Arena", address:"1200 SE Riverview Way, Vancouver, WA", home:true,
      kit:"Black shirts, black shorts", status:"scheduled", notes:"League opener. Bring both kit colours." },
    { id:"m2", team:"obsidian-ac", opponent:"Cascade United", date:"2026-09-16", kick:"21:15", arrive:"20:45",
      venue:"Cascade Sports Center", address:"3400 NE 78th St, Vancouver, WA", home:false,
      kit:"White shirts, black shorts", status:"scheduled", notes:"Parking fills quickly, arrive early." },
    { id:"m3", team:"obsidian-ac", opponent:"Fort Vancouver SC", date:"2026-09-23", kick:"20:30", arrive:"20:00",
      venue:"Riverview Indoor Arena", address:"1200 SE Riverview Way, Vancouver, WA", home:true,
      kit:"Black shirts, black shorts", status:"scheduled", notes:"" },
    { id:"m4", team:"caa-u12", opponent:"Camas Youth Green", date:"2026-09-12", kick:"10:00", arrive:"09:30",
      venue:"Lacamas Lake Fields", address:"Lacamas Lake Park, Camas, WA", home:true,
      kit:"Blue shirts, navy shorts", status:"scheduled", notes:"Shin guards required, no exceptions." },
    { id:"m5", team:"obsidian-ac", opponent:"Columbia Athletic", date:"2026-08-26", kick:"20:30", arrive:"20:00",
      venue:"Riverview Indoor Arena", address:"1200 SE Riverview Way, Vancouver, WA", home:true,
      kit:"Black shirts, black shorts", status:"completed", score:"Obsidian AC 5 – 3 Columbia Athletic", notes:"" },
    { id:"m6", team:"obsidian-ac", opponent:"Salmon Creek FC", date:"2026-08-19", kick:"21:15", arrive:"20:45",
      venue:"Cascade Sports Center", address:"3400 NE 78th St, Vancouver, WA", home:false,
      kit:"White shirts, black shorts", status:"completed", score:"Salmon Creek FC 2 – 2 Obsidian AC", notes:"" }
  ],

  trainings: [
    { id:"t1", program:"youth",       date:"2026-09-07", time:"17:00", location:"lacamas", spaces:4 },
    { id:"t2", program:"small-group", date:"2026-09-08", time:"16:30", location:"lacamas", spaces:2 },
    { id:"t3", program:"adult",       date:"2026-09-08", time:"19:30", location:"heritage", spaces:6 },
    { id:"t4", program:"technical",   date:"2026-09-09", time:"18:00", location:"heritage", spaces:5 },
    { id:"t5", program:"conditioning",date:"2026-09-10", time:"18:00", location:"lacamas", spaces:7 },
    { id:"t6", program:"private",     date:"2026-09-12", time:"09:00", location:"lacamas", spaces:1 }
  ],

  standings: {
    "obsidian-ac": {
      league:"Riverview Winter Indoor, Division 2",   // REPLACE
      rows:[
        { team:"Cascade United",    p:4, w:3, d:1, l:0, gf:19, ga:9,  pts:10 },
        { team:"Obsidian AC",       p:4, w:2, d:1, l:1, gf:16, ga:12, pts:7, us:true },
        { team:"Riverside FC",      p:4, w:2, d:0, l:2, gf:14, ga:13, pts:6 },
        { team:"Fort Vancouver SC", p:4, w:1, d:1, l:2, gf:11, ga:15, pts:4 },
        { team:"Columbia Athletic", p:4, w:0, d:1, l:3, gf:10, ga:21, pts:1 }
      ]
    }
  },

  /* Rosters stay behind login. Public pages show initials only for minors. */
  roster: {
    "obsidian-ac":[
      { n:"A. Mambe", pos:"Manager", num:"—", minor:false },
      { n:"D. Okonkwo", pos:"Goalkeeper", num:"1", minor:false },
      { n:"J. Reyes", pos:"Defender", num:"4", minor:false },
      { n:"T. Nguyen", pos:"Defender", num:"5", minor:false },
      { n:"M. Haddad", pos:"Midfielder", num:"8", minor:false },
      { n:"S. Whitfield", pos:"Midfielder", num:"10", minor:false },
      { n:"K. Baptiste", pos:"Forward", num:"9", minor:false },
      { n:"P. Sandoval", pos:"Forward", num:"11", minor:false }
    ],
    "caa-u12":[
      { n:"Player A", pos:"Goalkeeper", num:"1", minor:true },
      { n:"Player B", pos:"Defender", num:"3", minor:true },
      { n:"Player C", pos:"Midfielder", num:"7", minor:true },
      { n:"Player D", pos:"Forward", num:"9", minor:true }
    ],
    "caa-u15":[
      { n:"Player E", pos:"Defender", num:"2", minor:true },
      { n:"Player F", pos:"Midfielder", num:"6", minor:true }
    ]
  },

  /* YouTube: replace yt with the real 11-character video ID. */
  videos: [
    { id:"v1", cat:"Ball mastery", yt:"", title:"Five ball mastery patterns to start every session",
      level:"Ages 7+, all levels", desc:"A short warm-up sequence players can run alone before training or in the back garden.",
      points:["Small touches, ball close to the standing foot","Head up between every pattern","Both feet, same number of repetitions"], drills:["Sole rolls, 30 seconds","Toe taps, 30 seconds","Inside-inside, 45 seconds"] },
    { id:"v2", cat:"Dribbling", yt:"", title:"Beating a defender one against one",
      level:"Ages 9+, intermediate", desc:"How to attack a defender's front foot and commit them before you move.",
      points:["Approach at an angle, not straight on","Change pace after the touch, not before","Protect the ball with your body after you go past"], drills:["Cone gate 1v1s","Chop and go repetitions"] },
    { id:"v3", cat:"Passing", yt:"", title:"Passing weight and the half turn",
      level:"Ages 10+, all levels", desc:"Why the weight of a pass decides your teammate's next touch.",
      points:["Pass to the far foot","Open your body before the ball arrives","Follow the pass with your eyes, then scan"], drills:["Wall passing, 5 minutes each foot","Three-player rondo"] },
    { id:"v4", cat:"Shooting", yt:"", title:"Striking through the ball for a low, hard finish",
      level:"Ages 9+, all levels", desc:"Plant foot, ankle lock and follow-through, broken down slowly.",
      points:["Plant foot beside the ball, pointing at the target","Ankle locked, strike with the laces","Follow through low to keep the ball down"], drills:["Static strikes, 20 each foot","One-touch finishes from a rolled pass"] },
    { id:"v5", cat:"First touch", yt:"", title:"First touch away from pressure",
      level:"Ages 8+, all levels", desc:"Taking your first touch into space instead of into your own feet.",
      points:["Check your shoulder before the ball arrives","Cushion across your body","Second touch is a pass or a run, never a stop"], drills:["Wall control and turn","Two-touch rondo"] },
    { id:"v6", cat:"Defending", yt:"", title:"Defending one against one without diving in",
      level:"Ages 10+, all levels", desc:"Body shape, distance and patience when you are the last defender.",
      points:["Side-on stance, show them one way","Stay on the balls of your feet","Tackle when their touch is heavy, not before"], drills:["Channel 1v1s","Recovery run and delay"] },
    { id:"v7", cat:"Goalkeeping", yt:"", title:"Set position and handling basics",
      level:"Ages 10+, goalkeepers", desc:"Where your hands, feet and weight should be as the shot is struck.",
      points:["Hands ready in front, not at your sides","Weight forward on the balls of the feet","W shape with the hands for shots above the waist"], drills:["Close-range handling","Set, save, reset repetitions"] },
    { id:"v8", cat:"Speed and agility", yt:"", title:"First three steps: acceleration for soccer",
      level:"Ages 12+, all levels", desc:"Getting away from a defender in the space that actually matters.",
      points:["Push the ground behind you, don't reach forward","Aggressive arm drive","Stay low for the first three steps"], drills:["Five-yard starts","Reaction sprints from a jog"] },
    { id:"v9", cat:"Tactical education", yt:"", title:"When to press and when to drop",
      level:"Ages 12+, intermediate", desc:"Reading the pressing trigger as a unit instead of chasing individually.",
      points:["Press when their touch is poor or they face their own goal","Never press alone","If the press is broken, drop and reset together"], drills:["Half-pitch pressing shadow play"] },
    { id:"v10", cat:"At-home training", yt:"", title:"A fifteen-minute routine with one ball and a wall",
      level:"Ages 7+, all levels", desc:"No cones, no partner, no field. Just a wall and fifteen minutes.",
      points:["Quality over speed for the first week","Count repetitions so you can see progress","Both feet every time"], drills:["Wall passes","Control and turn","Juggling ladder"] },
    { id:"v11", cat:"Match analysis", yt:"", title:"How to review your own match footage",
      level:"Ages 13+, intermediate", desc:"What to look for when you watch yourself back, and what to ignore.",
      points:["Watch your movement when you don't have the ball","Count how often you scan before receiving","Pick two things to fix, not ten"], drills:["Clip and label five moments from your last match"] }
  ],

  news: [
    { id:"n1", date:"2026-09-01", title:"Fall small-group blocks are open",
      body:"Six-week small-group blocks start the week of 15 September at Lacamas Lake Fields and Heritage Park. Groups are capped at six players and split by age and level. Book through the booking page or message Coach Arnold with questions about placement." },
    { id:"n2", date:"2026-08-25", title:"Obsidian AC is recruiting for the winter season",
      body:"Obsidian AC is looking for a goalkeeper, a centre back and a wide midfielder ahead of the winter indoor season. Applications go through the Obsidian AC page. Trial sessions run on Wednesday nights." },
    { id:"n3", date:"2026-08-18", title:"New training video series on first touch",
      body:"A short series on receiving under pressure is going up on the academy YouTube channel through September. Each video comes with a home drill that takes under fifteen minutes." }
  ],

  testimonials: [
    { q:"My son went from hiding on the wing to asking for the ball. Six weeks. That is the whole review.", a:"Parent of a U11 player, Camas", role:"Youth development" },   // REPLACE
    { q:"I hadn't played since high school and I was nervous about looking foolish. Coach Arnold pitched the session so I was working hard without being embarrassed.", a:"Adult beginner, Vancouver", role:"Adult training" },  // REPLACE
    { q:"The video analysis was the first time anyone showed me what I actually do off the ball. Two fixes, and my coach noticed within a month.", a:"U16 club player", role:"Video analysis" },   // REPLACE
    { q:"He plans the session, runs it properly and holds standards. Our team's warm-up alone is a different thing now.", a:"Rec team manager, Washougal", role:"Team training" }   // REPLACE
  ],

  faqs: [
    { q:"What ages do you coach?", a:"Players from about age five through adults. Sessions are grouped by age and level, and adults train with adults." },
    { q:"My child has never played before. Is that a problem?", a:"No. A good number of players start with no experience at all. The first session is about finding a comfortable starting point, not testing anyone." },
    { q:"Where do sessions take place?", a:"Camas, Vancouver and Washougal in Washington, plus east Portland in Oregon. The exact field is confirmed in your booking email." },
    { q:"What should we bring?", a:"Boots or turf shoes, shin guards, a ball if you have one, and water. Spare balls are available if you need one." },
    { q:"What happens if it rains?", a:"Most sessions run in rain. If a field closes or conditions become unsafe, you'll get an email and a WhatsApp message, and the session is rescheduled at no cost." },
    { q:"How do I cancel or reschedule?", a:"Reschedule free with at least 24 hours' notice from your account or by replying to your confirmation email. Inside 24 hours the session is charged in full. Full terms are on the cancellation policy page." },
    { q:"Do you offer packages?", a:"Yes. Blocks of five and ten sessions are available at a reduced per-session rate, and youth development runs in six-week blocks." },
    { q:"Are you licensed and background checked?", a:"Coach Arnold holds US Soccer coaching licences and completes SafeSport training and background screening. Documentation is available to parents on request." },
    { q:"How do I join Obsidian AC?", a:"Apply through the Obsidian AC page. Coach Arnold reviews applications and invites suitable players to a Wednesday trial session before any commitment." },
    { q:"Do you coach goalkeepers?", a:"Yes, through position-specific coaching. Goalkeeper sessions are private or in pairs." }
  ],

  /* Demo accounts for the front-end preview. Replace with real
     authentication before launch — see README, section "Authentication". */
  demoUsers: [
    { email:"player@demo.test",  pass:"demo1234", role:"player", name:"Sam Whitfield", teams:["obsidian-ac"] },
    { email:"parent@demo.test",  pass:"demo1234", role:"parent", name:"Dana Whitfield", children:[{name:"Jordan Whitfield", age:11, team:"caa-u12"},{name:"Ellie Whitfield", age:8, team:null}] },
    { email:"coach@demo.test",   pass:"demo1234", role:"coach",  name:"Arnold Eoka Mambe" }
  ]
};
