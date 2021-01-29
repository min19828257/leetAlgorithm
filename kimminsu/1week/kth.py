class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        maxi = 10000
        sto = {}

        #Init storage dictionary
        for number in range(1,maxi+1):
            sto[number] = 0

        # allocate to storage eachdatas
        for eachdata in arr:
            sto[eachdata] = 1

        # find missing data
        cnt = 0
        for number in range(1,maxi+1):
            if sto[number] == 0:
                cnt += 1

                if cnt == k:
                    return number;
