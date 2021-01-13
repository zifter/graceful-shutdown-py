|License| |Release| |Supported versions| |Docs| |Contact| |Blog|

gracefull-shutdown-py
=====================

Helps to support gracefull shutdown for your python application.

Example of usage
----------------
Simple
^^^^^^
.. code:: python

    from gracefull_shutdown import ExitSignalHandler

    shutdown = ExitSignalHandler()
    while not shutdown.triggered:
        sleep(1)

.. |Release| image:: https://img.shields.io/github/release/zifter/gracefull-shutdown-py.svg
   :target: https://github.com/zifter/gracefull-shutdown-py/releases
.. |Supported versions| image:: https://img.shields.io/pypi/pyversions/gracefull-shutdown-py.svg
   :target: https://pypi.org/project/gracefull-shutdown-py/
.. |Contact| image:: https://img.shields.io/badge/telegram-write%20me-blue.svg
    :target:  https://t.me/zifter
.. |Blog| image:: https://img.shields.io/badge/site-my%20blog-yellow.svg
    :target:  https://zifter.github.io/
.. |License| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target:  https://opensource.org/licenses/MIT
.. |Docs| image:: https://readthedocs.org/projects/gracefull-shutdown-py/badge/?version=latest&style=flat
    :target:  https://gracefull-shutdown-py.readthedocs.io/en/latest/

