pub fn count_matches(items: &[[&str; 3]; 3], rule_key: &str, rule_value: &str) -> u32 {
    let mut num = 0u32;
    for item in items {
        match rule_key {
            "type" => {
                if item[0] == rule_value {
                    num += 1;
                }
            }
            "color" => {
                if item[1] == rule_value {
                    num += 1;
                }
            }
            "name" => {
                if item[2] == rule_value {
                    num += 1;
                }
            }
            _ => break,
        }
    }
    num
}
#[cfg(test)]
mod tests {
    use super::count_matches;
    #[test]
    fn test_count_matches() {
        assert_eq!(
            count_matches(
                &[
                    ["phone", "blue", "pixel"],
                    ["computer", "silver", "phone"],
                    ["phone", "gold", "iphone"]
                ],
                "type",
                "phone"
            ),
            2
        );
        assert_eq!(
            count_matches(
                &[
                    ["phone", "blue", "pixel"],
                    ["computer", "silver", "lenovo"],
                    ["phone", "gold", "iphone"]
                ],
                "color",
                "silver"
            ),
            1
        );
    }
}
