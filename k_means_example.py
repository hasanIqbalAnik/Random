from __future__ import division
import math

def euclid_dist(x1, y1, x2, y2):
	fsq = math.pow((x1-x2),2) #first squared
	ssq = math.pow((y1-y2), 2) # second squared
	return math.sqrt(fsq + ssq)

X = [1, 3, 5, 7, 9, 11, 13, 15, 17, 1, 3, 5, 7, 9, 11, 13, 15, 17]
Y = [0, 0, 0, 0, 0,  0,  0,  0,  0, 3, 3, 3, 3, 3, 3,  3,  3,  3]
err = .005 #stopping criteria
#initial cluster center 1
cx1 = 9 
cy1 = 3
#initial cluster center 2
cx2 = 11
cy2 = 3

while(True):
	new_assignment1 = []
	new_assignment2 = []

	for xi, yi in zip(X, Y):
		if(euclid_dist(xi, yi, cx1, cy1) <= euclid_dist(xi, yi, cx2, cy2)): #whichever cluster center is near
			new_assignment1.append([xi, yi])
		else:
			new_assignment2.append([xi, yi])		


	sumx1, sumy1, sumx2, sumy2, count1, count2 = 0, 0, 0, 0, 0, 0
	for item in new_assignment1:
		sumx1 = sumx1 + item[0]
		sumy1 = sumy1 + item[1]
		count1 = count1 + 1

	for item in new_assignment2:
		sumx2 = sumx2 + item[0]
		sumy2 = sumy2 + item[1]
		count2 = count2 + 1

	if(abs((sumx1 / count1) - cx1) <= err): 
		break
	else:	
		cx1 = sumx1 / count1
		cy1 = sumy1 / count1

		cx2 = sumx2 / count2
		cy2 = sumy2 / count2

		print new_assignment1
		print new_assignment2

		print cx1, cy1
		print cx2, cy2
