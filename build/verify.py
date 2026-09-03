import re, os, glob, sys
os.chdir('/home/claude/caa')
pages = sorted(glob.glob('*.html'))
files = set(pages)
problems = []

# 1. link check across html + js
targets = re.compile(r'href=["\']([^"\'#?]+\.html)')
for f in pages + ['assets/js/app.js','assets/js/dashboard.js']:
    src = open(f).read()
    for m in set(targets.findall(src)) | set(re.findall(r"href=['\"]?([a-z0-9\-]+\.html)", src)):
        if m.startswith(('http','mailto','tel')): continue
        if m not in files:
            problems.append(f"{f}: link to missing page {m}")

# 2. asset check
for f in pages:
    src = open(f).read()
    for a in re.findall(r'(?:src|href)="(assets/[^"]+)"', src):
        if not os.path.exists(a):
            problems.append(f"{f}: missing asset {a}")

# 3. getElementById targets exist in same page
for f in pages:
    src = open(f).read()
    ids = set(re.findall(r'id="([^"]+)"', src))
    script = "\n".join(re.findall(r'<script>(.*?)</script>', src, re.S))
    for gid in set(re.findall(r"getElementById\('([^']+)'\)", script)):
        if gid not in ids:
            problems.append(f"{f}: script targets #{gid} which is not in the page")

# 4. every page has title/desc/canonical/header/footer mounts
for f in pages:
    src = open(f).read()
    for need,label in [('<title>','title'),('name="description"','meta description'),
                       ('rel="canonical"','canonical'),('data-header','header mount'),
                       ('data-footer','footer mount'),('assets/js/app.js','app.js'),
                       ('skip','skip link')]:
        if need not in src: problems.append(f"{f}: missing {label}")

# 5. forms have data-form (so they get a confirmation) or an explicit id handler
for f in pages:
    src = open(f).read()
    for form in re.findall(r'<form[^>]*>', src):
        if 'data-form' not in form and 'id="signin-form"' not in form and 'id="register-form"' not in form and 'id="ann-form"' not in form:
            problems.append(f"{f}: form without data-form handler: {form[:70]}")

# 6. nav links in app.js all resolve
nav = re.findall(r"href: \"([a-z0-9\-]+\.html)\"", open('assets/js/app.js').read())
for n in nav:
    if n not in files: problems.append(f"app.js nav: {n} missing")

print(f"{len(pages)} pages checked, {len(nav)} nav links")
if problems:
    print("\nISSUES:")
    for p in problems: print(" -", p)
    sys.exit(1)
print("No issues found.")
