---
title: tmplScan
coverImage: /images/projects/tmplscan.png
slug: tmplscan
date: 2025-01-01
excerpt: A simple web tool to find who has used your HTML template, limited but functional.
tags: ['HTML', 'Tool', 'Web', 'Projects']
repo: https://github.com/NellowTCS/tmplScan
link: http://nellowtcs.me/tmplScan/
---

I released a website template for free, and then I got curious. Who's actually using it? Where did they deploy it? Did they modify it or just use it exactly as-is? There was no easy way to find out, so I built tmplScan.

It's a simple page where you point it at a template and it checks whether that organization or person is using your template. That's the whole thing. No server-side processing, no database, just client-side HTML analysis that looks for structural fingerprints matching your template's patterns. "Very limited, but it works!" is honestly the most accurate description I can give.

## How It Works

tmplScan fetches the target page and parses its HTML structure. It looks for specific element patterns, class names, and structural markers that match the template you're scanning for. If enough of those markers line up, it flags the site as a likely user. You can customize what patterns it looks for, so it's not locked to one specific template.

Everything happens in the browser. You enter a URL, the page fetches it, runs the analysis, and shows you the results. There are some limitations because of CORS restrictions, which means certain cross-origin pages won't cooperate, but for most cases it gets the job done.

## What This Is

Look, this isn't a web crawler. It's not trying to be. It's a quick and dirty way to satisfy your curiosity about who's using something you built. You point it at a URL, it tells you if the template matches, and you move on with your day.

The interface is minimal on purpose. You type in a domain, hit scan, and see the results. No account needed, no configuration required, no learning curve. It does one thing and it does it adequately.

## Current Status

I've used it to find a handful of sites running my templates, and every time it feels weird and cool in equal measure. There's something surreal about seeing your work live on someone else's domain. tmplScan won't win any awards for sophistication, but if you've ever released a template and wondered who picked it up, this scratches that itch. Sometimes limited tools are the ones that actually get used.
