#!/usr/bin/env python3

# Copyright      2017  Hossein Hadian

# Apache 2.0
# This script converts a BPE-encoded text to normal text. It is used in scoring

import sys, io
import string
import unicodedata
infile = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
output = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
for line in infile:
  words = line.strip().split()
  uttid = words[0]
  transcript = ' '.join(words[1:])
  text_normalized = unicodedata.normalize('NFC', transcript)
  output.write(uttid + ' ' + text_normalized + '\n')
