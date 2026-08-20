---
title: Picotility
coverImage: /images/projects/picotility.png
slug: picotility
date: 2025-07-01
excerpt: A PICO-8 fantasy console emulator that runs on ESP32 devices through the Tactility framework.
tags: ['C', 'Embedded', 'Emulator', 'ESP32', 'PICO-8', 'Projects']
repo: https://github.com/NellowTCS/Picotility
link: http://nellowtcs.me/Picotility/
---

PICO-8 is a fantasy console that reimines the constraints of 8-bit game hardware in a modern environment. It's charming. I wanted to take that one step further and run it on actual constrained hardware. That's Picotility, a PICO-8 emulator on ESP32.

## What This Does

It plays PICO-8 games on Tactility or in the browser via WASM. You load cartridges from an SD card or flash them directly to the device, and you get a pocket-sized game console. Sprites, tiles, the whole PICO-8 palette, rendered to a framebuffer on the ESP32's display.

## How It Works

The runtime is implemented in C. PICO-8's drawing and input APIs get mapped to Tactility's display and input drivers. The sprite and tile rendering pipeline translates PICO-8's drawing commands directly to framebuffer operations. Input comes through touch or physical buttons depending on your hardware setup.

The emulator handles PICO-8's Lua scripting environment, memory model, and graphics pipeline. Cartridges load from SD card or device storage. Sound goes through the ESP32's audio output.

## The Honest Assessment

Here's the truth: not every cartridge works yet. The core rendering and input handling work fine, but PICO-8 compatibility is not complete. Some games run, others don't. The goal is broad compatibility with the most popular PICO-8 titles, and I'm getting there, slowly.

PICO-8 already constrains you to 128x128 pixels and a 16-color palette, so running it on hardware that actually has those kinds of limitations feels oddly authentic. It's a fantasy console running on real fantasy hardware.

## Current Status

It's part of the Tactility app ecosystem, which handles the app management side. The emulator itself is functional but ongoing. Check it out at [nellowtcs.me/Picotility](http://nellowtcs.me/Picotility/) if you want to see a PICO-8 game running on something that fits in your pocket. It's not perfect yet, but it works, and that's a start.
