#!/usr/bin/env python3

from vt import VT
from apikey import APIKEY

def test_search_by_behaviour():
    test_search_terms = "behaviour:8.8.8.8"
    
    api = VT(APIKEY)

    result = api.search(test_search_terms)

    assert("Found samples" in result["verbose_msg"])

def test_search_by_tag():
    test_search_terms = "tag:peexe"

    api = VT(APIKEY)

    result = api.search(test_search_terms)

    assert("Found samples" in result["verbose_msg"])
