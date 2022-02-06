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

Below each of the technical design goals are unwrapped to explain what they mean and how the voicing process is used to implemented these requirements.

High maximum SPL
________________
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
__________________

It should be pleasent to listen to this speaker and at the same time you should be able to get an "audio experience". So no smiley curve frequency response, nor overly exaggerated lows; i.e. this is not a boom box. We are looking to implement a hi-fi speaker with fairly linear frequency response.

A requirement of a linearity within ±4dB isn't perfect, but it is a pretty decent middle ground.

The better the low range extension a speaker can achieve, the more of the audio frequency range it is capable of reproducing and the more "convincing" this speaker will sound.

As small drivers are used, subwoofer levels of extension are hard to come by, so a compromise is needed. By setting the -3dB point at 80Hz or lower, this speaker will not be a bass monster, but the bass it will reproduce will be crips and undistorted.

When placed on a wall even lower frequency extension will be possible.

Speech intelligibility
______________________



Measuring the speaker
---------------------

Here's an example of an eq'ed speaker.

.. chart:: guides/frequency-response.json

    Measured frequency response of an initial test cabinet. Primarily used for validation of the internal cabinet volume.


Adjusting the response
----------------------


camilla DSP
