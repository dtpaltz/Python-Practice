# This problem was recently asked by Amazon:
#
# You are given a 2D array of characters, and a target string.
# Return whether or not the word target word exists in the matrix.
# Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.
#
# Example:
#
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
#
# Given this matrix, and the target word FOAM, you should return true,
# as it can be found going up-to-down in the first column.

def word_search(matrix, word):
    # print(matrix)
    for i in range(len(matrix)):
        this_word = ''.join(matrix[i][:])
        # print(this_word)
        if word == this_word:
            return True

    trans_matrix = [list(x) for x in zip(*matrix)]
    # print(trans_matrix)

    for i in range(len(trans_matrix)):
        this_word = ''.join(trans_matrix[i][:])
        # print(this_word)
        if word == this_word:
            return True

    return False


matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]

print(word_search(matrix, 'FOAM'))
# True
