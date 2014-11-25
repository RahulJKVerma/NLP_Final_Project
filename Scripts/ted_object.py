import pickle


class ted(object):

	def __init__(self):
		pass

	def words_talk(self):
		return pickle.load('words_talks.p')

	def words_bag(self):
		'''list of str'''						# got it!
		return pickle.load('words_bag.p')

	def sents_talk(self):
		'''list of (list of str)'''				# got it!
		return pickle.load('sents_talks.p')

	def sents_bag(self):
		'''list of (list of str)'''				# got it!
		return pickle.load('sents_bag.p')

	def tagged_words_talk(self):
		'''list of (str,str) tuple'''			# got it!
		return pickle.load('tagged_words_talks.p')		

	def tagged_sents_talk(self):
		'''list of (list of (str,str))'''		# got it!
		return pickle.load('tagged_sents_talks.p')

	def tagged_paras(self):
		'''list of (list of (list of (str,str)))'''

	def chunked_sents(self):
		'''list of (Tree with (str,str) leaves)'''

	def parsed_sents(self):
		'''list of (Tree with str leaves)'''

	def parsed_paras(self):
		'''list of (list of (Tree with str leaves))'''

