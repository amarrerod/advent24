mod day1;

fn main() {
    let filename = "input.txt";
    let locations = day1::read_file(filename).unwrap_or(vec![]);
    println!("{:?}", locations);
    let total_distance = day1::part_one(&locations).unwrap_or_default();
    println!("{:}", total_distance);
    let score: i32 = day1::part_two(&locations).unwrap();
    println!("Similarity score: {score}");
}
