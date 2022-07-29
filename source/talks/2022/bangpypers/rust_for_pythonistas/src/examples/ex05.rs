pub fn run() {
    let x: String = "hello".to_string();
    println!("x = {}", x);
    let y = x;
    println!("y = {}", y);
    // ERROR IF UNCOMMENTED
    // println!("x = {}", x);
    let z: i8 = 10;
    println!("z={z}");
    let mut u = z;
    println!("u={u}");
    u = 50;
    println!("u={u}");
    println!("z={z}");
}
