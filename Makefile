# Makefile for TeXSubmit project
#
# INSTRUCTIONS:
# run 'make' or 'make example0' to compile original. Output is example0.pdf
# run 'make texsubmit' to run the python script and compile the new file.
#   Output is example0-texsubmit.pdf
# run 'make clean' to remove files created by both, including pdf files
#
# LICENSE:
# This file is part of TeXSubmit.
#
# TeXSubmit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# TeXSubmit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TeXSubmit. If not, see <http://www.gnu.org/licenses/>.
#
# v 0.1
# rev: 2013-09-25 (created)
# last major:

ECHO = /bin/echo
MV = /bin/mv
CP = /bin/cp

project = example0
onefile = $(project)-texsubmit

example0 :
	pdflatex $@
	@$(ECHO) '---------------------------------------------------------------'
	@$(ECHO) 'Make built $(project) [orig] successfully. Output is $@.pdf'
	@$(ECHO) '---------------------------------------------------------------'

texsubmit :
	python texsubmit.py $(project).tex
	pdflatex $(project)-$@
	@$(ECHO) '------------------------------------------------------------------------------'
	@$(ECHO) 'Make built $(project) [$@] successfully. Output is $(project)-$@.pdf'
	@$(ECHO) '------------------------------------------------------------------------------'

clean : 
	rm -f *.aux $(project).log $(project).pdf
	rm -f $(onefile).aux $(onefile).log $(onefile).pdf
