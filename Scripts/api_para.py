import json, urllib, csv
import nltk

def get_text(jobject):
	texts = []
	urls = []
	for talk in jobject['results']:
		if talk['url'] not in urls:
			#print talk['url']
			text = []
			for line in talk['collection1']:
				text.append(line['paragraph'].encode('ascii', 'ignore'))
			texts.append(text)
			urls.append(talk['url'])
	return texts, urls

# [[p1, p2, p3], []]
results = json.load(urllib.urlopen("https://www.kimonolabs.com/api/5m2wqe68?apikey=VP6IONzhcPRy5y0C3OVQ6o07Kp85v6vC&kimbypage=1"))
talks, urls = get_text(results)
pickle.dump(talks, open("talks_paragraphs.p", "wb"))
print talks[0]
print ("Number of talks = %d" % len(talks))

sent_tokenized = [[nltk.sent_tokenize(paragraph) for paragraph in talk] for talk in talks]	
print "Sentences are tokenized!"	
#[talks
#	[talk
#		[paragraph
#			[sentence  
#				[words] ] ] ] ] 

word_tokenized = [[[nltk.word_tokenize(sent) for sent in paragraph] for paragraph in talk] for talk in talks]
print "Words are tokenized! Pickling words..."
pickle.dump(word_tokenized, open( "words_paragraphs.p", "wb" ))
print word_tokenized[0]

print "POS tagging. This may take a while..."
tagged = [[[nltk.pos_tag(sent) for sent in paragraph] for paragraph in talk] for talk in word_tokenized]
pickle.dump(tagged, open("tagged_paragraphs.p", "wb"))
print "Done POS tagging!"
print tagged[0]
