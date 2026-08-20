---
title: BadApple-CL-32
slug: badapple-cl-32
date: 2025-01-01
hidden: true
excerpt: Yes, I played Bad Apple in a 32-character wide terminal. Yes, it works.
tags: ['ASCII Art', 'Terminal', 'Fun', 'Projects']
repo: https://github.com/NellowTCS/BadApple-CL-32
---

You know the Bad Apple shadow art video? The one that people render on everything from graphing calculators to traffic lights? Well, someone had to do it in a 32-character wide terminal, and that someone was me.

BadApple-CL-32 takes the iconic Bad Apple animation and renders it as ASCII art in a ridiculously narrow terminal window. The project description just says "yes," which honestly captures the energy of this whole thing perfectly. There's no deep technical reason for it to exist. I just wanted to see if I could, and the answer was yes.

## How it works

The original Bad Apple video gets processed frame by frame, converting each frame into a text-based representation that fits within 32 columns. The rendering maps brightness values to ASCII characters, creating a recognizable approximation of the animation using nothing but text characters. A simple playback loop handles timing between frames to maintain the animation's pace.

It's straightforward in concept but fiddly in execution. Fitting recognizable visuals into such a narrow character width means making smart choices about which characters map to which brightness levels. The result is chunky, low-fi, and honestly kind of beautiful in a retro terminal aesthetic sort of way.

## Features

- Renders Bad Apple at 32 characters wide
- Frame-by-frame ASCII conversion
- Smooth playback in compatible terminals
- Zero dependencies beyond a basic terminal
- The ultimate proof of concept that you can, in fact, render anything anywhere

## The real question

Why 32 characters? Because 80 felt too easy. The narrower the width, the more creative you have to get with the character mapping, and that constraint is what makes the whole thing interesting. Sometimes the best projects are the ones that exist purely because someone whispered "but could you though" in your ear.
