use structopt::StructOpt;
use rust_for_pythonistas::examples;

#[derive(Debug, StructOpt)]
#[structopt(
    name = "rust_for_pythonistas",
    about = "example code for the Rust for Pythonistas talk delivered on 2022-03-26 by Vinay Keerthi"
    )]
struct Opt {
    /// run example number
    #[structopt(short="n", long="number")]
    number: u8,
}
fn main() {
    let opt = Opt::from_args();
    match opt.number {
        1 => examples::ex01::run(),
        2 => examples::ex02::run(),
        3 => eprintln!("ERROR: example 3 has no executable code. It's meant to be read."),
        4 => examples::ex04::run(),
        5 => examples::ex05::run(),
        6 => examples::ex06::run(),
        7 => examples::ex07::run(),
        8 => examples::ex08::run(),
        9 => examples::ex09::run(),
        _ => eprintln!("ERROR: There is no exercise number {}.", opt.number),
    };
}
