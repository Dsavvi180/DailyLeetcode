class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        n = len(people)
        numBoats = 0
        left, right = 0, n-1

        while right<n and left<=right:
            if people[left] <= limit and people[left]+people[right]>limit:
                numBoats +=1
                left +=1
            elif left == right and people[left] <= limit:
                numBoats += 1
                left+=1
            elif people[left] + people[right] > limit:
                left +=1
            elif people[left] + people[right] <= limit:
                numBoats +=1
                left+=1
                right-=1
        return numBoats

            

            






