use std::collections::HashSet;
use std::fs::read_to_string;

pub fn run() {
    let input: Vec<Vec<char>> = read_to_string("input/day06.txt")
        .unwrap()
        .lines()
        .map(|line| line.chars().collect())
        .collect();

    println!("Result for Part 1: {}", solve1(&input));
}

fn solve1(input: &Vec<Vec<char>>) -> usize {
    let mut direction: char = ' ';
    let mut guard: [usize; 2] = [0, 0];
    let mut obstacles: Vec<[usize; 2]> = Vec::new();
    let mut visited: HashSet<[usize; 2]> = HashSet::new();

    let width = input.len();
    let height = input[0].len();

    for (row, line) in input.iter().enumerate() {
        for (col, &ch) in line.iter().enumerate() {
            if ch == '^' || ch == 'v' || ch == '<' || ch == '>' {
                guard = [row, col];
                direction = ch;
            } else if ch == '#' {
                obstacles.push([row, col]);
            }
        }
    }

    let in_grid = guard[0] != 0 && guard[0] != width - 1 && guard[1] != 0 && guard[1] != height - 1;

    while in_grid {
        match direction {
            '^' => {
                if let Some(mat) = obstacles
                    .iter()
                    .filter(|x| x[1] == guard[1] && x[0] < guard[0])
                    .max_by_key(|x| x[0])
                {
                    for i in (mat[0] + 1..guard[0]).rev() {
                        let coords: [usize; 2] = [i, guard[1]];
                        visited.insert(coords);
                        guard = coords;
                    }
                    direction = rotate(direction);
                } else {
                    for i in (0..guard[0]).rev() {
                        let coords: [usize; 2] = [i, guard[1]];
                        visited.insert(coords);
                        guard = coords;
                    }
                    break;
                }
            }
            '>' => {
                if let Some(mat) = obstacles
                    .iter()
                    .filter(|x| x[0] == guard[0] && x[1] > guard[1])
                    .min_by_key(|x| x[1])
                {
                    for i in guard[1] + 1..mat[1] {
                        let coords: [usize; 2] = [guard[0], i];
                        visited.insert(coords);
                        guard = coords;
                    }
                    direction = rotate(direction);
                } else {
                    for i in guard[1] + 1..height {
                        let coords: [usize; 2] = [guard[0], i];
                        visited.insert(coords);
                        guard = coords;
                    }
                    break;
                }
            }
            'v' => {
                if let Some(mat) = obstacles
                    .iter()
                    .filter(|x| x[1] == guard[1] && x[0] > guard[0])
                    .min_by_key(|x| x[0])
                {
                    for i in guard[0] + 1..mat[0] {
                        let coords: [usize; 2] = [i, guard[1]];
                        visited.insert(coords);
                        guard = coords;
                    }
                    direction = rotate(direction);
                } else {
                    for i in guard[0] + 1..width {
                        let coords: [usize; 2] = [i, guard[1]];
                        visited.insert(coords);
                        guard = coords;
                    }
                    break;
                }
            }
            '<' => {
                if let Some(mat) = obstacles
                    .iter()
                    .filter(|x| x[0] == guard[0] && x[1] < guard[1])
                    .max_by_key(|x| x[1])
                {
                    for i in (mat[1] + 1..guard[1]).rev() {
                        let coords: [usize; 2] = [guard[0], i];
                        visited.insert(coords);
                        guard = coords;
                    }
                    direction = rotate(direction);
                } else {
                    for i in (0..guard[1]).rev() {
                        let coords: [usize; 2] = [guard[0], i];
                        visited.insert(coords);
                        guard = coords;
                    }
                    break;
                }
            }
            _ => break,
        }
    }
    visited.len()
}

fn rotate(direction: char) -> char {
    match direction {
        '^' => '>',
        '>' => 'v',
        'v' => '<',
        '<' => '^',
        _ => direction, // Default case if the direction is not recognized
    }
}
