#!/bin/python3

import marko
import requests
from htmlslacker import HTMLSlacker
from os import getenv

WEBHOOK_URL = getenv("SLACK_WEBHOOK_URL")

# Stuff for the slack build kit format
section = lambda s: { "type" : "section", "text" : { "type" : "mrkdwn", "text" : s } }
divider = { "type" : "divider" }

slack_builder = [
    section("*There are updates to the AAW!!! Check out the <https://github.com/StatCan/daaas/blob/master/CHANGELOG.md|Changelog> to see what's new!*"),
    divider
]



# Get the *first* H1 Heading from the Changelog
with open("CHANGELOG.md") as f:
    # Only use the first h1 header
    lines = f.readlines()
    last = len(lines)
    count = 0
    for (i, line) in enumerate(lines):
        if line.startswith("# "):
            count += 1
            if count == 2:
                last = i
                break
    # If there's only one h1, then this is idempotent
    lines = lines[:last]
    doc = marko.parse(''.join(lines)).children




# Parsing the markdown
render = lambda x: HTMLSlacker(marko.render(x)).get_output()

def flatten(x):
    if not isinstance(x, list):
        return [x]
    else:
        return sum( [ flatten(e.children) for e in x ] , [])

def list_render(l):
    blocks = [ flatten(x.children) for x in l ]
    print(blocks)
    for block in blocks:
        block[0] = '*' + block[0] + '*'
        for i in range(1, len(block)):
            block[i] = '• ' + block[i]

    return '\n\n'.join( '\n'.join(block) for block in blocks )

for e in doc:
    if isinstance(e, marko.block.Heading):
        item = "*" + render(e) + "*"
    elif isinstance(e, marko.block.Quote):
        item = "> " + render(e)
    elif isinstance(e, marko.block.BlankLine):
        continue
    elif isinstance(e, marko.block.List):
        item = list_render(e.children)
    else:
        item = render(e)
    slack_builder.append(section(item))

print(slack_builder)



# Push!
payload = {
    "channel": "#general",
    "username": "AAW Updates",
    "blocks": slack_builder,
    "icon_emoji": ":rocket:"
}

x = requests.post(WEBHOOK_URL, json=payload)
print(x)
