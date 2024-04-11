class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        soldier_row = []
        for i in range(m):
            x = mat[i].count(1)

            soldier_row.append((x, i))

        soldier_row.sort()

        answer = []
        for i in range(k):
            answer.append(soldier_row[i][1])

        return answer