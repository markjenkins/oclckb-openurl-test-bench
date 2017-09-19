Allows testing the OCLC Knowledge Base OpenURL based search.

To work, you need to create a oclc_api_key.py with your api key
defined as OCLC_KB_API_KEY
like
OCLC_KB_API_KEY="myapikey"

Configure a webserver that can serve up style.css and index.html and run /kbsearch.py as a cgi program.