#VT API

Just a python wrapper to VT's api.

I use it a lot, so it's useful.

##Installation

`sudo python3 setup.py install`

##Tests

First, set up an apikey to test with

`nano tests/apikey.py`

apikey.py
```python
APIKEY = "SOME_API_KEY"
```

Then you can run your tests,
`python3 setup.py nosetests`

##Usage

```python
from vt import VT

api = VT("some_api_key")

# Search for samples
samples = api.search("behaviour:8.8.8.8")

# Get a report for a resource
report  = api.report("deadbeef212393281918")
```
