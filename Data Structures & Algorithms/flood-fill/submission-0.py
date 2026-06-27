class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image
        def dfs(image, sr, sc, color, visit, orig_color):
            ROWS, COLS = len(image), len(image[0])
            if (min(sr, sc)) < 0 or sr == ROWS or sc == COLS or (sr, sc) in visit:
                return
            if image[sr][sc] != orig_color:
                return 
            image[sr][sc] = color
            visit.add((sr, sc))

            dfs(image, sr+1, sc, color, visit,orig_color)
            dfs(image, sr-1, sc, color, visit,orig_color)
            dfs(image, sr, sc+1, color, visit,orig_color)
            dfs(image, sr, sc-1, color, visit,orig_color)

            return image

        return dfs(image, sr, sc, color, set(),original )

        