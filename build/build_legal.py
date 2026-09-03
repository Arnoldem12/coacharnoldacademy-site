from shared import shell, page_hero

REVIEW = ('<div class="notice"><strong>Template wording, not legal advice.</strong>'
          '<p>These policies are a solid starting point written for a small coaching business in Washington State. '
          'Coach Arnold should have them reviewed by an attorney or insurer before launch, and the waiver in particular '
          'should match the wording his liability insurance requires.</p></div>')

UPDATED = '<p class="print-note">Last updated 1 September 2026. Coach Arnold Academy, Camas, Washington.</p>'


def legal(fname, title, h1, lede, sections, seo_desc, review=True):
    body = page_hero(title, h1, lede) + '<section><div class="wrap-n legal">'
    body += '<div class="toc"><strong>On this page</strong>'
    body += "".join('<a href="#s%d">%s</a>' % (i, s[0]) for i, s in enumerate(sections))
    body += "</div>"
    if review:
        body += REVIEW
    for i, (head, content) in enumerate(sections):
        body += '<h2 id="s%d">%s</h2>%s' % (i, head, content)
    body += UPDATED + '<div class="btn-row"><a class="btn dark-ghost" href="policies.html">All policies</a>'
    body += '<a class="btn dark-ghost" href="contact.html">Ask about this policy</a></div>'
    body += "</div></section>"
    shell(fname, title + " | Coach Arnold Academy", seo_desc, body)


# ----------------------------------------------------------------- POLICIES INDEX
pol_body = page_hero("Policies", "Policies and documents",
  "Everything you agree to when you book a session or join a team, in plain language.") + """
<section>
  <div class="wrap">
    <div class="grid g3">
      <article class="tile"><h3>Cancellation and refunds</h3><p>Rescheduling windows, no-shows, weather, refunds and packages.</p><div class="foot"><a class="btn sm" href="refunds.html">Read</a></div></article>
      <article class="tile"><h3>Privacy policy</h3><p>What information is collected, why, how long it's kept, and your rights over it.</p><div class="foot"><a class="btn sm" href="privacy.html">Read</a></div></article>
      <article class="tile"><h3>Terms of use</h3><p>The rules for using this website and booking coaching services.</p><div class="foot"><a class="btn sm" href="terms.html">Read</a></div></article>
      <article class="tile"><h3>Liability waiver</h3><p>Assumption of risk and release, agreed at booking by every participant.</p><div class="foot"><a class="btn sm" href="waiver.html">Read</a></div></article>
      <article class="tile"><h3>Parent and guardian consent</h3><p>What a parent agrees to when registering a child under 18.</p><div class="foot"><a class="btn sm" href="consent.html">Read</a></div></article>
      <article class="tile"><h3>Code of conduct</h3><p>Expectations for players, parents and coaches, and what happens if they're broken.</p><div class="foot"><a class="btn sm" href="conduct.html">Read</a></div></article>
      <article class="tile"><h3>Concussion and player safety</h3><p>Recognising a head injury, the removal-from-play rule, and return-to-play steps.</p><div class="foot"><a class="btn sm" href="safety.html">Read</a></div></article>
      <article class="tile"><h3>Accessibility statement</h3><p>How this website is built for accessibility and how to report a problem.</p><div class="foot"><a class="btn sm" href="accessibility.html">Read</a></div></article>
      <article class="tile"><h3>Frequently asked questions</h3><p>Practical answers about sessions, pricing and joining a team.</p><div class="foot"><a class="btn sm" href="faq.html">Read</a></div></article>
    </div>
  </div>
</section>
"""
shell("policies.html", "Policies, Waivers and Consent Forms | Coach Arnold Academy",
      "Cancellation policy, privacy policy, terms of use, liability waiver, parent consent, code of conduct and concussion safety information for Coach Arnold Academy.",
      pol_body)

