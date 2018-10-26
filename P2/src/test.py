import math

def test1(x):

	a = []
	b = []

	for i in xrange(0,5):
		a.append(x[i])
	for j in xrange(5, len(x)):
		b.append(x[j])

	c = [a,b]
	return c

def entropy(x):
	one_count = 0
	two_count = 0
	three_count = 0
	four_count = 0

	for i in xrange(0, len(x)):
		if x[i] == 1:
			one_count = one_count + 1
		if x[i] == 2:
			two_count = two_count + 1
		if x[i] == 3:
			three_count = three_count + 1
		if x[i] == 4:
			four_count = four_count + 1


	one_count = float(one_count)/(len(x))
	two_count = float(two_count)/(len(x))
	three_count = float(three_count)/(len(x))
	four_count = float(four_count)/(len(x))


	if one_count == 0:
		one_count = 1
	if two_count == 0:
		two_count =1
	if three_count == 0:
		three_count =1
	if four_count == 0:
		four_count =1 


	entropy = (-1)*one_count*(math.log(one_count)/math.log(2)) + (-1)*two_count*(math.log(two_count)/math.log(2)) + (-1)*three_count*(math.log(three_count)/math.log(2)) + (-1)*four_count*(math.log(four_count)/math.log(2))
	return entropy

x = [1,1,2,2,3,3,3,4]
xL = test1(x)[0]
xR = test1(x)[1]

c1 = float(len(xL))/len(x)
c2 = float(len(xR))/len(x)


ent = entropy(x)
Lentropy = entropy(xL)
Rentropy = entropy(xR)

conditional_entropy = c1*Lentropy + c2*Rentropy


print x
print xL
print xR
print "entropy: ", ent
print "conditional entropy: ", conditional_entropy 
print "information gain: ", (ent - conditional_entropy)




