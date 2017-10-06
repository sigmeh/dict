#!/usr/bin/env python
'''
Simple python command-line tool for dictionary lookup from 'thefreedictionary.com'. 
Utilizes the requests module for data retrieval and 
python BeautifulSoup parser with lxml library. 

Usage:
	
	$ python dict.py [dictionary_term]

Add function to .bashrc to run command from any directory; e.g., 

	dict(){
		python <path_to_file>/dict.py $@
	}
	
	then, 
	
	$ dict [dictionary_term]

'''

from bs4 import BeautifulSoup as bs
import requests
import sys

headers = {
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:43.0) Gecko/20100101 Firefox/44.0',
		'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'accept-language' : 'en-US,en;q=0.5',
		'dnt' : '1'
	}

def main():
	if len(sys.argv) < 2:
		print 'Need search term argument.'
		return
		
	term = sys.argv[1] 
	url = 'http://www.thefreedictionary.com/%s' % term
	
	r = requests.get(url,headers=headers)
	doc = r.text

	soup = bs(doc, 'lxml')
	definition = soup.find(id='Definition')
	
	sections = definition.find_all('section')
	for i,s in enumerate(sections):
		print '%s.  %s' % (i, s.get_text())

if __name__ == '__main__':
	main()