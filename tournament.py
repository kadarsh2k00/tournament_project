def round1(teams):
    if teams >= 24:
        no_of_groups = 8
    else:
        no_of_groups = 4

    temp = teams//no_of_groups
    rem = teams%no_of_groups

    # Number of teams in each group
    group_list = [temp]*no_of_groups

    for i in range(rem):
        group_list[i] += 1

    round1_sum = 0
    for i in range(len(group_list)):
        x = group_list[i]
        round1_sum += (x*(x-1))//2

    return round2(2*len(group_list)) + round1_sum
	
def round2(teams):
	if teams == 16:
		# The top two teams will be picked from each group
		# After that tournament structure will be as follow
		#1. ROUND OF 16
		#2. QUARTER FINAL
		#3. SEMI FINAL
		#4. FINAL
		return 8 + 4 + 2 + 1
	else:
		# The top two teams will be picked from each group
		# After that tournament structure will be as follow
		#1. QUARTER FINAL
		#2. SEMI FINAL
		#3. FINAL
		return  4 + 2 + 1
		
N = int(input("Enter Number of teams: "))
if N <= 4:
    # One on One matches
    # If number of teams > 2, A final between top two teams
    if N==2:
        print(1)
    if N==3:
        print(4)
    if N==4:
        print(7)
else:
    matches = round1(N)
    print(matches)
