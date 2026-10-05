class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        len_arr = len(arr)
        final_arr = []
        if 0 not in arr:
            return arr
        else:
            for i in range(len_arr):
                if arr[i]==0:
                    final_arr.append(0)
                    final_arr.append(0)
                else:
                    final_arr.append(arr[i])
            arr[:] = final_arr[:len_arr]
            return arr

        