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

m_key = np.array([(ord(letter) - 65 ) for letter in args.k]).reshape((2,2))

# Full credit to -----> @krshrimali
def multi_inverse(b, n):
    r1 = n
    r2 = b
    t1 = 0
    t2 = 1

    while(r1 > 0):
        q = int(r1/r2)
        r = r1 - q * r2
        r1 = r2
        r2 = r
        t = t1 - q * t2
        t1 = t2 
        t2 = t

        if(r1 == 1):
            inv_t = t1
            break

    return inv_t

def encode(message, key):
    msg = np.array([ord(letter) - 65 for letter in message]).reshape((3, 2))
    multiplication = np.dot(msg, key) % len(dictionary)

    result = multiplication.flatten()
    print(result)
    result_list = []

    for char in result[0]:
        result_list.append(char)

    # print('Key: {}'.format(key))
    # print(result)
    return ''.join([dictionary[num] for num in result])

def decode(message, key):
    key = np.matrix([[3,3], [2,5]])
    determinant = int(np.linalg.det(key))
    inv_key = np.linalg.inv(key) *  determinant 
    inv_key *= multi_inverse(determinant, 26)
    inv_key = inv_key % 26
    inv_key = inv_key.astype(int)
    return encode(message, inv_key)

if args.c:
    print(encode(args.message, m_key))
elif args.d:
    print(decode(args.message, m_key))
elif args.b:
    print('Still not implemented sorry bois')