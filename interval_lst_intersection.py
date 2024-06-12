#!/usr/local/bin/python

"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""


class Solution:
    def intervalIntersection(self, A, B):
        result = []
        """
        A.sort(key= lambda x: x[0])
        B.sort(key= lambda x: x[0])
        
        def find_common(i, j, result):
            print(i,j)
            ret_lst = []
            if i[0] < j[0] and i[1] < j[0] or j[0] < i[0] and j[1] < i[0]:
                print("Not inserting anything since condition did not match") 
                return
            
            if i[0] >= j[0] and i[0] < j[1]:
                if i[1] > j[1]:
                    result.append([i[0],j[1]])
                else:
                    result.append([i[0],i[1]])
                print("Append-1") 
            if j[0] >= i[0] and j[0] < i[1]:
                if j[1] > i[1]:
                    result.append([j[0],i[1]])
                else:
                    result.append([j[0],j[1]])
                print("Append-2") 
            else:
                print("No Append") 
                pass

                
            
        print(A)      
        print(B)      
        for i, j in zip(A,B):
            find_common(i,j, result)
            print(f' result is {result}')
        #return result
        print(result)
        """
        new_result = []
        # Let us try by two list version. 
        aindex = bindex = 0 
        while aindex < len(A) or bindex < len(B):
            lo = max(A[aindex][0], B[bindex][0])
            hi = min(A[aindex][1], B[bindex][1])
            if lo <= hi:
                new_result.append([lo,hi])
            
            if A[aindex][1] < B[bindex][1]:
                aindex += 1
            else:
                bindex += 1
        return new_result
            

        

def main():
    sol = Solution()
    print(sol.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))

if __name__ == '__main__':
    main()
