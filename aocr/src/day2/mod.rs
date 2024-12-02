use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::{Path, PathBuf};

fn read_file(filename: &str) -> io::Result<Vec<Vec<i32>>> {
    let data_file = Path::new(file!()).parent().unwrap().join(filename);

    let file = File::open(data_file)?;
    let reader = io::BufReader::new(file);
    let mut reports: Vec<Vec<i32>> = Vec::new();

    for line in reader.lines() {
        let line = line?;

        let parts: Vec<i32> = line
            .split_whitespace()
            .map(|n| n.parse::<i32>().unwrap())
            .collect();
        reports.push(parts);
    }
    Ok(reports)
}

fn is_report_safe(report: &Vec<i32>) -> bool {
    let differences: Vec<i32> = report.windows(2).map(|pair| pair[1] - pair[0]).collect();
    differences.iter().all(|d| 1 <= *d && *d <= 3)
        || differences.iter().all(|d| -3 <= *d && *d <= -1)
}

fn is_report_safe_2(report: &Vec<i32>) -> bool {
    if is_report_safe(report) {
        return true;
    } else {
        for i in 0..report.len() {
            let subreport = [&report[..i], &report[(i + 1)..]].concat();
            if is_report_safe(&subreport) {
                return true;
            }
        }
    }
    return false;
}

pub fn solve_parts() {
    let filename = "input.txt";
    let reports = read_file(filename).unwrap_or(vec![]);
    println!("{:?}", reports);
    let mut safe_reports = reports.iter().filter(|r| is_report_safe(r)).count();
    println!("Safe reports: {:}", safe_reports);
    safe_reports = reports.iter().filter(|r| is_report_safe_2(r)).count();
    println!("Safe reports 2: {:}", safe_reports);
}
