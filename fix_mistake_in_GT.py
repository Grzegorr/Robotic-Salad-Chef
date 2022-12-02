import cv2
import numpy as np

name = "FinalSalad5_GTstates.npy"

GTstates = np.load(name)

print(GTstates.shape)
print(GTstates)

###Fixes here
### Remember indexing moved by 1
GTstates[112] = 7
GTstates[113] = 7
GTstates[114] = 7







np.save(name, GTstates)