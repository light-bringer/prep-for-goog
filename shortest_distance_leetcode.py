'''
Shortest Distance to Character

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

'''

def shortest_distance(string, char):
    char_locations = [i for i, c in enumerate(string) if c==char]
    print(char_locations)

    result = []

    for idx, _ in enumerate(string):
        result.append((_, min(map(lambda x : abs(idx-x), char_locations))))
    
    return result

def shortest_distance_optimized(string, char):
    print("start")
    n = len(string)
    out = [n]*n
    print(out)
    i, l, r = 0, -n, 2*n
    print(i, l, r)
    
    while i < n:
        j = n - 1 - i
        print(j)
        if string[i] == char:
            l = i
            out[i] = 0
            print("here 1")
            print(l, out[i])
        else:
            out[i] = min(out[i], i - l)
            print("here 2")
            print(l, out[i])
        if string[j] == char:
            r = j
            out[j] = 0
            print("here 3")
            print(l, r, out[i])
        else:
            out[j] = min(out[j], r - j)
            print("here 4")
            print(l,r, out[i])
        
        i += 1

        print(out) 
        print("#################")
    return out



print(shortest_distance('geeksforgeeks', 'e'))
shortest_distance_optimized('geeks', 'e')