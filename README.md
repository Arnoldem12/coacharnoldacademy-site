# Coach Arnold Academy

Website for Coach Arnold Academy: soccer coaching for youth and adults in Camas, Vancouver and Washougal WA, and Portland OR. Includes the Obsidian AC indoor team section.

Built as a static site: plain HTML, CSS and JavaScript. No build step, no framework, no dependencies to install. Open `index.html` in a browser and it runs.

---

## What works right now, and what doesn't

Being straight about this so nothing surprises you after launch.

**Fully working today**
- All 30 pages, navigation, mobile layout, accessibility features
- Every form: validation, error messages, success confirmations, spam honeypot
- Booking flow, team applications, tryout registration, contact, newsletter, feedback
- Match availability responses, recorded and visible to the coach
- Schedule with filtering, search, results and calendar links (Google Calendar, plus `.ics` for Apple Calendar and Outlook)
- WhatsApp click-to-chat throughout, with private group links kept off public pages
- SEO: titles, meta descriptions, Open Graph, structured data, sitemap, robots.txt

**Works as a realistic preview, needs a backend to be real**
- **Form delivery.** Submissions are stored in the visitor's browser, not emailed to you. Until a form service is connected, you will not receive them. This is the first thing to fix. See *Forms and email* below.
- **Payments.** No card processing. The booking form records the chosen payment method and you send a payment link manually. No card data ever touches this site. See *Payments*.
- **File uploads.** The photo field on the team application does not upload anywhere yet.
- **Automated WhatsApp messages.** Click-to-chat links work today. Automatic sending needs the WhatsApp Business API, which is a separate paid service. Email is the primary notification channel.

Everything in the second list is marked clearly in the interface, so nobody is misled about what happened when they press a button.

---

## Deploying

### GitHub Pages (simplest)
1. Create a repository and push these files to the `main` branch.
2. Settings → Pages → Source → **GitHub Actions**.
3. The included workflow at `.github/workflows/deploy.yml` publishes on every push.
4. For a custom domain: Settings → Pages → Custom domain, then add a `CNAME` file containing your domain, and point your DNS at GitHub.

`.nojekyll` is included so GitHub serves the files as-is.

### Netlify or Cloudflare Pages
Drag the folder into the dashboard, or connect the repository. Build command: none. Publish directory: `/`. Both give free HTTPS and better form handling than Pages, which matters — see below.

### After the domain is live
Search and replace `https://www.coacharnoldacademy.com` with your real domain in:
- every `.html` file (canonical URLs, Open Graph tags, structured data)
- `robots.txt`
- `sitemap.xml`
- `build/shared.py`, if you regenerate pages

---

## Editing content without touching code

Almost everything is in **`assets/js/data.js`**. It is a plain text file with comments. Change a price, add a fixture, edit a program description, add a news post: all there.

Anything marked `// REPLACE` must be changed before launch:

- `site.email`, `site.phone`, `site.whatsapp` — currently a fictional 555 number
- `site.facebook`, `site.youtube` — placeholder URLs (Instagram is real)
- `site.ga4` — your Google Analytics 4 measurement ID
- All five entries in `locations` — real field names and addresses
- Prices on all ten programs
- Team histories, league name, standings
- All four testimonials
- Every `yt` field in `videos` — the eleven-character YouTube ID

Your US Soccer coaching ID is deliberately **not** published anywhere on the site. It's an identifier tied to your record; there's no benefit to putting it on a public page. The About page says documentation is available on request instead.

### Editing content
Everything is in `assets/js/data.js`. Edit it, commit and push; Netlify redeploys in about thirty seconds. If that becomes tiresome, move the content into a hosted CMS (Decap, Sanity and Contentful all work with a static site like this) — the page structure doesn't need to change.

---

## Connecting the missing pieces

Each of these is a contained job. Claude Code can do them one at a time.

### Forms and email
**Netlify Forms is already connected and receiving.** All four forms (`contacts`, `bookings`, `applications`, `tryouts`) carry `data-netlify="true"` and a hidden `form-name`, and `netlifySubmit()` in `app.js` POSTs to `/` on submit. Submissions appear at app.netlify.com → your site → **Forms**.

