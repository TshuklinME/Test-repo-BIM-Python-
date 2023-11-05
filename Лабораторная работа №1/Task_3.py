list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

L = len(list_players)
A = round(L/2)

K1 = list_players[:A]
K2 = list_players[A:]

print(K1)
print(K2)
