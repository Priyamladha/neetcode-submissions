class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l,r = 0, rows-1

        while l<=r:

            rowm = (l+r)//2

            if target > matrix[rowm][cols-1]:
                l = rowm+1
            elif target < matrix[rowm][0]:
                r = rowm-1
            else:
                left, right = 0, cols-1
                while left <= right:

                    colm = (left+right)//2

                    if target < matrix[rowm][colm]:
                        right = colm - 1
                    elif target > matrix[rowm][colm]:
                        left = colm + 1
                    else:
                        return True
                return False

        return False