class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for i in range(len(temperatures))]
        stack = []
        for index,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                    days = index - stack[-1][1]
                    answer[stack[-1][1]] = days
                    stack.pop()
            stack.append((temp,index))
        return answer
        