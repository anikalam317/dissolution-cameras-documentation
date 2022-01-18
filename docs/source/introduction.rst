.. toctree::

Introduction
============

The dissolution camera system employs a set of `smart cameras 
<http://xeon/presentation/smart-camera>`_. that provide timelapse videos of
dissolution experiments. The cameras are wirelessly interconnected to a server
that synchronizes the operation (e.g. image resolution, capture frequency,
start time, end time, meta data saved with picture, ...etc) of multiple cameras
from a single web interface that can be accessed anywhere on the Pfizer
network. Each camera is assigned a unique identification allowing cameras to
added, removed, or substituted.  Moreover, a small camera-to-network module
allows the cameras to communicate with other equipment on the Pfizer network,
such that the camera's operation can be started/stopped based on signals from
external equipment. Lastly, the cameras can be fitted with a number of
different lens systems, providing various levels of magnifiation, field of
vision, and wavelength detection range.

.. figure:: _static/Fig1.png
   :width: 300px
   :alt: This is a test image
   :class: with-shadow
   :name: Fig1
   :align: center

   Caption for Sphinx documentation logo (remember to keep it indented as the figure itself in the rst-file).

You can write more stuff starting here (without indentation).

.. csv-table:: This is an example of attached csv data file.
   :file: _files/Table_1.csv
   :name: Table1
   :header-rows: 1
   :delim: ;

Below I'm adding more examples of other cool thinks that can be done in Sphinx :ref:`[1]<1>` :

#. This is a numbered item citing a reference [#f1]_ to the footnote below.

* This is a bulleted list citing the figure above :numref:`Fig1`. 
* The same can be done to cite tables :numref:`Table1`.

This is a reference to an acronym: :term:`API` 

For more features not covered within this template, refer to the `Sphinx documentation <https://www.sphinx-doc.org/en/master/>`_.


.. rubric:: Footnotes

.. [#f1] This is a footnote example.
