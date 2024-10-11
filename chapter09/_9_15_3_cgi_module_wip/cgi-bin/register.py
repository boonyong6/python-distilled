#!/usr/bin/env python
import cgi

try:
    form = cgi.FieldStorage()
    name = form.getvalue("name")
    email = form.getvalue("email")
    
    # Validate the responses and do whatever
    
    # Produce an HTML result (or redirect)
    print("Status: 302 Found\r")
    print("Location: https://boonyong.serv00.net/\r")
    print("\r")
except Exception as e:
    print("Status: 501 Error\r")
    print("Content-type: text/plain\r")
    print("\r")
    print("Some kind of error occurred.\r")
    