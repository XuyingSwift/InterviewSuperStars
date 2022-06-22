# Interview Question 1.1, Alg to determine if a string has all unique characters

# Naive Solution
# Takes in a string and checks if it has all unique characters n^2
def unique(check_str):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {check_str}')  # Press Ctrl+F8 to toggle the breakpoint.
    for i in range(len(check_str)):
        for j in range(len(check_str)):
            if i != j:
                if check_str[i] == check_str[j]:
                    return False
    return True

def boolean(str):
    if len(str) > 128:
        return False
    char_set = [None] * 128
    for i in range(len(str)):
        val = str[i]
        if char_set[ord(val)]:
            return False
        char_set[ord(val)] = True

    return True

def permu1(str1,str2):
    if len(str1) != len(str2):
        return False
    char_set1 = [0] * 128
    char_set2 = [0] * 128
    for i in range(len(str1)):
        val1 = str1[i]
        val2 = str2[i]
        char_set1[ord(val1)] += 1
        char_set2[ord(val2)] += 1
    for i in range(len(char_set1)):
        if char_set1[i] != char_set2[i]:
            return False
    return True

def permu2(str1,str2):
    if len(str1) != len(str2):
        return False
    sorted1 = sorted(str1)
    print(sorted1)
    sorted2 = sorted(str2)
    print(sorted2)
    for i in range(len(sorted1)):
        if sorted1[i] != sorted2[i]:
            return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(unique('PyCharmy'))
    print(boolean('Pycharmy'))
    print(permu1('abc', 'bac'))
    print(permu2('abc', 'bac'))
    print(permu1('abc', 'aac'))
    print(permu2('abc', 'aac'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
