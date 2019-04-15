
'''
Given a struct array of type Height, having two elements feet and inches. Find the maximum height, where height is calculated sum of feet and inches after converting feet into inches.

Input:
First line of input contains number of testcases. For each testcase, first line of input contains N, number of given heights. Next line contains 2*N number of elements (feet and inches for each N).

Output:
Output maximum height from array.

Your Task: Your task is to only complete the function of find maximum height from given array.

Constraints:
1<=T<=100
1<=N<=105
0<=Feet, Inches<=105

Example:
Input:
2
2
1 2 2 1
4
3 5 7 9 5 6 5 5

'''

def feets_to_inches(ft, inch):
    return 12*ft + inch

def get_max_height(arr):
    heights = []
    for i in range(0, len(arr), 2):
        heights.append(feets_to_inches(arr[i], arr[i+1]))
    return max(heights)

def test():
    test_cases = int(input())
    for test in range(test_cases):
        size = int(input())
        heights = list(map(int, raw_input().split()))
        print get_max_height(heights)

test()