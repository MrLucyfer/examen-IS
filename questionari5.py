import numpy as np

G = np.array([
        [1,0,0,1,1,0,1],
        [0,1,0,0,1,1,1],
        [0,0,1,1,1,1,0]
    ])

def codificar():

    m = np.array([0,1,0,0,1,1,0,0,1,1,0,1])
    m = m.reshape((4,3))

    final_result = []

    for row in m:
        final_result.append(np.dot(row, G) % 2)

    final_result = np.array(final_result)

    print(final_result.flatten())


def decodifica():

    x = np.array([
        [1,1,0,1],
        [0,1,1,1],
        [1,1,1,0]
    ])

    x_trans = x.T

    identity = np.identity(x_trans.shape[0])

    control = np.concatenate((x_trans, identity), axis=1)
    syndrome = control.T
    print('Syndrome: \n{}'.format(syndrome))

    string = '110101011001111110100'

    cadena = np.array([int(num) for num in string]) 
    #print(cadena.shape)
    cadena = cadena.reshape((3,7))
    print('Cadena: \n{}'.format(cadena))

    error = np.identity(control.T.shape[0])
    print('Error: \n{}'.format(error))

    Hw = np.dot(cadena, syndrome) % 2
    print('H(w)\n{}'.format(Hw))

    indeces = []
    indeces.append(error[0])

    final_result = []
    associada = []
    print("Correcting errors:")
    for i in range(len(indeces)):
        final_result.append(abs(cadena[i+1] - indeces[i] % 2))
        associada.append((abs(cadena[i+1] - indeces[i]) % 2)[:3])
    
    final_result = np.array(final_result).flatten()
    associada = np.array(associada).flatten()
    print(final_result)
    print(associada)

    
decodifica()