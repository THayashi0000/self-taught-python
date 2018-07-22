#coding: utf-8
import re
"""
with open("zen.txt", "r", encoding="utf-8") as f:
    text= f.read()
    #print(text)
    m = re.findall("If", text, re.MULTILINE)
    print(m)
"""

s = "The ghost that says boo haunts the loo"
n = re.findall(".*oo", s, re.IGNORECASE)
print(n)
