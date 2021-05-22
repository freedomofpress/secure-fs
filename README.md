> By contributing to this project, you agree to abide by our [Code of Conduct](https://github.com/freedomofpress/.github/blob/main/CODE_OF_CONDUCT.md).

# secure-fs

[![CircleCI branch](https://img.shields.io/circleci/project/github/freedomofpress/secure-fs/main.svg)](https://circleci.com/gh/freedomofpress/workflows/secure-fs/tree/main)

An open-source library that ensures restrictive file permissions and safe paths when creating and working with files and directories.

The development of secure-fs is primarily motivated by the creation of the [SecureDrop Workstation](https://github.com/freedomofpress/securedrop-workstation) based on Qubes OS. It is used by the SecureDrop Workstation components: [SecureDrop Client](https://github.com/freedomofpress/securedrop-client) and [securedrop-export](https://github.com/freedomofpress/securedrop-export).

# Quick Start

To run tests, semgrep, bandit, safety, mypy, and all other linters:
```
make venv
source .venv/bin/activate
make check
```

To use this library in your project's `virtualenv` for testing purposes:
```
pip uninstall secure-fs
pip install git+https://github.com/freedomofpress/secure-fs@main#egg=secure-fs
```

# Update dependencies

To update dev dependencies:
```
make update-pip-dependencies
```

# Making a release

To make a release, you should:

1. Create a branch named `release/$new_version_number`
2. Update `CHANGELOG.md` and `setup.py`
3. Commit the changes.
4. Create a PR and get the PR reviewed and merged into ``main``.
5. ``git tag $new_version_number`` and push the new tag.
6. Checkout the new tag locally.
7. Delete the wheel from your `dist/` directory to make sure it's not uploaded in the next step.
8. Push the new release source tarball to the PSF's PyPI [following this documentation](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives).
9. If you want to publish a new release to the FPF PyPI mirror, Hop over to the the `securedrop-debian-packaging` repo and follow the [build-a-package](https://github.com/freedomofpress/securedrop-debian-packaging/blob/HEAD/README.md#build-a-package) instructions to push the package up to our PyPI mirror: https://pypi.org/simple
