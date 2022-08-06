# STRØM
**An Open Wifi Speaker**

The _Strøm_ open source speaker project have been started with the main goal of creating a fully functional "wifi speaker", but as an open sourced product.

## License
This project and all it's work are licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/) license.

![BY SA License!](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg "The license")
[![Documentation Status](https://readthedocs.org/projects/stroem/badge/?version=latest)](https://stroem.readthedocs.io/en/latest/?badge=latest)

## Getting started

### Checking out the repository
As this project uses the git `submodule` feature to fetch all the needed source files, one would need to have this in mind when performing the checkout.

To checkout everything - including all submodules - the following snippet are handy:
```
git clone --recurse-submodules -j$(nproc) https://github.com/LydByDissing/stroem.git
```

## Project description and Design Goals
As mentioned above, this project aims at designing a **wifi speaker**, capable of streaming audio using **Bluetooth** and **Spotify Connect**.

The primary design goals of the _Strøm_ speaker are:

* Minimalistic design language
* Playback via Spotify Connect and Bluetooth
* Wall mountable
* Sustainable materials
* Open Source

Making it a modern, minimalistic and fully capable speaker. Further requirement details can be found in the [requirements document](https://stroem.readthedocs.io/en/latest/requirements.html).

Besides making a modern and capable wifi speaker we are also aiming at validating the concept of "local manufactoring" - how we exactly are going to succeed with this are still an unanswered questions; see [issue #5](https://wikifactory.com/+opennext/lydbydissing/issues/local-production-but-how) for further discussions on the matter.

## Open Next Demonstrator
This project takes part in Open Next 2022 as a demonstrator project - one of twelve to be exact.
Most Strøm and Open Next communication will happen over at [this](https://wikifactory.com/@sidsel/osd-platform-for-maker) page.

## Project Documentation

The main project documentation and any permanent documentation are written in the `reStructuredText` (`.rst`) format, using the [Sphinx documentation framework](https://www.sphinx-doc.org/en/master/).

The code resides in the Strøm GitHub repo ([LydByDissing/stroem](https://github.com/LydByDissing/stroem)) and the compiled documentation are available over at Read The Docs: [stroem.readthedocs.io](https://stroem.readthedocs.io/).

## Contributions and collaboration
We love contributions! And all forms of contributions and collaborations are welcome.

The development of the speaker and most of the involved parts are tracked here at [LydByDissing/stroem](hhttps://github.com/LydByDissing/stroem).
The main documentation of the project, the parts and the assembly process and any permanent documentation are documented using the Sphinx documentation framework as mentioned above.

### Want to participate, but not sure where to start?
Take a look at one of the open [issues](https://github.com/LydByDissing/stroem/issues) already created and chip in with your knowledge and experience. Sometimes all it takes is a single comment, to push a someone else in the right direction; so don't hold yourself back.

Or read our [contributing guidelines](https://github.com/LydByDissing/stroem/blob/main/CONTRIBUTING.md) for further details on how to be involved.
