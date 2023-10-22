def GetRightPosition(A,l,r,key):
	while r-l>1:
		m=l+(r-l)//2
		if A[m]<=key:
			l=m
		else:
			r=m
	return l
# Input: Indices Range (l ... r]
# Invariant: A[r] >= key and A[l] > key
def GetLeftPosition(A,l,r,key):
	while r-l>1:
		m=l+(r-l)//2
		if A[m]>=key:
			r=m
		else:
			l=m
	return r
def countOccurrences(A,size,key):
	#Observe boundary conditions
	left=GetLeftPosition(A,-1,size-1,key)
	right=GetRightPosition(A,0,size,key)
	# What if the element doesn't exists in the array?
	# The checks helps to trace that element exists

	if A[left]==key and key==A[right]:
		return right-left+1
	return 0
"""Code is written by Rajat Kumar"""
