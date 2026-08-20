---
title: tBMP
coverImage: /images/projects/tbmp.png
slug: tbmp
date: 2025-01-01
excerpt: A brand new image format I created from scratch, with multiple encoding modes, schema-driven structure, and zero dependencies.
tags: ['C', 'Image Format', 'Library', 'Projects']
repo: https://github.com/NellowTCS/tBMP
cargo: tbmp
link: http://nellowtcs.me/tBMP/
docs: http://nellowtcs.me/tBMP/
---

I wanted a tiny image format. Not "tiny" as in "a wrapper around BMP" but actually tiny. A new format, designed from scratch, for compact and efficient image storage. That became tBMP.

tBMP is a binary image format with its own file structure, its own encoding modes, its own metadata system, and its own schema. The `.tbmp` file format is defined in a Kaitai Struct schema (`tBMP.ksy`), which means the binary layout is formally specified, not just implied by code.

## How It Works

The format supports multiple encoding modes: RAW (uncompressed), RLE (run-length encoding), zero-range, span, sparse pixel, and block-sparse. You pick the encoding that fits your image. A solid-color sprite? RLE compresses it to almost nothing. A scattered particle effect? Sparse pixel encoding skips the empty space entirely.

The library is zero-allocation. You provide the buffers, tBMP reads into them. No malloc, no hidden allocations, no surprises. This matters when you're targeting embedded systems or performance-critical paths.

Metadata uses MessagePack. You can attach palettes, color masks, titles, authors, tags, DPI, colorspace info, and arbitrary custom key-value pairs. The metadata system is extensible through EXTRA chunks in the file format.

## The Tooling

There's a CLI that handles encode, decode, validate, inspect, export-png, and dump-rgba. You can encode an image with `--pick-encoding` to auto-select between raw and RLE, `--auto-palette` to generate indexed color, and `--dither` for Floyd-Steinberg dithering. The inspect command prints header fields, section sizes, palette info, metadata entries, and warnings.

There's also a web demo at [nellowtcs.me/tBMP](https://nellowtcs.me/tBMP/) built with WebAssembly. Same C core, running in the browser. Load a `.tbmp` file, inspect its structure, visualize the pixels.

## Published

Available on crates.io (`tbmp`) and npm (`@nellowtcs/tbmp`). The C library builds with CMake, produces `libtbmp.a`, and has a full test suite. Apache 2.0 licensed.

This one's probably my most technically dense project. The format design took longer than the code.
