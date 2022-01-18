.. toctree::
   :maxdepth: 3

===========
API service
===========

The dissolution camera services expose a RESTful API to provide remote interactivity
with multiple cameras from a single service API. The API service is containerized and
orchestrated with an additional database container (to hold file information), and
a web GIU.

RESTful API
===========
Below defines the endpoints of the dissolution system API.

API module
----------

.. automodule:: api
   :members:
   :private-members:
   :special-members:

   .. autodecorator:: app

``api.py``
^^^^^^^^^^

Dissocam module
---------------

.. automodule:: dissocam
   :members:
   :private-members:
   :special-members: __init__
   
``dissocam.py``
^^^^^^^^^^^^^^^

---------------

.. automodule:: helper_functions
   :members:
   :private-members:
   :special-members:

``helper_functions.py``
^^^^^^^^^^^^^^^^^^^^^^^
