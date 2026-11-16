class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)

        lower, upper = 1 , maxPile
        res = upper
        while lower<=upper:
            k = (lower+upper)//2

            totalH = sum([math.ceil(x/k) for x in piles])

            if totalH > h:
                lower = k+1
            else:
                upper = k-1
                res = k

        return res