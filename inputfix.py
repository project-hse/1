coords = []
fin = open("input_big.txt", "r")
line = fin.readline()
line = fin.readline()
while line:
	s = line.split('\t')
	coords.append([s[4], float(s[5]), float(s[6])])
	line = fin.readline()
fin.close()
