users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

S = {"Общее количество" : len(users), "Уникальные посещения" : 0}

S1 = set(users)
L = len(S1)

S["Уникальные посещения"] = L
print(S)
