# DBnomics Python client

Access DBnomics time series from Python.

This project relies on [Python Pandas](https://pandas.pydata.org/).

## Tutorial

A tutorial is available as a [Jupyter notebook](./index.ipynb).

### Use with a proxy

This Python package uses [requests](https://requests.readthedocs.io/), which is able to work with a proxy (HTTP/HTTPS, SOCKS). For more information, please check [its documentation](https://requests.readthedocs.io/en/master/user/advanced/#proxies).

## Install

```bash
pip install dbnomics
```

See also: https://pypi.org/project/DBnomics/

## Development

To work on dbnomics-python-client source code:

```bash
git clone https://git.nomics.world/dbnomics/dbnomics-python-client.git
cd dbnomics-python-client
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -e .
```

If you plan to use a local Web API, running on the port 5000, you'll need to use the `api_base_url` parameter of the `fetch_*` functions, like this:

```python
dataframe = fetch_series(
    api_base_url='http://localhost:5000',
    provider_code='AMECO',
    dataset_code='ZUTN',
)
```

Or globally change the default API URL used by the `dbnomics` module, like this:

```python
import dbnomics
dbnomics.default_api_base_url = "http://localhost:5000"
```

### Open the demo notebook

Install jupyter if not already done, in a virtualenv:

```bash
pip install jupyter
jupyter notebook index.ipynb
```

## Tests

Run tests:

```bash
# Only once
pip install -r requirements.txt
pip install -r requirements-test.txt
pip install -e .

pytest

# Specify an alterate API URL
API_URL=http://localhost:5000 pytest
```

## Release

To release a version on PyPI:

- merge one or many feature branches into master (no need to do a release for every feature...)
- update `setup.py` incrementing the package version (we use Semantic Versioning so determine if it's a major, minor or patch increment)
- ensure the changelog is up to date
- `git commit setup.py CHANGELOG.md -m "Release"`
- create a Git tag with a `v` before version number and push it (`git tag v1.2.0; git push; git push --tags`)
- the [CI](./.gitlab-ci.yml) will run a job to publish the package on PyPI at https://pypi.org/project/DBnomics/

It's advised to do `pip install -e .` to let your virtualenv know about the new version number.
