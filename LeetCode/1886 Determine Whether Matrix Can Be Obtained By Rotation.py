#Given two n x n binary matrices mat and target, 
# return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

# Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
# Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
# Output: false
# # Explanation: It is impossible to make mat equal to target by rotating mat.
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.



class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        n = len(mat)
        for times in range(4):
            for i in range(n):
                for j in range(i+1,n):
                    mat[i][j],mat[j][i] = mat[j][i],mat[i][j] # swap(mat[i][j],mat[j][i])
            for i in range(n):
                for j in range(n//2):
                    mat[i][j], mat[i][n-1-j] = mat[i][n-1-j], mat[i][j] #swap(mat[i][j], mat[i][n-1-j])
            if(mat == target):
                return True
        return False

mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]

Sol = Solution()
print(Sol.findRotation(mat, target)) #true