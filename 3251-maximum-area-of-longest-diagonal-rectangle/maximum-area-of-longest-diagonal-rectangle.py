class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        long_diag = 0
        ans = 0
        for dimension in dimensions:
            if (dimension[0] ** 2) + (dimension[1] ** 2) > long_diag:
                long_diag = (dimension[0] ** 2) + (dimension[1] ** 2)
                ans = dimension[0] * dimension[1]
            elif (dimension[0] ** 2) + (dimension[1] ** 2) == long_diag:
                ans = max(ans, dimension[0] * dimension[1])

        return ans