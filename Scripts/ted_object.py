import pickle


class ted(object):

	def __init__(self):
		pass
	def dummy_function(self):
		print "I am a dummy"

	def words_talk(self):
		return pickle.load(open('../Corpus/words_talks.p', 'rb'))

	def words_bag(self):
		'''list of str'''						# got it!
		return pickle.load(open('../Corpus/words_bag.p', 'rb'))

	def sents_talk(self):
		'''list of (list of str)'''				# got it!
		return pickle.load(open('../Corpus/sents_talks.p', 'rb'))

	def sents_bag(self):
		'''list of (list of str)'''				# got it!
		return pickle.load(open('../Corpus/sents_bag.p', 'rb'))

	def tagged_words_talk(self):
		'''list of (str,str) tuple'''			# got it!
		return pickle.load(open('../Corpus/tagged_words_talks.p', 'rb'))		

	def tagged_sents_talk(self):
		'''list of (list of (str,str))'''		# got it!
		return pickle.load(open('../Corpus/tagged_sents_talks.p', 'rb'))

	def tagged_paras(self):
		'''list of (list of (list of (str,str)))'''

	def chunked_sents(self):
		'''list of (Tree with (str,str) leaves)'''

	def parsed_sents(self):
		'''list of (Tree with str leaves)'''

	def parsed_paras(self):
		'''list of (list of (Tree with str leaves))'''

