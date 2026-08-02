class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        current = [None, None, None]
        for triplet in triplets:
            left, middle, right = triplet[0], triplet[1], triplet[2]
            if left > target[0] or middle > target[1] or right > target[2]:
                continue
            current[0] = max(current[0], triplet[0]) if current[0] else triplet[0]
            current[1] = max(current[1], triplet[1]) if current[1] else triplet[1]
            current[2] = max(current[2], triplet[2]) if current[2] else triplet[2]
            if current == target:
                return True
        return False

        
        
        