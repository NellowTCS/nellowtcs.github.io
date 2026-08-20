---
title: Tamaru
coverImage: /images/projects/tamaru.png
slug: tamaru
date: 2025-02-01
excerpt: A browser library that adds a virtual trackball to any webpage, complete with procedural sound effects and haptic feedback.
tags: ['TypeScript', 'Library', 'Audio', 'UI', 'Projects']
repo: https://github.com/NellowTCS/Tamaru
npm: tamaru
link: http://nellowtcs.me/Tamaru/
---

I had this idea one day: what if you could flick a webpage like a trackball? Not scroll, not swipe, but actually grab the page and throw it, watching it coast to a stop with real momentum. So I built Tamaru, a virtual trackball widget that does exactly that, and then I got way too carried away with the sound effects.

## What This Is

It's a draggable floating ball you flick to scroll a page with momentum and inertia. But honestly that description undersells it, because Tamaru also has procedural sound effects, haptic feedback, and a "Stick Mode" where it takes over your mouse entirely.

## The Physics

The physics engine runs on a `requestAnimationFrame` loop with friction decay of 0.92 per frame, a dead zone at 0.1, and velocity clamped to the range [-60, 60]. Simple, but it feels right when you're actually flicking the thing around.

## The Sound Engine (552 Lines)

This is where it got out of hand. Every single sound is generated from scratch using the Web Audio API. There are no samples, no audio files, nothing. The grab sound is layered noise bursts mixed with a low sine thump. Release is a softer, shorter version. Snap is a highpass burst with a triangle tone. Spin ticks are bandpass noise with frequency tied to scroll speed. The stop sound uses low bandpass plus a decaying sine. And then there's the rolling sound, which loops a 2.2-second noise buffer through a bandpass, highshelf, waveshaper, and gain chain, with gain and frequency ramped by speed. Every parameter has 12% random variation per event so no two sounds are identical.

The haptic engine uses the tactus library with a fallback to `navigator.vibrate()`, and different vibration patterns fire for different events.

## Stick Mode

Pointer Lock API takes over, the widget shrinks to 40% of its size, and mouse movement drives scroll directly. It's weirdly satisfying.

## Themes and Distribution

There are 7 themes, from default to neon to sunset. It works as an npm module, a Chrome extension, a bookmarklet, or a CDN script. The bookmarklet is one line of JS, which I'm unreasonably proud of.

## What's Next

Published to npm as `tamaru v0.1.1`. The name comes from Japanese "tamaru" meaning "to accumulate," which felt appropriate for a tool that accumulates momentum. Look, the truth is, the rolling sound alone took longer to build than most of my other entire projects.
