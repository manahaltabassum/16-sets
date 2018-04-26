def union(a,b):
	list1 = [x for x in a if x not in b]
	list2 = [x for x in a if x in b ]
	list3 = [x for x in b if x not in a]
	combined = list1 + list2 + list3
	print combined
	
union([1,2,3,5,6], [2,3,4])

def intersection(a,b):
	list2 = [x for x in a if x in b]
	print list2

intersection([1,2,3,5,6], [2,3,4])

def setdiff(a,b):
	list1 = [x for x in a if x not in b]
	print list1
	
setdiff([1,2,3,5,6], [2,3,4])

def symdiff(a,b):
	list1 = [x for x in a if x not in b]
	list3 = [x for x in b if x not in a]
	combined = list1 + list3
	print combined

symdiff([1,2,3,5,6], [2,3,4])

def cartesian(a,b):
	
	product = [ (var1, var2) for var1 in a for var2 in b]
	
	print product
	
cartesian([1,2], ["red", "white"])