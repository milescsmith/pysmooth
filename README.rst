Pysmooth
==========

A Python implementation of R's stats::smooth() Tukey's (running median) smoother

|PyPI| |Status| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit| |Black|

|Repobeats analytics image|

.. |PyPI| image:: https://img.shields.io/pypi/v/pysmooth.svg
   :target: https://pypi.org/project/pysmooth/
   :alt: PyPI
.. |Status| image:: https://img.shields.io/pypi/status/pysmooth.svg
   :target: https://pypi.org/project/pysmooth/
   :alt: Status
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/pysmooth
   :target: https://pypi.org/project/pysmooth
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/pysmooth
   :target: https://opensource.org/licenses/GPL-3.0
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/pysmooth/latest.svg?label=Read%20the%20Docs
   :target: https://pysmooth.readthedocs.io/
   :alt: Read the documentation at https://pysmooth.readthedocs.io/
.. |Tests| image:: https://github.com/milescsmith/pysmooth/workflows/Tests/badge.svg
   :target: https://github.com/milescsmith/pysmooth/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/milescsmith/pysmooth/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/milescsmith/pysmooth
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black
.. |Repobeats analytics image| image:: https://repobeats.axiom.co/api/embed/6870249c18b93b2fcc0d967ec9f7308d74ca42cc.svg
   :target: https://repobeats.axiom.co
   :alt: Repobeats analytics image

Features
--------

* TODO
  - Replace C/R-style coding with more Pythonic methods


Requirements
------------

* Python 3.8, 3.9, or 3.10
* Numpy 1.20


Installation
------------

You can install *pysmooth* via pip_ from PyPI_:

.. code:: console

   $ pip install pysmooth


Usage
-----

Pysmooth is intended to be used within another module.

.. code:: console

   from pysmooth import smooth

   smooth(x=arr, kind="3RS3R", twiceit=False, endrule="Tukey")


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the `GPL 3.0 license`_,
*Pysmooth* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

This project was generated from `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.

.. _@cjolowicz: https://github.com/cjolowicz
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _GPL 3.0 license: https://opensource.org/licenses/GPL-3.0
.. _PyPI: https://pypi.org/
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _file an issue: https://github.com/milescsmith/pysmooth/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
.. _Usage: https://pysmooth.readthedocs.io/en/latest/usage.html
