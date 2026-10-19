import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	a = np.array(a)
	b = np.array(b)
	
	if a[1].shape != b.shape:
		return [-1]
	
	return (a@b).tolist()