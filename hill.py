import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Caesar cipher Tema 7')


parser.add_argument('message', type=str, help="Message to operate")
parser.add_argument('-k', type=str, help='Key')
parser.add_argument('-c', action='store_true', help="Encode a string")
parser.add_argument('-d', action='store_true', help="Decode a string")
parser.add_argument('-b', action='store_true', help="Bruteforce")

dictionary = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

args = parser.parse_args()

key = np.array([(ord(letter) - 65 ) for letter in args.k]).reshape((2,2))

def encode(message, key):
    msg = np.array([ord(letter) - 65 for letter in message]).reshape((3,2))
    multiplication = np.dot(msg, key) % len(dictionary)
    result = multiplication.flatten()
    return ''.join([dictionary[num] for num in result])

result = encode(args.message, key)
print(result)
result = encode(result, key)
print(result)