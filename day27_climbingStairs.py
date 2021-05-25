# https: // leetcode.com/problems/climbing-stairs/

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n):
    way_list = [1, 2]
    for i in range(2, n):
        way_list[i % 2] = way_list[0]+way_list[1]
    return way_list[(n-1) % 2]


print(climbStairs(3))
