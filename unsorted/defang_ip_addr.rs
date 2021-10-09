///https://leetcode.com/problems/defanging-an-ip-address/
pub fn defang_ip_addr(address: &str) -> String {
    let target: String = address.replace(".", "[.]");
    target
}
#[cfg(test)]
mod tests {
    use super::defang_ip_addr;
    #[test]
    fn test_defang_ip_addr() {
        assert_eq!(defang_ip_addr("1.1.1.1"), "1[.]1[.]1[.]1");
        assert_eq!(defang_ip_addr("255.100.50.0"), "255[.]100[.]50[.]0");
    }
}
