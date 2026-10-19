import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	cols = len(a[0])
	rows = len(a)

	if (rows*cols) != (new_shape[0] * new_shape[1]):
		return []

	aux_list = []
	
	for i in range(rows):
		for j in range(cols):
			aux_list.append(a[i][j])

	k = 0
	l = 0

	shape1 = new_shape[0]
	shape2 = new_shape[1]

	new_row = []
	reshaped_matrix = []

	for i in range(len(aux_list)):
		new_row.append(aux_list[i])
		k+=1
		if(k == shape2):
			reshaped_matrix.append(new_row)
			k = 0
			new_row = []

	return reshaped_matrix