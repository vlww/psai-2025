import numpy as np

IMAGE = np.array([
    [1, 2, 1, 0, 1],
    [0, 1, 3, 2, 1],
    [1, 2, 4, 1, 0],
    [0, 1, 2, 3, 1],
    [1, 0, 1, 2, 2],
])

DETECTOR = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

new_thing = np.zeros((3,3))
for i in range(3):
    for j in range(3):
        image_segment = IMAGE[i:i+3, j:j+3]
        d = np.dot(image_segment.flatten(), DETECTOR.flatten())
        new_thing[i, j] = d

print(new_thing)
