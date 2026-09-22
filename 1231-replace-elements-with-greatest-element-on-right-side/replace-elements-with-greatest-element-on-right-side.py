class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        arr_len = len(arr)
        max_val = -1
        for i in range(arr_len-1, -1, -1):
            curr_val = arr[i]
            arr[i] = max_val
            max_val = max(curr_val, max_val)
        return arr
        