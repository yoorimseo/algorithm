import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    commands = sys.stdin.readline().split()

    if len(commands) == 1:
        if commands[0] == "all":
            S = set(list(range(1, 21)))
        else:
            S = set()
    
    else:
        command, num = commands[0], int(commands[1])
        
        if command == "add":
            S.add(num)
        elif command == "remove":
            S.discard(num)
        elif command == "check":
            print(1 if num in S else 0)
        elif command == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)