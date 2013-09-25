#!/usr/bin/env python
#
# texsubmit.py - script to compile all relevant tex files into one
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# v 0.1
# rev 2013-09-17 (created)
# last major:

import os
import re
import sys

def prettyprint(iterable_items):
    for item in iterable_items:
        print item

class DocLaTeX():
    def __init__(self, f_input):
        # assumes the file input is here, the cwd
        self.dtex = os.getcwd()

        # create the output filename
        self.f_input = f_input
        self.__f_output_create()

        # init self.lines
        self.lines = []

        # fread
        self.__file_read_init()

        # includes (and inputs)
        self.__expand_includes()

    def save(self):
        with open(self.fname_out, 'wb') as f_out:
            for line in self.lines:
                if line:
                    if line.startswith('\n'):
                        f_out.write(line)
                    else:
                        f_out.write('%s\n' % line)

    def __f_output_create(self):
        fprefix = self.f_input.split('.tex')[0]
        self.fname_out = os.path.join(self.dtex, '%s-texsubmit.tex' % fprefix)

    # custom fread for preserving lines
    def __file_read_init(self):
        self.lines = self.__file_read(self.f_input)

    def __file_read(self, f_in):
        with open(f_in, 'rb') as f:
            lines_tmp = []
            for line in f:
                if line in ['\n', '\r\n']:
                    lines_tmp.append('\n')
                else:
                    lines_tmp.append(line.rstrip('\n'))

            return [line for line in lines_tmp if line]

    # trying to avoid making a whole copy of the file
    def comment_strip(self):
        lines_comment = []

        for line in self.lines:
            if line.lstrip() and line.lstrip()[0] == '%':
                lines_comment.append(line)

        # must be done this way to avoid screwing with self.lines during the loop!
        for line_comment in lines_comment:
            self.lines.remove(line_comment)

    # cut off as soon as *any* include/input is detected
    def __includes_check(self):
        for line in self.lines:
            l_raw = line.strip()
            if l_raw.startswith(('\\input{', '\\include{')):
                return 1

        return 0

    # loops through while there are still includes 
    # and expands them at each level
    def __expand_includes(self):
        while self.__includes_check():
            # new doc
            doc_expanded = []

            for line in self.lines:
                # check for raw lines
                l_raw = line.strip()

                # handle empty lines
                if not l_raw:
                    doc_expanded.append(line)

                elif l_raw.startswith(('\\input{', '\\include{')):
                    fprefix = re.findall(r'\{([^}]*)\}', l_raw)[0]
                    fname = os.path.join(self.dtex, '%s.tex' % fprefix)
                    lines_f = self.__file_read(fname)

                    # horrid handling of adding clearpage to include
                    if l_raw.startswith('\\include{'):
                        doc_expanded.append('\n\\clearpage\n')
                    
                    # add all the lines
                    doc_expanded.extend(lines_f)

                    # horrid handling of adding clearpage to include
                    if l_raw.startswith('\\include{'):
                        doc_expanded.append('\\clearpage\n')
                    
                else:
                    doc_expanded.append(line)

            self.lines = doc_expanded

if __name__ == '__main__':
    try:
        f_start = sys.argv[1]
    except:
        sys.exit("File not specified. Usage: python texsubmit.py {f_start.tex}")

    doc_latex = DocLaTeX(f_start)
    doc_latex.comment_strip()
    doc_latex.save()
    # prettyprint(doc_latex.lines)
