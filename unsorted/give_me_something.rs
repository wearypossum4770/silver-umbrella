pub fn give_me_something(words:&str)->String{
  let mut something = String::from("something ");
  something.push_str(words);
  something 
}
#[cfg(test)]
mod tests {
    use super::give_me_something;
    #[test]
    fn test_give_me_something() {
        assert_eq!(give_me_something("a"), "something a");
        assert_eq!(give_me_something("is cooking"), "something is cooking");
        assert_eq!(give_me_something(" is cooking"), "something  is cooking");
        
    }
}
