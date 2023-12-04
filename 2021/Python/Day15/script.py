# Iterative function to find the minimum cost to traverse from the
# first cell to the last cell of a matrix
def findMinCost(cost):

	# `M × N` matrix
	(M, N) = (len(cost), len(cost[0]))

	# `T[i][j]` maintains the minimum cost to reach cell (i, j) from cell (0, 0)
	T = [[0 for x in range(N)] for y in range(M)]

	# fill the matrix in a bottom-up manner
	for i in range(M):
		for j in range(N):
			T[i][j] = cost[i][j]

			# fill the first row (there is only one way to reach any cell in the
			# first row from its adjacent left cell)
			if i == 0 and j > 0:
				T[0][j] += T[0][j - 1]

			# fill the first column (there is only one way to reach any cell in
			# the first column from its adjacent top cell)
			elif j == 0 and i > 0:
				T[i][0] += T[i - 1][0]

			# fill the rest with the matrix (there are two ways to reach any
			# cell in the rest of the matrix, from its adjacent
			# left cell or adjacent top cell)
			elif i > 0 and j > 0:
				T[i][j] += min(T[i - 1][j], T[i][j - 1])

	# last cell of `T[][]` stores the minimum cost to reach destination cell
	# (M-1, N-1) from source cell (0, 0)
	return T[M - 1][N - 1]


if __name__ == '__main__':

	cost = [
		[4, 7, 8, 6, 4],
		[6, 7, 3, 9, 2],
		[3, 8, 1, 2, 4],
		[7, 1, 7, 3, 7],
		[2, 9, 8, 9, 3]
	]

	print("The minimum cost is", findMinCost(cost))
