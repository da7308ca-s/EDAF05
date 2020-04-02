N = int(input())
men = [None]*N
women = [None]*N
numbers = []

"""
#Tänkte skriva om utan att lägga till allt i en lista som ett mellansteg
while n_numbers<2*N*(N+1):
	for x in input().split():
		if n_numbers%(N+1)==0
			index = int(x) 
			c = 1
			temp = [None]*(N+1)
		if c<N+1:
			temp[c] = int(x)

		n_numbers+=1
"""

#Store all the input numbers in a list
while len(numbers)<2*N*(N+1):
	for x in input().split():
		numbers.append(int(x))

# Loop over all the numbers and create men and women lists with following structure
# man: [index, first_choice, second_choice, ...]
# woman: [reference to current man/ None if single, rating_of_man1, rating_of_man2, ....]

for i in range(2*N):
	index = numbers[i*(N+1)]-1
	temp = numbers[i*(N+1):i*(N+1)+N+1]
	if women[index] == None:
		temp2 = [None]*(N+1)
		#Swap from preference list to rating list
		for j, t in enumerate(temp):
			temp2[t] = j
		women[index] = temp2
	else:
		men[index] = temp

def prefers_new_partner(w,m_old,m_new):
	return w[m_new] < w[m_old]

#Helper method for debugging
def print_lists():
	print("Men")
	for m in men:
		print(m)
	print("Women")
	for w in women:
		print(w)

while len(men) is not 0:
	m = men.pop(0) #Next man to propose
	w = women[m.pop(1)-1] #His first choice
	current_partner = w[0] #Her current partner, None if single
	if not current_partner: #If shes free they create a pair
		w[0] = m 
	elif prefers_new_partner(w,current_partner[0],m[0]): #If shes not free but prefers the new guy, swap and put the previous guy back in the queue
		w[0] = m
		men.append(current_partner)
	else: #If she prefers her current partner nothing happens except the current proposing man cant propose to the same woman again
		men.append(m)

#Print the results
for w in women:
	print(w[0][0])


