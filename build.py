#!/usr/bin/env python3
"""Builds the Drone Estates site pages. Run: python3 build.py"""
from pathlib import Path
ROOT = Path(__file__).parent

LOGO = '''<svg viewBox="0 0 40 40" fill="none" aria-hidden="true"><rect x="1" y="1" width="38" height="38" stroke="#3ea6f2" stroke-width="1.5"/><path d="M1 9V1h8M31 1h8v8M39 31v8h-8M9 39H1v-8" stroke="#fff" stroke-width="2"/><circle cx="20" cy="20" r="6" stroke="#fff" stroke-width="1.5"/><path d="M20 8v6M20 26v6M8 20h6M26 20h6" stroke="#3ea6f2" stroke-width="1.5"/></svg>'''

NAV = [("index.html","Home"),("services.html","Services"),("pricing.html","Pricing"),("build.html","Build a package"),("gallery.html","Gallery"),("about.html","About")]

def vf(img, alt, extra="", hud="", cls="vf", lazy=True, attrs=""):
    load = ' loading="lazy"' if lazy else ''
    return (f'<div class="{cls}"{attrs}><img src="img/{img}" alt="{alt}"{load}>'
            f'<div class="thirds"></div><div class="brk"><i></i><i></i><i></i><i></i></div><div class="xh"></div>{hud}{extra}</div>')

import json, html as _html
DOMAIN = "https://droneestates.com/"
HOME_LD = {"@context": "https://schema.org", "@type": "ProfessionalService", "name": "Drone Estates",
    "url": DOMAIN, "description": "Drone photos and aerial views for homeowners, events, and real estate.",
    "image": DOMAIN + "img/hero.jpg", "serviceType": "Aerial photography and video"}

def seo_head(slug, title, desc):
    url = DOMAIN + ("" if slug == "index.html" else slug)
    e = lambda s: _html.escape(s, quote=True)
    out = f"""<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon.png" sizes="32x32">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Drone Estates">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}img/hero.jpg">
<meta name="twitter:card" content="summary_large_image">"""
    if slug == "index.html":
        out += '\n<script type="application/ld+json">\n' + json.dumps(HOME_LD, indent=2) + '\n</script>'
    return out

def page(slug, title, desc, body):
    links = "".join(f'<a href="{h}"{" class=\"on\"" if h==slug else ""}>{t}</a>' for h,t in NAV)
    links += f'<a href="inquire.html" class="cta{" on" if slug=="inquire.html" else ""}">Inquire</a>'
    foot = "".join(f'<a href="{h}">{t}</a>' for h,t in NAV+[("inquire.html","Inquire")])
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
{seo_head(slug, title, desc)}
</head>
<body>
<header class="site-head"><div class="wrap">
<a class="brand" href="index.html">{LOGO}<span>Drone Estates<small>Aerial photography</small></span></a>
<input type="checkbox" id="mt" class="menu-toggle"><label for="mt" class="menu-btn" aria-label="Menu"><span></span></label>
<nav class="nav">{links}</nav>
</div></header>
<main>
{body}
</main>
<footer class="site-foot"><div class="wrap">
<a class="brand" href="index.html">{LOGO}<span>Drone Estates<small>Aerial photography</small></span></a>
<nav>{foot}</nav>
<span class="mono">&copy; 2026 Drone Estates</span>
</div></footer>
<script>
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}}),{{threshold:.12}});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
</script>
</body>
</html>
'''

# ---------- HOME ----------
home = f'''
<section class="hero vf" style="padding:0">
<img src="img/hero.jpg" alt="Aerial view over a wooded neighborhood with mountains on the horizon">
<div class="brk"><i></i><i></i><i></i><i></i></div><div class="xh"></div>
<div class="hud tl mono"><span class="rec">Rec</span></div>
<div class="hud tr mono"><span>Aerial view</span></div>
<div class="hud br mono"><span>Frame 01</span></div>
<div class="scale"></div><div class="scale scale-l"></div>
<div class="hero-copy"><div class="wrap">
<div class="kicker mono">Drone photography + aerial views</div>
<h1>See your place <em>from above.</em></h1>
<p class="lead">Drone photos and aerial views for homeowners, parties and events, real estate listings, and anyone who wants to see the bigger picture.</p>
<div class="btns"><a class="btn" href="inquire.html">Plan a shoot <span class="arr">&rarr;</span></a><a class="btn ghost" href="gallery.html">View the gallery</a></div>
</div></div>
</section>

