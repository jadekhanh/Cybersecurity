# plaintext = "BOSTONUNIVERSITYSUPERSECRETTEXT"

# key = "EC521"

# ciphertext = "" # cipher text = encrypted text

## Encryption: xor each letter of the plaintext with the corresponding ciphertext letter
# for pos in range(len(plaintext)):
#  	ciphertext += chr(ord(plaintext[pos])^ord(key[pos%len(key)]))

# print("cipher text:", ciphertext)

# plaintext2 = ""  # = decrpypted/true text

## Decryption: do the same as encryption
# ciphertext = "(=7$5SE8*813:##*<G"
# key = "kontact"
# for pos in range(len(ciphertext)):
#  	plaintext2 += chr(ord(ciphertext[pos])^ord(key[pos%len(key)]))

# print("plain text 2:", plaintext2)
 	
## Plaintext attack: by knowing part of the plaintext, we can recover the key
# pt = "BOSTONUNIVERSITY"

# recoveredkey = ""

# for pos in range(len(ciphertext)):
#  	recoveredkey += chr(ord(ciphertext[pos])^ord(pt[pos%len(pt)]))

# print("recovered key:", recoveredkey)

###############################################################################

First 6 bytes of the zip file is 504B03041400, 
XOR it with the cipher text to get the key
first_6_bytes = bytes.fromhex("0A1257485539")   # Convert hex string to bytes
header = bytes.fromhex("504B03041400")          # Convert hex string to bytes
key = bytes()

for pos in range(len(first_6_bytes)):
    key += bytes([first_6_bytes[pos] ^ header[pos % len(header)]])

print("recovered key:", key)
print("Length of recoveredkey:", len(key))

file_path = "challenge3"
  
decrypted_contents = b''

# Create a file named "results.zip" and save the decrypted content
output_filename = "results.zip"

pos = 0
file = open(file_path, "rb")
with open(output_filename, "wb") as results_file:
    while True:
        ciphertext = file.read(1) # read character 1 by 1
        if not ciphertext:
            break
        text = bytes(chr((ord(ciphertext)^key[pos%len(key)])),"latin-1")
        results_file.write(text)
        pos +=1
        
print("Decrypted content saved to 'results.zip' file")


