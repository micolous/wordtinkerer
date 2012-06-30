#!/usr/bin/env python

from subprocess import Popen, PIPE

def html2rst(html):
	"From http://johnpaulett.com/2009/10/15/html-to-restructured-text-in-python-using-pandoc/"
	
	p = Popen(
		['pandoc', '--from=html', '--to=rst'],
		stdin=PIPE, stdout=PIPE
	)
	
	return p.communicate(html)[0]

