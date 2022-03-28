// Rustlings exercise: functions4.rs
// Make me compile! Execute `rustlings hint functions4` for hints :)

// This store is having a sale where if the price is an even number, you get
// 10 Rustbucks off, but if it's an odd number, it's 3 Rustbucks off.

/// This is the function that is triggered when you're building a binary, a CLI or a server
/// instance for example.
pub fn run() {
    let original_price = 51;
    println!("Your sale price is {}", sale_price(original_price));
}

/// This function takes an i32 integer and returns an i32 integer.
/// Rusts typing is extremely strict. If it looks like a duck, don't trust it.
/// If you want something that quacks, then don't ask for a duck. Ask for something
/// that quacks.
fn sale_price(price: i32) -> i32 {
    if is_even(price) {
        return price - 10
    } else {
        price - 3
    }
}

/// This function takes an i32 and returns a boolean value.
/// Even the number size really matters. Rust showed me that we use inconsistent
/// database schemas in some places because I was using u32 (unsigned integer 32 bit),
/// and one particular database schema returned a u64 instead. That's an error you wouldn't get
/// with Python.
fn is_even(num: i32) -> bool {
    num % 2 == 0
}
