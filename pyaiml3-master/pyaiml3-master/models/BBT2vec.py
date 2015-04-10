import os, gensim, string



def MySentences(dirname):
	#dirname = "data"
	for fname in os.listdir(dirname):
		for line in open(os.path.join(dirname, fname)):
			try:
				ret = line.lower().translate(string.maketrans("",""), string.punctuation).encode('utf-8').split()
				shel = ret.pop(0)
			except:
				print "blank or failed"# yield [""]

			#if shel == 'sheldon':
			yield ret

sentences = MySentences('data')
#for i in sentences:
#	print i

model = gensim.models.Word2Vec(sentences,  size=500, window=5, min_count=5, workers=12)
print model.doesnt_match("aqua nuts comic toys".split())
model.save('BBTmodel')
#print model['computer']
#for i in model.vocab:
#	print i
print model.doesnt_match("sheldon nuts comic toys".split())
print model.doesnt_match("breakfast cereal dinner lunch".split())

print model.most_similar(positive=['sheldon','like'])
print model.most_similar(positive=['sheldon', 'like'],negative=['dont'])
print model.most_similar(positive=['sheldon','dont'])
print model.most_similar(positive=['sheldon','dont', 'like'])

print model.most_similar(positive=['like'])
print model.most_similar(positive=['like'],negative=['dont'])
print model.most_similar(positive=['dont'])
print model.most_similar(positive=['dont', 'like'])

print model.most_similar(positive=['sheldon','love','comic'])
print model.most_similar(positive=['sheldon','love'])
print model.most_similar(positive=['sheldon','hate'])
print model.most_similar(positive=['love', 'hate'])


sentences2 = MySentences('data')
sentences3 = MySentences('data')
bigram = gensim.models.Phrases(sentences2)
model2 = gensim.models.Word2Vec(bigram[sentences3], size=300, window=5, min_count=5, workers=12)
model2.save('BBTmodel_bigram')
"""
print model.doesnt_match("sheldon nuts comic toys".split())
print model.doesnt_match("breakfast cereal dinner lunch".split())
print model.most_similar(positive=['penny', 'leonard'])
print model.most_similar(positive=['leonard', "penny"],negative=['do'])
print model2.most_similar(positive=['sheldon','dont'], negative=['like'])
print model.most_similar(positive=['sheldon','dont'], negative=['like'])
print model2.most_similar(positive=['sheldon','like'],negative=['dont'])
print model.most_similar(positive=['sheldon', 'like'],negative=['dont'])
print model2.most_similar(positive=['sheldon','dont'])
print model.most_similar(positive=['sheldon','dont', 'like'])"""

