#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
	name="wordtinkerer",
	version="0.1",
	description="Wordpress to Tinkerer conversion routine.",
	author="Michael Farrell",
	author_email="micolous@gmail.com",
	url="https://github.com/micolous/wordtinkerer",
	license="FreeBSD",
	requires=(
		'mysqldb',
		'tinkerer',
	),
	
	
	# TODO: add scripts to this.
	packages=find_packages(),
	
	entry_points={
		'console_scripts': [
			'wordtinkerer = wordtinkerer.main:main',
		]
	},
	
	classifiers=[
	
	],
)

