class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)-1
        if n == 0:
            return 0
        i = 0
        count = 0
        while i <= n:
            l , r = 1, nums[i]
            if i + nums[i] >= n:
                return count + 1
            # print("l: ", l)
            # print("r: ", r)
            maxIndex = i 
            maxNext = i
            for x in range(l,r+1):
                if i+x>n:
                    break
                if i + x + nums[i+x] > maxNext:
                    maxNext = i + x + nums[i+x]
                    maxIndex = i + x
            count += 1
            if maxIndex>=n:
                return count
            i = maxIndex
            # print(i)
            
            






                

        