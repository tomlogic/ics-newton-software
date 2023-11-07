"""
  Registration Code Generator
      for Newton Shareware
by Innovative Computer Solutions

In the 1990's, ICS released multiple programs for the Newton MessagePad as
shareware, in addition to commercial releases of NewtCase and X-Port.

This Python script implements the registration code algorithm used so Newton
enthusiasts can enjoy our programs on their devices in the 21st century and
beyond.

In case you can't get this Python script to work, you can use the following
codes for user "Izzy Newt":

    MultiTask: LOSUBNHJIE
    GestureLaunch: BHUASHGBKJ
    BarKeep: RIBLROSLEE
    WhatToDo: XKYSHRDXJX
    Twerx: JNOVKPPCZH

Dan Rowley and Tom Collins
https://web.archive.org/web/20021209184428/http://www.newts.com/newton/
"""

import re, sys


def paddedName(name):
	# Convert name to all uppercase
	name = re.sub(r'[^A-Z]', '', name.upper())
	if len(name) == 0:
		name = 'AX'
	# Pad name with copies of itself if less than 10 characters
	i = 0
	while len(name) < 10:
		name = name + name[i]
		i += 1;

	return name

	
def genICS(c1, c2, padded):
	key = 13
	check = key
	m = chr(key + 65)

	for i in range(0, len(padded)):
		o = (ord(padded[i]) - 48 + key) % 26
		check += o
		key = ((o + key) * c1 + c2) % 127
		m += chr(o + 65)

	m += chr((2600-check) % 26 + 65)
	
	return m[-10:]


codes = [
	{ 'name':'MultiTask',     'c1':234, 'c2':345 },
	{ 'name':'GestureLaunch', 'c1':361, 'c2':511 },
	{ 'name':'BarKeep',       'c1':567, 'c2':304 },
	{ 'name':'WhatToDo',      'c1':521, 'c2':317 },
	{ 'name':'Twerx',         'c1':513, 'c2':379 }
]


def main():
	if len(sys.argv) != 2:
		print('usage: python ics_newton_codes.py <name>')
		exit()

	name = sys.argv[1]

	print('ICS Newton Registration codes for user "%s":' % name)

	padded = paddedName(name)
	for entry in codes:
		print('%s: %s' % (entry['name'], genICS(entry['c1'], entry['c2'], padded)))


if __name__ == '__main__':
	main()
