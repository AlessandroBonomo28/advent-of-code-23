/*
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
*/
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::env;
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

fn predict_next_value(sequences: &[Vec<i32>]) -> i32 {
    let mut sum = 0;
    for i in (0..sequences.len()).rev() {
        sum += sequences[i][sequences[i].len()-1];
    }
    sum
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Please provide a filename");
        return;
    }
    let filename : &String = &args[1];
    let mut total = 0;
    if let Ok(lines) = read_lines(filename) {
        for line in lines {
            if let Ok(values_str) = line {
                let values : Vec<&str> = values_str.split(" ").collect();
                
                let sequence: Vec<i32> = values
                    .iter()
                    .map(|&s| s.parse().expect("Failed to parse integer"))
                    .collect();
                
                let mut sequences : Vec<Vec<i32>> = vec![sequence.clone()];
                
                for i in 1..sequence.len() {
                    let sub_sequence = create_sub_sequence(&sequences[i-1]);
                    let is_zero : bool = is_zero_sequence(&sub_sequence);
                    if is_zero {
                        sequences.push(sub_sequence.clone());
                        break;
                    } else {
                        sequences.push(sub_sequence.clone());
                    }
                }

                let prediction : i32 = predict_next_value(&sequences);
                total += prediction;
                //println!("Predict: {}", prediction);
                //dbg!(sequences);
            }
        }
    }
    println!("Total: {}", total);
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}