|License| |Release| |Supported versions| |Docs| |Contact| |Blog|

gracefull-shutdown-py
=====================

Helps to support gracefull shutdown for your python application.

Example of usage
----------------
Roman
^^^^^
.. code:: python

    from gracefull_shutdown import ExitSignalHandler

    shutdown = ExitSignalHandler()
    while not shutdown.triggered:
        sleep(1)

.. |Release| image:: https://img.shields.io/github/release/zifter/numeral-system-py.svg
   :target: https://github.com/zifter/numeral-system-py/releases
.. |Supported versions| image:: https://img.shields.io/pypi/pyversions/numeral-system-py.svg
   :target: https://pypi.org/project/numeral-system/
.. |Contact| image:: https://img.shields.io/badge/telegram-write%20me-blue.svg
    :target:  https://t.me/zifter
.. |Blog| image:: https://img.shields.io/badge/site-my%20blog-yellow.svg
    :target:  https://zifter.github.io/
.. |License| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target:  https://opensource.org/licenses/MIT
.. |Docs| image:: https://readthedocs.org/projects/numeral-system-py/badge/?version=latest&style=flat
    :target:  https://numeral-system-py.readthedocs.io/en/latest/

