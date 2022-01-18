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

Classes and modules
-------------------

.. automodule:: api
   :members:
   :private-members:
   :special-members: __init__

.. autodecorator::

.. automodule:: dissocam
   :members:
   :private-members:
   :special-members: __init__
..
    Source code
    ------------

    .. literalinclude:: ../../pythonScripts/api.py
       :language: python

..
    Dissolution system library
    ==========================

    Python source codes and dependencies
    ------------------------------------
    This section includes all the source codes written in python language and their dependencies.

    ``api.py``
    ^^^^^^^^^^

    .. literalinclude:: ../../pythonScripts/api.py
       :language: python

    ``dissocam.py``
    ^^^^^^^^^^^^^^^

    .. literalinclude:: ../../pythonScripts/dissocam.py
       :language: python

    ``helper_functions.py``
    ^^^^^^^^^^^^^^^^^^^^^^^

    .. literalinclude:: ../../pythonScripts/helper_functions.py
       :language: python

