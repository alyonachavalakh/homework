import sys
sumfor = sys.argv[0]
f = open(sumfor, 'r')
for line in reversed(list((f))):
	print(line)
f.close()