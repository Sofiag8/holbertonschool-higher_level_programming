#!/bin/bash
# sends a POST request to the passed URL . POST use
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" $1
