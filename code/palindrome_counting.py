def palindrome_counting(word: str) -> int:

    # dp[i][j] is a boolean array that is true if
    # word[i:j] is a palindrome.
    dp = [[False for _ in range(len(word))] for _ in range(len(word))]

    count = 0

    for word_length in range(len(word)):
        for j in range(len(word) - word_length):
            start, end = j, j + word_length
            # base case 1: all words of length 1 are palindromes
            if word_length == 0:
                dp[start][end] = True

            # base case 2: words of length 2 are palindromes
            # if the two letters are equal
            elif word_length == 1:
                dp[start][end] = word[start] == word[end]

            else:
                dp[start][end] = dp[start + 1][end - 1] and word[start] == word[end]

            count += 1 if dp[start][end] else 0

    return count


assert palindrome_counting("aaa") == 6
assert palindrome_counting("aba") == 4
assert palindrome_counting("a") == 1
assert palindrome_counting("ab") == 2
