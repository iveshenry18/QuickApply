#!/bin/sh

# Set working directory
here="`dirname \"$0\"`"
cd "$here"

QuickApplyRoot=~/Documents/Dev/QuickApply

# Just do it all in one line
${QuickApplyRoot}/.venv/bin/python3 ${QuickApplyRoot}/QuickApply.py
