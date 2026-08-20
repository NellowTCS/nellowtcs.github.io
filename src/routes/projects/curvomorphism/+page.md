---
title: Curvomorphism
coverImage: /images/projects/curvomorphism.png
slug: curvomorphism
date: 2025-01-01
excerpt: An original UI design concept where corner rounding follows position and direction rather than being uniform.
tags: ['Design', 'UI', 'Concept', 'Projects']
repo: https://github.com/NellowTCS/Curvomorphism
---

Most UI design trends treat corner rounding as a one-size-fits-all number. You set `border-radius: 12px` and every corner on every element gets the same curve. I thought that was a missed opportunity, so I came up with Curvomorphism. The name is a portmanteau of "curve" and "neumorphism," and yes, I'm aware that's a lot.

## What This Is

The core idea is simple but the implications are kind of beautiful. Corner rounding should be positional and directional, not uniform. Elements closer to the center of the screen get rounded inner corners, the ones facing inward. Elements near the edges get sharp outer corners. It creates this visual "pull" toward the center, a subtle gravitational effect that guides the eye without you noticing.

Think about it. If you have a card in the top-left corner, its bottom-right corners (the ones facing the center) should curve inward. Its top-left corners, pointing away, stay sharp. That's Curvomorphism in a nutshell.

## How It Works

There are two approaches in the repo. The CSS version uses static classes like `.position-top-left` that you apply based on where the element sits. The JavaScript version is more interesting: `applyCurvomorphism(element, centerX, centerY)` dynamically calculates which corners face the center and rounds only those. It compares the element's center to the screen center and applies border-radius selectively.

It's a concept repo, not a code library. The README lays out the philosophy, the technique, and a single SVG example. I cite iOS Shortcuts as a real-world example of something approaching this pattern, though Apple has never committed to the full concept. There's a "Why Bother?" section in the README that includes "Aesthetic-ness" as a bullet point, which I think is honest.

## Current Status

I'm currently using Curvomorphism in beta for HTMLPlayer v2. The author hedge in the README says it "guides the eye naturally to the center (i'd assume)" and I think that's fair. It's a design hypothesis more than a proven technique. But every new UI trend started as someone's weird idea, and I'd rather put mine out there than keep it in a notebook. The repo is open, the idea is documented, and if anyone wants to run with it, go for it. I just wanted to see if the concept worked. Turns out it kind of does.
