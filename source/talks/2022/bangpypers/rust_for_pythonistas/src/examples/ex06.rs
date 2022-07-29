fn borrow_a_string(x: &str) {
    println!("I've only borrowed a string. The value is '{}'.", x);
}

fn move_a_string(x: String) {
    println!("I've taken ownership of a string. The value is '{}'. You cannot use it after this.", x);
}

pub fn run() {
    let v = String::from("The cake is a lie!");
    borrow_a_string(&v); // v is still in scope because this is just a borrow.
    move_a_string(v); // v is a move, so it cannot be used after this.
    // ERROR IF UNCOMMENTED
    // println!("v={}", v); // if you try this, the compiler will complain.
}
