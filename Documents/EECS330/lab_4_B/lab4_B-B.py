def OffByOne(char1, char2):
    if len(char1) != 1 or len(char2) != 1:
        return False
    diff = abs(ord(char1) - ord(char2))
    return diff == 1

char1 = 'b'
char2 = 'a'
print(OffByOne(char1, char2)) #print True
