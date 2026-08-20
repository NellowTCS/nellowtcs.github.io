---
title: TactileWeb
coverImage: /images/projects/tactileweb.png
slug: tactileweb
date: 2025-01-01
excerpt: A text-based web browser that runs on ESP32 microcontrollers, fetching and displaying web pages on a tiny screen.
tags: ['C++', 'Embedded', 'Browser', 'ESP32', 'Projects']
repo: https://github.com/NellowTCS/TactileWeb
---

Running a web browser on 520KB of RAM is inherently absurd, and that's exactly why I had to do it.

TactileWeb is a text-based web browser for the ESP32. You type in a URL, it fetches the HTML over WiFi, strips out every tag, and displays whatever text is left in a scrollable LVGL text area. That's the whole thing. No images, no CSS, no JavaScript, no rendering engine. Just raw text, pixel by pixel, on a tiny screen that probably can't fit a tweet.

## What This Is

The core of it is dead simple. The browser does an HTTP GET using `esp_http_client`, reads up to 32KB of raw HTML, then runs it through a bundled `html2text` library adapted from giwa/html2text. The adaptation is minimal, basically a two-state scanner with `HTML_FIRST` and `HTML_MID` states that skips everything between `<` and `>`. It truncates the result to about 8KB for display. That's your whole web experience now. Plain text. Welcome back to 1992.

## The Engineering Bits

This is C++17 compiled for the Xtensa architecture via ESP-IDF, using LVGL for the UI and Tactility as the app framework. I had to reimplement `local_strncmp` from scratch because it's not exported from the Tactility SDK, which felt like a rite of passage.

There's a known bug where the first `idf.py` build always returns an error code even when the ELF binary is actually created. So the tool just checks for the ELF's existence and moves on. Sometimes you just have to work around the toolchain and accept the chaos.

## Current Status

It works. It fetches pages, strips tags, displays text. The Tactility preferences system remembers your last URL between sessions, which is a nicer UX than you'd expect from something running on a chip smaller than a postage stamp. The whole project is a reminder that underneath all the JavaScript frameworks and CSS animations, the web is really just text. Sometimes less isn't just more, it's everything.
