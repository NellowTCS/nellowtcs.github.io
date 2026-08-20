---
title: be-annoyed
coverImage: /images/projects/beannoyed.png
slug: be-annoyed
date: 2025-01-01
excerpt: A website deliberately engineered to be as annoying as possible, with random rickrolls, fake progress bars, and keyboard theft.
tags: ['JavaScript', 'Prank', 'Web', 'Projects']
repo: https://github.com/NellowTCS/be-annoyed
link: http://nellowtcs.me/be-annoyed/
---

I wanted to build a website where every single design decision was made in bad faith. Not broken, not bad, but deliberately hostile. Like, what if a web developer woke up and chose violence? That's be-annoyed, and honestly it was one of the most fun things I've ever coded.

## What This Is

It's a webpage engineered to be as annoying as possible. Before you even see it, there's a 20% chance you get rickrolled on load. Links show fake "Loading..." states then "404?" messages. A progress bar asymptotically approaches 98% and literally cannot reach 100%. Random "nail tap" sounds fire every 5 seconds via Web Audio. Text inputs randomly insert "oops" or delete your characters. Checkboxes toggle all their siblings when you click one.

## The 622-Line Main Event

`main.js` is where the real chaos lives. Random screen effects like invert, blur, and zoom fire every 2.5 seconds. About 7% of your keypresses are silently eaten, except Tab and F5 which I figured should still work out of mercy. Random elements get Comic Sans mid-sentence. Every single click spawns confetti. Fake system notifications pop up. The cookie banner has multiple lives and you have to click Accept 3 times. Popup windows multiply. Tab key sends focus to random elements. The page title changes to "I miss you!" when you switch tabs. Scroll gets jacked. Links jump on hover. The cursor randomly changes to "wait." I could keep going but you get the idea.

## Easter Eggs

Type "annoy" for MAXIMUM ANNOYANCE MODE. Type "github" to actually go to the source code. Type "google" and you get "I'm not a search engine." The TODO list has one item: "make the website more yandere haha (yes seriously)."

## The Technical Reality

Every annoying behavior is modular JavaScript: `navigation.js`, `fakeProgress.js`, `sounds.js`, `formAnnoyances.js`, `mouseTrail.js`, `marqueeFooter.js`, and `main.js`. It can be bundled as a single HTML file. Yes, you can install this as a PWA. I'm not sure why you would, but the option exists.

## Current Status

Look, the truth is, it works exactly as advertised. It's terrible. I'm proud of it.
