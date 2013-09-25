TeXSubmit
=========

Simple python script to prepare multifile document for submission to journals requiring source .tex file

Who needs this?
===============

--If you have mutliple .tex files and use includes and inputs to source the files

--If you need to combine these files into one file for submission

--If you anticipate having to combine files more than once, after revising the original .tex files

Features
========

--Parses includes and inputs recursively

--Preserves lines and whitespace as originally written

--Removes whole line comments (does not remove inline comments, and you deserve to have the editors see your comment curses at the reviewers if you're commenting inline!)

--Saves one tex file to current working directory

--Automatically makes your paper more interesting to Nature editors (beta)

Requirements
============

--Working Python 2 (tested on 2.7.5 from MacPorts on OS X 10.8.5 (12F37))

--Requires the following modules: os, re, sys

Usage
=====

Backup your stuff. And then back it up again. And then print it out and put it in the safety deposit box at your local bank.

Drop texsubmit.tex in your folder of beautiful LaTeX code for that important manuscript. 

--Must be run from source directory

--Run command is 'python texsubmit.py toptexfile.tex' where 'toptexfile.tex' is your top level LaTeX file.

--If there are no errors, the output will be saved in the current working directory as toptexfile-submit.tex

To check to see if it worked you can always try:

latex toptexfile-submit

If you have a BibTeX bibliography also run ... 

bibtex toptexfile-submit
latex toptexfile-submit
latex toptexfile-submit

The resultant file will be a toptexfile-submit.dvi, which should be converted via your favorite means to PDF. One simple way of doing this might be:

dvipdf toptexfile-submit.dvi

which should result in the file toptexfile-submit.pdf. Enjoy.

Example
=======

To run the example, you need GNU Make. To compile the original, run:

make

The output of this is example0.pdf. You can use this for comparison. Then run:

make texsubmit

The output will be example0-texsubmit.pdf.

You can also clean the directory with:

make clean


A Real Example:
===========

After moving texsubmit.py into /Users/yourusername/sandbox/thisiswheremytexis, go into that folder and run:

python texsubmit.py toptexfile.tex

where toptexfile.tex is the first file that specifies documentclass and other includes/inputs.

Limitations and Known Issues
============================

This code has been minimally tested to run with well-formed files and inputs on Unix and Unix-like machines. It is not guaranteed to be safe, bug-free, etc. etc. Unclear it if would choke on big projects, this should be fine for thesis length or shorter, unless you're in the humanities, in which case your thesis is too verbose, and you're not using LaTeX anyhow. Always make backups before using.

It might work for files that are in subdirectories, assuming the subdirectories are well-formed and correctly referred to.

It will not work for fancy includes and inputs that are wrapped in some other command.

This program did not ruin your thesis. It cannot destroy anything. It obeys the three laws. Anyway, you can always go back to your last backup/vcs commit, right? What, you don't use vcs??!

Sorry it's only minimally commented. But hey, it's python, so it's readable!

Improvements/Bug reports
========================
Please improve this software! You are welcome to fork, maintain, submit patches, etc. You are welcome to contact me via github regarding this project and only this project.
