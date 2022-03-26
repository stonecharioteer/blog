pub fn run() {
    let x: String = "hello".to_string();
    println!("x = {}", x);
    let y = x;
    println!("y = {}", y);
    // ERROR IF UNCOMMENTED
    // println!("x = {}", x);
}
