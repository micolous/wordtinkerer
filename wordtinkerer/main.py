#!/usr/bin/env python
"""
This file is a part of wordtinkerer.
Copyright (c) 2012 Michael Farrell
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from optparse import OptionParser
from wordtinkerer.pandoc import html2rst
import MySQLdb
from os import makedirs
from os.path import exists, join
from sys import exit
import tinkerer.post
import tinkerer.paths

def nl2br(i):
	"Emulate nl2br function from php, because Wordpress does this."
	return i.replace('\r','').replace('\n\n', '<p>')


def convert_blog(database, username, hostname, output_dir, password):
	# check for master.rst file
	if not exists(join(output_dir, 'master.rst')):
		# master file doesn't exist.
		print 'The `master.rst` file does not exist in your output directory.'
		print 'Have you run `tinker --setup`?  Is the output path correct?'
		return False
		
	tinkerer.paths.set_paths(root_path=output_dir)
		
	if password:
		# TODO: mask input
		password = raw_input('password?')
	else:
		password = None
	
	if password:
		conn = MySQLdb.connect(host=hostname, user=username, db=database, passwd=password)
	else:
		conn = MySQLdb.connect(host=hostname, user=username, db=database)
	
	cur = conn.cursor()
	
	
	cur.execute('SELECT id, post_date_gmt, post_content, post_title, post_name from wp_posts WHERE post_status=\'publish\' and post_type=\'post\'')
	
	
	for i, row in enumerate(cur):
		print 'Post %d of %d: %s' % (i+1, cur.rowcount, row[3])
		post = tinkerer.post.create(row[3].replace('\r','').replace('\n',''), date=row[1])
		
		posttext = html2rst(nl2br(row[2])).decode('utf8')
		post.write(content=posttext)
		
	
	#print cur.fetchall()
	return True


def main():
	parser = OptionParser(usage='%prog -D wordpress -u wordpress')
	
	parser.add_option('-D', '--database', dest='database', default='wordpress', help='Database where wordpress data is stored.')
	parser.add_option('-u', '--username', dest='username', default='wordpress', help='Username to connect to wordpress database.')
	parser.add_option('-H', '--hostname', dest='hostname', default='localhost', help='Hostname where MySQL is running.')
	parser.add_option('-p', '--password', dest='password', default=False, action='store_true', help='Prompt for a password to connect to the database.')
	parser.add_option('-o', '--output-directory', dest='output_dir', help='Destination directory for files.')
	
	options, args = parser.parse_args()
	
	if not options.username:
		parser.error('Username not specified.')
	
	if not options.database:
		parser.error('Database not specified.')
		
	if not options.hostname:
		parser.error('Hostname not specified.')
		
	if not options.output_dir:
		parser.error('Output directory not specified.')
		
	r = convert_blog(options.database, options.username, options.hostname, options.output_dir, options.password)

	if not r:
		exit(1)

if __name__ == '__main__':
	main()

