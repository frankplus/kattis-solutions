s = input()
while s != ".":
    i = 0
    j = 1
    while j < len(s):
        if s[i] == s[j]:
            i += 1
            j += 1
        elif i == 0:
            j += 1
        else:
            i = 0
    res = len(s)//(len(s) - i) if len(s)%(len(s) - i) == 0 else 1
    print(res)
    s = input()

""" Bruteforce solution
s = input()
while s != ".":
    #print("string: "+s)
    for i in range(len(s)):
        if len(s) % (i+1) == 0:
            found = False
            for j in range(len(s)):
                    if s[j%(i+1)] != s[j]:
                        break
                    if j == len(s)-1:
                        found = True
            if found:
                print(len(s) // (i+1))
                break

    s = input()
"""