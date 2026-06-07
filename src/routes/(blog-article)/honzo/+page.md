---
    title: "Honzo"
    slug: "honzo"
    coverImage: "/images/posts/honzo.webp"
    excerpt: "so uhhh... i made an ebook format. like a real one"
    date: "2026-06-07T07:46:12.053-06:00"
    hidden: false
    tags:
      - honzo
      - ebook
      - format
      - project
    keywords:
      - Showcase
      - Something I Made
      - Rust
---

so uhhh  
i made an ebook format  
like a real one  
like a whole ecosystem  

it just kind of happened while i was minding my own business and suddenly it was 110 hours later and i had a reader and a converter and a spec and a demo suite and a drm system that i reinvented twice because apparently i enjoy pain

this is the story  
or whatever this is  
idk man i just work here ~ my brain

---

## the beginning where i lie to myself

i started honzo with the classic lie  
the one every engineer tells themselves  
the little whisper that says  
**i’ll just make a tiny prototype**  
and then you blink and you’re knee deep in a binary container format with chunked compression and crc32 and a header that looks like it belongs in a museum

<img src="https://cdn.hackclub.com/019e27b8-693f-72b3-930a-ab926f3a37f9/Screenshot%202026-05-14%2011.07.25%20AM.png" alt="image"/>

i wrote a 52 byte header and thought  
cool i’m done  
and then my brain said  
haha no you’re not  
and dragged me into a three week sprint i did not sign up for

---

## the reader of which i accidentally grew a soul

<img src="https://cdn.hackclub.com/019e9c37-2cf2-7b3d-a784-e5b7b017d00e/Screenshot%202026-06-06%20at%201.50.49%E2%80%AFAM.png" alt="image"/>

the reader was supposed to be a test harness  
like a little thing to see if the format worked  
and then suddenly i was building pagination and themes and manga mode and search and print mapping and a whole layout engine that honestly should not exist but here we are

this was the moment i realized  
oh  
this is not a toy anymore  
this is a creature  
and i am responsible for it now

---

## the tools where i blacked out and rebuilt the ui

<img src="https://cdn.hackclub.com/019e9c3c-11e0-76e4-81f5-2893ddbfd0d9/Screenshot%202026-06-06%20at%203.20.22%E2%80%AFAM.png" alt="image"/>

inspect and convert were originally just html i slapped together at 3am  
they looked like they were built by a sleep deprived gremlin  
which is fair because they were

then one night i blinked and suddenly i was rebuilding the entire ui

- new header  
- new layout  
- new grid system  
- new panels  
- new chunk table  
- new everything  

i basically did a full renovation like i was on some hgtv show for developers

now the demo tools look like they belong in the same universe as the reader  
which is wild because i did not plan any of this  
it just happened  
like a fever dream but with css

---

## the drm saga where i reinvent cryptography twice

this part is my favorite because it is so stupid

i implemented drm once  
cbc plus rsa  
felt proud for like a bit  
then realized i had basically recreated a cryptographic crime scene  
so i ripped it all out and rebuilt it with gcm and x25519 like a normal person

so yes  
i reinvented drm twice  
in one day  
because apparently i enjoy suffering and also because i refuse to ship cursed crypto

honestly iconic behavior

---

## also I

did a lot

<img src="https://cdn.hackclub.com/019ea049-529f-768e-8040-fb1d97157c05/Screenshot%202026-06-06%20at%209.59.45%E2%80%AFPM.png" alt="image"/>

- docs  
- spec  
- kaitai  
- c bindings  
- ts bindings  
- converters  
- book maker gui  
- design system  
- diagrams  
- examples  
- polish  

See the Macondo page lolll: https://macondo.hackclub.com/projects/3584 for my rambles.

and then suddenly  
it was done  
like actually done  
not fake done  
not i’ll finish it later done  
but real done  
the kind where you sit back and go  
oh  
i made a thing

and then i shipped it  
because why not  
chaos is my brand

---

## the moment after where i stare at the wall

after shipping something big there’s this weird quiet  
like the world holds its breath for a second  
and you just sit there thinking  
wow  
i actually did that  
me  
the guy who said this would be a tiny experiment  
lol

honzo exists now  
it’s real  
it’s out there  
and i made it  
in 111.2 hours  
which is honestly unhinged but also kind of cool

---

## what now

no idea  
maybe nothing  
maybe everything  
maybe honzo becomes a footnote  
maybe it becomes a standard  
maybe i use it for something wild later  
who knows  
i’m just vibing

anyway  
that’s the story  
thanks for coming to my accidental ted talk

we're here >:3
