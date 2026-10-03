class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        print(people)
        n = len(people)
        numBoats = 0
        left, right = 0, n-1
        pairs = []

        while right<n and left<=right:
            if people[left] <= limit and people[left]+people[right]>limit:
                print("added: ", people[left], "leftIndex: ", left)
                pairs.append([people[left]])
                numBoats +=1
                left +=1
            elif left == right and people[left] <= limit:
                pairs.append([people[left]])
                numBoats += 1
                left+=1
            elif people[left] + people[right] > limit:
                left +=1
            elif people[left] + people[right] <= limit:
                pairs.append([people[left], people[right]])
                numBoats +=1
                left+=1
                right-=1
        
        print(pairs)
        return numBoats

            

            






