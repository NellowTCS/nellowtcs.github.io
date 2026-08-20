---
title: lexepub
coverImage: /images/projects/lexepub.png
slug: lexepub
date: 2025-08-01
excerpt: A streaming Rust library for parsing ePub files without loading the entire document into memory.
tags: ['Rust', 'Parser', 'Embedded', 'ePub', 'Projects']
repo: https://github.com/NellowTCS/lexepub
cargo: lexepub
docs: http://nellowtcs.me/lexepub/
---

I needed to parse ePub files on embedded hardware with 512KB of RAM. Every existing parser loads the entire ZIP archive into memory first, which is fine on a laptop but absolutely not fine on an ESP32 reading from an SD card. So I built lexepub, a streaming ePub parser in Rust that never loads the whole file.

## Why Streaming Matters

An ePub is really a ZIP archive with specific XML files inside. Traditional parsers unzip everything, hold it in RAM, and then parse the XML. For a 10MB ePub on constrained hardware, that's a non-starter. lexepub reads ZIP entries sequentially using `async_zip`, parses the container XML and OPF manifest on the fly, and hands you content as it's found. Memory usage stays constant regardless of file size.

The `from_reader` API is designed for embedded. Plug in a reader backed by SD card, LittleFS, or flash storage, and you get a fully parsed document without ever holding the whole file.

## More Than You'd Expect

The container parser reads `META-INF/container.xml`. The OPF parser extracts metadata, manifest, and spine. A caching layer stores metadata, AST chapters, text chapters, and word counts so you're not re-parsing on every access. Chapter Stream implements `futures::Stream` for async iteration.

But here's where it gets wild. The CSS parser is 344 lines written from scratch. It handles `@media`, `@supports`, `@font-face`, `@page`, `@import`, `@namespace`, and standard rules. For an ePub library, that's remarkably complete. You can get text-only content cheaply or full AST with CSS styles applied.

## Three Targets

It publishes as a Rust crate on crates.io, an npm package via WASM (wasm-pack plus wasm-bindgen), and builds as C/C++ FFI through Diplomat. Same streaming parser, three different ways to use it.

Check the docs at [nellowtcs.me/lexepub](http://nellowtcs.me/lexepub/). The streaming approach means you can parse an ePub of any size with a fixed memory budget, and honestly that's the whole point.