# ----------------------------------------------------------------- REFUNDS
legal("refunds.html", "Cancellation and refund policy", "Cancellation and refund policy",
  "How rescheduling, cancellations, weather and refunds work. Written to be fair in both directions.",
  [
   ("Rescheduling", "<p>Sessions can be rescheduled free of charge with at least 24 hours' notice, from your account or by replying to your confirmation email. There is no limit on how often you reschedule, provided the notice period is met.</p>"),
   ("Cancelling inside 24 hours", "<p>A session cancelled with less than 24 hours' notice is charged in full, because the slot cannot realistically be refilled. If you are ill, or something genuinely unavoidable happens, contact Coach Arnold. Illness and family emergencies are not treated as no-shows.</p>"),
   ("No-shows", "<p>A player who does not arrive and does not make contact is charged in full. Coach Arnold waits at the field for twenty minutes before recording a no-show.</p>"),
   ("Cancellations by Coach Arnold", "<p>If a session is cancelled by Coach Arnold for any reason, including illness, field closure or unsafe conditions, you are offered a rescheduled session at no cost, or a full refund. You choose which.</p>"),
   ("Weather", "<p>Sessions run in rain, which is normal in this part of the world. Sessions are cancelled for lightning, ice, extreme heat, hazardous air quality, or a field closure by the facility. You will be told by email and WhatsApp as early as possible, and the session is rescheduled at no cost.</p>"),
   ("Packages and blocks", "<p>Five and ten session blocks expire ten and twenty weeks after the first session respectively. Unused sessions in an expired block are not refunded, but an extension will be granted for injury or illness if you ask. A block can be transferred to a sibling.</p>"),
   ("Monthly memberships", "<p>Memberships bill on the same date each month and can be cancelled with 30 days' notice. Cancelling part-way through a month does not produce a partial refund, and access continues to the end of the paid period.</p>"),
   ("Team and season fees", "<p>Season fees cover league registration, referees and venue hire, most of which is paid up front and is non-refundable once the season begins. A refund before the season starts is given minus any registration cost already paid to the league. Tryout fees, where charged, are refunded only if the tryout is cancelled.</p>"),
   ("How refunds are issued", "<p>Refunds go back to the original payment method within ten working days. Card refunds may take a further few days to appear depending on your bank. No card details are stored by Coach Arnold Academy at any point.</p>"),
   ("Injuries", "<p>If a player suffers an injury that prevents training for more than two weeks, remaining sessions are credited rather than lost. A note from a medical professional is helpful but not required.</p>"),
   ("Disputes", "<p>If you think a charge is wrong, contact Coach Arnold directly before disputing it with your bank. Almost everything is resolved in a single message.</p>")
  ],
  "Cancellation and refund policy for Coach Arnold Academy soccer coaching: rescheduling windows, weather cancellations, packages, memberships and season fees.")

