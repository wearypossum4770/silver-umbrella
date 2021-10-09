/// copyright https://edabit.com/challenge/8q54MKnRrm89pSLmW 
pub fn convert_minutes_to_seconds(minutes:i32)-> i32{
let seconds: i32 = minutes*60;
seconds
}
#[cfg(test)]
mod tests {
    use super::convert_minutes_to_seconds;
    #[test]
    fn test_convert_minutes_to_seconds() {
        assert_eq!(convert_minutes_to_seconds(6), 360);
        assert_eq!(convert_minutes_to_seconds(4), 240);
        assert_eq!(convert_minutes_to_seconds(8), 480);
        assert_eq!(convert_minutes_to_seconds(60), 3600);
    }
}
