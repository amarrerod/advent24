use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashMap;


fn read_file(filename: &str) -> io::Result<(HashMap<u32, Vec<u32>>, Vec<Vec<u32>>)> {
    let data_file = Path::new(file!()).parent().unwrap().join(filename);

    let file = File::open(data_file)?;
    let reader = io::BufReader::new(file);

    let mut rules: HashMap<u32, Vec<u32>> = HashMap::new();
    let mut updates : Vec<Vec<u32>> = Vec::new();
    let mut update: bool = false;
    for line in reader.lines() {
        let line = line?;
        if line.is_empty() {
            update = true;
            continue;
        }
        if update {
            updates.push(line.split(",").map(|s| s.parse::<u32>().unwrap()).collect());
        } else {
            let values = line.split("|").map(|s| s.parse::<u32>().unwrap()).collect::<Vec<u32>>();
            rules.entry(values[0]).or_insert(vec![]);
            rules.entry(values[1]).or_insert(vec![]).push(values[0]);
        }
    }
   
    Ok((rules, updates))
}


fn check_update_is_correct(update: &Vec<u32>, rules: &HashMap<u32, Vec<u32>>) -> Vec<bool> {
    let mut correct: Vec<bool> = vec![];
    for i in 0..update.len() -1 {
        let r =  update[i+1..].iter().all(|&y| rules.get(&y).unwrap().contains(&update[i]));
        correct.push(r);
    }
    correct
}

fn compute_middle_page(rules: &HashMap<u32, Vec<u32>>, updates: &Vec<Vec<u32>>, part_one: bool) -> u32 {
    let mut sum_of_middles : u32 = 0;
    for update in updates {
        let mut correctness = check_update_is_correct(&update, &rules);
        if part_one {
            if correctness.iter().all(|&x| x) {
            sum_of_middles += update[update.len() / 2];
            }
        } else {
            if !correctness.iter().all(|&x| x) {
                // Fix the update
                let mut cloned_update = update.clone();
                while !correctness.iter().all(|&x| x) {
                    for i in 0..correctness.len() {
                        if !correctness[i] {
                            cloned_update.swap(i, i+1);
                        }
                        correctness = check_update_is_correct(&cloned_update, &rules);
                    }
                }
                sum_of_middles += cloned_update[cloned_update.len() / 2];
            }
        }
    }
    return sum_of_middles;
}





pub fn solve_parts() {
    println!("{:} Day 5 {:}", "=".repeat(20), "=".repeat(20));

    let (rules, updates) = read_file("input.txt").unwrap();
    let middle_page = compute_middle_page(&rules, &updates, true);
    println!("Middle page: {:?}", middle_page);
    let middle_page_fixed = compute_middle_page(&rules, &updates, false);
    println!("Middle page of fixed: {:?}", middle_page_fixed);
}