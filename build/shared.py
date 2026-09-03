"""Shared HTML shell for every page of the Coach Arnold Academy site."""
import os, re

OUT = "/home/claude/caa"
SITE = "https://www.coacharnoldacademy.com"  # REPLACE when the domain is live

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,400;0,500;0,600;1,400&'
         'family=Saira+Condensed:wght@600;700;800&display=swap" rel="stylesheet">')

def shell(fname, title, desc, body, jsonld="", extra_js="", body_attr="", og_type="website"):
    canonical = SITE + "/" + ("" if fname == "index.html" else fname)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#05070E">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Coach Arnold Academy">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/logo-512.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/img/logo-512.png">
<!-- Google Search Console: paste the verification token from data.js site.searchConsole -->
<meta name="google-site-verification" content="REPLACE_WITH_VERIFICATION_TOKEN">
<link rel="icon" href="assets/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="assets/css/site.css">
{jsonld}
</head>
<body{body_attr}>
<a class="skip" href="#main">Skip to content</a>
<div data-header></div>
<main id="main">
{body}
</main>
<div data-footer></div>
<script src="assets/js/data.js"></script>
<script src="assets/js/app.js"></script>
{extra_js}
<!-- Google Analytics 4 — uncomment and paste your measurement ID from data.js site.ga4
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XXXXXXXXXX');</script>
-->
</body>
</html>
"""
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(html)
    return fname


def ld(obj):
    return '<script type="application/ld+json">' + obj + "</script>"


def page_hero(crumbs, h1, lede, actions=""):
    c = ""
    if crumbs:
        c = '<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / ' + crumbs + "</nav>"
    a = f'<div class="btn-row">{actions}</div>' if actions else ""
    return f"""<section class="page-hero" data-pitch>
  <div class="wrap inner">
    {c}
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    {a}
  </div>
</section>"""


LOCAL_BUSINESS = """{
  "@context":"https://schema.org",
  "@type":"SportsActivityLocation",
  "name":"Coach Arnold Academy",
  "description":"Private, small-group and team soccer coaching for children, teenagers and adults in Camas and Vancouver, Washington and the Portland metro area.",
  "url":"%s",
  "logo":"%s/assets/img/logo-512.png",
  "image":"%s/assets/img/logo-512.png",
  "telephone":"+1-360-555-0142",
  "email":"coach@coacharnoldacademy.com",
  "priceRange":"$$",
  "address":{"@type":"PostalAddress","addressLocality":"Camas","addressRegion":"WA","addressCountry":"US"},
  "areaServed":[
    {"@type":"City","name":"Camas"},{"@type":"City","name":"Vancouver"},
    {"@type":"City","name":"Washougal"},{"@type":"City","name":"Portland"}
  ],
  "sport":"Soccer",
  "founder":{"@type":"Person","name":"Arnold Eoka Mambe","jobTitle":"US Soccer licensed coach"},
  "sameAs":["https://instagram.com/coacharnoldacademy"],
  "openingHoursSpecification":[{
    "@type":"OpeningHoursSpecification",
    "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "opens":"08:00","closes":"21:00"
  }]
}""" % (SITE, SITE, SITE)
