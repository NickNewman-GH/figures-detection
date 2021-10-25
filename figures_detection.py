import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from scipy.ndimage import morphology
import pickle

image = pickle.load(open("./imgs/ps.bin", "rb"))
image_copy = np.copy(image)
labeled = label(image)
print('Total figures in the picture -', np.max(labeled))

mask1 = np.array([
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
])

mask2 = np.array([
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,0,0,1,1],
    [1,1,0,0,1,1]
])

r = {}

print('Base mask:')
for line in mask2:
    print(line)

result = morphology.binary_opening(image, mask1)

labeled = label(result)

r['Rectangles'] = np.max(labeled)
image -= result

val = ['Base mask', 'BM rotated 90deg', 'BM rotated 180deg', 'BM rotated 270deg']
for i in range(4):
    result = morphology.binary_opening(image, mask2)
    labeled = label(result)
    r[val[i]] = np.max(labeled)
    mask2 = np.rot90(mask2)

print(r)
