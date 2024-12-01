use regex::Regex;
use std::fs::read_to_string;

pub fn run() {
    let input: Vec<String> = read_to_string("input/day01.txt")
        .unwrap()
        .lines()
        .map(String::from)
        .collect();

    println!("Result for Part 1: {}", solve1(&input));
    println!("Result for Part 2: {}", solve2(&input));
}

/// Get the vectors from the input
///
/// # Arguments
///
/// * `input` - A vector of strings
///
/// # Returns
///
/// A tuple of two vectors of usize
fn get_vectors(input: &Vec<String>) -> (Vec<usize>, Vec<usize>) {
    let count: usize = input.len();
    let mut left: Vec<usize> = vec![0; count];
    let mut right: Vec<usize> = vec![0; count];

    let re: Regex = Regex::new(r"^([0-9]+)\s{3}([0-9]+)$").unwrap();
    for (i, line) in input.iter().enumerate() {
        let Some(caps) = re.captures(&line) else {
            return (left, right);
        };
        left[i] = caps[1].parse().unwrap();
        right[i] = caps[2].parse().unwrap();
    }
    left.sort();
    right.sort();
    (left, right)
}

fn solve1(input: &Vec<String>) -> usize {
    let (left, right) = get_vectors(input);
    let mut sum_vals: usize = 0;
    for i in 0..left.len() {
        sum_vals += left[i].abs_diff(right[i]);
    }
    sum_vals
}

fn solve2(input: &Vec<String>) -> usize {
    let (left, right) = get_vectors(input);
    let mut sum_vals: usize = 0;
    for i in 0..left.len() {
        sum_vals += right[i] * left.iter().filter(|&n| *n == right[i]).count();
    }
    sum_vals
}
