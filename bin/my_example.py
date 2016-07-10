#!/usr/bin/env python

"""Retrieve and print words from a URL.

Usage:

        python3 example.py <URL>
        
        OR
        
        chmod a+x example.py
        ./example <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from the document.
    """
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)

#http://www.diveintopython.net/scripts_and_streams/command_line_arguments.html
def main(argv):                          1
    grammar = "kant.xml"                
    try:                                
        opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="])
    except getopt.GetoptError:          
        usage()                         
        sys.exit(2)                     
    for opt, arg in opts:                2
        if opt in ("-h", "--help"):      3
            usage()                     
            sys.exit()                  
        elif opt == '-d':                4
            global _debug               
            _debug = 1                  
        elif opt in ("-g", "--grammar"): 5
            grammar = arg               

    source = "".join(args)               6

    k = KantGenerator(grammar, source)
    print k.output()


#def main(url):
#    words = fetch_words(url)
#    print_items(words) # code comment can be done this way with sharp


if __name__ == '__main__':
    main(sys.argv[1:])
