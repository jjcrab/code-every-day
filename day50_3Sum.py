'''
Description
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.

Example
Example 1:

Input:

numbers = [2,7,11,15]
Output:

[]
Explanation:

Cannot find triples such that the sum of three numbers is 0.
Example 2:

Input:

numbers = [-1,0,1,2,-1,-4]
Output:

[[-1, 0, 1],[-1, -1, 2]]
Explanation:

[-1, 0, 1] and [-1, -1, 2] are two triples.1, 2]]
'''


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # edge cases:
        result = []
        if not numbers or len(numbers) < 3:
            return result

        numbers.sort()
        print(numbers)

        for i in range(len(numbers) - 2):
            # no duplicate
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            # normal two sum question
            array = []
            last_pair = ()
            left, right = i + 1, len(numbers) - 1
            while left < right:
                if numbers[left] + numbers[right] < 0 - numbers[i]:
                    left += 1
                elif numbers[left] + numbers[right] == 0 - numbers[i]:
                    if (numbers[left], numbers[right]) != last_pair:
                        array = [numbers[i], numbers[left], numbers[right]]
                        result.append(array)
                    last_pair = (numbers[left], numbers[right])
                    left += 1
                    right -= 1
                else:
                    right -= 1

        return result
