# -*- coding: utf8 -*-

'''
Find total number of Squares in a N*N cheesboard.

Input:
The first line contains an integer T, depicting total number of test cases. Then following T lines contains an integer N that is the side of the chessboard.

Output:
Each seperate line showing the maximum number of squares possible.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100

Example:
Input:
2
1
2

Output:
1
5
'''



def get_squares_in_chess_board(n):
    ## squares in chess board is : 1^2 + 2^2 + 3^2 + 4^2 + ..... + n^2 
    ## 
    squares = (n * (n+1)*(2*n + 1))/6
    return squares


print get_squares_in_chess_board(2)
# number_of_test_cases = int(input())
# for test_case in range(number_of_test_cases):
#     number_to_find = int(input())
#     print get_squares_in_chess_board(number_to_find)