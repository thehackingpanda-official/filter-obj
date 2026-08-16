# filter-obj

Filter object (dict) keys and values with a simple predicate.

## Install

```bash
pip install filter-obj
```

## Usage

```python
from filter_obj import filter_obj

filter_obj({"a": 1, "b": 2, "c": 3}, lambda k, v: v > 1)
# {'b': 2, 'c': 3}
```

## Publishing

This project publishes to [PyPI](https://pypi.org/project/filter-obj/) via a
[trusted publisher](https://docs.pypi.org/trusted-publishers/) (OpenID Connect),
so no API tokens are stored in the repo. The `.github/workflows/test.yaml`
workflow runs the tests, builds the distribution, and publishes to PyPI from the
`pypi` environment whenever a GitHub Release is published.

To cut a release: create a release/tag on GitHub — the workflow does the rest.

## License

MIT
