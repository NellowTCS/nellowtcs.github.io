---
title: infinitescroll
coverImage: /images/projects/infinitescroll.png
slug: infinitescroll
date: 2025-01-01
excerpt: An endless animated gradient background with interactive controls that literally never stops scrolling.
tags: ['JavaScript', 'CSS', 'Animation', 'Projects']
repo: https://github.com/NellowTCS/infinitescroll
link: http://nellowtcs.me/infinitescroll/
---

I had this dumb idea one day: what if a gradient just... never stopped? Not in the "oh it loops" way, but in the "the page keeps growing forever and the gradient keeps cycling through colors" way. So I built infinitescroll, and then I accidentally made it way more technical than a dumb gradient page has any right to be.

## What This Is

It's a full-screen animated gradient that cycles through 17-color palettes, shifts angle based on your mouse position, has floating depth orbs with parallax, and the page literally never ends. When you get within 3000px of the bottom, the content height increases by 400vh. You cannot reach the bottom. That's the whole point.

## The CSS Houdini Part

Here's where it gets interesting. The gradient uses CSS Houdini's `CSS.registerProperty()` to register 8 custom properties as typed color values. This lets CSS actually animate between gradient stops, which normal CSS custom properties can't do. Without this, you'd just get a hard jump between colors. With it, you get smooth, buttery cycling through the entire palette.

## Themes and Controls

Six themes: Pastel, Neon, Ocean, Sunset, Forest, and Cosmic. Each one defines its own 17-color palette that the gradient cycles through. Mouse X position shifts the gradient angle plus or minus 20 degrees, so moving your cursor actually changes how the gradient flows. Saturation intensity is adjustable from 20 to 150 percent.

## Keyboard Shortcuts

Space toggles pause and play. F goes fullscreen, and yes, the README notes that F means "to pay respects." S opens settings. Plus and minus control speed. Can't make this stuff up.

## The Floating Orbs

There are floating orbs with depth parallax that drift around on top of the gradient. They're purely decorative and I love them.

## Distribution

It respects `prefers-reduced-motion`, which feels important for something this visually intense. It can bundle as a single HTML file. Published to npm. There's PWA support, which the README acknowledges as unnecessary with the note "Install as a standalone app on any device. for some reason."

## What's Next

Look, the truth is, this project started as a joke and turned into a genuinely interesting CSS experiment. The Houdini stuff alone taught me more about how browsers render gradients than I ever expected to learn. Sometimes you build something dumb and it accidentally teaches you something real.
