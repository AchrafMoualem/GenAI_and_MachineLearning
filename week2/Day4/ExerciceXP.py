# Exercise 1: Random Sentence Generator
import random

file_path = 'words.txt'  # Path to the file containing words
def get_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def generate_sentence(lenght):
    sentence = []
    for _ in range(lenght):
        word = random.choice(get_words_from_file(file_path))
        sentence.append(word)
    return " ".join(sentence).lower() + "."

# Example usage
sentence_length = 5  # You can change this value to generate sentences of different lengths 
random_sentence = generate_sentence(sentence_length)
print(random_sentence)

def main():
    print("Welcome to the Random Sentence Generator! The purpose of this program is to generate a random sentence based on the words provided in the file.")
    
    try:
        sentence_length = int(input("Enter the desired length of the sentence: "))
    except ValueError:
        print("Invalid input. Please enter a positive integer between 2 and 20.")
        return

    if sentence_length < 2 or sentence_length > 20:
        print("Invalid input. Please enter a positive integer between 2 and 20.")
        return

    random_sentence = generate_sentence(sentence_length)
    print(f"Generated sentence with {sentence_length} words: {random_sentence}")

if __name__ == "__main__":    
    main()

# -------------------------------------------------------------------------------------------

# Exercise 2: Working with JSON
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Load the JSON string
data = json.loads(sampleJson)

# Access the nested “salary” key
salary = data["company"]["employee"]["payable"]["salary"]
print(f"Salary: {salary}")

# Add the “birth_date” key
data["company"]["employee"]["birth_date"] = "1990-01-01"

# Save the JSON to a file
with open('updated_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)

