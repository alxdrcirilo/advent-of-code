use num::Integer;
use std::fs::read_to_string;

pub fn run() {
    let input: String = read_to_string("input/day04.txt").unwrap();

    println!("Result for Part 1: {}", solve1(&input));
    println!("Result for Part 2: {}", solve2(&input));
}

fn solve1(input: &String) -> usize {
    const PATTERN: [char; 4] = ['X', 'M', 'A', 'S'];

    fn is_match(chunk: Vec<char>, xmas: &mut usize) {
        if chunk == PATTERN {
            *xmas += 1
        }
    }

    let line_count: usize = input.lines().count();
    let char_count: usize = input.lines().next().unwrap().chars().count();
    let chars: Vec<char> = input.replace("\n", "").chars().collect();

    // Find all occurences of 'X'
    let occurrences: Vec<usize> = chars
        .iter()
        .enumerate()
        .filter_map(|(i, &c)| if c == 'X' { Some(i) } else { None })
        .collect();

    let mut xmas: usize = 0;
    for &idx in &occurrences {
        let (row, col) = idx.div_rem(&char_count);
        // Horizontal
        if col <= char_count - 4 {
            // Forward
            is_match(chars[idx..idx + 4].to_vec(), &mut xmas);
        }
        if col >= 3 {
            // Backward
            is_match((0..4).map(|i| chars[idx - i]).collect(), &mut xmas);
        }
        // Vertical
        if row <= line_count - 4 {
            // Forward
            is_match(
                (0..4).map(|i| chars[idx + i * char_count]).collect(),
                &mut xmas,
            );
        }
        if row >= 3 {
            // Backward
            is_match(
                (0..4).map(|i| chars[idx - i * char_count]).collect(),
                &mut xmas,
            );
        }
        // Diagonal
        if row <= line_count - 4 && col <= char_count - 4 {
            // SE
            is_match(
                (0..4).map(|i| chars[idx + i * (char_count + 1)]).collect(),
                &mut xmas,
            );
        }
        if row >= 3 && col <= char_count - 4 {
            // NE
            is_match(
                (0..4).map(|i| chars[idx - i * (char_count - 1)]).collect(),
                &mut xmas,
            );
        }
        if row >= 3 && col >= 3 {
            // NW
            is_match(
                (0..4).map(|i| chars[idx - i * (char_count + 1)]).collect(),
                &mut xmas,
            );
        }
        if row <= line_count - 4 && col >= 3 {
            // SW
            is_match(
                (0..4).map(|i| chars[idx + i * (char_count - 1)]).collect(),
                &mut xmas,
            );
        }
    }
    xmas
}

fn solve2(input: &String) -> usize {
    let line_count: usize = input.lines().count();
    let char_count: usize = input.lines().next().unwrap().chars().count();
    let chars: Vec<char> = input.replace("\n", "").chars().collect();

    // Find all occurrences of 'A'
    let occurrences: Vec<usize> = chars
        .iter()
        .enumerate()
        .filter_map(|(i, &c)| if c == 'A' { Some(i) } else { None })
        .collect();

    let mut xmas: usize = 0;
    for &idx in &occurrences {
        let (row, col) = idx.div_rem(&char_count);
        // X
        if row <= line_count - 2 && row >= 1 && col <= char_count - 2 && col >= 1 {
            let check_patterns = |indexes: [usize; 3]| -> bool {
                let mat: Vec<char> = indexes
                    .iter()
                    .filter_map(|&i| chars.get(i))
                    .cloned()
                    .collect();
                mat == ['M', 'A', 'S'] || mat == ['S', 'A', 'M']
            };

            if check_patterns([idx - char_count - 1, idx, idx + char_count + 1])
                && check_patterns([idx - char_count + 1, idx, idx + char_count - 1])
            {
                xmas += 1;
            }
        }
    }
    xmas
}
