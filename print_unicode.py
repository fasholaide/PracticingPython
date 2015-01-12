#!/usr/bin/env python3

import sys
import unicodedata


def print_unicode_table(words, length):
    print("decimal   hex   chr  {0:^40}".format("name"))
    print("-------  -----  ---  {0:-<40}".format(""))

    code = ord(" ")
    end = min(0xD800, sys.maxunicode) # Stop at surrogate pairs

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        know = int(0)
        tmp = length - 1
        while tmp >= 0:
            if words[tmp] in name.lower():
                know += 1
            else:
                know -= 1
            tmp -= 1
           
        if words is None or know == length:
            print("{0:7}  {0:5X}  {0:^3c}  {1}".format(
                  code, name.title()))
        code += 1


words = []
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [strings...]\n\nYou can type as many strings as you desire.".format(sys.argv[0]))
        words = []
    else:
        wordtemp = sys.argv[1:]
        for word in wordtemp:
            words.append(word.lower())
if words != []:
    print_unicode_table(words, len(words))
