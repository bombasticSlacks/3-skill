#!/usr/bin/env python3

# embeds md blocks
import os
import subprocess
import sys

dir = sys.argv[1]
sprites = "Game/Content/Sprites"

allSprites = os.listdir(sprites)

for block in os.listdir(dir):
    # Skip .bak files
    if block.find(".bak") == -1:
        address = dir + "/" + block
        name = block.removesuffix(".md")
        print(name)

        with open(address, 'r') as f:
            # Wrap our block with some HTML
            contents = '<div class="block">\n\n'
            # Add image if there is one
            if name + ".png" in allSprites:
                contents += '<div class="sprite">\n\n'
                contents += "<img class='imgstack' src='/Content/Sprites/Base.png' />"
                contents += "<img class='imgstack' src='/Content/Sprites/" + name + ".png' />"
                contents += '\n\n</div>'
            contents += '<div class="blockdetails" markdown="1">\n\n'
            contents += f.read()
            contents += '\n\n</div>'
            contents += '\n\n</div>'

        # find the relevant files
        result = subprocess.run(
            ["grep", "-r", "-l", f"--regexp=!\[{name}]({dir}/{name})", "Game/"], capture_output=True, text=True)
        files = result.stdout.split("\n")
        # remove last empty entry
        files.pop()
        for fi in files:
            print("Found in:")
            print(fi)
            with open(fi, 'r') as fileBuffer:
                fileContents = fileBuffer.read()

            # Replace the strings
            fileContents = fileContents.replace(
                f'![{name}]({dir}/{name})', contents)

            # Replace the file
            with open(fi, 'w') as fileBuffer:
                fileBuffer.write(fileContents)
