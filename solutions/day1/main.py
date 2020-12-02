#! /usr/bin/env python3

def readData():
	dataFile = open("data.txt", "r")
	data=[]
	for line in dataFile:
		if not line:
			break
		data.append(int(line.strip()))

	data.sort()
	# Return a list of integers from the file
	return data

def productOfMatchingPair(data, key):
	start = 0
	end = len(data) - 1
	while(start < end):
		sum = data[start] + data[end]
		if(sum < key):
			start = start + 1
		if(sum > key):
			end = end - 1
		if(sum == key):
			return data[start] * data[end]

def main():
	data = readData()
	result = productOfMatchingPair(data,2020)
	print(result)

if __name__ == "__main__":
    main()