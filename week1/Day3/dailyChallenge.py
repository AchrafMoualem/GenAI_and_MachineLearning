# Challenge 1: Letter Index Dictionary
word = input("Enter a word: ")

letter_dict = {}

for index, letter in enumerate(word):
    if letter in letter_dict:
        letter_dict[letter].append(index)
    else:
        letter_dict[letter] = [index]

print(letter_dict)

# Challenge 2: Affordable Items
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# Clean the wallet
money = int(wallet.replace("$", "").replace(",", ""))

basket = []

for item, price in items_purchase.items():
    # Clean each price
    cost = int(price.replace("$", "").replace(",", ""))
    
    if cost <= money:
        basket.append(item)
        money -= cost

if basket == []:
    print("Nothing")
else:
    print(sorted(basket))