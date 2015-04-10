import gensim

model = gensim.models.Word2Vec.load('BBTmodel')
model_bi = gensim.models.Word2Vec.load('BBTmodel_bigram')

model_sheldon = gensim.models.Word2Vec.load('BBTmodel_sheldon')
model_bi_sheldon = gensim.models.Word2Vec.load('BBTmodel_bigram_sheldon')



print model_sheldon.most_similar(positive=['power'])
#print model_sheldon.most_similar(positive=['friend'])

#print model.most_similar(positive=['stool'])
#print model.most_similar(positive=['friends','leonard'])
#print model.doesnt_match("breakfast cereal dinner lunch".split())

#print model.doesnt_match("But tonight Thursday pills".lower().split())

"""
print model.doesnt_match("breakfast cereal dinner lunch".split())
print model.most_similar(positive=['penny', 'leonard'])
print model.most_similar(positive=['leonard', "penny"],negative=['do'])
print model_bi.most_similar(positive=['sheldon','dont'], negative=['like'])
print model.most_similar(positive=['sheldon','dont'], negative=['like'])
print model_bi.most_similar(positive=['sheldon','like'],negative=['dont'])
print model.most_similar(positive=['sheldon', 'like'],negative=['dont'])
print model_bi.most_similar(positive=['sheldon','dont'])
print model.most_similar(positive=['sheldon'], negative=['hate', 'dont'])
print model_bi.most_similar(positive=['sheldon','happy'], negative=['unhappy'])
print model.most_similar(positive=['sheldon','happy'], negative=['unhappy'])
print model.most_similar(positive=['sheldon','like'], negative=['not','dont'])
print model.most_similar(positive=['sheldon','love'])
print model.most_similar(positive=['sheldon','comics'])
print model_bi.most_similar(positive=['sheldon','comics'])
print model.most_similar(positive=['sheldon','toys'])
print model_bi.most_similar(positive=['sheldon'])"""

