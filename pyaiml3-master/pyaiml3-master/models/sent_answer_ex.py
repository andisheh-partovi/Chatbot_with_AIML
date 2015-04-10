__author__ = 'dan'
import os, string,re

def MySentences(dirname):
	#dirname = "data"
	f = open("sheldon_scripted.aiml", 'a')
	isAnswer = False
	question = ""
	for fname in os.listdir(dirname):
		for line in open(os.path.join(dirname, fname)):
			line = line.strip()
			try:
				if line[-1:] == '?':
					line = re.sub(r'\([^)]*\)', '', line)
					ret = line.lower().translate(string.maketrans("",""), string.punctuation).encode('utf-8').split()
					questPerson = ret.pop(0)
					print ret
					if questPerson != 'sheldon':
						question = " ".join(ret)
					else:
						print  "test" #line
					isAnswer = True
				elif isAnswer == True:
					line = re.sub(r'\([^)]*\)', '', line)
					ret = line.lower().translate(string.maketrans("",""), string.punctuation).encode('utf-8').split()
					shelAns = ret.pop(0)
					ret = [w.replace(questPerson, '<bot name="name"/>') for w in ret]
					if shelAns == 'sheldon':
						#if questPerson in line:
						#	line.replace(questPerson, '<bot name="name"/>')
						f.write("<category>\n")
						f.write('\t<pattern>' + question.translate(string.maketrans("",""), string.punctuation) + '</pattern>\n')
						f.write('\t<template>'+ " ".join(ret) +'</template>\n')
						f.write('</category>\n')
						#print 'test'
					isAnswer = False
			except:
				print ""
			"""
			try:
				ret = line.lower().translate(string.maketrans("",""), string.punctuation).encode('utf-8').split()
				shel = ret.pop(0)
			except:
				print "blank or failed"# yield [""]

			#if shel == 'sheldon':
			yield ret"""

MySentences('data')