# ----------------------------------------------------------------- PRIVACY
legal("privacy.html", "Privacy policy", "Privacy policy",
  "What information this website collects, why it is collected, how long it is kept, and what you can ask for.",
  [
   ("Who is responsible", "<p>Coach Arnold Academy, operated by Arnold Eoka Mambe in Camas, Washington, is responsible for the personal information collected through this website. Questions about privacy go to <span data-site-email></span>.</p>"),
   ("What is collected", "<p>Depending on what you use, the site collects:</p><ul>"
    "<li><strong>Contact details</strong> such as name, email address, phone number and city, from booking, application and contact forms.</li>"
    "<li><strong>Player details</strong> such as age, skill level, position and development goals.</li>"
    "<li><strong>Health information</strong> such as injuries, medical conditions, allergies and medication, provided voluntarily so that sessions are run safely.</li>"
    "<li><strong>Emergency contact details</strong> for the person to call if something happens during a session.</li>"
    "<li><strong>Account information</strong> if you create a login, including your name, email and a password.</li>"
    "<li><strong>Technical information</strong> such as pages visited, if you accept analytics cookies.</li></ul>"),
   ("Children's information", "<p>Children under 18 do not create their own accounts. Registration, consent, medical details and communication are handled by a parent or legal guardian. A child's full name, photograph, date of birth or contact details are never published on a public page. Rosters visible to signed-in team members show a first name and last initial for anyone under 18.</p>"
    "<p>A parent may ask at any time to see, correct or delete everything held about their child, and the request will be actioned within thirty days. Where the Children's Online Privacy Protection Act applies, information about a child under 13 is collected only from a parent or guardian.</p>"),
   ("Why information is used", "<p>To run bookings and registrations, to keep players safe during sessions, to communicate about schedules and changes, to process payments, and to send announcements you have asked for. It is not used for anything else.</p>"),
   ("Who it is shared with", "<p>Personal information is not sold, rented or traded. It is shared only with service providers that make the site work, such as the website host, the email service and the payment processor, and only to the extent needed. It may also be shared where the law requires it, or in a medical emergency where sharing is necessary to protect someone.</p>"),
   ("Payments", "<p>Card payments are handled entirely by a payment processor. Card numbers, expiry dates and security codes are never seen by, transmitted to, or stored on this website.</p>"),
   ("Photographs and video", "<p>Photographs and video are published only where consent has been given. Consent is separate from every other agreement, is optional, and can be withdrawn at any time by emailing or messaging Coach Arnold. Existing images are removed within two working days of a request. No image of a minor is published without written parental consent.</p>"),
   ("Cookies", "<p>Essential cookies keep you signed in and remember your cookie choice. They cannot be turned off without breaking the login. Optional analytics cookies help show which pages are useful, and are only set if you accept them. You can change your choice at any time by clearing your browser storage for this site.</p>"),
   ("How long information is kept", "<p>Booking and registration records are kept for as long as needed to run the service and meet legal and insurance requirements, and are then deleted. Contact form messages are deleted once the conversation has ended. Newsletter subscriptions are kept until you unsubscribe. Health information is kept only while a player is active and is deleted afterwards.</p>"),
   ("Your rights", "<p>You can ask for a copy of what is held about you or your child, ask for corrections, ask for deletion, withdraw consent for photographs or marketing, and unsubscribe from emails using the link in any message. Requests go to <span data-site-email></span> and are answered within thirty days.</p>"),
   ("Security", "<p>The site is served over an encrypted connection. Accounts are protected by passwords, and access to personal and health information is limited to Coach Arnold. No system is perfect, so information collected is deliberately kept to the minimum needed.</p>"),
   ("Changes", "<p>If this policy changes materially, the date at the bottom is updated and anyone with an account is notified by email.</p>")
  ],
  "Privacy policy for Coach Arnold Academy: what information is collected from parents, players and visitors, how it is protected, and how to request deletion.")

# ----------------------------------------------------------------- TERMS
legal("terms.html", "Terms of use", "Terms of use",
  "The rules for using this website and booking coaching services from Coach Arnold Academy.",
  [
   ("Agreement", "<p>Using this website, creating an account or booking a session means you accept these terms. If you do not accept them, do not use the site.</p>"),
   ("Who can book", "<p>You must be 18 or over to create an account or make a booking. A booking for a player under 18 must be made by that player's parent or legal guardian, who is responsible for the accuracy of the information provided.</p>"),
   ("Accounts", "<p>Keep your password private and tell Coach Arnold promptly if you think someone else has access to your account. You are responsible for activity that happens under your login. Accounts may be suspended for behaviour that breaches the code of conduct.</p>"),
   ("Bookings", "<p>A booking request is a request, not a confirmed session, until Coach Arnold confirms it. If a requested slot has gone, you will be offered the nearest alternative. Sessions are subject to the cancellation and refund policy.</p>"),
   ("Fees", "<p>Prices are shown on the programs pages and can change, though a change never affects a session already confirmed. Fees are payable before or at the session unless agreed otherwise.</p>"),
   ("Accuracy of information", "<p>Health, injury and emergency contact information must be accurate and kept current. Coaching decisions are made on the basis of what you tell us, and incomplete information can put a player at risk.</p>"),
   ("Acceptable use", "<p>Do not attempt to gain access to accounts or areas you are not entitled to, submit false information, upload harmful files, scrape the site, or use it to harass anyone. Team information, rosters, tactics and WhatsApp group links are for team members only and must not be shared outside the squad.</p>"),
   ("Content on this site", "<p>Text, images, video, coaching materials, the academy crest and the Obsidian AC crest belong to Coach Arnold Academy and may not be reproduced commercially without permission. You are welcome to share links, and to use training videos for personal practice.</p>"),
   ("No guarantee of outcome", "<p>Coaching improves players who put the work in, but no specific outcome is promised: not selection for a team, not a scholarship, not a particular level of play.</p>"),
   ("Limitation of liability", "<p>To the extent permitted by Washington State law, Coach Arnold Academy is not liable for indirect or consequential losses arising from use of this website. Nothing in these terms limits liability for death or personal injury caused by negligence, or for anything else that cannot lawfully be limited.</p>"),
   ("Third-party links", "<p>Links to YouTube, WhatsApp, Instagram, Facebook, mapping services and payment providers are provided for convenience. Those services have their own terms and privacy policies.</p>"),
   ("Governing law", "<p>These terms are governed by the laws of the State of Washington, and disputes are subject to the courts of Clark County, Washington.</p>")
  ],
  "Terms of use for the Coach Arnold Academy website: accounts, bookings, fees, acceptable use, content ownership and limitation of liability.")

