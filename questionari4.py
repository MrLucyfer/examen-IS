import numpy as np
import math

inpt = ''
side = input('Enter side of identity:')
matrix = []

while inpt != 's':
    inpt = input()
    if inpt == 's':
        break
    row = [int(num) for num in inpt]
    matrix.append(row)

# G = np.array([
#     [1,0,1],
#     [0,1,0],
#     [1,1,0],
#     [1,1,1],
#     [1,1,1]
# ])

G = np.matrix(matrix)

g = G.T

if side == 'left':
    identity = np.identity(g.shape[0])
    array = np.concatenate((g, identity), axis=1)
elif side == 'right':
    identity = np.identity(g.shape[0])
    array = np.concatenate((identity, g), axis=1)

n = g.shape[0] + g.shape[1]
k = g.shape[1]

num_info = k
bits_redundancia = n-k
num_paraules = 2**k
taxa_transmisio = math.log2(num_paraules)/n

print('INFOS:')
print('Array: \n{}'.format(array))
print('N: {}'.format(n))
print('K: {}'.format(k))
print('Nombre bits informacio: {}'.format(num_info))
print('Nombre de bits redundancia: {}'.format(bits_redundancia))
print('Nombre de paraules: {}'.format(num_paraules))
print('Taxa de transmisio: {}'.format(taxa_transmisio))