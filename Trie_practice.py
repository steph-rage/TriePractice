wordlist = []
#with open('/usr/share/dict/cracklib-small') as dictionary:
 #   for line in dictionary:
  #      wordlist.append(line.strip()

trie = {}
wordlist_test = ["Amy", "Annie", "Ann", "Amanda", "Robert", "Rodney", "Shelley", "Susan"]



def add_word_to_trie(word, trie):
	word = word.lower()
	current_level = trie
	last_letter = word[len(word)-1]
	for letter in word:
		if letter in current_level:
			current_level = current_level[letter]
		else:
			current_level[letter] = {}
			current_level = current_level[letter]
	current_level['end'] = 'end'

def is_member_of_trie(word, trie):
	word = word.lower()
	current_level = trie
	member = False
	last_letter = word[len(word)-1]
	for letter in word:
		if letter in current_level:
			current_level = current_level[letter]
			if letter == last_letter:
				if 'end' in current_level:
					member = True
	return member

print("These words should all be in the trie: ")

for word in wordlist_test:
	add_word_to_trie(word, trie)
	print(word)

for _ in range(5):
	test = input("Pick a word to see if it is a member of the trie: ")
	print(is_member_of_trie(test, trie))
