.. _Requirements:

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

.. acoustic-requirements-start

* Max SPL of 100dB
* Frequency range: 80Hz - 17kHz; ±3dB
* Reasonable flat response; within ±4dB
* High speech intelligibility
* SPL dependent bass boost to match the nonlinearity of the human hearing

.. acoustic-requirements-end

Below each of the technical design goals are unwrapped to explain what they mean and how the voicing process is used to implemented these requirements.

High maximum SPL
----------------
:abbr:`SPL (Sound Pressure Level)` is a measure of "how loud" a sound is. And the maximum SPL of a speaker tells something about how loud a speaker is capable of playing.

Usually the SPL is measured at a distance of one meter [m]. The unit of SPL is decibel [dB].

The Strøm speaker isn't a large speaker, but it should still be a capable speaker. A speaker that is capable of "playing loud". But as this can be hard to quantify as the perception of "loud" various a great deal from person to person. It is also highly affected by the distance between the speaker and the listener as well as it's placement in the room.
And finally this perception is impacted by any audible distortion from the speaker. The higher the distortion, the higher the SPL is perceived.

So instead of stating that the speaker must play "loud", a quantifiable number is needed.

We also want to add a few more limitations to this design goal. The maximum SPL should:

* be reachable "anywhere" on the frequency band,

* without reaching the mechanical limits of the driver,

* and should avoid clipping

We have settle on **100dB of maximum SPL** for this small speaker. This will be more than sufficient for must small and medium sized rooms.
The implementation of this requirement will affect (limit) the frequency response of the speaker. Most drivers can play down to 20Hz, but maybe not a great volume. So by limitting the frequency band we can push the drivers to higher SPL levels.

Frequency response
------------------

It should be pleasent to listen to this speaker and at the same time you should be able to get an "audio experience". So no smiley curve frequency response, nor overly exaggerated lows; i.e. this is not a boom box. We are looking to implement a hi-fi speaker with fairly linear frequency response.

A requirement of a linearity within ±4dB isn't perfect, but it is a pretty decent middle ground.

The better the low range extension a speaker can achieve, the more of the audio frequency range it is capable of reproducing and the more "convincing" this speaker will sound.

As small drivers are used, subwoofer levels of extension are hard to come by, so a compromise is needed. By setting the targeted -3dB point at 80Hz, this speaker will not be a bass monster, but the bass it will reproduce will be crips and undistorted.

When placed on a wall even lower frequency extension will be possible at the same (or higher) SPL.

Drivers
=======
In order to fulfill the requirements of a small form factor speaker, shallow drivers are needed. This makes it possible to minimize the overall depth of the cabinet.

Only a few really larger shallow drivers exists, which also tends to be rather expensive. They usually deliver good performance, but most of them are considered to be too expensive for this project.
In stead of using one large driver, 4 miniature full range transducers are targeted instead. This makes it possible to decrease the overall depth of the cabinet.

The following drivers are used:

* 2.5" full range driver: :ref:`SB65WBAC25-4 <full-range-driver>`.
