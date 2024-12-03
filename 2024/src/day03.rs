use regex::Regex;
use std::fs::read_to_string;

pub fn run() {
    let input = read_to_string("input/day03.txt").unwrap();

    println!("Result for Part 1: {}", solve1(&input));
    println!("Result for Part 2: {}", solve2(&input));
}

fn solve1(input: &String) -> isize {
    let re: Regex = Regex::new(r"mul\(([0-9]+),([0-9]+)\)").unwrap();
    let result: isize = re
        .captures_iter(input)
        .map(|cap| {
            let digit1: isize = cap[1].parse().unwrap();
            let digit2: isize = cap[2].parse().unwrap();
            digit1 * digit2
        })
        .sum();
    result
}

fn solve2(input: &String) -> isize {
    let re_do = Regex::new(r"do[^n]").unwrap();
    let re_dont = Regex::new(r"don't").unwrap();

    // Find all the indexes of "do" and "don't"
    let mut idx_do: Vec<usize> = re_do.find_iter(input).map(|m| m.start() + 2).collect();
    let mut idx_dont: Vec<usize> = re_dont.find_iter(input).map(|m| m.start()).collect();
    idx_do.insert(0, 0);
    idx_dont.insert(idx_dont.len(), input.len());

    let re: Regex = Regex::new(r"mul\(([0-9]+),([0-9]+)\)").unwrap();
    let mut result: isize = 0;
    let mut prev_idx_dont: usize = 0;

    for a in idx_do {
        // If the next "do" is before the last "don't", skip
        if a < prev_idx_dont {
            continue;
        }

        // Find the next "don't" after the "do"
        let mut b: usize = idx_dont.remove(0);
        while a > b && idx_dont.len() > 0 {
            b = idx_dont.remove(0);
        }

        // Calculate the result
        result += re
            .captures_iter(&input[a..b])
            .map(|cap| {
                let digit1: isize = cap[1].parse().unwrap();
                let digit2: isize = cap[2].parse().unwrap();
                digit1 * digit2
            })
            .sum::<isize>();

        prev_idx_dont = b;
    }
    result
}