Turn on **Forms → Settings → Form notifications → Email** so submissions reach an inbox rather than waiting to be found.

`wireForms()` also keeps a copy in the submitting visitor's own `localStorage`. That copy is per-browser and never reaches Coach Arnold — Netlify is the real record.

Note that booking and application forms carry health information about children. Check Netlify's data handling is something you're comfortable with, and keep notifications on so nothing sits unread.

### Authentication (removed)
There is no login on this site. It previously had a browser-only one whose password sat in the public `data.js`, guarding a dashboard that could only ever show the current browser's own data. It was removed rather than repaired.

If real accounts are ever needed, Supabase Auth, Clerk and Auth0 all have free tiers and handle password hashing, resets and sessions properly. That needs a backend for the data too — see below.

### Database
The store keys used are: `bookings`, `applications`, `tryouts`, `contacts`, `questions`, `newsletter`, `testimonials`, `sponsors`, `announcements`, `content`. Each maps to a table. Supabase (Postgres) fits well and pairs with its own auth.

### Payments
Stripe Checkout is the least work and never exposes card data to your site: create a Checkout Session server-side, redirect the customer, handle the webhook to mark the booking paid. Supports single sessions, packages, subscriptions for monthly memberships, and discount codes natively. **Never collect card numbers in a form on this site.**

### Social embeds
Instagram's live feed needs the Basic Display API or a third-party widget. Facebook's Page plugin is a copy-paste iframe. Both slots are marked on the home page.

### Team store
The Obsidian AC store section is a placeholder. Shopify Buy Buttons, Square Online or Printful all drop into that card.

---

## File structure

```
index.html                  Home
about.html                  Coach Arnold biography
programs.html               Program directory
program.html?id=            Program detail (one page, driven by data.js)
book.html                   Booking and registration
teams.html                  Team directory
team.html?id=               Team detail
obsidian-ac.html            Obsidian AC section
join-team.html              Team application
schedule.html               Fixtures, results, training, availability
videos.html / video.html    Training videos
news.html                   Announcements
contact.html                Contact
faq / testimonials / gallery / sponsorship / policies
privacy / terms / waiver / consent / conduct / safety / accessibility / refunds
404.html

assets/css/site.css         All styling, tokens at the top
assets/js/data.js           All content — edit this
assets/js/app.js            Header, footer, forms, auth, calendar
assets/img/                 Logo and favicons

build/                      Python scripts that generated the pages
build/verify.py             Checks links, assets, forms, meta tags
```

`build/` is for regenerating pages in bulk. You can delete it and edit the HTML directly — nothing at runtime depends on it. Keep `verify.py` if you'd like to re-run the checks.

---

## Child safety decisions built into the site

These were deliberate, and worth keeping if you change things later.

- Minors are never asked to create anything. A parent submits registration and consent.
- Rosters, tactics, lineups and WhatsApp links are never published. Squad members get them from Coach Arnold directly.
- Photo consent is a separate optional tick box on every form, never bundled with the waiver, and can be withdrawn.
- Medical and emergency contact fields are collected but never displayed publicly.
- The privacy policy commits to deleting a child's data on request within thirty days.
- The concussion page follows Washington's Lystedt Law: written medical clearance before return to play, no exceptions.

---

## Before you launch

- [ ] Replace every `// REPLACE` value in `data.js`
- [x] Netlify Forms connected — turn on email notifications in the Netlify dashboard
- [ ] Have an attorney or your insurer review the waiver, privacy policy and terms
- [ ] Confirm real prices, locations and league details
- [ ] Add real photographs, and check photo consent is on file for any minor shown
- [ ] Add YouTube video IDs
- [x] Live at https://coacharnoldacademy.com
- [x] GA4 connected (`site.ga4` in `data.js`); the tag loads only after a visitor accepts analytics cookies
- [x] Verified in Google Search Console and Bing, `sitemap.xml` submitted to both
- [ ] Run `python3 build/verify.py` one last time
