pub fn run() {
    let x = "ನಮಸ್ಕಾರ";
    println!("{} = {:?}", x, x.as_bytes());
    println!("{} = {:?}", x, x.chars().collect::<Vec<char>>());
}
