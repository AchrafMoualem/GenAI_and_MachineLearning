class AnagramChecker:
    def __init__(self, word_file='words.txt'):
        with open(word_file, 'r') as file:
            self.words = [w.lower() for w in file.read().splitlines()]
        
    def is_valid_word(self, word):
        return word.lower() in self.words

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        word_lower = word.lower()
        anagrams = []
        for w in self.words:
            if w != word_lower and self.is_anagram(word_lower, w):
                anagrams.append(w)
        return anagrams

