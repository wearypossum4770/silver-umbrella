/// https://leetcode.com/problems/running-sum-of-1d-array/
pub fn running_sum(nums: &[u32]) -> Vec<u32> {
    let mut array = nums.to_vec();
    let mut target: Vec<u32> = Vec::with_capacity(nums.len());
    if !array.is_empty() {
        for _num in nums.iter() {
            let sum = array.iter().fold(0, |acc, x| acc + x);
            target.insert(0, sum);
            array.pop();
        }
    }
    target
}
#[cfg(test)]
mod tests {
    use super::running_sum;
    #[test]
    fn test_running_sum() {
        assert_eq!(running_sum(&[1, 2, 3, 4]), vec![1, 3, 6, 10]);
        assert_eq!(running_sum(&[1, 1, 1, 1, 1]), vec![1, 2, 3, 4, 5]);
        assert_eq!(running_sum(&[3, 1, 2, 10, 1]), vec![3, 4, 6, 16, 17]);
    }
}
