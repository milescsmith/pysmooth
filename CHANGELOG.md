# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0]

## Changed

- Altered the maximum allowed Python version so that newer versions of 3.10.* are not excluded


## [1.1.4]

### Changed

- Miscellaneous fixes for mypy and passing tests
- Add `smooth` to `__all__` for explicit export of the symbol

### Removed

- Custom `Numeric` type for type hinting in lieu of following PEP 484 and the
    Numeric Tower


## [1.1.3]

### Changed

- Renamed `smooth` submodule so that it does not conflict with the `smooth()`
    function.
- Updated README.rst to include requirements and example usage


## [1.1.2]

Version bump for pypi


## [1.1.1]

### Changed

- Decreased required vesions of numpy to 1.20.3 so that it does not conflict with
    numba


## [1.1.0]

### Added

- Added unit test to `sm_3` for a 2-element list

### Changed

- Removed click, typer, and rich requirements
- Moved hypothesis and nox-poetry to dev requirements

### Removed

- `main` function, as it was unused and `pysmooth` is not intended to be a cli
    application

[1.3.0]: https://github.com/olivierlacan/keep-a-changelog/compare/1.2.0...1.3.0
[1.2.0]: https://github.com/olivierlacan/keep-a-changelog/compare/1.1.3...1.2.0
[1.1.3]: https://github.com/olivierlacan/keep-a-changelog/compare/1.1.2...1.1.3
[1.1.2]: https://github.com/olivierlacan/keep-a-changelog/compare/1.1.1...1.1.2
[1.1.1]: https://github.com/olivierlacan/keep-a-changelog/compare/1.1.0...1.1.1
[1.1.0]: https://github.com/olivierlacan/keep-a-changelog/compare/1.0.1...1.1.0
[1.0.1]: https://github.com/olivierlacan/keep-a-changelog/releases/tag/1.0.1
