#!/usr/bin/env python3

# kbsearch.py -- Pass on a search to the OCLC KB and display results as links
#
# Copyright University of Winnipeg 2017
#
# All rights reserved
#
# @author Mark Jenkins <ma.jenkins@uwinnipeg.ca>

import cgitb
cgitb.enable()
# use when going to production
#cgitb.enable(display=0, logdir="/path/to/logdir")

import cgi
from urllib.parse import urlencode

from oclckb import oclc_kb_openurl

def list_of_results(return_json):
    return '\n'.join(
        '<li><a href="%s">%s</a></li>' % (
            ('' if 'url' not in result else result['url']),
            ('' if 'title' not in result else result['title'])
        ) # tuple for string format
        for result in return_json
    ) # join

def main():
    print("Content-Type: text/html")
    print()

    f = cgi.FieldStorage()

    # user provided paramaters
    additional_params = f.getfirst("additional_params")
    additional_params_append = ("" if additional_params in ("",None) else
                                "&" + additional_params)
    
    # don't allow the svc_id paramater to be specified, as this could
    # tell OCLC KB to send XML instead of json
    if "svc_id" in additional_params_append:
        print("""<!DOCTYPE html>
<title>Error</title>
<p>Please don't set the svc_id parameter</p>""")
        return
    
    main_query_dict =  {
        key: f.getfirst(key)
        for key in f
        if key not in ("additional_params", "svc_id") and
        f.getfirst(key) not in (None, "")
    } # end dictionary generator

    query_url, status, return_json = \
        oclc_kb_openurl( urlencode(main_query_dict) +
                         "&svn_id=json" + # output is json by default, 
                                          # but lets be explicit
                         additional_params_append )
    print("""<!DOCTYPE html>
<title>OCLC KB Search Result</title>""")
    if len(return_json) > 0:
        print("""<ul>
%s
</ul>
""" %  list_of_results(return_json))
    else: # 0 results
        print( "<p>No results found</p>")
    
if __name__=="__main__":
    main()
