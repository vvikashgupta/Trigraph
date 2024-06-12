
"""
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
Note:

N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].
"""






class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        from collections import defaultdict
        dict = defaultdict(str)
        if not N or not K:
            return 0
        dict[1] = str(0)
        if N == 1:
            return 0
        
        def helper(num):
            if num > N:
                return
            st = dict[num-1]
            result = ""
            for ch in st:
                if ch == '0':
                    result += "01"
                elif ch == '1':
                    result += "10"
                else:
                    pass
            dict[num] = result
            helper(num+1)
            
            
            
        helper(2)
        st = dict[N]
        return st[K-1]
