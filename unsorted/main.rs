use crate::addition::addition;
use crate::convert_minutes_to_seconds::convert_minutes_to_seconds;
use crate::count_matches::count_matches;
use crate::defang_ip_addr::defang_ip_addr;
use crate::give_me_something::give_me_something;
use crate::increment::increment;
use crate::is_palindrome::is_palindrome;
use crate::next_integer::next_integer;
use crate::running_sum::running_sum;
mod addition;
mod convert_minutes_to_seconds;
mod count_matches;
mod defang_ip_addr;
mod give_me_something;
mod increment;
mod is_palindrome;
mod next_integer;
mod running_sum;
fn main() {
    let _vector_big_strings = vec![give_me_something("A")];
    let _vector_boolean = vec![is_palindrome(-121)];
    let _vector_strings = vec![defang_ip_addr("1.1.1.1")];
    let _vector_i32 = vec![next_integer(1), convert_minutes_to_seconds(10),increment(1), addition(2, 3)];
    let _vector_vector_u32 = vec![running_sum(&[1, 2, 3, 4])];
    let _vector_u32 = vec![count_matches(
        &[
            ["phone", "blue", "pixel"],
            ["computer", "silver", "phone"],
            ["phone", "gold", "iphone"],
        ],
        "type",
        "phone",
    )];

    println!("Hello, world!");
    println!("{:?}",_vector_big_strings);
    println!("{:?}", _vector_boolean);
    println!("{:?}", _vector_u32);
    println!("{:?}", _vector_i32);
    println!("{:?}", _vector_strings);
    println!("{:?}", _vector_vector_u32);
}
