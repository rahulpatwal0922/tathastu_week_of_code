p1_runs = int(input("Enter runs scored by player 1 in 60 balls"))
p2_runs = int(input("Enter runs scored by player 2 in 60 balls"))
p3_runs = int(input("Enter runs scored by player 3 in 60 balls"))
S_rate1 = (p1_runs*100)/60
S_rate2 = (p2_runs*100)/60
S_rate3 = (p3_runs*100)/60
print("Strike rate of player 1 is ",S_rate1)
print("Strike rate of player 2 is ",S_rate2)
print("Strike rate of player 3 is ",S_rate3)
print("Runs scored by player 1 if he plays 60 more balls is {} runs".format(p1_runs*2))
print("Runs scored by player 2 if he plays 60 more balls is {} runs".format(p2_runs*2))
print("Runs scored by player 3 if he plays 60 more balls is {} runs".format(p3_runs*2))
print("Max sixes hitted by player 1 is",p1_runs//6)
print("Max sixes hitted by player 2 is",p2_runs//6)
print("Max sixes hitted by player 3 is",p3_runs//6)
