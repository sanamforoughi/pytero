# Pytero
Pytero is a paper-thin API wrapper for interacting with the Natero REST API in
Python, built on and modeled after [Requests: HTTP for Humans™](https://github.com/psf/requests).

## Examples
```python
from pytero import NateroClient

MY_API_KEY = "foobar"
natero = NateroClient(MY_API_KEY, region="us")

my_accounts = natero.accounts(include=["my_custom_metric_1", "my_custom_metric_2"])
```

