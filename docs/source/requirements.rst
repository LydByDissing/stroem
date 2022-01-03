Requirements
############
The main goal of the *Strøm* open source speaker project are to create a fully functional and open source "wifi speaker".

The Speaker concept
===================
The primary features of the *Strøm* speaker are:

* Minimalistic design language
* Playback via Spotify Connect and Bluetooth
* Wall mountable
* Sustainable materials
* Open Source

Making it a modern, minimalistic and fully capable speaker.

Design Goals
============
The following parameters are used as design goals. These are not *hard* requirements, but reflects the ideal characteristics of the final speaker.

Sustainability
**************
It is important to use materials that are produced and sourced using sustainable methods, as well as using sustainable productions methods of the speaker itself.
A non exhaustive lists of considerations:

* The cabinet must primarily be made out of wood

  * like MDF and plywood
* No plastic
* Built to be repairable

Making a 100% sustainable active speaker is, however, not 100% realistic as there isn't any fully sustainable PCB's. At least not readable available.

Cabinet
*******
The design of the cabinet must reflect a minimalistic design approach. This means a small physical form factor and a minimalist visual appearance.
A non exhaustive lists of considerations:

* Small form factor
* Shallow cabinet for better on-wall placement
* Ultra mat finish of the cabinet
* Cloth covered drivers

Acoustics
*********
With this project it is not the goal to create another `boombox <https://en.wikipedia.org/wiki/Boombox>`_, with over attenuated lows (bass) and highs (treble) as this will quickly result in listening fatigue. This is also called a `smiley face curve <https://en.wikipedia.org/wiki/Smiley_face_curve>`_.

However a slight bass boost at lower SPL levels to accommodate for the non-linear human hearing will make the speaker sound natural a lower sound pressure levels (SPL). This boost should be less pronounced at higher SPL levels; the dynamic part of this requirement can become hard to realize, but it will make for a much more appealing listening proposition.
A non exhaustive lists of further considerations:

* Max SPL of 100dB
* Frequency range: 80Hz - 17kHz; ±3dB
* Reasonable flat response; within ±4dB
* High speech intelligibility
* SPL dependent bass boost to match the nonlinearity of the human hearing

Drivers
=======
In order to fulfill the requirements of a small form factor speaker, shallow drivers are needed. This makes it possible to minimize the overall depth of the cabinet.

Only a few really larger shallow drivers exists, which also tends to be rather expensive. They usually deliver good performance, but most of them are considered to be too expensive for this project.
In stead of using one large driver, 4 miniature full range transducers are targeted instead. This makes it possible to decrease the overall depth of the cabinet.

The following drivers are used:

* 2.5" full range driver: :ref:`SB65WBAC25-4 <full-range-driver>`.
