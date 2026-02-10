import numpy as np
arr = np.arange(24)
reshaped = arr.reshape(4, 3, 2)
transposed = reshaped.transpose(0, 2, 1)
print("Final shape:", transposed.shape)
print(transposed)
