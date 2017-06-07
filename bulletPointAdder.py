#! python3
# bulletPointAdder.py - Adds Wikkipedia bullet points to the start
# of each line og text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.

lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the "lines" lines
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)
