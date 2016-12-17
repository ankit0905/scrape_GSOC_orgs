from bs4 import BeautifulSoup
import requests, sys, os

f = open('GSOC-Organizations.txt', 'w')
r = requests.get("https://summerofcode.withgoogle.com/archive/2016/organizations/")
soup = BeautifulSoup(r.content, "html.parser")
a_tags = soup.find_all("a", {"class": "organization-card__link"})
title_heads = soup.find_all("h4", {"class": "organization-card__name"})
links,titles = [],[]
for tag in a_tags:
    links.append("https://summerofcode.withgoogle.com"+tag.get('href'))
for title in title_heads:
	titles.append(title.getText())
for i in range(0,len(links)):
	print "Currently Scraping : ", 
	print titles[i]
	req = requests.get(links[i])
	page = BeautifulSoup(req.content, "html.parser")
	technologies = page.find_all("li",{"class": "organization__tag--technology"})
	topics = page.find_all("li",{"class":"organization__tag--topic"})
	name = titles[i] + "\n\n" + "\tTECHNOLOGIES: \n"
	name = name.encode('utf-8')
	f.write(str(name))
	for item in technologies:
		text = ("\t\t* " + item.getText()+"\n").encode('utf-8')
		f.write(str(text))
	category = page.find("li",{"class":"organization__tag--category"}).getText()
	category = category.rstrip().lstrip()
	f.write("\n\tCATEGORY: "+" "+category+"\n\n")
	f.write("\tTOPICS: \n")
	for topic in topics:
		text = ("\t\t* " + topic.getText() + "\n").encode('utf-8')
		f.write(text)
	newlines=("\n\n").encode('utf-8')
	f.write(newlines)
