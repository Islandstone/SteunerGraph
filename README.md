# Støner Graph Generator 0.1

Generates Støner graphs based on input from a CSV file. By default, the file 
named Majstrie.csv will be used.

### Usage:

Do not run this in the Dropbox folder unless required.

Running make will perform all tasks required. 

If a manual approach is preferred, do as follows:

* Run graph.py with python, specify an input file if desired.
* Generate a jpg-file from the dot-file using the command
    dot -Tjpg -o"outputdir/filename.jpg"

### Known issues

* Not all dot-files are free of syntax errors. Currently malformed input is
believed to be the source of these, but this is not confirmed.
* No part of the database may contain commas, as in the sign *,*, because the
program uses commas to separate columns.
* The makefile is split into two files because of some plebbery in how
makefiles evaluate targets, since the dot-files don't exist in a clean state.
Since the files doesn't exist (yet), make believes there's nothing more to do.
* Make sure Støner removes the verb category column from the input file,
unless it's proven that the script still works when the column is present. 
* Dropbox is slow when it comes to synching files between users. If the output
is urgently required, provide Støner with the "Share this folder"-URL instead
of waiting for Dropbox.

### Adding a new language

The language tree structure is defined in tree.json. Ask Støner where in the
tree the language is, and add the language to the subs-array in the json file
accordingly. The file *input.csv.eq* can be used to create a language tree that
can be verified by Støner.
