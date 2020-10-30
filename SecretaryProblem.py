import random

def fisheryates(array, n):
	for i in range(n-1,0,-1):
		j = random.randint(0, i)
		array[i], array[j] = array[j], array[i]
	return array

def testSecretaryProblem(array, stopPercentage, numTests):
	n = len(array)
	numSuccesses = 0
	averageRank = 0
	worstRank = 1
	for i in range(numTests):
		fisheryates(array, n)
		bestSeen = n + 1
		best = 0
		for j in range(n):
			if array[j] < bestSeen:
				bestSeen = array[j]
				if j > n*stopPercentage:
					best = bestSeen
					break
			if j == n-1:
					best = array[j]
		if best == 1:
			numSuccesses += 1
		if best > worstRank:
			worstRank = best
		averageRank += best

	averageRank /= numTests
	probabilitySuccess = numSuccesses/numTests
	return [probabilitySuccess, averageRank, worstRank]


stopPercentage = 0.37
numTests = 100

array10 = []
array1000 = []
array10000 = []

array100 = [i+1 for i in range(100)]
array1000 = [i+1 for i in range(1000)]
array10000 = [i+1 for i in range(10000)]

test1 = testSecretaryProblem(array100, stopPercentage, numTests)
test2 = testSecretaryProblem(array1000, stopPercentage, numTests)
test3 = testSecretaryProblem(array10000, stopPercentage, numTests)

print(f"For n=100 \nProbability of success: {test1[0]}\nAverage rank: {test1[1]}\nWorst rank: {test1[2]}\n")
print(f"For n=1000 \nProbability of success: {test2[0]}\nAverage rank: {test2[1]}\nWorst rank: {test2[2]}\n")
print(f"For n=10000 \nProbability of success: {test3[0]}\nAverage rank: {test3[1]}\nWorst rank: {test3[2]}\n")

