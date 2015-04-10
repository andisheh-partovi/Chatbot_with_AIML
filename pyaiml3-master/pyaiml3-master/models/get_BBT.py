from bs4 import BeautifulSoup
import urllib


Do not run

url = 'https://bigbangtrans.wordpress.com/series-1-episode-1-pilot-episode/'
page=urllib.urlopen(url)
soup = BeautifulSoup(page.read())


for links in soup.findAll(attrs={'id':'pages-2'}):
	for link in links.find_all('a', href=True):
		url = link['href']
		print url
		str = url.split('-')
		#str = str.split('-', 1 )
		try:
			if int(str[1]) >= 6:
				print str[1]
				page=urllib.urlopen(url)
				soup = BeautifulSoup(page.read())
				for s in soup.findAll(attrs={"id": "content"}):
					fname= s('h2')[0].text.encode("ascii", 'ignore').replace (" ", "_").replace("/", "_")
					print fname
					f = open('data/' + fname + ".txt",'a')
					for p in s('p'):
						f.write(p.text.encode("ascii", 'ignore') + "\n")
		except:
			print 'about'






#raw = soup.getText("\n", strip=True)
#
#f.write(raw.encode("ascii",'ignore'))