# ----------------------------------------------------------------- WAIVER
legal("waiver.html", "Liability waiver", "Liability waiver and assumption of risk",
  "Agreed by every participant at booking. Parents or guardians agree on behalf of players under 18.",
  [
   ("Assumption of risk", "<p>Soccer is a physical sport played at speed on grass, turf and indoor surfaces. Participation carries risks including, but not limited to, sprains, strains, fractures, dental injury, concussion and other head injury, collisions with other players, equipment or surfaces, injury from weather or field conditions, and in rare cases serious or catastrophic injury. By taking part, the participant knowingly and voluntarily accepts these risks.</p>"),
   ("Fitness to participate", "<p>The participant confirms they are physically able to take part, and that any medical condition, injury, allergy or medication relevant to their safety has been disclosed at registration and will be kept up to date.</p>"),
   ("Release", "<p>In exchange for being allowed to take part, the participant, and where the participant is a minor their parent or legal guardian, releases Coach Arnold Academy, Arnold Eoka Mambe, and any assistant coaches, volunteers or venue operators from claims for injury, loss or damage arising from participation, except where caused by gross negligence or wilful misconduct.</p>"),
   ("Medical treatment", "<p>If a participant is injured and a parent or guardian cannot be reached, Coach Arnold is authorised to arrange emergency medical treatment, including calling emergency services and transport to hospital. The participant or guardian is responsible for the cost of any treatment.</p>"),
   ("Insurance", "<p>Participants are strongly encouraged to hold their own health insurance. Coach Arnold Academy does not provide medical or accident insurance for participants.</p>"),
   ("Equipment", "<p>Shin guards are required at every session and every match, with no exceptions. Appropriate footwear must be worn for the surface. Jewellery, watches and hard hair accessories must be removed before play.</p>"),
   ("Photography", "<p>Photography and video consent is a separate, optional agreement recorded at registration. Declining it has no effect on participation.</p>"),
   ("Agreement", "<p>By ticking the waiver box during booking, registration or a team application, the person completing the form confirms that they have read and understood this waiver, that they are the participant or that participant's parent or legal guardian, and that they are signing it freely.</p>"),
   ("Printable copy", '<p>A printed copy can be requested at any time. <button class="btn sm dark-ghost" type="button" onclick="window.print()">Print this page</button></p>')
  ],
  "Liability waiver and assumption of risk for Coach Arnold Academy soccer coaching sessions, training and matches in Washington State.")

