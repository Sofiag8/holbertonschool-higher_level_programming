#!/bin/bash
# script that takes in a URL and shows its bytes size
curl -s $1 | wc -c
