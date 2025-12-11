user=input("Enter Amount From the list ==> [1$, 2$, 5$, 10$, 20$, 50$, 100$]:")

 
money={1:"GeorgeWashington",
2:"ThomasJefferson",
5:"AbrahamLincoln",
10:"AlexanderHamilton",
20:"AndrewJackson",
50:"UlyssesS.Grant",
100:"BenjaminFranklin"}
amount=int(cleaned)
if amount in money:

    print(money[amount])
else:
    print("WARNING$")