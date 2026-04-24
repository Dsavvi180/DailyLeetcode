class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for i in range(len(temperatures))]
        stack = []
        for index,temp in enumerate(temperatures):
            if not stack:
                stack.append((temp,index))
            else:
                top = stack[-1]
                while stack and temp > top[0]:
                    days = index - top[1]
                    answer[top[1]] = days
                    stack.pop()
                    if stack:
                      top = stack[-1]
                stack.append((temp,index))
        return answer
        