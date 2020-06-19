import numpy as np

G = np.array([
    [1,0,0,1,1,0,1],
    [0,1,0,0,1,1,1],
    [0,0,1,1,1,1,0]
])

m = np.array([0,1,0,0,1,1,0,0,1,1,0,1])
m = m.reshape((4,3))

final_result = []

for row in m:
    final_result.append(np.dot(row, G) % 2)

final_result = np.array(final_result)

print(final_result.flatten())
