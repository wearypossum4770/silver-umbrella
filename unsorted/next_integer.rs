/// copyright https://edabit.com/challenge/NAQhEoxbofPidLxm9
pub fn next_integer(x:i32)->i32{
let next: i32 = x+1;
next
}
#[cfg(test)]
mod tests {
    use super::next_integer;
    #[test]
    fn test_next_integer() {
        assert_eq!(next_integer(2), 3); // "2 plus 1 equals 3.")
        assert_eq!(next_integer(-9), -8); // "-8 plus 1 equals -9.")
        assert_eq!(next_integer(0), 1); // "0 plus 1 equals 1.")
        assert_eq!(next_integer(999), 1000); // "999 plus 1 equals 1000.")
        assert_eq!(next_integer(73), 74); // "73 plus 1 equals 74.")
    }
}