# ----------------------------------------------------------------- CONSENT
legal("consent.html", "Parent and guardian consent", "Parent and guardian consent",
  "What a parent or legal guardian agrees to when registering a player under 18.",
  [
   ("Who must complete registration", "<p>Every player under 18 must be registered by a parent or legal guardian. Children do not hold their own accounts, do not receive direct messages from the coach, and are not asked for personal information directly.</p>"),
   ("Consent to participate", "<p>The parent or guardian consents to the child taking part in coaching sessions, training and, where applicable, matches, and confirms that the child is physically able to take part.</p>"),
   ("Medical consent", "<p>The parent or guardian authorises emergency medical treatment if they cannot be reached, and confirms that medical conditions, allergies, medication and recent injuries have been disclosed and will be kept current.</p>"),
   ("Emergency contacts", "<p>At least one emergency contact, reachable during sessions, must be provided. A second contact is strongly recommended.</p>"),
   ("Collection and drop-off", "<p>Children must be collected promptly at the end of a session. Coach Arnold stays with any child who has not been collected and will contact the emergency numbers. Tell Coach Arnold in advance if someone other than the usual adult will be collecting the child.</p>"),
   ("Photography and video consent", "<p>This is optional and separate. Without it, no image of the child is published on the website, on social media, or in any promotional material. Consent can be withdrawn at any time, in writing or by message, and images are removed within two working days. Declining photo consent has no effect whatsoever on the child's coaching.</p>"),
   ("Communication", "<p>All communication about a child goes through the parent or guardian account. Coach Arnold does not message players under 18 privately. Where a team WhatsApp group includes minors, a parent must also be in the group.</p>"),
   ("Safeguarding", "<p>Coach Arnold is SafeSport trained and background screened. Sessions are open for parents to watch at any time. Concerns about a child's welfare should be raised directly and will be taken seriously.</p>"),
   ("Behaviour", "<p>The parent or guardian agrees to the code of conduct on the child's behalf and agrees to support it from the sideline.</p>"),
   ("Withdrawing consent", "<p>Consent can be withdrawn at any time by contacting Coach Arnold. Withdrawal ends participation from that point and is handled without argument.</p>")
  ],
  "Parent and guardian consent for youth soccer coaching at Coach Arnold Academy: participation, medical consent, photography consent and safeguarding.")

# ----------------------------------------------------------------- CONDUCT
legal("conduct.html", "Code of conduct", "Code of conduct",
  "What is expected from players, parents and coaches. Short, and applied consistently.",
  [
   ("Players", "<ul><li>Arrive on time and ready to work.</li><li>Listen when someone is speaking, including teammates.</li>"
    "<li>Try the difficult thing. Mistakes made while trying are not a problem.</li><li>Respect teammates, opponents and officials, whatever the score.</li>"
    "<li>No abusive, discriminatory or intimidating language of any kind.</li><li>Look after equipment and the facility.</li>"
    "<li>Tell a coach immediately if you are hurt, or if you see something that isn't right.</li></ul>"),
   ("Parents and spectators", "<ul><li>Support every player on the field, not just your own.</li><li>Leave the coaching to the coach during sessions and matches.</li>"
    "<li>Never criticise an official, a child or another parent.</li><li>Be on time for drop-off and collection.</li>"
    "<li>Raise concerns with Coach Arnold directly and privately, never on the sideline or online.</li></ul>"),
   ("Coaches", "<ul><li>Plan every session before it starts.</li><li>Treat every player fairly regardless of ability, background or how much they pay.</li>"
    "<li>Keep players safe, and stop a session if conditions are unsafe.</li><li>Never be alone and unobserved with a child.</li>"
    "<li>Communicate with minors through their parent or guardian.</li><li>Be honest about a player's development, kindly.</li></ul>"),
   ("Discrimination and harassment", "<p>Discrimination or harassment on any basis, including race, ethnicity, national origin, religion, sex, gender identity, sexual orientation, disability or age, ends participation immediately. There is no warning stage for this.</p>"),
   ("What happens if the code is broken", "<p>Most issues are resolved with a quiet word. Where they are not: a conversation with the player and parent, then a session or match suspension, then removal from the program. Serious incidents skip straight to removal. Fees are not refunded where participation ends because of conduct.</p>"),
   ("Raising a concern", "<p>Speak to Coach Arnold directly, or write to <span data-site-email></span>. Concerns about the safety or welfare of a child are treated urgently, and where necessary reported to the appropriate authority.</p>")
  ],
  "Code of conduct for players, parents and coaches at Coach Arnold Academy, covering behaviour, respect, discrimination and how breaches are handled.",
  review=False)

