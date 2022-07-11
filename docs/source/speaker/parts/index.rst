Speaker parts
#############

.. toctree::
   :maxdepth: 1
   :glob:

   *

Generate a parts ID when adding a new part
==========================================

To generate a ID for a part, follow the below example. The following tool is used: `Short UUID <https://github.com/simplyhexagonal/short-unique-id>`_.

.. code-block:: bash

  suid -l 6 -d utils/uuid-dict.json

Please note that a simplified `dictionary <https://raw.githubusercontent.com/LydByDissing/stroem/main/utils/uuid-dict.json>`_ have been used to ensure only uppercase characters are used.
