Documentation
===================

These instructions assume you are using the latest version of Ubuntu. These instructions may not produce the desired result with other distributions.

This page documents how to build this documentation. This documentation was creating using `Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_ and `reStructuredText <https://en.wikipedia.org/wiki/ReStructuredText>`_.

Linux
--------------------

Both the documentation and program is hosted on Github. It is necessary to install git to be able to download the documentation. To install git:

``sudo apt install git``

You may be prompted for your user’s password.

To download the documentation and program:

``git clone https://github.com/alex634/EECS581-Project.git``

Finally, install the Sphinx documentation building tools and program dependencies:

``sudo apt install sphinx-{common,rtd-theme-common}``

``sudo apt install python3-{tabulate,pygame}``


Building
^^^^^^^^^^^^^^^^^^^^^

If not in the documentation directory, enter it:

``cd EECS581-Project/Documentation``

Then build:

``make html``

The resulting HTML will be put in the ``EECS581-Project/Documentation/build`` directory.