<section>
<div class="wrap">
<div class="strip rv">
<a href="services.html#homeowners"><span class="n mono">01</span><h3>Homeowners</h3><p>Aerial photos of your home and property.</p></a>
<a href="services.html#events"><span class="n mono">02</span><h3>Parties and events</h3><p>Overhead shots of the gathering and the setting.</p></a>
<a href="services.html#agents"><span class="n mono">03</span><h3>Real estate agents</h3><p>Listing aerials that show the whole lot.</p></a>
<a href="services.html#custom"><span class="n mono">04</span><h3>Custom drone views</h3><p>Anyone who wants a view from the air.</p></a>
</div>
</div>
</section>

<section style="padding-top:20px">
<div class="wrap">
<div class="sec-head rv"><div><div class="eyebrow mono">Featured frames <b>/ 03</b></div><h2>Every angle,<br>from above.</h2></div>
<p>A drone can show what a camera on the ground cannot: the full shape of the lot, the roofline, the trees, and how the house sits in its surroundings.</p></div>
<div class="feat rv">
{vf("front.jpg","Front view of a two-story home with a two-car garage and green lawn", extra='<div class="cap"><span class="mono">Frame 02 / Front elevation</span><h3>The house, framed</h3></div>', hud='<div class="hud tr mono"><span class="rec">Rec</span></div>')}
<div class="stack">
{vf("overhead.jpg","High angle drone view of a home surrounded by tall trees", extra='<div class="cap"><span class="mono">Frame 03 / High angle</span><h3>The whole lot</h3></div>')}
{vf("topdown.jpg","Straight-down drone view of a roof, driveway and yard", extra='<div class="cap"><span class="mono">Frame 04 / Top down</span><h3>Straight overhead</h3></div>')}
</div>
</div>
</div>
</section>

<section>
<div class="wrap split">
<div class="rv">{vf("overhead-sm.jpg","Overhead view of a house, lawn and driveway", hud='<div class="hud bl mono"><span>Top down</span></div>')}</div>
<div class="rv">
<div class="eyebrow mono">Why aerial <b>/ 01</b></div>
<h2>The view people remember.</h2>
<p style="color:var(--mute);margin-top:18px">Ground photos show a room or a doorway. Aerial photos show the place: the yard, the trees, the driveway, the roof, and the neighborhood around it.</p>
<ul class="checks">
<li>High angle and straight-down views</li>
<li>Wide shots that take in the land and the horizon</li>
<li>Photos for your own keepsake, a listing, or an event</li>
</ul>
<div class="btns"><a class="btn ghost" href="services.html">See services</a></div>
</div>
</div>
</section>

<section class="price-teaser" style="padding-top:0">
<div class="wrap">
<div class="teaser rv">
<div class="teaser-copy"><div class="eyebrow mono">Pricing <b>/ Packages</b></div>
<h2>Clear pricing, no surprises</h2>
<p>Aerial photos and video for real estate in the Lake George, Glens Falls and Schroon Lake area.</p>
<ul class="checks">
<li><b>Basic</b> from $250. Aerial photos and a short clip.</li>
<li><b>Standard</b> from $475. Adds a full listing video and lot overview.</li>
<li><b>Premium</b> from $750. Adds a marked-up roof and lot report.</li>
</ul>
<p>No travel charge within 15 miles of Queensbury or in Schroon Lake*. We serve properties up to 60 road miles away. Final quotes are confirmed after your inquiry.</p>
<p style="font-size:14px">*Schroon Lake is included in Zone 1 at no travel charge because we're there often and schedule visits around regular trips. Same-day requests have the same-day fee no matter where you are.</p></div>
<div class="btns"><a class="btn ghost" href="pricing.html">See packages</a><a class="btn" href="inquire.html">Send an inquiry <span class="arr">&rarr;</span></a></div>
</div>
</div>
</section>

