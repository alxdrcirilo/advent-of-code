extern crate meval;
use meval::eval_str;
use std::fs::read_to_string;

pub fn run() {
    let input: String = read_to_string("input/day07.txt").unwrap();

    println!("Result for Part 1: {}", solve1(&input));
}

fn solve1(input: &String) -> usize {
    let mut result: usize = 0;
    for line in input.lines() {
        let parts: Vec<&str> = line.split(":").collect();
        let res: usize = parts[0].parse().unwrap();
        let values: Vec<&str> = parts[1].split_whitespace().collect();

        let operators = ['+', '*'];
        let mut combinations: Vec<Vec<char>> = Vec::new();
        generate_combinations(
            &operators,
            values.len() - 1,
            &mut Vec::new(),
            &mut combinations,
        );
        result += get_val(combinations, values, res);
    }
    result
}

fn generate_combinations(
    operators: &[char],
    length: usize,
    current: &mut Vec<char>,
    combinations: &mut Vec<Vec<char>>,
) {
    if current.len() == length {
        combinations.push(current.clone());
        return;
    }
    for &op in operators {
        current.push(op);
        generate_combinations(operators, length, current, combinations);
        current.pop();
    }
}

fn get_val(combinations: Vec<Vec<char>>, values: Vec<&str>, res: usize) -> usize {
    for comb in combinations {
        let mut temp: usize =
            eval_str(values[0].to_string() + &comb[0].to_string() + values[1]).unwrap() as usize;
        if temp == res && values.len() == 2 {
            return res;
        }
        for i in 1..values.len() - 1 {
            temp =
                eval_str(temp.to_string() + &comb[i].to_string() + values[i + 1]).unwrap() as usize;
        }
        if temp == res {
            return res;
        }
    }
    0
}
