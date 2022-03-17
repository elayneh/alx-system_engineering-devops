#!/usr/bin/bash
# script that takes a URL, sends to that URL and displays the size of the body of the response

curl -sI GET "$URL" | grep -i "Content-Length"
