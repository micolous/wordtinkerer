#!/usr/bin/env python
"""
From:
http://johnpaulett.com/2009/10/15/html-to-restructured-text-in-python-using-pandoc/
"""

from subprocess import Popen, PIPE


def html2rst(html):
	p = Popen(
		['pandoc', '--from=html', '--to=rst', '--base-header-level=2'],
		stdin=PIPE, stdout=PIPE
	)

	return p.communicate(html)[0]

