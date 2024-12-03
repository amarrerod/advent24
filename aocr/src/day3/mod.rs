use regex::Regex;
use std::fs::File;
use std::io::{self, Read};
use std::path::Path;

fn read_file(filename: &str) -> io::Result<String> {
    let data_file = Path::new(file!()).parent().unwrap().join(filename);

    let mut file = File::open(data_file)?;
    let mut content: String = String::new();
    file.read_to_string(&mut content)?;
    Ok(content)
}

fn solve(content: &str) -> i32 {
    let re = Regex::new(r"mul\(\d+,\d+\)|do\(+\)|don\'t\(+\)").unwrap();
    let instructions: Vec<&str> = re.find_iter(content).map(|cap| cap.as_str()).collect();
    let mut compute: bool = true;
    let total_sum: i32 = instructions
        .into_iter()
        .map(|i| {
            if i == "don't()" {
                compute = false;
                0
            } else if i == "do()" {
                compute = true;
                0
            } else if compute {
                i[4..=(i.find(")").unwrap() - 1)]
                    .split(",")
                    .map(|x| x.parse::<i32>().unwrap_or(0))
                    .fold(1, |acc, item| acc * item)
            } else {
                0
            }
        })
        .sum();

    println!("The total sum is: {:#?}", total_sum);
    total_sum
}

pub fn solve_parts() {
    println!("{:} Day 3 {:}", "=".repeat(20), "=".repeat(20));

    let content = read_file("input.txt").unwrap_or(String::new());
    println!("{:}", content);
    solve(&content);
}
