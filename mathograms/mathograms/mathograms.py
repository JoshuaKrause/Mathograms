'''
Mathograms by Joshua Krause (jkrause@joshuakrause.net)

This function solves mathograms supplied as strings.
Currently functions with 9-, 18-, and 27- digit variations.

Done as an exercise from reddit.com/r/dailyprogrammer/
'''


def mathogram(input):
    # Covert the mathogram into a nine-character list.
    m = unformat_mathogram(input)
    
    # Prune the list of available numbers.
    n = []
    for i in range(len(m)/9):
        n += ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for each in m:
        if each in n:
            n.remove(each)
    
    # Iterate through permutations of the available numbers
    # until the mathogram is solved.            
    for p in get_permutation(n):
        p_copy, m_copy = p[:], m[:]  
        for i in range(len(m_copy)):                      
            if not m_copy[i].isdigit():
                m_copy[i] = p_copy.pop(0)
        if test_mathogram(''.join(m_copy)):
            return reformat_mathogram(''.join(m_copy))

# Turn the mathogram into a nine character list.
def unformat_mathogram(input):        
    output = []
    for c in input:
        if c.isalnum():
            output.append(c)
    return output

# Reformat the mathogram for its final output.
def reformat_mathogram(input):
    a = split_mathogram(input)
    if len(input) == 9:
        return a[0] +' + '+ a[1] +' = '+ a[2]
    elif len(input) == 18:
        return a[0] +' + '+ a[1] +' + '+ a[2] +' + '+ a[3] +' = '+ a[4] +' + '+ a[5]
    elif len(input) == 27:
        return a[0] +' + '+ a[1] +' + '+ a[2] +' + '+ a[3] +' + '+ a[4] +' = '+ a[5] +' + '+ a[6] +' + '+ a[7] +' + '+ a[8]

# Returns a list of three-digit integers.
def split_mathogram(input):
    output = []
    for i in range(0, len(input), 3):
        output.append(input[i : i + 3])
    return output

# Generates permutations of the supplied list.
def get_permutation(input):
    if len(input) <= 1:
        yield input
    else:
        for i in range(len(input)):
            for p in get_permutation(input[:i] + input[i + 1:]):
                yield [input[i]] + p

# Confirm that the mathogram works.
def test_mathogram(input):
    output = False
    a = split_mathogram(input)
    if len(input) == 9:
        if int(a[0]) + int(a[1]) == int(a[2]):
            output = True
    if len(input) == 18:
        if int(a[0]) + int(a[1]) + int(a[2]) + int(a[3]) == int(a[4]) + int(a[5]):
            output = True
    elif len(input) == 27:
        if int(a[0]) + int(a[1]) + int(a[2]) + int(a[3]) + int(a[4]) == int(a[5]) + int(a[6]) + int(a[7]) + int(a[8]):
            output = True
    return output

m1 = '1xx + xxx = 468'
m2 = 'xxx + x81 = 9x4'
m3 = 'xxx + 5x1 = 86x'
m4 = 'xxx + 39x = x75'

n1 = 'xxx + xxx + 5x3 + 123 = xxx + 795'
n2 = 'xxx + xxx + 23x + 571 = xxx + x82'
n3 = 'xxx + xxx + xx7 + 212 = xxx + 889'
n4 = 'xxx + xxx + 1x6 + 142 = xxx + 553'

o1 = 'xxx + xxx + xxx + x29 + 821 = xxx + xxx + 8xx + 867'
o2 = 'xxx + xxx + xxx + 4x1 + 689 = xxx + xxx + x5x + 957'
o3 = 'xxx + xxx + xxx + 64x + 581 = xxx + xxx + xx2 + 623'
o4 = 'xxx + xxx + xxx + x81 + 759 = xxx + xxx + 8xx + 462'
o5 = 'xxx + xxx + xxx + 6x3 + 299 = xxx + xxx + x8x + 423'
o6 = 'xxx + xxx + xxx + 58x + 561 = xxx + xxx + xx7 + 993'



print mathogram(o3)
