from anagram_checker import AnagramChecker

def main():
    word = input("Enter a word to find its anagrams: ")
    checker = AnagramChecker(word)
    
    if not checker.is_valid_word(word):
        print(f"'{word}' is not a valid word.")
        return
    
    anagrams = checker.get_anagrams(word)
    
    if anagrams:
        print(f"Anagrams of '{word}': {', '.join(anagrams)}")
    else:
        print(f"No anagrams found for '{word}'.")

if __name__ == "__main__":
    main()