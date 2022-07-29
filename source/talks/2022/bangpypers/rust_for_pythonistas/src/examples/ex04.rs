pub fn run() {
    let x = 10;
    {
        let mut x = 15;
        println!("x = {}", x);
        x = 18;
        println!("x = {}", x);
    }
    println!("x = {}", x);
}
