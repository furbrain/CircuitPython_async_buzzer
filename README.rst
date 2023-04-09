Introduction
============


.. image:: https://readthedocs.org/projects/circuitpython-async-buzzer/badge/?version=latest
    :target: https://circuitpython-async-buzzer.readthedocs.io/
    :alt: Documentation Status



.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/furbrain/CircuitPython_async_buzzer/workflows/Build%20CI/badge.svg
    :target: https://github.com/furbrain/CircuitPython_async_buzzer/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

Play simple tunes on a piezo buzzer asynchronously


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `CircuitPython asyncio module <https://github.com/adafruit/Adafruit_CircuitPython_asyncio>`_

Installing from PyPI
=====================
On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/circuitpython-async-buzzer/>`_.
To install for current user:

.. code-block:: shell

    pip3 install circuitpython-async-buzzer

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-async-buzzer

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install circuitpython-async-buzzer

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install async_buzzer

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: python

    import asyncio

    import pwmio

    from async_buzzer import Buzzer
    import board

    tune = [
        ("E5",500),
        ("G5",500),
        ("A5",1000),
        ("E5",500),
        ("G5",500),
        ("B5",250),
        ("A5",750),
        ("E5",500),
        ("G5",500),
        ("A5",1000),
        ("G5",500),
        ("E5",1500)
    ]

    pwm = pwmio.PWMOut(board.D10, variable_frequency=True)
    buzzer = Buzzer(pwm)


    async def main():
        buzzer.play(tune, wait=False)
        for i in range(5):
            print(i)
            await asyncio.sleep(1)
        await buzzer.wait()

    asyncio.run(main())

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://circuitpython-async-buzzer.readthedocs.io/>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/furbrain/CircuitPython_async_buzzer/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
