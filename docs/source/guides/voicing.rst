Voicing of the *Strøm* speaker
##############################

.. note::
  One important aspect of developing a speaker are to tune the frequency response, as well as to ensure that the drivers isn't driven over their capabilities.
  It is here the sound of the speaker is developed.

  This process is called **voicing**.

The voicing of a speaker consists of several steps and this *howto* will try to outline a few of them. The following topics will be covered below:

* Voicing goals
* Measurements
* Adjusting the response

Voicing goals
-------------

With the Strøm speaker several design goals have been defined (see more in the :ref:`Requirements` section) and those related to sound reproduction should – where applicable – be implemented through the voicing process.

The following acoustic design goals have been set for the speaker:

.. include:: ../requirements.rst
  :start-after: acoustic-requirements-start
  :end-before: acoustic-requirements-end

Most of these design goals can be asserted using various measurement techniques.

Measuring the speaker
---------------------

What you need to measure the speaker:

* A measurement microphone like the `UMIK-1 <https://www.minidsp.com/products/acoustic-measurement/umik-1>`_ (or similar)
* Assembled cabinet with drivers
* External amplifier
* Laptop (or similar) with `Camilla DSP <https://github.com/HEnquist/camilladsp>`_ installed.
* Room EQ Wizard (`REW <https://www.roomeqwizard.com>`_)

In order to measure the speaker, make sure that you can *"answer yes"* to all of the above bullets.

What do we want to measure?
___________________________

With ``REW`` it is possible to measure a large suite of things, but bare in mind, that this program is initial created to measure rooms and not speakers.
We will use REW to perform the following measurements:
* frequency response
* phase response
* impulse response

Frequency and phase response
____________________________
Here's an example of an eq'ed speaker. The frequency and phase response are depicted.

.. chart:: guides/frequency-response.json

    Measured frequency response of an initial test cabinet. Primarily used for validation of the internal cabinet volume.


Adjusting the response
----------------------


camilla DSP
