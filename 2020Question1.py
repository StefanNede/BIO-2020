# numerals = {'I': 1, 'IV': 4, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def getNumeral(num, res):
    if num == 0:
        return res
    if num >= 1000:
        res += 'M'
        return getNumeral(num - 1000, res)
    if num >= 500:
        res += 'D'
        return getNumeral(num - 500, res)
    if num >= 100:
        res += 'C'
        return getNumeral(num - 100, res)
    if num >= 50:
        res += 'L'
        return getNumeral(num - 50, res)
    if num >= 10:
        res += 'X'
        return getNumeral(num - 10, res)
    if num >= 5:
        res += 'V'
        return getNumeral(num - 5, res)
    if num >= 4:
        res += 'IV'
        return getNumeral(num-4, res)
    if num >= 1:
        res += 'I'
        return getNumeral(num - 1, res)
    

def lookAndSay(rn):
    res = ''
    previous = rn[0]
    count = 1
    if len(rn) == 1:
        res = 'I' + rn[0]
    for i in range(1, len(rn)):
        if rn[i] == previous:
            count += 1
        if rn[i] != previous:
            res += getNumeral(count, '') + previous
            count = 1
            previous = rn[i]
        if i == len(rn)-1 and rn[i] != previous:
            res += 'I' + rn[i]
        if i == len(rn)-1 and rn[i] == previous:
            res += getNumeral(count, '') + previous
    return res

def q1():
    inp = input().split(' ')
    rn, n = inp[0], int(inp[1])

    for i in range(n):
        rn = lookAndSay(rn)
    # print(rn)
    return rn.count('I'), rn.count('V')

q11, q12 = q1()
print(q11, q12)