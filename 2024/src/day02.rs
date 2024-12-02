use std::fs::read_to_string;

pub fn run() {
    let input: Vec<String> = read_to_string("input/day02.txt")
        .unwrap()
        .lines()
        .map(String::from)
        .collect();

    println!("Result for Part 1: {}", solve1(&input));
    println!("Result for Part 2: {}", solve2(&input));
}

/// Computes the differences between consecutive elements in the `digits` vector.
///
/// # Arguments
///
/// * `digits` - A vector of integers from which the differences between consecutive elements will be calculated.
///
/// # Returns
///
/// A vector of differences between each pair of consecutive elements in the input vector.
fn get_diffs(digits: &Vec<isize>) -> Vec<isize> {
    let diffs: Vec<isize> = digits
        .windows(2)
        .map(|window| window[1] - window[0])
        .collect();
    diffs
}

/// Checks if the given vector of integers is safe.
///
/// # Arguments
///
/// * `digits` - A vector of integers to be checked for safety.
/// * `tolerate_one_level` - A boolean value indicating whether one level of tolerance is allowed.
///
/// # Returns
///
/// A boolean value indicating whether the input vector is safe.
fn is_safe(digits: &Vec<isize>, tolerate_one_level: bool) -> bool {
    let diffs = get_diffs(digits);
    if is_all_positive_or_negative(&diffs) && is_in_allowed_range(&diffs) {
        return true;
    }
    if tolerate_one_level && (!is_all_positive_or_negative(&diffs) || !is_in_allowed_range(&diffs))
    {
        for i in 0..digits.len() {
            let mut sub_digits = digits.clone();
            sub_digits.remove(i);
            let sub_diffs = get_diffs(&sub_digits);
            if is_all_positive_or_negative(&sub_diffs) && is_in_allowed_range(&sub_diffs) {
                return true;
            }
        }
        return false;
    }
    false
}

/// Checks if all diffs are in the allowed range.
///
/// # Arguments
///
/// * `diffs` - A vector of integers representing the differences between consecutive elements.
///
/// # Returns
///
/// A boolean value indicating whether all differences are in the allowed range.
fn is_in_allowed_range(diffs: &Vec<isize>) -> bool {
    diffs.iter().all(|&x| x.abs() <= 3 && x.abs() >= 1)
}

/// Checks if all diffs are either positive or negative.
///
/// # Arguments
///
/// * `diffs` - A vector of integers representing the differences between consecutive elements.
///
/// # Returns
///
/// A boolean value indicating whether all differences are either positive or negative.
fn is_all_positive_or_negative(diffs: &Vec<isize>) -> bool {
    diffs.iter().all(|&x| x > 0) || diffs.iter().all(|&x| x < 0)
}

fn solve1(input: &Vec<String>) -> isize {
    let mut safe_reports: isize = 0;

    for line in input.iter() {
        let strings: Vec<&str> = line.split_whitespace().collect();
        let digits: Vec<isize> = strings.iter().flat_map(|&x| x.parse()).collect();
        if is_safe(&digits, false) {
            safe_reports += 1;
        }
    }
    safe_reports
}

fn solve2(input: &Vec<String>) -> isize {
    let mut safe_reports: isize = 0;

    for line in input.iter() {
        let strings: Vec<&str> = line.split_whitespace().collect();
        let digits: Vec<isize> = strings.iter().flat_map(|&x| x.parse()).collect();
        if is_safe(&digits, true) {
            safe_reports += 1;
        }
    }
    safe_reports
}
