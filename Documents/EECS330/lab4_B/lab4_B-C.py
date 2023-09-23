def OffByN(char1, char2, N):
    if len(char1) != 1 or len(char2) != 1:
        return False
    diff = abs(ord(char1) - ord(char2))
    return diff == N

char1 = 'b'
char2 = 'e'
N = 3
print(OffByN(char1, char2, N)) #Prints True