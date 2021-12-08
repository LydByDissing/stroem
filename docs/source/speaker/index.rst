*************
Speaker Parts
*************

Each speaker part have its own unique ID to make it easier to identify the correct part. Externally sourced parts will likely also have a SKU or similar.

Parts
=====

.. toctree::
   :maxdepth: 1
   :glob:

   parts/*


Generate a parts ID
===================

To generate a ID for a part, follow the below example. The following tool is used: `Short UUID <https://github.com/simplyhexagonal/short-unique-id>`_.

.. code-block:: bash

 suid -l 6 -d uuid-dict.json

Please note that a simplyfied `dictionary <https://raw.githubusercontent.com/LydByDissing/stroem/main/uuid-dict.json>`_ have been used to ensure only uppercase characters are used.
