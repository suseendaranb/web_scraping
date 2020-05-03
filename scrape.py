import requests # grans the html file
from bs4 import BeautifulSoup # helps us work with the html file
import pprint


res = requests.get('https://news.ycombinator.com/') # this is what any browser is using underneath the hood
soup = BeautifulSoup(res.text, 'html.parser') # bs can parser html and xml etc
#print(soup.find(id ='score_23023675')) # .body.contents, .title, .a, .find
links = soup.select('.storylink') #css selector is a list ways to grab an  element from html file
#here '.' means it is a class
subtext = soup.select('.subtext')
#votes = soup.select('.score')

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key=lambda k:k['votes'], reverse = True)


def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points',''))
			if points > 99:
				hn.append({'title':title, 'link':href, 'votes':points})
	return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))