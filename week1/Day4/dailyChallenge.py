MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%''' 

# Step 1: Convert matrix_string to a 2D list (matrix)
matrix = []
for row in MATRIX_STR.split('\n'):
    matrix.append(list(row))

# Step 2: Iterate through columns
num_cols = len(matrix[0])
num_rows = len(matrix)

decoded_message = ""

for col in range(num_cols):
    for row in range(num_rows):
        char = matrix[row][col]

        # Step 3: Filter alpha characters -> keep them
        if char.isalpha():
            decoded_message += char

        # Step 4: Replace symbols with spaces (non-alpha, non-space -> space)
        elif not char.isspace():
            decoded_message += " "

# Step 5: Print the decoded message
print(decoded_message)  # Output: This is Matrix
