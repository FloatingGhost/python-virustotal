#!/usr/bin/env python3

import requests

class RateLimit(Exception):
    pass

class ServerError(Exception):
    pass

class VT:
    """
        A class to interact with the virustotal API
        :param apikey: Your API Key
    """
    def __init__(self, apikey):
        self.apikey = apikey
        self.searchURL = "https://www.virustotal.com/vtapi/v2/file/search"

        self.headers = {
                            "Accept-Encoding" : "gzip, deflate",
                            "User-Agent"      : "FloatingGhost-Python-Bindings"
                        }

    def _check_response(self, requestResponse):
        """
            Check that VT returned happily

            :param requestResponse: A Requests object
        """

        # Check for ratelimit
        if requestResponse.status_code == 204:
            raise RateLimit("You've hit a rate limit!")

        if requestResponse.status_code == 500:
            raise ServerError("VT errored!")

        
    def search(self, query):
        """
            Search the VT respository for samples.
            NOTE: Will only search past 30 days
            because of search restrictions
            
            :param query: Your Query string
        """

        params = {"apikey" : self.apikey, 
                  "query"  : query
                 }
        
        resp = requests.post(self.searchURL, data=params, headers=self.headers)
        self._check_response(resp)
        return resp.json()        
