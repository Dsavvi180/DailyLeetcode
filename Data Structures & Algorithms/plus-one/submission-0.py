class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [i for i in str(int(''.join(map(lambda x: str(x), digits)))+1)]
        