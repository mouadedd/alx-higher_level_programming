#!/bin/bash
#takes in a URL, sends a request to that URL, and displays size in bytes of the body of the response
curl -s "$1" | wc -c
