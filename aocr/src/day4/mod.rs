use itertools::{all, iproduct};
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_file(filename: &str) -> io::Result<Vec<Vec<String>>> {
    let data_file = Path::new(file!()).parent().unwrap().join(filename);

    let file = File::open(data_file)?;
    let reader = io::BufReader::new(file);
    let reports: Vec<Vec<String>> = reader
        .lines()
        .map(|line| {
            line.unwrap()
                .split("")
                .filter(|s| !s.is_empty())
                .map(String::from) // This line turns &str into String for safe return
                .collect::<Vec<String>>()
        })
        .collect();

    Ok(reports)
}

pub fn count_xmas_fun(matrix: &Vec<Vec<String>>) -> i32 {
    let expected_word: Vec<&str> = "XMAS".split("").filter(|s| !s.is_empty()).collect();
    let rows = matrix.len() as isize;
    let columns = matrix[0].len() as isize;

    iproduct!(0..rows, 0..columns)
        .filter(|&(i, j)| matrix[i as usize][j as usize] == "X")
        .map(|(i, j)| {
            iproduct!(-1..=1, -1..=1)
                .filter(|&(ni, nj)| !(ni == 0 && nj == 0))
                .map(|(ni, nj)| {
                    if (0..4).zip(expected_word.iter()).all(|(k, &c)| {
                        let ni = i + k * ni;
                        let nj = j + k * nj;
                        ni >= 0
                            && ni < rows
                            && nj >= 0
                            && nj < columns
                            && matrix[ni as usize][nj as usize] == *c
                    }) {
                        1
                    } else {
                        0
                    }
                })
                .sum::<i32>()
        })
        .sum()
}

fn count_mas_fun(matrix: &Vec<Vec<String>>) -> i32 {
    let rows = matrix.len() as isize;
    let columns = matrix[0].len() as isize;

    iproduct!(1..rows - 1, 1..columns - 1)
        .filter(|&(i, j)| matrix[i as usize][j as usize] == "A")
        .map(|(i, j)| {
            let i = i as usize;
            let j = j as usize;
            let left = &(matrix[i - 1][j - 1].to_owned() + &matrix[i][j] + &matrix[i + 1][j + 1]);
            let right = &(matrix[i - 1][j + 1].to_owned() + &matrix[i][j] + &matrix[i + 1][j - 1]);
            if all(&[left, right], |&x| x == "MAS" || x == "SAM") {
                1
            } else {
                0
            }
        })
        .sum::<i32>()
}

pub fn count_xmas(matrix: &Vec<Vec<String>>) -> i32 {
    let expected_word: Vec<&str> = "XMAS".split("").filter(|s| !s.is_empty()).collect();
    let rows = matrix.len() as isize;
    let columns = matrix[0].len() as isize;
    let mut xmas: i32 = 0;

    for i in 0..rows {
        for j in 0..columns {
            if matrix[i as usize][j as usize] == "X" {
                for (ni, nj) in iproduct!(-1..=1, -1..=1) {
                    if ni == nj && nj == 0 {
                        continue;
                    }
                    if (0..4).zip(expected_word.iter()).all(|(k, c)| {
                        let ni = i + k * ni;
                        let nj = j + k * nj;
                        ni >= 0
                            && ni < rows
                            && nj >= 0
                            && nj < columns
                            && matrix[ni as usize][nj as usize] == *c
                    }) {
                        xmas += 1;
                    }
                }
            }
        }
    }
    return xmas;
}

fn count_mas(matrix: &Vec<Vec<String>>) -> i32 {
    let rows = matrix.len() as isize;
    let columns = matrix[0].len() as isize;
    let mut xmas: i32 = 0;
    for i in 1..rows - 1 {
        for j in 1..columns - 1 {
            let i = i as usize;
            let j = j as usize;
            if matrix[i][j] == "A" {
                let left =
                    &(matrix[i - 1][j - 1].to_owned() + &matrix[i][j] + &matrix[i + 1][j + 1]);
                let right =
                    &(matrix[i - 1][j + 1].to_owned() + &matrix[i][j] + &matrix[i + 1][j - 1]);
                if all(&[left, right], |&x| x == "MAS" || x == "SAM") {
                    xmas += 1
                }
            }
        }
    }
    xmas
}

pub fn solve_parts() {
    println!("{:} Day 4 {:}", "=".repeat(20), "=".repeat(20));

    if let Some(data) = read_file("input.txt").ok() {
        let n_xmas = count_xmas_fun(&data);
        println!("The number of XMAS is {:}", n_xmas);
        let n_mas = count_mas_fun(&data);
        println!("The number of crossed MAS is: {:}", n_mas);
    }
}
