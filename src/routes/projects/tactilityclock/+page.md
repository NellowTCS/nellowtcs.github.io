---
title: TactilityClock
coverImage: /images/projects/tactilityclock.png
slug: tactilityclock
date: 2025-01-01
excerpt: A clock app for ESP32 with both digital and analog modes, rendering a full clock face from scratch using LVGL primitives.
tags: ['C++', 'Embedded', 'ESP32', 'Clock', 'Projects']
repo: https://github.com/NellowTCS/TactilityClock
---

I kept wanting a clock on my ESP32 and nobody was building one the way I wanted it. Not a timer, not an alarm, just a clock. Digital mode, analog mode, time synced over WiFi, running on Tactility. So I built TactilityClock, and it turned out to be way more interesting than a "simple clock app" sounds.

## What This Is

Two modes. Digital shows HH:MM:SS with date, updated every second via an LVGL timer. Analog renders a full clock face from scratch using LVGL line primitives. That means custom vector graphics on a microcontroller. 12 hour markers drawn as `lv_line` objects using trigonometric calculations, quarter-hour markers thicker at 4px and longer than the intermediates at 1 to 2px. Three hands, hour, minute, second, as line objects from center to calculated endpoint. The second hand is red (`#FF0000`), the others white. It actually looks good, which surprised me.

## The Engineering Bits

This is C++17 with LVGL, ESP-IDF, and FreeRTOS. The dual-timer architecture is the piece I'm most proud of. An LVGL timer fires every second to update the UI. A separate FreeRTOS periodic timer fires every five seconds to check sync status and sets a `needs_redraw` flag. That separation keeps rendering and network operations on different threads without data races. It's proper engineering for a microcontroller, not just hacking something together.

Hand lengths are proportional to clock radius: 25% for hour, 35% for minute, 40% for second. Time sync happens via SNTP over WiFi, and if the year is still 1970, it prompts you to connect. Mode preference persists via Tactility's NVS flash preferences, so you don't lose your choice on reboot.

## What's Running Under There

The sdkconfig reveals WiFi enabled, Bluetooth disabled, FreeRTOS at 1000Hz tick rate. Three gallery photos show it running on actual hardware, which matters because LVGL on a real screen versus a simulator is a different beast.

It's a small project but it taught me a lot about thread safety on constrained hardware and building UIs with nothing but line primitives. Drawing a clock face from scratch using trigonometry and line segments is the kind of thing that sounds easy until you realize you're doing floating-point math on a chip with no FPU. Look, the truth is, a clock shouldn't be this interesting. But on an ESP32, everything is a little more interesting than it should be.
