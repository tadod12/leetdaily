class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = ''
            
            if backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1):
                return True
            
            board[i][j] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False

        # res = [False]
        # len_x = len(board) # num_row
        # len_y = len(board[0]) # num_col
        # len_word = len(word)
        # checked = [[False] * len_y for _ in range(len_x)]

        # def is_cand(prev_x, prev_y, next_x, next_y):
        #     if prev_x == -1 and prev_y == -1:
        #         return True
        #     elif checked[next_x][next_y]:
        #         return False
        #     elif ((next_x - prev_x == 1 or next_x - prev_x == -1) and next_y - prev_y == 0) or \
        #         ((next_y - prev_y == 1 or next_y - prev_y == -1) and next_x - prev_x == 0):
        #         return True
        #     else:
        #         return False

        # def backtracking(prev_x, prev_y, curr_len, curr_word):
        #     for i in range(0, len_x):
        #         for j in range(0, len_y):
        #             if is_cand(prev_x, prev_y, i, j):
        #                 checked[i][j] = True
        #                 curr_word += board[i][j]
        #                 curr_len += 1
        #                 if curr_len == len_word:
        #                     if word == curr_word:
        #                         res[0] = True
        #                         return
        #                 else:
        #                     backtracking(i, j, curr_len, curr_word)
        #                 checked[i][j] = False
        #                 curr_word = curr_word[:-1]
        #                 curr_len -= 1

        # backtracking(-1, -1, curr_len=0, curr_word="")
        # return res[0]