# ----------------------------------------------------------------- SAFETY
legal("safety.html", "Concussion and player safety", "Concussion and player safety",
  "How head injuries are handled, plus the everyday safety practices used at every session.",
  [
   ("The rule", "<p><strong>When in doubt, sit them out.</strong> Any player suspected of having sustained a concussion is removed from play immediately and does not return that day, regardless of how they feel five minutes later, what the score is, or how much they want to carry on. This applies at every session and every match.</p>"),
   ("Recognising a concussion", "<p>A concussion does not require a loss of consciousness. Watch for:</p><ul>"
    "<li>Headache, pressure in the head, dizziness or balance problems</li><li>Nausea or vomiting</li>"
    "<li>Confusion, slow responses, or being unsure of the score or opponent</li><li>Blurred or double vision, sensitivity to light or noise</li>"
    "<li>Memory problems, particularly about the incident itself</li><li>Behaviour or personality changes, unusual irritability or emotion</li>"
    "<li>Feeling foggy, sluggish or simply not right</li></ul>"
    "<p>Symptoms can appear hours later. Parents should watch for them through the evening.</p>"),
   ("Emergency signs", "<p>Call 911 immediately if a player has one pupil larger than the other, cannot be woken, has a worsening headache, has slurred speech or weakness, has a seizure, vomits repeatedly, or becomes increasingly confused or agitated. Do not drive them yourself.</p>"),
   ("Return to play", "<p>Washington State's Zackery Lystedt Law requires written clearance from a licensed health care provider trained in concussion evaluation before a youth athlete returns to play. Coach Arnold follows this without exception, and will not accept a parent's verbal assurance in place of written clearance.</p>"
    "<p>Return happens in stages: light aerobic activity, then sport-specific movement without contact, then non-contact drills, then full training, then match play. Each stage takes at least 24 hours, and any returning symptom sends the player back a stage.</p>"),
   ("Heading the ball", "<p>In line with US Soccer guidance, heading is not taught or practised with players aged 10 and under. For ages 11 and 12, heading in training is limited and taught with proper technique using appropriate balls.</p>"),
   ("Heat, cold and air quality", "<p>Sessions are modified or cancelled in extreme heat, with extra water breaks and reduced intensity. Sessions are cancelled for lightning, and do not resume until 30 minutes after the last strike. Sessions are cancelled when air quality reaches unhealthy levels, which matters in this region during wildfire season.</p>"),
   ("Equipment and surfaces", "<p>Shin guards are mandatory. Goals are checked for anchoring before every session. Fields are walked for hazards before players arrive. Jewellery and hard hair accessories are removed before play.</p>"),
   ("Injury reduction", "<p>Every session includes a structured warm-up and a cool-down. Conditioning work includes ankle, knee and hip strengthening drawn from established injury-prevention programs, which meaningfully reduce non-contact knee injuries in youth players.</p>"),
   ("First aid", "<p>Coach Arnold carries a first aid kit to every session and holds current first aid and CPR certification. Emergency contact details for every registered player are accessible at the field.</p>"),
   ("Talk to us", "<p>If a player has a history of concussion, a chronic condition, or an injury they're returning from, tell Coach Arnold before the first session. Sessions are adapted willingly and without fuss.</p>")
  ],
  "Concussion protocol and player safety information for Coach Arnold Academy: recognising head injuries, return-to-play steps, heading guidance and weather policy.",
  review=False)

