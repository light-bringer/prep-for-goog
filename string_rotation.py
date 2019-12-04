from __future__ import print_function

'''
## Check if strings are rotations of each other or not


Given strings s1 and s2, you need to find if s2 is a rotated version of the string s1. The strings are lowercase.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each testcase contains two lines for s1 and s2.

Output:
For each testcase, in a new line, you need to print 1 if s2 is a rotated version of s1; else print 0.

Constraints:
1 <= T <= 103
1 <= |s1|, |s2| <= 107

Example:
Input:
4
geeksforgeeks
forgeeksgeeks
mightandmagic
andmagicmigth
mushroomkingdom
itsamemario
geekofgeeks
geeksgeekof

Output:
1
0
0
1

Explanation:
Testcase 1: s1 is geeksforgeeks, s2 is forgeeksgeeks. Clearly, s2 is a rotated version of s1 as s2 can be obtained by left-rotating s1 by 5 units.
'''

def find_rotation(s1, s2):
    double_string = s1+s1

    if len(s1)!=len(s2):
        return 0
    else:
        if double_string.count(s2) >= 1:
            return 1
        else:
            return 0


str1 = "m"
str2 = "m"
print(find_rotation(str1, str2))


test_cases = int(input())
for test_case in range(test_cases):
    first_string = str(input())
    second_string = str(input())
    print(find_rotation(first_string, second_string))