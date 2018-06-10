cats = False
d = False
a = 0
pee = " "
lizt = []
def adamsmom(a):
	global n
	try:
		exec(a)
	except:
			n = 1
def printer():
	global d
	global pee
	if d == False:
		pee = (''.join(s for s in lizt[i] if ord(s)>31 and ord(s)<126) + ";")
	if d == True:
		pee = (''.join(s for s in lizt[i] if ord(s)>31 and ord(s)<126))
	d = False
ele = input("path to file plzz: ")
with open(str(ele), 'r') as f:
	for line in f:
		adamsmom("lizt.append(line)")
aa = input("new text file for the shizz?: ")
aaa = open(str(aa), "w")
for i in range(0, len(lizt)):
	c = ''.join(s for s in lizt[i] if ord(s)>31 and ord(s)<126)
	if c == " ":
		d = True
	if not c:
		d = True
	if i < len(lizt):
		b = lizt[i] 
		b = list(b)
		for ii in range(0, len(b)):
			if b[ii] == "{" or b[ii] == "}" or b[ii] == "*":
				d = True
			if b[ii] == "e":
				adamsmom('if b[ii] + b[ii + 1] + b[ii + 2] + b[ii + 3] == "else": d = True')
		dads = lizt[i] 
		dad = dads.split(" ")
		for iii in range(0, len(dad)):
			if dad[iii] == "else" or dad[iii] == "if" or dad[iii] == "namespace" or dad[iii] == "class" or dad[iii] == "static":
				d = True		
	printer()
	print(pee)
	aaa.write(pee + '\n')
aaa.close()
