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
We will use ``REW`` to perform the following measurements:
* frequency response
* phase response
* impulse response

Frequency and phase response
____________________________

We do not have easy access to an anechoic chamber, but that doesn't mean that we can't produce some useful results. And for this speaker we actively rely on the walls and boundaries to increase our bass response. So a measurement "in place" isn't actually that bad.

We have placed the microphone within 10cm from the baffle to limit the impact of reflections.

Here's the speaker measured before voicing. A single 8th order high pass (HP) filter have been added at 45Hz to protect the driver (from exceeding :math:`X_{max}`).

The frequency and phase response are depicted. It is worth noting that the results haven't been normalize, resulting in that the measured dB can't be related to anything (other than other measurements using the same setup).

.. chart:: guides/80hz-target-no-filter-frequency-response.json

    Measured frequency response of an initial test cabinet. Primarily used for validation of the internal cabinet volume.


Adjusting the response
----------------------

As a developement workflow I am using the great `HEnquist/camilladsp <https://github.com/HEnquist/camilladsp>`_ project. This makes it possible to specify the filter banks as a simple YAML config file. For the initial 80Hz target tuning this file have been used: `voicing/voicing-80hz-target.yaml <https://github.com/LydByDissing/stroem/tree/main/voicing>`_.

As we can't make the bass higher – without additional :math:`X_{max}` of the driver - we need to lower the rest of the frequency response. This will lower the overall efficiency of the speaker, but result in a much more linear frequency response. See the below graph for a measurement of the inital filters applied to the signal chain.

.. chart:: guides/80hz-target-initial-filters-frequency-response.json

    Measurement result when initial filtering have been applied.

The result isn't perfect but a really good starting point (and a good sounding one of that) which proves that these little drivers are pretty capable in this little cabinet.
