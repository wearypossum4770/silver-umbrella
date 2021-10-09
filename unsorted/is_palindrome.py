def is_palindrome(x):
    """
    copyright: https://leetcode.com/problems/palindrome-number/submissions/
    Runtime: 56 ms, faster than 79.65% of Python3 online submissions for Palindrome Number.
    Memory Usage: 14.1 MB, less than 91.87% of Python3 online submissions for Palindrome Number.
    """
    num = str(x)
    return num == num[::-1]
