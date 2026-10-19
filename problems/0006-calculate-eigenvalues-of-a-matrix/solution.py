import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
	eigenvalues = []

	rows = len(matrix)
	cols = len(matrix[0])

	trace = 0

	for i in range(rows):
		for j in range(cols):
			if i == j:
				trace+=matrix[i][j]

	det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1] 

	delta = trace**2 - 4*det

	solution1 = (trace + math.sqrt(delta))/2
	solution2 = (trace - math.sqrt(delta))/2

	eigenvalues.append(solution1)
	eigenvalues.append(solution2)

	return eigenvalues