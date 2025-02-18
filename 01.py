with open("input.txt","r") as f:
	j = f.readline().strip()
	s = f.readline().strip()

js = set(list(j))
r = sum(1 for l in s if l in js)

with open("output.txt","w") as f:
	f.write(str(r))