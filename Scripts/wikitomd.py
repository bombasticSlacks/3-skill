#!/usr/bin/env python3
# makes wikilinks into markdown links
import fileinput
import re
import os


# \[\[(.*?)\]\]\g is wikilink
# \[\[(.*?)#(.*?)\]\]\g wikilink w. anchor
# \[\[(.*?)\|(.*?)\]\]\g wikilink w. name
# \[\[(.*?)#(.*?)\|(.*?)\]\]\g wikilink w. name and anchor

# Do in most specific to least specific

# Grab groups, verify file url, replace.

# Find all relevant files
def findAll(name: str, path: str) -> str:
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))


    if len(result) == 0:
        err = f"No results for {name}"
        raise Exception(err)
    if len(result) > 1:
        err = f"Multiple files for {name}"
        raise Exception(err)
    return result[0]

def linkParse(file: str, anchor = "", title = "" ) -> str:
    # We parse the file making sure file exists, finding unique location and adding other bits
    if anchor:
        anchor = f"#{anchor}"

    if not title:
        title = file

    # Convert file to URL
    file = findAll(f"{file}.md", "Game")

    file = file.split(".md")[0]

    text = f"[{title}]({file}{anchor})"
    return text

for line in fileinput.input(encoding="utf-8", inplace=True):
    line = re.sub(r'\[\[(.+?)#(.+?)\|(.+?)\]\]',
                 lambda m: linkParse(m.group(1), m.group(2), m.group(3)), line)
    
    line = re.sub(r'\[\[(.+?)\|(.+?)\]\]',
                 lambda m: linkParse(m.group(1), "", m.group(2)), line)
    line = re.sub(r'\[\[(.+?)#(.+?)\]\]',
                 lambda m: linkParse(m.group(1), m.group(2), ""), line)
    
    line = re.sub(r'\[\[(.+?)\]\]',
                 lambda m: linkParse(m.group(1), "", ""), line)
    
    print(line, end='')



