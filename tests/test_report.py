#!/usr/bin/env python3

from vt import VT
from apikey import APIKEY

def test_search_by_hash():
    test_hash = "001221d6393007ca918bfb25abbb0497981f8e044e377377d51d82867783a746"
    
    api = VT(APIKEY)

    result = api.report(test_hash)

    assert(result["response_code"] == 1)

