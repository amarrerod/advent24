use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_file(filename: &str) -> io::Result<Vec<Vec<i32>>> {
    let data_file = Path::new(file!()).parent().unwrap().join(filename);

    let file = File::open(data_file)?;
    let reader = io::BufReader::new(file);
    let mut col1: Vec<i32> = Vec::new();
    let mut col2: Vec<i32> = Vec::new();
    for line in reader.lines() {
        let line = line?;
        let parts: Vec<&str> = line.split_whitespace().collect();
        if let (Ok(x), Ok(y)) = (parts[0].parse::<i32>(), parts[1].parse::<i32>()) {
            col1.push(x);
            col2.push(y);
        }
    }
    Ok(vec![col1, col2])
}

fn part_one(locations: &Vec<Vec<i32>>) -> Result<i32, i32> {
    if locations.len() != 2 {
        println!("Error in the size of the locations");
        return Err(-1);
    }
    let mut col1 = locations[0].clone();
    let mut col2 = locations[1].clone();
    col1.sort();
    col2.sort();
    let total_distance = col1.iter().zip(col2).map(|(a, b)| (a - b).abs()).sum();
    Ok(total_distance)
}

fn part_two(locations: &Vec<Vec<i32>>) -> Result<i32, i32> {
    let counter: HashMap<i32, i32> = locations[1].iter().fold(HashMap::new(), |mut acc, item| {
        *acc.entry(*item).or_insert(0) += 1;
        acc
    });
    let score: i32 = locations[0]
        .iter()
        .map(|n| n * counter.get(n).unwrap_or(&0))
        .sum();

    Ok(score)
}

pub fn solve_parts() {
    println!("{:} Day 1 {:}", "=".repeat(20), "=".repeat(20));
    let filename = "input.txt";
    let locations = read_file(filename).unwrap_or(vec![]);
    let total_distance = part_one(&locations).unwrap_or_default();
    println!("Total distance {:}", total_distance);
    let score: i32 = part_two(&locations).unwrap();
    println!("Similarity score: {score}");
}
