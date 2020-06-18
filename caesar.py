import argparse
import sys

parser = argparse.ArgumentParser(description='Caesar cipher Tema 7')


parser.add_argument('message', type=str, help="Message to operate")
parser.add_argument('-k', type=int, help='Key')
parser.add_argument('-c', action='store_true', help="Encode a string")
parser.add_argument('-d', action='store_true', help="Decode a string")
parser.add_argument('-b', action='store_true', help="Bruteforce")

dictionary = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

args = parser.parse_args()

def encode(message, key):
    encoded = ''
    for letter in message:
        char = ((ord(letter) - 65) + key) % len(dictionary)
        encoded += dictionary[char]    
    return encoded

def decode(message, key):
    decoded = ''
    for letter in message:
        char = ((ord(letter) - 65) - key) % len(dictionary)
        decoded += dictionary[char]
    return decoded

def bruteforce(message):
    messages = []
    for i in range(26):
        decoded = ''
        for letter in message:
            char = ((ord(letter) - 65) - i) % len(dictionary)
            decoded += dictionary[char]
        messages.append(decoded)
    return messages
    
if args.c:
    print(encode(args.message, args.k))
    
elif args.d:
    print(decode(args.message, args.k))
elif args.b:
    messages = bruteforce(args.message)
    for i, message in enumerate(messages):
        print('{} - {}'.format(i, message))
