|License| |Release| |Supported versions| |Docs| |Contact| |Blog|

graceful-shutdown-py
=====================

Helps to support graceful shutdown for your python application.

Example of usage
----------------
Simple
^^^^^^
.. code:: python

    from graceful_shutdown import ExitSignalHandler

    shutdown = ExitSignalHandler()
    while not shutdown.triggered:
        sleep(1)

.. |Release| image:: https://img.shields.io/github/release/zifter/graceful-shutdown-py.svg
   :target: https://github.com/zifter/graceful-shutdown-py/releases
.. |Supported versions| image:: https://img.shields.io/pypi/pyversions/graceful-shutdown-py.svg
   :target: https://pypi.org/project/graceful-shutdown-py/
.. |Contact| image:: https://img.shields.io/badge/telegram-write%20me-blue.svg
    :target:  https://t.me/zifter
.. |Blog| image:: https://img.shields.io/badge/site-my%20blog-yellow.svg
    :target:  https://zifter.github.io/
.. |License| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target:  https://opensource.org/licenses/MIT
.. |Docs| image:: https://readthedocs.org/projects/graceful-shutdown-py/badge/?version=latest&style=flat
    :target:  https://graceful-shutdown-py.readthedocs.io/en/latest/

