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
    msg = np.array([ord(letter) - 65 for letter in message]).reshape((2, 3))
    multiplication = np.dot(key, msg) % len(dictionary)
    result = multiplication.flatten()
    # print('Key: {}'.format(key))
    # print(result)
    return ''.join([dictionary[num] for num in result])

def decode(message, key):
    inv_key = np.asmatrix(key)
    inv_key = inv_key.H
    det = np.linalg.det(key)
    inv_key = inv_key / det
    print(inv_key)
    return encode(message, key)

if args.c:
    print(encode(args.message, key))
elif args.d:
    print(decode(args.message, key))
elif args.b:
    print('Still not implemented sorry bois')