/*
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
*/
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn create_sub_sequence(main_seq :&[i32]) -> Vec<i32> {
    let mut sub_sequence: Vec<i32> = Vec::new();
    let mut i = 1;
    while i < main_seq.len() {
        let diff = main_seq[i] - main_seq[i-1];
        sub_sequence.push(diff);
        i += 1;
    }
    sub_sequence
}

fn is_zero_sequence(sequence: &[i32]) -> bool {
    let sum: i32 = sequence.iter().sum();
    sum == 0
}

fn main() {
    if let Ok(lines) = read_lines("./calibration.txt") {
        for line in lines {
            if let Ok(values_str) = line {
                let values : Vec<&str> = values_str.split(" ").collect();
                
                let sequence: Vec<i32> = values
                    .iter()
                    .map(|&s| s.parse().expect("Failed to parse integer"))
                    .collect();
                
                let sub_sequence = create_sub_sequence(&sequence);
                let sub_sequence2 = create_sub_sequence(&sub_sequence);
                println!("Main sequence:");
                dbg!(sequence); // print debug info
                println!("Subsequence:");
                dbg!(sub_sequence); 
                println!("Subsequence 2:");
                dbg!(sub_sequence2); 
                let is_zero = is_zero_sequence(&sub_sequence2);
                //println!("Is zero sequence: {}", is_zero);
                println!();
            }
        }
    }
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}