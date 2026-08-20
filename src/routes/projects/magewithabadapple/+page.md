---
title: MageWithABadApple
slug: magewithabadapple
date: 2025-01-01
hidden: true
excerpt: I got Bad Apple playing on a PocketMage and it was the most fun I've had with C++ in a while.
tags: [C++, hardware, demo, 'Projects']
repo: https://github.com/NellowTCS/MageWithABadApple
---

There's a long tradition of getting Bad Apple to play on things it was never meant to play on, and I wanted my crack at it. MageWithABadApple is my attempt at running the iconic shadow art animation on the PocketMage, a tiny handheld device that I probably shouldn't have been able to get video working on, but here we are.

The PocketMage has a small display and limited processing power, so the main challenge was fitting the animation data and the playback logic into something that could actually run. I used C++ for the core logic, handling frame decoding and display updates. The animation data is preprocessed into a compact format that the device can read through quickly enough to maintain a smooth frame rate.

Getting the timing right was the hardest part. The PocketMage doesn't have a ton of memory or CPU headroom, so I had to optimize the rendering path carefully. I ended up doing some bit-level manipulation to squeeze performance out of every frame draw. The result is a bit rough around the edges but it plays the full animation and honestly that was all I wanted.

This project was pure fun. No practical purpose, just me and a silly challenge. I think every developer needs projects like this that exist purely because they're entertaining.
