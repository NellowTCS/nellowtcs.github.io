---
title: TactilityNews
coverImage: /images/projects/tactilitynews.png
slug: tactilitynews
date: 2025-01-01
excerpt: A news reader app for the Tactility framework, displaying articles on ESP32 touchscreen devices.
tags: ['C++', 'Embedded', 'ESP32', 'News', 'Projects']
repo: https://github.com/NellowTCS/TactilityNews
---

What if you could check the news on a tiny ESP32 device with a touchscreen? Not read it on your phone like a normal person, but actually pull headlines onto a microcontroller the size of a credit card. That question is what kicked off TactilityNews, and the answer turned out to be more interesting than the question itself.

TactilityNews is a news reader app built for the Tactility framework. It fetches RSS feeds over WiFi, parses the XML into structured data, and renders headlines and summaries on the ESP32's display. It's part of the growing Tactility ecosystem, bringing real-world utility to embedded devices beyond the usual sensor readings and LED blink demos.

## How It Works

The app uses the ESP32's HTTP client to fetch RSS feeds, then parses the XML using a lightweight library that won't eat all your available memory. The C++ implementation handles network requests, XML parsing, and display rendering through Tactility's widget system. Headlines show up in a scrollable, touch-friendly interface that actually feels usable, not just technically impressive.

Memory management is the real challenge here. An ESP32 doesn't have much RAM, so the app has to be careful about what it loads and when. Feed data gets parsed and stored efficiently, and the UI only renders what's currently visible on screen. It's a constant balancing act between functionality and the very real constraints of the hardware.

## The Engineering Bits

The trickiest part was making the touch scrolling feel natural on a small screen. Tactility's UI framework gives you the building blocks, but getting smooth scrolling performance on an ESP32 means you can't be wasteful with redraws or memory allocations. Every frame matters when your processor is running at 240MHz and your display is the size of a postage stamp.

## Current Status

It works, it fetches news, and it's honestly one of those projects that makes me more excited about embedded development than almost anything else. The ESP32 platform keeps getting more capable, and projects like Tactility make me rethink what "embedded apps" actually means. It's not just blinking LEDs anymore. It's real software on real hardware doing real things, and that still feels like magic even though I built the thing myself.
