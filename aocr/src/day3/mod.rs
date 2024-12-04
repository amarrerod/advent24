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

fn solve(content: &str) -> Result<i32, i32> {
    let re = Regex::new(r"mul\(\d+,\d+\)|do\(+\)|don\'t\(+\)").unwrap();
    let instructions: Vec<&str> = re.find_iter(content).map(|cap| cap.as_str()).collect();
    let mut compute: bool = true;
    let total_sum = instructions
        .into_iter()
        .map(|i| {
            if i == "don't()" {
                compute = false;
                Ok(0)
            } else if i == "do()" {
                compute = true;
                Ok(0)
            } else if compute {
                Ok(i[4..=(i.find(")").ok_or(-1)? - 1)]
                    .split(",")
                    .map(|x| x.parse::<i32>().map_err(|_| -2))
                    .fold(1, |acc, item| acc * item.unwrap()))
            } else {
                Ok(0)
            }
        })
        .collect::<Result<Vec<i32>, i32>>()
        .map(|results| results.into_iter().sum());

    println!("The total sum is: {:#?}", total_sum.unwrap());
    total_sum
}

pub fn solve_parts() {
    println!("{:} Day 3 {:}", "=".repeat(20), "=".repeat(20));

    let content = read_file("test2.txt").unwrap_or(String::new());
    println!("{:}", content);
    let r = solve(&content);
    match r {
        Err(_e) => println!("Error in the solution"),
        Ok(_) => {}
    }
}
