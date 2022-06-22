def permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            return False
        return True

def permutation2(str1, str2):
    if len(str1) != len(str2):
        return False
    if len(str1) > 256 or len(str2) > 256:
        return False
    letters1 = [0] * 256
    letters2 = [0] * 256
    for i in str1:
        letters1[ord(i)] += 1
    for i in str2:
        letters2[ord(i)] += 1
    for i in range(0, 256):
        if letters1[i] != letters2[i]:
            return False
    return True

def isUnique(str1):
    if len(str1) == len(set(str1)):
        return True
    return False

def isUnique1(str1):
    for i in range(0, len(str1)):
        for j in range(i+1, len(str1)):
            if str1[i] == str1[j]:
                return False
    return True

def isUnique2(str1):
    if len(str1) > 256:
        return False
    letters = [0] * 256
    for i in str1:
        letters[ord(i)] += 1
    for i in range(0, 256):
        if letters[i] > 1:
            return False
    return True

if __name__ == '__main__':
    print(permutation("abc", "bca"))
    print(permutation("abc", "bbc"))
    print(permutation2("abc", "bca"))
    print(permutation2("abc", "bbc"))
    print(isUnique("abc"))
    print(isUnique("bbc"))
    print(isUnique1("abc"))
    print(isUnique1("bbc"))
    print(isUnique2("abc"))
    print(isUnique2("bbc"))

