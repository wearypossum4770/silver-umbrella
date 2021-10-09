///https://leetcode.com/problems/palindrome-number/submissions/
/// Runtime: 8 ms, faster than 58.61% of Rust online submissions for Palindrome Number.
/// Memory Usage: 2.1 MB, less than 25.83% of Rust online submissions for Palindrome Number.
pub fn is_palindrome(x: i64) -> bool {
    let value: String = x.to_string();
    let reversed: String = value.chars().rev().collect();
    value == reversed
}
#[cfg(test)]
mod tests {
    use super::is_palindrome;
    #[test]
    fn test_is_palindrome() {
        assert_eq!(is_palindrome(-121), false);
        assert_eq!(is_palindrome(121), true);
        assert_eq!(is_palindrome(10), false);
    }
}
