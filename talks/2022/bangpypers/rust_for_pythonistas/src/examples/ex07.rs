fn append_to_a_vector(v: &mut Vec<u32>, a: u32) {
    v.push(a);
}

pub fn run() {
    let mut x = vec![10, 20, 30, 40];
    println!("Initial Vector: {:?}", x);
    append_to_a_vector(&mut x, 10);
    println!("Final Vector: {:?}", x);
}
