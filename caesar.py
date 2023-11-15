# The Caesar cipher, also known as the Caesar shift or Caesar's code, is one of the simplest and oldest methods of encryption in the field of cryptography. It is a type of substitution cipher in which each letter in the plaintext is shifted a fixed number of positions down or up the alphabet. This shift is called the "key" or "shift value." The method is named after Julius Caesar, who is historically believed to have used it for confidential communication.

# Here's how the Caesar cipher works:

# Choose a shift value, often denoted as "k."
# Take the plaintext message and replace each letter with the letter that appears k positions down the alphabet. If you reach the end of the alphabet, you wrap around to the beginning.
# Keep the case (uppercase or lowercase) of the letters the same.
# Non-alphabet characters (such as spaces, numbers, and punctuation) are typically left unchanged.
# Here's an example with a Caesar cipher using a shift value of 3:

# Plaintext: "HELLO"
# Encryption with a Caesar cipher (shift value of 3): "KHOOR"
# To decrypt the message, you would simply reverse the process:

# Ciphertext: "KHOOR"
# Decryption with a Caesar cipher (shift value of 3): "HELLO"

ciphertext = "WX]_N[b\][9WPL[bY]X"
plaintexts = []

# Iterate through all possible shift lengths from 1 to 127
for shift_len in range(1, 128):
    plaintext = ""
    
    for ch in ciphertext:
        # Shift each character by shift_len, modulo 128 to avoid overflow
        pt = chr((ord(ch) + shift_len) % 128)  
        plaintext += pt
    
    # Store the shift length and corresponding plaintext
    plaintexts.append((shift_len, plaintext))

# Print all possible plaintexts
for shift_len, plaintext in plaintexts:
    print(f"Shift Length {shift_len}: {plaintext}")



cipher = ""

for pt in plaintext:
    ct = chr((ord(pt)-shift_len)%128) #shift each character back to encrypt
    cipher += ct

print("ciphertext:", cipher)




