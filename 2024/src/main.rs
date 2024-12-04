use std::env;

mod day01;
mod day02;
mod day03;
mod day04;

fn main() {
    let args: Vec<String> = env::args().collect();
    let day = args
        .get(1)
        .expect("Please provide a day number as argument!");

    match day.as_str() {
        "1" => day01::run(),
        "2" => day02::run(),
        "3" => day03::run(),
        "4" => day04::run(),
        _ => println!("Day not implemented!"),
    }
}
