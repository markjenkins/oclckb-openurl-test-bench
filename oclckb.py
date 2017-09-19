#!/usr/bin/env python3

import cgi
import json

# apt install python3-requests on Ubuntu 16.04
import requests

from oclc_api_key import OCLC_KB_API_KEY

OCLC_KB_BASE_URL = "https://worldcat.org/webservices/kb"
OCLC_KB_OPENURL = OCLC_KB_BASE_URL + "/openurl/resolve"

def oclc_kb_openurl(query):
    oclc_url = "%s?%s&wskey=%s" % (
        OCLC_KB_OPENURL, query, OCLC_KB_API_KEY )
    r = requests.get(oclc_url)
    r.raise_for_status()
    return oclc_url, r.status_code, r.json()

