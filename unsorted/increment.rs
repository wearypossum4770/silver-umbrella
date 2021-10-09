///https://edabit.com/challenge/NAQhEoxbofPidLxm9
pub fn increment(num: i32) -> i32 {
    let target: i32 = num + 1;
    target
}
#[cfg(test)]
mod tests {
    use super::increment;
    #[test]
    fn test_increment() {
        assert_eq!(increment(2), 3);
        assert_eq!(increment(-9), -8);
        assert_eq!(increment(0), 1);
        assert_eq!(increment(999), 1000);
        assert_eq!(increment(73), 74);
    }
}
