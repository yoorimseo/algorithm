N, game = input().split()
minigame = {'Y': 1, 'F': 2, 'O': 3}
people = set()
for _ in range(int(N)):
    people.add(input())

res = len(people) // minigame[game]

print(res)