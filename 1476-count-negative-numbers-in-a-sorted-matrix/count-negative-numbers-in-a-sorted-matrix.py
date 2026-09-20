class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        final_neg_count = 0
        for row in grid:
            final_neg_count+=len([i for i in row if i<0])
        return final_neg_count
        