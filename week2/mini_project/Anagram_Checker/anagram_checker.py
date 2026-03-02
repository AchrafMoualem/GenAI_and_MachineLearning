class AnagramChecker:
    def __init__(self, word):
        self.word = word
        with open('words.txt', 'r') as file:
            self.words = [w.lower() for w in file.read().splitlines()]
        
    def is_valid_word(self, word):
        return word.lower() in self.words

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        anagrams = []
        for w in self.words:
            if self.is_anagram(word, w):
                anagrams.append(w)
        return anagrams





