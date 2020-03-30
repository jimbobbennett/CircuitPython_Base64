Introduction
============

.. image:: https://readthedocs.org/projects/circuitpython-base64/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/base64/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://github.com/jimbobbennett/CircuitPython_base64/workflows/Build%20CI/badge.svg
    :target: https://github.com/jimbobbennett/CircuitPython_base64/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

RFC 3548: Base16, Base32, Base64 Data Encodings


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Adafruit CircuitPython BinAscii <https://github.com/adafruit/Adafruit_CircuitPython_binascii>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/circuitpython-base64/>`_. To install for current user:

.. code-block:: shell

    pip3 install circuitpython-base64

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-base64

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install circuitpython-base64

Usage Example
=============

Base64 encode a byte string.

.. code-block:: python

    encoded = base64.encodebytes(bytes_to_encode)

Decode a base64 encoded string to bytes.

.. code-block:: python

    decoded = base64.decodebytes(string_to_decode)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/jimbobbennett/CircuitPython_base64/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
