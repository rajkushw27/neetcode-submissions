class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row,col = len(matrix),len(matrix[0])

        l,r = 0,row*col-1

        while l<=r:
            mid  = (l+r)//2

            r1,c1 = mid//col , mid%col

            if matrix[r1][c1] < target:
                l = mid + 1
            elif matrix[r1][c1] > target:
                r = mid - 1
            else:
                return True

        return False