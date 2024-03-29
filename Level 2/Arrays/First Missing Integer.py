'''

Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space

'''

class Solution:
    def firstMissingPositive(self, A):
        A = list(filter(lambda x : x > 0, A))
        A.sort()
        for i in range(len(A)):
            if A[i]!=i+1:
                return i+1
        return len(A)+1