<section class="band">
{vf("canopy.jpg","View from above a roofline into tall trees", cls="vf", extra='<div class="inner"><div class="wrap"><div class="eyebrow mono">Ready when you are</div><h2>Have a place you want to see from the air?</h2><p>Tell us the date, the location, and what you want to capture.</p><div class="btns"><a class="btn" href="inquire.html">Start an inquiry <span class="arr">&rarr;</span></a></div></div></div>', hud='<div class="hud tr mono"><span class="rec">Rec</span><span>Frame 05</span></div>')}
</section>
'''

# ---------- SERVICES ----------
def card(id_, n, img, alt, title, text, tags, note="", start=""):
    t = "".join(f"<li>{x}</li>" for x in tags)
    nt = f'<span class="ph-note">{note}</span>' if note else ""
    nt = f'<p class="from">{start} <a class="mono" href="pricing.html">See pricing &rarr;</a></p>' + nt
    return f'''<article class="card rv" id="{id_}">{vf(img, alt, hud=f'<div class="hud tl mono"><span>{n}</span></div>')}
<div class="body"><span class="num mono">Service {n}</span><h3>{title}</h3><p>{text}</p><ul>{t}</ul>{nt}</div></article>'''

services = f'''
<section class="page-hero"><div class="wrap">
<div class="eyebrow mono">Services <b>/ 04</b></div>
<h1>What we shoot.</h1>
<p>Drone photos and aerial views for homes, gatherings, listings, and anything else that looks better from above.</p>
</div></section>
<section><div class="wrap">
<div class="cards">
{card("homeowners","01","front.jpg","Front view of a home from a drone","Homeowners","Aerial photos of your home and property. See the house, the yard, the trees, and the land around it the way you never can from the ground.",["Home + property","High angle","Top down"], start="Aerial photos with a short clip, starting at $250.")}
{card("events","02","lawn.jpg","Overhead view of a backyard lawn and patio","Parties and events","Overhead coverage of your party or event and the setting it happens in, from the backyard to the open field.",["Parties","Gatherings","Venues"],"Sample photo. Event photos coming soon.", start="Quoted per event. Send an inquiry with the date and place.")}
{card("agents","03","overhead.jpg","High angle view of a home for a listing","Real estate agents","Listing aerials that show the whole lot, the roofline, and the surroundings, so buyers understand the property at a glance.",["Listings","Lot + land","Neighborhood"], start="Aerial listing photos with a short clip, starting at $250. Full listing video starting at $475.")}
{card("custom","04","valley.jpg","Wide aerial landscape","Custom drone views","Anyone who wants drone photos or views. Land, a favorite spot, a project, or just the view from up there. Tell us what you have in mind.",["Land","Landscapes","Your idea"], start="Land and acreage maps starting at $250 for up to 10 acres. Other views quoted per property.")}
</div>
</div></section>
<section style="padding-top:0"><div class="wrap">
<div class="sec-head rv"><div><div class="eyebrow mono">Starting at <b>/ Pricing</b></div><h2>What it costs.</h2></div>
<p>Final quotes are confirmed after your inquiry. Travel charges may apply beyond 15 miles of Queensbury.</p></div>
<ul class="addons rv">
<li><span><b class="t">Listing Photos and Clips</b>Aerial listing photos with a short clip.</span><b>Starting at $250</b></li>
<li><span><b class="t">Listing Videos</b>Full aerial listing video with photos and a lot overview.</span><b>Starting at $475</b></li>
<li><span><b class="t">Roof and Lot Reports</b>Marked-up roof and lot report, a visual review from aerial images (not a home inspection). $295 on its own, or $750 with full listing media.</span><b>Starting at $295</b></li>
<li><span><b class="t">Land and Acreage</b>Overhead land maps with approximate boundary overlay, up to 10 acres.</span><b>Starting at $250</b></li>
<li><span><b class="t">Camps and Commercial (coming soon)</b>Quoted per property. Send an inquiry with the address and what you need.</span><b>By quote</b></li>
</ul>
<div class="btns rv"><a class="btn ghost" href="pricing.html">See packages</a></div>
</div></section>
<section style="padding-top:0"><div class="wrap">
<div class="sec-head rv"><div><div class="eyebrow mono">How it works <b>/ 03</b></div><h2>Simple from start to finish.</h2></div></div>
<div class="steps rv">
<div class="step"><span class="mono">Step 01</span><h3>Tell us about it</h3><p>Send the date, the location, and the type of shoot through the inquiry form.</p></div>
<div class="step"><span class="mono">Step 02</span><h3>We plan the flight</h3><p>We talk through the shots you want and pick a time that works.</p></div>
<div class="step"><span class="mono">Step 03</span><h3>You get the photos</h3><p>Your aerial photos are delivered for you to keep and share.</p></div>
</div>
<div class="btns rv" style="margin-top:40px"><a class="btn" href="inquire.html">Start an inquiry <span class="arr">&rarr;</span></a></div>
</div></section>
'''

# ---------- GALLERY ----------
G = [("valley","wide","Wide aerial over a wooded valley","Wide"),
     ("front","","Front of a home from the drone","Front elevation"),
     ("overhead","tall","High angle view of a home in the trees","High angle"),
     ("topdown","","Straight-down view of a roof and yard","Top down"),
     ("canopy","","View from above the roofline into tall trees","Over the roofline"),
     ("lawn","pano","Straight-down view of a lawn and patio","Detail")]
gitems = "".join(vf(f"{k}-sm.jpg" if c=="" else f"{k}.jpg", a, cls=f"vf {c}".strip(), hud=f'<div class="hud bl mono"><span>{i+1:02d} / {lbl}</span></div>', attrs=f' data-full="img/{k}.jpg" data-cap="{i+1:02d} / {lbl}"') for i,(k,c,a,lbl) in enumerate(G))
gallery = f'''
<section class="page-hero"><div class="wrap">
<div class="eyebrow mono">Gallery <b>/ {len(G):02d}</b></div>
<h1>From the air.</h1>
<p>Example drone photos of a home and its surroundings. Tap any frame to view it larger.</p>
</div></section>
<section><div class="wrap">
<div class="gallery rv">{gitems}</div>
</div></section>
<div class="lb" id="lb"><button class="x" aria-label="Close">Close &times;</button><img alt=""><div class="lbcap mono"></div></div>
<script>
const lb=document.getElementById('lb'),li=lb.querySelector('img'),lc=lb.querySelector('.lbcap');
document.querySelectorAll('.gallery .vf').forEach(v=>v.addEventListener('click',()=>{{li.src=v.dataset.full;li.alt=v.querySelector('img').alt;lc.textContent=v.dataset.cap;lb.classList.add('open')}}));
lb.addEventListener('click',e=>{{if(e.target!==li)lb.classList.remove('open')}});
document.addEventListener('keydown',e=>{{if(e.key==='Escape')lb.classList.remove('open')}});
</script>
'''

# ---------- ABOUT ----------
about = f'''
<section class="page-hero"><div class="wrap">
<div class="eyebrow mono">About <b>/ 01</b></div>
<h1>Your place, seen from above.</h1>
</div></section>
<section><div class="wrap split">
<div class="rv">{vf("canopy.jpg","View from above a roofline into tall trees", hud='<div class="hud bl mono"><span>Over the roofline</span></div>')}</div>
<div class="rv">
<h3>The gear</h3>
<p>Every shoot is flown on DJI drones and captured in 4K, for both photos and video.</p>
<h3>What we do</h3>
<p>Drone Estates captures aerial photos and video of homes, properties, and events. You tell us what you want to see from the air, and we plan the shoot around your date and location.</p>
<h3>How it works</h3>
<ol>
<li>Send an inquiry with the date, the place, and what you'd like captured.</li>
<li>We confirm the details and plan the flight.</li>
<li>The shoot is flown, and you receive your photos and video.</li>
</ol>
<div class="btns"><a class="btn" href="inquire.html">Inquire <span class="arr">&rarr;</span></a><a class="btn ghost" href="gallery.html">View the gallery</a></div>
</div>
</div></section>
'''

# ---------- INQUIRE ----------
inquire = f'''
<section class="page-hero"><div class="wrap">
<div class="eyebrow mono">Inquire <b>/ Plan a shoot</b></div>
<h1>Let's get you in the air.</h1>
<p>Tell us the date, the location, and what you want to capture.</p>
</div></section>
<section><div class="wrap form-grid">
<form class="inq rv" id="inquiry-form" action="https://formspree.io/f/xbgggqqk" method="POST" aria-describedby="fn">
<div class="form-note" id="fn">Send us the details below and we'll get back to you.</div>
<input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">
<input type="hidden" name="_subject" value="Drone Estates inquiry">
<fieldset style="border:0">
<div class="fields">
<div class="f"><label for="n">Name</label><input id="n" name="name" type="text" placeholder="Your name"></div>
<div class="f"><label for="e">Email</label><input id="e" name="email" type="email" placeholder="you@example.com"></div>
<div class="f"><label for="p">Phone</label><input id="p" name="phone" type="tel" placeholder="Phone number"></div>
<div class="f"><label for="d">Date</label><input id="d" name="date" type="date"></div>
<div class="f full"><label for="l">Location</label><input id="l" name="location" type="text" placeholder="Town or address of the shoot"></div>
<div class="f full"><label for="t">Type of shoot</label><select id="t" name="type"><option>Homeowner: home and property</option><option>Party or event</option><option>Real estate listing</option><option>Custom drone view</option><option>Something else</option></select></div>
<div class="f full"><label for="m">Message</label><textarea id="m" name="message" placeholder="What would you like to capture?"></textarea></div>
</div>
<button class="btn" type="submit">Send inquiry <span class="arr">&rarr;</span></button>
<p id="form-status" role="status" tabindex="-1" aria-live="polite" style="margin-top:16px"></p>
</fieldset>
</form>
<aside class="side rv">
{vf("topdown-sm.jpg","Straight-down drone view of a home", hud='<div class="hud tl mono"><span class="rec">Rec</span></div>')}
<div class="contact">
<h3>Contact</h3>
<p>The form is the best way to reach us. Tell us the date, the place, and what you'd like to capture, and we'll reply by email.</p>
<p>You can also reach us through <a href="https://mjnrealty.com">mjnrealty.com</a>.</p>
</div>
</aside>
</div></section>
<section style="padding-top:0"><div class="wrap">
<div class="quote-note rv">
<div class="eyebrow mono">Pricing and Packages</div>
<p>Every property is different, so each package has a range. Your final quote is confirmed after you send an inquiry, before anything is booked.</p>
<ul class="addons">
<li><span><b class="t">Basic</b>Aerial photos plus a short clip.</span><b>$250 to $350</b></li>
<li><span><b class="t">Standard</b>Everything in Basic, plus a full aerial listing video and a lot overview.</span><b>$475 to $695</b></li>
<li><span><b class="t">Premium</b>Everything in Standard, plus a roof and lot report (a visual review, not a home inspection) and a short written summary.</span><b>$750 to $995</b></li>
</ul>
<p>Travel is measured in road miles from Queensbury: no charge up to 15 miles and in Schroon Lake*, $40 from 15 to 30, $75 from 30 to 45, and $125 from 45 to 60 on scheduled days. We do not travel past 60 road miles.</p>
<p class="radius" style="color:var(--mute)">*Schroon Lake is included in Zone 1 at no travel charge because we're there often and schedule visits around regular trips. Same-day requests have the same-day fee no matter where you are.</p>
<div class="btns"><a class="btn" href="build.html">Design your own package <span class="arr">&rarr;</span></a><a class="btn ghost" href="pricing.html">See full pricing and add-ons</a></div>
</div>
</div></section>
<script src="js/inquiry.js"></script>
'''

# ---------- PRICING (DRAFT, Grant's numbers, pending Matthew's OK) ----------
def tier(n, name, rng, lead, items, feat=False):
    li = "".join(f"<li>{x}</li>" for x in items)
    return f'''<article class="tier rv{" feat" if feat else ""}">
