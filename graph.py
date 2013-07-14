#!/usr/bin/env python
# encoding: utf-8

import codecs
import json
import sys

# The index line in the .csv file
first_line = []

# An arbitrary offset for languages not in the index
count = 100

# Index dictionary for the languages
index_dict = {}

# The tree for the languages as defined in JSON
lang_tree = None

# Returns the index in the CSV line for a language if it exits, a unique index otherwise
def lang_index(lang):
    global count
    try:
        if not index_dict.has_key(lang):
            index_dict[lang] = first_line.index(lang)
        return index_dict[lang]
    except:
        if not index_dict.has_key(lang):
            index_dict[lang] = count
            count += 1
        return index_dict[lang]

# Write nodes to the dotfile.
# Returns true if something was drawn
def traverse(f, tree, words):
    index = lang_index(tree["lang"])
    inf_index = lang_index(tree["lang"] + "_inf")
    indexs = str(index) # Index string

    has_children = tree.has_key("sub")
    has_nonempty_children = False

    # TODO: [style=dotted] from JSON file
    if has_children:
        for sub in tree["sub"]:
            did_create_node = traverse(f, sub, words)
            if did_create_node:
                f.write(indexs + " -> " + str(lang_index(sub["lang"])) + "\n")
                has_nonempty_children = True

    # If we have a language not in the database, or there's no word in this
    # language, draw the name of this language only if it has nonempty children.
    if index > len(words) or len(words[index]) == 0:
        if has_children and has_nonempty_children: # TODO: Logic consequence?
            f.write(indexs)
            f.write(" [shape=none,label=\"")
            f.write(tree["lang"])
            f.write("\"]\n")
        else:
            return False
    else:
        f.write(indexs)
        f.write(" [shape=none,label=<")
        f.write("(" + tree["abbr"] + ") " + words[index])
        if len(words[inf_index]) != 0:
            f.write("<br/>" + "<i>" + words[inf_index] + "</i>")
        f.write(">]\n")

    return True

# Returns the language tree as defined in JSON
def get_tree():
    global lang_tree
    if not lang_tree:
        lang_tree = json.load(open("tree.json", "r"))
    return lang_tree

def sanitize_filename(fname):
    return fname.replace('*', '').replace('-', '').replace(' ', '').replace('/', '').replace('(','').replace(')', '')

def write_dotfile(words):
    tree = get_tree()

    f = codecs.open("%s.dot" % sanitize_filename(words[0]), 'w', 'utf-8')

    # Write header
    f.write("digraph {\n")

    # Peamble
    f.write("node [fontname=\"Georgia\"];\n")
    f.write("edge [arrowhead=none,arrowtail=dot];\n")

    # Body
    traverse(f, tree, words)

    # Footer
    f.write("}\n")

    f.close()

def main():
    global first_line
    #f = open("input.csv", "r")

    if len(sys.argv) == 2:
        input_file = sys.argv[1]
    else:
        input_file = "input.csv"

    f = codecs.open(input_file, encoding="utf-8", mode="r")

    lines = f.readlines()

    for n in range(0, len(lines)):
        # Skip the first since it's headers
        if n == 0:
            # Store the index
            first_line = lines[n].split(",")
            continue

        line = lines[n]

        words = line.split(",")
        write_dotfile(words)

if __name__ == '__main__':
    main()
