class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        import math
        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of columns
        loops = min(math.ceil(m / 2), math.ceil(n / 2))
        ans = []
        for circle in range(1, loops + 1):
            # Determine the four corners of a "circle"
            topleft_x, topleft_y = circle - 1, circle - 1
            bottomright_x, bottomright_y = m - circle, n - circle
            # Traverse the circle clock-wisely
            if topleft_x < bottomright_x and topleft_y < bottomright_y:
                for j in range(topleft_y, bottomright_y):
                    ans.append(matrix[topleft_x][j])
                for i in range(topleft_x, bottomright_x):
                    ans.append(matrix[i][bottomright_y]) 
                for j in range(bottomright_y, topleft_y, -1):
                    ans.append(matrix[bottomright_x][j])
                for i in range(bottomright_x, topleft_x, -1):
                    ans.append(matrix[i][topleft_y])
            elif topleft_x == bottomright_x and topleft_y < bottomright_y:
                for j in range(topleft_y, bottomright_y + 1):
                    ans.append(matrix[topleft_x][j])
            elif topleft_y == bottomright_y and topleft_x < bottomright_x:
                for i in range(topleft_x, bottomright_x + 1):
                    ans.append(matrix[i][topleft_y])
            else: # all four coordinates are equal
                ans.append(matrix[topleft_x][topleft_y])
        return ans   