<span class="num mono">Tier {n}</span><h3>{name}</h3>
<div class="range">{rng}</div>
<p>{lead}</p><ul class="checks">{li}</ul>
</article>'''

pricing = f'''
<section class="page-hero"><div class="wrap">
<div class="eyebrow mono">Pricing <b>/ Packages</b></div>
<h1>Pricing and Packages</h1>
<p>Every property is different, so each package has a range. Where your job lands depends on the size of the home, the size of the lot, and how much there is to cover. These ranges help you plan. Your final quote is confirmed after you send an inquiry, before anything is booked.</p>
</div></section>

<section><div class="wrap">
<div class="tiers">
{tier("01","Basic","$250 to $350","Aerial photos plus a short clip.",["15 to 25 edited aerial photos","A 15 to 30 second aerial clip, sized for MLS and social media","Delivery in 2 business days"])}
{tier("02","Standard","$475 to $695","Everything in Basic, plus:",["A full aerial listing video, 60 to 90 seconds, with music","A lot overview image showing the approximate property lines and key features"],feat=True)}
{tier("03","Premium","$750 to $995","Everything in Standard, plus:",["A roof and lot report: a visual review with marked-up aerial images showing visible wear, damage, drainage and other items worth a closer look","A short written summary you can share with buyers, sellers or a contractor"])}
</div>
<div class="moves rv">
<h3>What moves a price within the range</h3>
<ul class="checks">
<li>Home size and roof complexity</li>
<li>Lot size (packages cover up to 5 acres)</li>
<li>Extra buildings such as a garage, barn or shed</li>
<li>Tree cover, terrain or airspace that takes more flight time</li>
</ul>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap split-even">
<div class="rv">
<div class="eyebrow mono">Travel <b>/ From Queensbury</b></div>
<h2>Travel</h2>
<p style="color:var(--mute);margin-top:18px">Measured in road miles from Queensbury.</p>
<table class="zones">
<thead><tr><th class="mono">Zone</th><th class="mono">Road miles</th><th class="mono">Trip charge</th></tr></thead>
<tbody>
<tr><td>Zone 1<small>Glens Falls, Queensbury, Lake George, Hudson Falls, Warrensburg, Schroon Lake*</small></td><td>Up to 15, plus Schroon Lake*</td><td>No charge</td></tr>
<tr><td>Zone 2<small>Bolton Landing, Lake Luzerne, Saratoga Springs, Chestertown, Brant Lake</small></td><td>15 to 30</td><td>$40</td></tr>
<tr><td>Zone 3<small>North Creek, Hague, Minerva</small></td><td>30 to 45</td><td>$75</td></tr>
<tr><td>Zone 4<small>Ticonderoga, North Hudson, Indian Lake</small></td><td>45 to 60</td><td>$125, on scheduled days only</td></tr>
</tbody></table>
<p class="radius">*Schroon Lake is included in Zone 1 at no travel charge because we're there often and schedule visits around regular trips. Same-day requests have the same-day fee no matter where you are.</p>
<p class="radius">Maximum service radius: 60 road miles. We do not travel past 60 road miles from Queensbury.</p>
</div>
<div class="rv">
<div class="eyebrow mono">Add-ons <b>/ Extras</b></div>
<h2>Add-ons</h2>
<ul class="addons">
<li><span>Land or acreage map, stitched overhead image with approximate boundary overlay</span><b>Up to 10 acres $250<br>10 to 25 acres $395<br>25 to 50 acres $595<br>Over 50 acres by quote</b></li>
<li><span>Twilight shoot</span><b>$150</b></li>
<li><span>Next-day delivery</span><b>$75</b></li>
<li><span>Same-day delivery, when the schedule allows</span><b>$125</b></li>
<li><span>Extra round of edits (one round is included)</span><b>$50</b></li>
<li><span>Extra edited photos</span><b>$15 each</b></li>
<li><span>Vertical social media reel</span><b>$125</b></li>
<li><span>Extra building or structure beyond the main home</span><b>$50</b></li>
<li><span>Return visit, such as a seasonal or progress update</span><b>$125 plus travel</b></li>
</ul>
<p class="radius" style="color:var(--mute)">Weather: if it is not safe to fly, we reschedule at no charge. A reshoot requested after a completed shoot is 50% of the package price.</p>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="quote-note rv">
<h3>Good to know</h3>
<ul class="checks">
<li>The roof and lot report is a visual review from aerial images. It is not a licensed home inspection, an engineering report, or a land survey. Property lines on images are approximate.</li>
<li>Final quotes depend on the property and conditions, and are confirmed after your inquiry.</li>
</ul>
<div class="btns"><a class="btn" href="build.html">Design your own package <span class="arr">&rarr;</span></a><a class="btn ghost" href="inquire.html">Send an inquiry</a><a class="btn ghost" href="services.html">See services</a></div>
</div>
</div></section>
'''

PAGES = {
 "build.html": ("Build a package | Drone Estates", "Design your own Drone Estates package and send it as an inquiry.", (ROOT/"src"/"build_body.html").read_text()),
 "index.html": ("Drone Estates | Drone photos and aerial views", "Drone photos and aerial views for homeowners, events, and real estate.", home),
 "services.html": ("Services | Drone Estates", "Drone photography for homeowners, parties and events, real estate agents, and custom views.", services),
 "pricing.html": ("Pricing | Drone Estates", "Drone Estates packages, travel charges and add-ons.", pricing),
 "gallery.html": ("Gallery | Drone Estates", "Example drone photos from Drone Estates.", gallery),
 "about.html": ("About | Drone Estates", "About Drone Estates.", about),
 "inquire.html": ("Inquire | Drone Estates", "Plan a drone shoot with Drone Estates.", inquire),
}
for slug,(t,d,b) in PAGES.items():
    (ROOT/slug).write_text(page(slug,t,d,b))
print("built", ", ".join(PAGES))
