#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 14:48:39 2021

@author: campbellhogg
"""

#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re


"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  list = []

  # Open and read the file.
  file_1 = open(filename, 'rU')
  text = file_1.read()
  # Could process the file line-by-line, but regex on the whole text
  # at once is even easier.

  # Get the year.
  year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
  if not year_match:
    # no year then exit with an error message.
    sys.stderr.write('Couldn\'t find the year!\n')
    sys.exit(1)
  year = year_match.group(1)
  list.append(year)

  # Extract all the data (rank, boy name, girl name) with a findall()
  tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
  #print tuples

  # Store data into a dict 
  names_rank =  {}
  for rank_tuple in tuples:
    (rank, boyname, girlname) = rank_tuple  #separate tuple
    if boyname not in names_rank:
      names_rank[boyname] = rank
    if girlname not in names_rank:
      names_rank[girlname] = rank

  # Get the names, sorted in the right order
  sorted_names = sorted(names_rank.keys())

  # Build up result list, one element per line
  for name in sorted_names:
    list.append(name + " " + names_rank[name])

  return list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print("usage: [--summaryfile] file [file ...]")
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    list = extract_names(filename)

    # Make text out of the whole list
    text = '\n'.join(list)

    if summary:
      outf = open(filename + '.summary', 'w')
      outf.write(text + '\n')
      outf.close()
    else:
      print(text)

if __name__ == '__main__':
  main()