# ----------------------------------------------------------------- ACCESSIBILITY
legal("accessibility.html", "Accessibility statement", "Accessibility statement",
  "How this website is built to be usable by everyone, and how to tell us when it isn't.",
  [
   ("Our aim", "<p>This site aims to meet the Web Content Accessibility Guidelines version 2.1 at level AA. Accessibility is treated as part of building the site, not a later addition.</p>"),
   ("What has been done", "<ul>"
    "<li>Every page works with a keyboard alone, and the focused element is always clearly visible.</li>"
    "<li>Colour contrast meets AA for body text and interface elements.</li>"
    "<li>Headings are properly nested so screen reader users can navigate by structure.</li>"
    "<li>Form fields have real labels, and errors say what is wrong in plain words rather than only turning a border red.</li>"
    "<li>A skip link at the top of every page jumps straight to the main content.</li>"
    "<li>Animation is minimal, and is switched off entirely for anyone whose device requests reduced motion.</li>"
    "<li>Text reflows properly at 200 percent zoom and on small screens.</li>"
    "<li>Images that carry meaning have alternative text. Decorative graphics are hidden from screen readers.</li></ul>"),
   ("Known gaps", "<p>Two things still need work, and they are listed here rather than quietly ignored:</p><ul>"
    "<li>Training videos need captions. Captions will be added to every video on the YouTube channel.</li>"
    "<li>Photo galleries currently use placeholder images. Real alternative text will be written for each photograph as it is added.</li></ul>"),
   ("Accessibility at sessions", "<p>Players with disabilities, chronic conditions or additional needs are welcome. Sessions are adapted, and it helps enormously to know in advance what would make the session work better. The booking form has a field for this, and Coach Arnold reads it.</p>"),
   ("Tell us about a problem", "<p>If something on this site is hard to use, please say so. Email <span data-site-email></span> with the page and what happened, and it will be fixed. A reply comes within five working days, and an alternative way of getting the information will be offered straight away.</p>")
  ],
  "Accessibility statement for the Coach Arnold Academy website, covering WCAG 2.1 AA conformance, keyboard access, reduced motion and how to report problems.",
  review=False)

# ----------------------------------------------------------------- 404
err_body = """
<section class="hero" data-pitch style="min-height:62vh;display:grid;align-items:center">
  <div class="glow"></div>
  <div class="wrap inner hero-anim">
    <span class="kicker"><i></i> Error 404</span>
    <h1>That page has gone out of play</h1>
    <p class="lede">The link is broken, or the page has moved. Nothing is lost. Here is where most people are heading.</p>
    <div class="btn-row">
      <a class="btn" href="index.html">Back to the home page</a>
      <a class="btn ghost" href="programs.html">Coaching programs</a>
      <a class="btn ghost" href="book.html">Book a session</a>
      <a class="btn ghost" href="contact.html">Contact Coach Arnold</a>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="head"><span class="rule"></span><h2>Or try one of these</h2></div>
    <div class="grid g4">
      <div class="feature"><h3><a href="about.html">About Coach Arnold</a></h3><p>Philosophy, experience and credentials.</p></div>
      <div class="feature"><h3><a href="teams.html">Teams</a></h3><p>Academy squads and how to join one.</p></div>
      <div class="feature"><h3><a href="obsidian-ac.html">Obsidian AC</a></h3><p>The adult indoor side.</p></div>
      <div class="feature"><h3><a href="schedule.html">Schedule</a></h3><p>Fixtures, results and open sessions.</p></div>
      <div class="feature"><h3><a href="videos.html">Training videos</a></h3><p>Drills you can do at home.</p></div>
      <div class="feature"><h3><a href="news.html">News</a></h3><p>Announcements and registration windows.</p></div>
      <div class="feature"><h3><a href="faq.html">FAQ</a></h3><p>Practical answers about sessions.</p></div>
      <div class="feature"><h3><a href="policies.html">Policies</a></h3><p>Waivers, privacy and cancellations.</p></div>
    </div>
    <p class="small muted" style="margin-top:1.6rem">If a link on this site sent you here, please <a href="contact.html">tell Coach Arnold</a> so it can be fixed.</p>
  </div>
</section>
"""
shell("404.html", "Page not found | Coach Arnold Academy",
      "That page could not be found. Head back to the home page, browse coaching programs, or contact Coach Arnold.",
      err_body)

print("legal pages built")
