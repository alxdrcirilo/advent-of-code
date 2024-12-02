use std::env;

mod day01;
mod day02;

fn main() {
    let args: Vec<String> = env::args().collect();
    let day = args
        .get(1)
        .expect("Please provide a day number as argument!");

    match day.as_str() {
        "1" => day01::run(),
        "2" => day02::run(),
        _ => println!("Day not implemented!"),
    }
}
