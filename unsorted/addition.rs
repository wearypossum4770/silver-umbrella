///https://edabit.com/challenge/3LpBLgNRyaHMvNb4j
///
pub fn addition(x: i32, y: i32) -> i32 {
    let target: i32 = x + y;
    target
}
#[cfg(test)]
mod tests {
    use super::addition;
    #[test]
    fn test_addition() {
        assert_eq!(addition(2, 3), 5);
        assert_eq!(addition(-3, -6), -9);
        assert_eq!(addition(7, 3), 10);
        assert_eq!(addition(88, 2), 90);
    }
}
