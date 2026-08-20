---
title: UTAU.js
coverImage: /images/projects/utaujs.png
slug: utau-js
date: 2025-03-01
excerpt: A browser-based singing voice synthesizer that creates vocal audio from pure math, no samples or AI needed.
tags: ['TypeScript', 'Web Audio', 'Music', 'DSP', 'Projects']
repo: https://github.com/NellowTCS/UTAU.js
link: http://nellowtcs.me/UTAU.js/
---

I've been obsessed with vocal synthesis for years, and at some point I realized I didn't just want to _use_ these tools, I wanted to understand what's actually happening under the hood. Like, what does it really take to make a computer sing? Not sample-based, not AI, but actual math generating a voice from scratch. So I built UTAU.js, a complete parametric singing voice synthesizer that runs entirely in the browser.

## What This Is

This is not what you think it is. It's not loading samples and stitching them together. UTAU.js generates singing audio from pure mathematical source-filter modeling. The voice is built from scratch using DSP, which is both really cool and kind of unhinged when you think about the fact that it runs in a web browser.

## The Engineering Bits

The core uses a Liljencrants-Fant glottal source model, the same math from the actual academic paper that describes how human vocal cords vibrate. It has jitter, shimmer, aspiration noise, a DC blocker, the works. The output then passes through a formant cascade made of biquad IIR filters, Direct Form I, with anti-resonators and resonators stacked up. Coefficients get placed using bilinear transform pole placement, and formant targets are interpolated with smoothstep so you don't get weird artifacts between phonemes.

The formant coefficients update roughly every 5ms, which is about 220 samples at 44100Hz. There's a comment in the code explaining why `sin(PI*x)` prevents clicks at glottal closure, and yeah, there are academic citations in the source. It's the kind of thing that makes me feel like I'm doing real engineering instead of just hacking on a side project.

## How It Actually Works

The renderer pipeline goes lyric to phoneme symbols via G2P, then phoneme lookup, LF glottal pulse generation, formant cascade, noise mixing, amplitude envelope, and normalization. There are three G2P systems: Japanese handles hiragana, romaji, and kanji with EDICT2 data. English uses ARPAbet via CMUDict. Mandarin does pinyin. The voice system uses a "OneVoice" approach where you map high-level sliders to DSP parameters with `scaleVoice()`.

The whole thing uses AsyncGenerators for lazy rendering through a stream pipeline, so you're not loading the entire song into memory at once.

## Current Status

It's published to npm as `utaujs v0.1.0` with 160+ tests. You can import and export through 16 and 14 different formats respectively, all via utaformatix-ts. Look, the truth is, it generates singing from pure math. No samples, no recordings, no AI. That still kind of blows my mind.
