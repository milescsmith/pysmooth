import os
import shutil
import sys
from pathlib import Path

import nox

PACKAGE = "pysmooth"
PYTHON_VERSIONS = ["3.10", "3.11"]
os.environ["PDM_IGNORE_SAVED_PYTHON"] = "1"
os.environ["PDM_IGNORE_ACTIVE_VENV"] = "0"
nox.needs_version = ">=2024.4.15"
nox.options.sessions = (
    "mypy",
    "tests",
)

locations = (
    "src",
    "tests",
)

@nox.session
def lint(session: nox.Session) -> None:
    """Lint using ruff."""
    args = session.posargs or locations
    session.install("ruff")
    session.run("ruff", *args)


@nox.session(python="3.10")
def mypy(session: nox.Session) -> None:
    """Type-check using mypy."""
    session.run_always("pdm", "install", "--no-self", "--no-default", "--dev", external=True)
    session.run(
        "mypy",
        "--install-types",
        "--non-interactive",
        f"--python-executable={sys.executable}",
        "noxfile.py",
        external=True,
    )


@nox.session(python=PYTHON_VERSIONS)
def lockfile(session: nox.Session) -> None:
    """Run the test suite."""
    session.run_always("pdm", "lock", external=True)


@nox.session(python=PYTHON_VERSIONS)
def tests(session: nox.Session) -> None:
    """Run the test suite."""
    session.run_always("pdm", "install", "--fail-fast", "--frozen-lockfile", "--dev", external=True)
    session.run(
        "coverage", "run", "--parallel", "-m", "pytest", "--numprocesses", "auto", "--random-order", external=True
    )


@nox.session(python=PYTHON_VERSIONS)
def coverage(session: nox.Session) -> None:
    """Produce the coverage report."""
    args = session.posargs or ["report"]
    session.install("coverage[toml]", "codecov", external=True)

    if not session.posargs and any(Path().glob(".coverage.*")):
        session.run("coverage", "combine")

    session.run("coverage", "json", "--fail-under=0")
    session.run("codecov", *args)


@nox.session(python=PYTHON_VERSIONS)
def docs(session: nox.Session) -> None:
    """Build and serve the documentation with live reloading on file changes."""
    args = session.posargs or ["--open-browser", "docs", "docs/_build"]
    session.install(".")
    session.install("sphinx", "sphinx-autobuild", "sphinx-click", "sphinx-rtd-theme")

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    session.run("sphinx-autobuild", *args)


@nox.session(name="docs-build", python=PYTHON_VERSIONS)
def docs_build(session: nox.Session) -> None:
    """Build the documentation."""
    args = session.posargs or ["docs", "docs/_build"]
    session.install(".")
    session.install("sphinx", "sphinx-click", "sphinx-rtd-theme")

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    session.run("sphinx-build", *args)

@nox.session(python=PYTHON_VERSIONS)
def typeguard(session: nox.Session) -> None:
    """Runtime type checking using Typeguard."""
    session.install(".")
    session.install("pytest", "typeguard", "pygments", "hypothesis")
    session.run("pytest", f"--typeguard-packages={PACKAGE}", *session.posargs)
