def swap_case(s):
    modified=""
    for char in s:
        if char.islower():
            modified+=char.upper()
        elif char.isupper():
            modified+=char.lower()
        else:
            modified+=char
            
    return modified

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
