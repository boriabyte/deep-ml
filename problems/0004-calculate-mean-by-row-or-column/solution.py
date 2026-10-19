def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	cols = len(matrix[0])
	rows = len(matrix)

	means = []
	m = 0
	s = 0

	if mode == "column":
		for i in range(cols):
			m = 0
			s = 0
			for j in range(rows):
				s+=matrix[j][i]
			m = s/rows
			means.append(m)
	elif mode == "row":
		for i in range(rows):
			m = 0
			s = 0
			for j in range(cols):
				s+=matrix[i][j]
			m = s/cols
			means.append(m)

	return means