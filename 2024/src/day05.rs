use std::{collections::HashMap, fs::read_to_string};

pub fn run() {
    let input: String = read_to_string("input/day05.txt").unwrap();

    println!("Result for Part 1: {}", solve1(&input));
}

fn solve1(input: &String) -> usize {
    let parts: Vec<&str> = input.split("\n\n").collect();
    let (rules, updates) = (parts[0], parts[1]);

    // Key as a digit, value as a list of digits that follow it
    let mut edges: HashMap<&str, Vec<&str>> = HashMap::new();
    for line in rules.lines() {
        if let Some((key, value)) = line.split_once('|') {
            edges.entry(key).or_insert_with(Vec::new).push(value);
        }
    }

    // Iterate over all updates
    let mut result: usize = 0;
    for update in updates.lines() {
        let digits: Vec<&str> = update.split(",").collect();
        if is_correct(&digits, &edges) {
            if let Some(middle) = digits.get(digits.len() / 2) {
                result += middle.parse::<usize>().unwrap();
            }
        }
    }
    result
}

fn is_correct(digits: &Vec<&str>, edges: &HashMap<&str, Vec<&str>>) -> bool {
    for (i, &digit) in digits.iter().enumerate() {
        if let Some(values) = edges.get(digit) {
            // Check if any of the digits before the current digit are in the values
            if digits[..i].iter().any(|&d| values.contains(&d)) {
                // Digit is not allowed
                return false;
            }
        }
    }
    true
}
