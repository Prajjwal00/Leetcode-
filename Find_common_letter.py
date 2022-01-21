class Solution(object):
	def commonChars(self, words):
		"""
		:type words: List[str]
		:rtype: List[str]
		"""
		final_list = []

		for letter in set(words[0]):
			cnt = []
			occurances = words[0].count(letter)
			for word in words:
				cnt.append(word.count(letter))
				if letter not in (word):
					break
			else:
				fnl = [letter]*min(cnt)
				final_list.extend(fnl)
		return final_list
