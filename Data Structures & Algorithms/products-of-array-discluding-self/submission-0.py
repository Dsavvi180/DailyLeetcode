class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cumProdLeft = [nums[0]]
        cumProdRight = deque([nums[-1]])
        n = len(nums)
        answer = [None]*n
        for i in range(1,n):
            j = n-i-1
            cumProdLeft.append(cumProdLeft[-1] * nums[i])
            cumProdRight.appendleft(cumProdRight[0]*nums[j])
        for i in range(n):
            if i == 0:
                answer[i] = cumProdRight[i+1]
            elif i == n-1:
                answer[i] = cumProdLeft[i-1]
            else:
                answer[i] = cumProdLeft[i-1]*cumProdRight[i+1]
        return answer 