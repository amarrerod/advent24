use itertools::enumerate;
use regex::Regex;
use std::fs::{self};
use std::io::{self};
use std::path::Path;

fn read_file(filename: &str) -> io::Result<Vec<[i128; 6]>> {
    let re = Regex::new(
        r"Button\sA:\sX\+(\d+),\sY\+(\d+)\nButton\sB:\sX\+(\d+),\sY\+(\d+)\nPrize:\sX=(\d+),\sY=(\d+)",
    ).unwrap();
    let data_file = Path::new(file!()).parent().unwrap().join(filename);
    let mut numbers = Vec::new();
    let content: String = fs::read_to_string(data_file)?;
    for (_, [ax, ay, bx, by, px, py]) in re.captures_iter(&content).map(|c| c.extract()) {
        numbers.push([
            ax.parse::<i128>().unwrap(),
            ay.parse::<i128>().unwrap(),
            bx.parse::<i128>().unwrap(),
            by.parse::<i128>().unwrap(),
            px.parse::<i128>().unwrap(),
            py.parse::<i128>().unwrap(),
        ]);
    }
    Ok(numbers)
}

fn divmod(dividend: i128, divisor: i128) -> (i128, i128) {
    let n = dividend / divisor;
    let r = dividend % divisor;
    (n, r)
}

fn is_possible_to_win(configuration: &[i128; 6]) -> [i128; 2] {
    let [ax, ay, bx, by, x, y] = configuration;
    let det: i128 = ax * by - bx * ay;
    let mut solution = [0, 0];
    for (i, (x, y)) in enumerate([
        (*x, *y),
        (x + 10000000000000 as i128, y + 10000000000000 as i128),
    ]) {
        let (na, ra) = divmod(by * x - bx * y, det);
        let (nb, rb) = divmod(ax * y - ay * x, det);
        if (na >= ra && ra == 0) && (rb == 0 && rb <= nb) {
            solution[i] = 3 * na + nb;
        }
    }
    solution
}

pub fn solve_parts() {
    println!("{:} Day 13 {:}", "=".repeat(20), "=".repeat(20));
    if let Ok(configurations) = read_file("input.txt") {
        let results = configurations
            .iter()
            .map(|config| is_possible_to_win(config))
            .fold([0i128; 2], |acc, item| [acc[0] + item[0], acc[1] + item[1]]);
        println!("The results are: {:?}", results);
    }
}
