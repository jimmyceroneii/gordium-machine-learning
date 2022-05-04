#!/bin/bash

## NOTE: This script must be used from the /Users/jrcii/Documents/Me folder
## EXAMPLE: ./file_names.sh NAME-OF-IDEA

## navigate to our problems folder
cd /Users/jrcii/Documents/"Gordium Brain"/Gordium/Problems

## create a list of all the files in the folder
ls > /Users/jrcii/Documents/Me/gordium-machine-learning/file_names.txt

## return to the original folder
cd -

## run the python script
python3 nlp.py --file /Users/jrcii/Documents/Me/gordium-machine-learning/file_names.txt $1