.. _installing:

==========
Installing
==========

``emsarray`` can be installed using ``pip``.

.. code-block:: python

   $ pip install emsarray

Before installing ``emsarray`` via ``pip``
you have to ensure that the :ref:`non-Python dependencies are met <dependencies>`.
There are some optional dependencies for ``emsarray``.
You can install these by :ref:`choosing some extras at install time <extras>`.

.. _dependencies:

Dependencies
============

``emsarray`` depends on
`shapely <https://shapely.readthedocs.io/en/stable/project.html#installing-shapely>`_ and
`cartopy <https://scitools.org.uk/cartopy/docs/latest/installing.html>`_.
These use the non-Python dependencies ``geos`` and ``proj`` respectively.

These can be installed via your package manager or via ``conda``.
Installing from ``conda`` is the recommended approach
as these packages are often more up-to-date than the system packages
and it guarantees that compatible versions of ``geos`` and ``proj`` are installed:

.. code-block:: shell-session

   $ conda create -n my-env
   $ conda activate my-env
   $ conda install proj geos

If ``geos`` and ``proj`` are installed using your system package manager,
and ``shapely`` and ``cartopy`` are installed via pip,
you must ensure that you install versions of ``shapely`` and ``cartopy``
that are compatible with these system libraries.
``pip`` will not check for these version constraints for you.
A version mismatch between the Python and non-Python libraries
can lead to the installation failing,
or Python crashing when calling ``shapely`` or ``cartopy`` functions.

Building
========

On any computer, run the following commands to build a package:

.. code-block:: shell-session

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip3 install --upgrade pip build
    $ rm -rf dist/
    $ python3 -m build

Two new files will be created in the ``dist/`` directory.
This is the Python package you can install in other environments.
Use either one of them when installing ``emsarray`` in your chosen environment:

.. code-block:: shell-session

    $ cd /path/to/other-project
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip3 install /path/to/emsarray/dist/emsarray-*-py3-none-any.whl

.. _extras:

Extras
======

When installed via ``pip``, ``emsarray`` can be installed with "extras".
These extra packages are optional.

``plot``
--------

.. code-block:: shell

   $ pip install emsarray[plot]

Allows ``emsarray`` to produce plots, using :meth:`.Format.plot`.

``tutorial``
------------

.. code-block:: shell

   $ pip install emsarray[tutorial]

Installs packages required to access the tutorial datasets,
accessible via the :func:`emsarray.tutorial.open_dataset` method.

``complete``
------------

.. code-block:: shell

   $ pip install emsarray[complete]

Includes all extras.
Use this for the complete ``emsarray`` experience.

``testing``
-----------

The ``testing`` extras are intended for development.
When setting up a development environment for ``emsarray``,
clone the repository and install ``emsarray`` in editable mode
with the ``testing`` extras:

.. code-block:: shell

   $ pip install -e .[testing]
   $ pytest  # Run the test suite
   $ make -C docs html  # Build the docs
