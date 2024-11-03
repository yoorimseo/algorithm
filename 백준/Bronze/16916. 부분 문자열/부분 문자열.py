import sys
input = sys.stdin.readline

def kmp(pat, text):
    table = make_table(pat)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pat[j]:
            j = table[j - 1]

        if text[i] == pat[j]:
            if j == len(pat) - 1:
                return True
            else:
                j += 1
    return False

def make_table(pat):
    table = [0 for _ in range(len(pat))]
    j = 0
    for i in range(1, len(pat)):
        while j > 0 and pat[i] != pat[j]:
            j = table[j - 1]

        if pat[i] == pat[j]:
            j += 1
            table[i] = j
    return table


text = input().rstrip()
pat = input().rstrip()

print(1) if kmp(pat, text) else print(0)