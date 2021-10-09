use std::collections::HashMap;
use regex::Regex;

pub fn fiscal_code() {
let consonants = Regex::new("[^aeiou]").unwrap();
//let vowels = Regex::new();
    let months: [(i32,&str);12] = [
        (1, "A"),
        (2, "B"),
        (3, "C"),
        (4, "D"),
        (5, "E"),
        (6, "H"),
        (7, "L"),
        (8, "M"),
        (9, "P"),
        (10, "R"),
        (11, "S"),
        (12, "T"),
    ];
    println!("{:?}", consonants);
    println!("{:?}", months);
}
#[cfg(test)]
mod tests {
    use super::fiscal_code;
    #[test]
    fn test_fiscal_code() {
        let helen_yu: HashMap<&str, &str> = [
            ("name", "Helen"),
            ("surname", "Yu"),
            ("gender", "F"),
            ("dob", "1/12/1950"),
        ]
        .iter()
        .cloned()
        .collect();
        let matt_edabit: HashMap<&str, &str> = [
            ("name", "Matt"),
            ("surname", "Edabit"),
            ("gender", "M"),
            ("dob", "1/1/1900"),
        ]
        .iter()
        .cloned()
        .collect();
        let mickey_mouse: HashMap<&str, &str> = [
            ("name", "Mickey"),
            ("surname", "Mouse"),
            ("gender", "M"),
            ("dob", "16/1/1928"),
        ]
        .iter()
        .cloned()
        .collect();
        assert_eq!(fiscal_code(matt_edabit), "DBTMTT00A01");
        assert_eq!(fiscal_code(helen_yu), "YUXHLN50T41");
        assert_eq!(fiscal_code(mickey_mouse), "MSOMKY28A16");
    }
}
