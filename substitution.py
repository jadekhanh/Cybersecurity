import string
import random

#You need a long text to make sure that the statistical distribution of letters 
# in the English language is respected
with open("challenge2.txt", "r") as file:
    ciphertext = file.read()
print(ciphertext)

frequencies = {}

for letter in ciphertext:
    if letter not in frequencies:
        frequencies[letter] = 1
    else:
        frequencies[letter] += 1

print("frequencies:", frequencies)

# Most frequently appeared character in the plaintext (most to least):
# S = 233, B = 160, N = 156, D = 155, M = 149, G = 138, W = 137, E = 120, 
# Z = 116, K = 110, F = 84, X = 65, I = 48, Y = 47, O = 46, A = 44, U = 43, 
# H = 37, P = 36, C = 28, L = 24, Q = 16, V = 3, R = T = 2,

# Most frequently appeared letters (most to least): 
# https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
# E, T, (A, I, N, O, S), H, R, D, L, U, (C, M), F, (W, Y), (G, P), B, V, K, 
# Q, (J, X), Z

# Create a dictionary for character substitution
substitution = {
    'S': 'E',
    'B': 'T',
    'N': 'A',
    'D': 'O',
    'M': 'S',
    'G': 'R',
    'W': 'N',
    'E': 'H',
    'Z': 'I',
    'K': 'D',
    'F': 'L',
    'X': 'U',
    'I': 'W',
    # 'T': 'M',
    'U': 'F',
    'A': 'G',
    'C': 'K',
    'L': 'B',   
    'O': 'P',   
    # 'P': 'F',
    # 'J': 'X',
    'Q': 'V',
    'H': 'M',  
    'V': 'Q',
    # 'R': 'L',
    'Y': 'Y',
    ' ': ' ',
    ',': ',',
    '.': '.',
    ';': ';',
    "'": "'",
    '"': '"',
    '-': '-',
    '?': '?'
}

# Create a separate dictionary for random mappings for unknown characters
random_mapping = {}
alphabet = string.ascii_uppercase

for char in alphabet:
    if char not in substitution.values() and char not in random_mapping.values():   # pick a character A not from substitution & random_mapping
        unused_chars = [c for c in alphabet if c not in random_mapping]             # list of unused characters
        random_char = random.choice(unused_chars)                                   # pick a character B from the list of unused characters
        random_mapping[char] = random_char                                          # map A to B  & make sure that A is not mapped again

# Decrypt the ciphertext using the substitution and random mapping
decrypted_content = ""
for letter in ciphertext:
    if letter in substitution:
        decrypted_content += substitution[letter]
    elif letter in random_mapping:
        decrypted_content += random_mapping[letter]

# Print the result
print()
print("Decrypted content:", decrypted_content)
