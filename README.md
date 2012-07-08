# wordtinkerer #

A simple conversion routine for converting from
[Wordpress](http://wordpress.org) to [Tinkerer](http://tinkerer.bitbucket.org/).

Copyright 2012 Michael Farrell <http://micolous.id.au/>

This is a work in progress and incomplete.

## requires ##

 * Python 2.7 (2.6 may work if you have my patches for Tinkerer).
 * python-mysqldb 
 * pandoc (used to convert HTML to Restructured Text)
 * MySQL database with your Wordpress data

## doesn't require ##

 * Wordpress to be installed.
 * PHP

## running ##

    $ python -m wordtinkerer.main -o blog -p

This will attempt to convert the wordpress blog in the MySQL database
`wordpress` using the username `wordpress` on `localhost`, prompting for a
password and outputting to the blog at `blog`.

Additional command line arguments `--help` will let you change the behaviours.

## outstanding issues to address ##

 * Image embedding.
 * Some Unicode issues.
 * Page hierarchy, author or creation date isn't properly preserved.
 * Post categories and tags are not preserved.
 * Importing from Wordpress backup XML (do we want to support this?)
 * Having multiple `<h1>` tags in a post causes tinkerer to crash.  Should fix
   our output so that it doesn't include this.

## licensing ##

wordtinkerer is licensed under the same terms as Tinkerer itself (FreeBSD).
See the accompanying file `COPYING` for details.

