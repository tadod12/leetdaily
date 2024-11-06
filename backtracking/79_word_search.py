class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        len_x = len(board[0])
        len_y = len(board)
        len_word = len(word)
        res = []

        def is_cand(prev_x, prev_y, next_x, next_y, checked):
            if [next_x, next_y] in checked:
                return False
            else:
                if prev_x == -1 and prev_y == -1:
                    return True
                elif next_x < 0 or next_y < 0:
                    return False
                elif ((next_x - prev_x == 1 or next_x - prev_x == -1) and next_y - prev_y == 0) or \
                    ((next_y - prev_y == 1 or next_y - prev_y == -1) and next_x - prev_x == 0):
                    return True
                else:
                    return False

        def backtracking(prev_x, prev_y, curr_len, checked, curr_word):
            for i in range(0, len_y):
                for j in range(0, len_x):
                    if is_cand(prev_x, prev_y, i, j, checked):
                        checked.append([i, j])
                        curr_word += board[i][j]
                        curr_len += 1
                        if curr_len == len_word:
                            if word == curr_word:
                                res.append(curr_word)
                        else:
                            backtracking(i, j, curr_len, checked, curr_word)
                        checked.pop()
                        curr_word = curr_word[:-1]
                        curr_len -= 1

        backtracking(-1, -1, 0, [], "")
        return len(res) > 0

# TIME LIMIT EXCEEDED