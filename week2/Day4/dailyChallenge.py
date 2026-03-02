# Part I: Analyzing a Simple String

import re
import string


class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self):
        words = self.text.split()
        frequency = {}
        for word in words:
            word = word.lower().strip('.,!?";()')  # Remove punctuation and convert to lowercase
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        return frequency
    
    def most_common_word(self):
        frequency = self.word_frequency()
        most_common = max(frequency, key=frequency.get)
        return most_common, frequency[most_common]
    
    def unique_words(self):
        frequency = self.word_frequency()
        unique = [word for word, count in frequency.items() if count == 1]
        return unique
    
# Part II: Analyzing Text from a File

def from_file(self, file_path):
    with open(file_path, 'r') as file:
        self.text = file.read()
    return Text(self.text)
    

class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)

    def remove_punctuation(self):
        punctuation = string.punctuation
        self.text = ''.join(char for char in self.text if char not in punctuation)
        return self.text
    
    def remove_stop_words(self, stop_words):
        words = self.text.split()
        self.text = ' '.join(word for word in words if word.lower() not in stop_words)
        return self.text
    
    def remove_special_characters(self):
        self.text = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return self.text
    
def main():
    text = Text("Hello world! Hello everyone. Welcome to the world of Python programming.")
    print("Word Frequency:", text.word_frequency())
    print("Most Common Word:", text.most_common_word())
    print("Unique Words:", text.unique_words())
    text_modification = TextModification(text.text)
    print("Text without punctuation:", text_modification.remove_punctuation())
    stop_words = ['the', 'is', 'in', 'and', 'to', 'of']
    print("Text without stop words:", text_modification.remove_stop_words(stop_words))
    print("Text without special characters:", text_modification.remove_special_characters())

        
if __name__ == "__main__":    
    main()       