use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

#[derive(Debug, Clone)]
struct Marker {
    start: i64,
    end: i64,
    chars: i64,
    repeat: i64,
}

fn find_next_marker(input: &str, start: usize) -> Option<Marker> {
    assert!(input.is_ascii());

    if start >= input.len() {
        return None;
    }

    let chars: Vec<char> = input.chars().collect();
    let mut marker = Marker {
        start: -1,
        end: -1,
        chars: -1,
        repeat: -1,
    };

    for i in start..input.len() {
        if chars[i] == '(' {
            marker.start = i as i64;
        } else if chars[i] == ')' && marker.end < 0 {
            if marker.start > -1 {
                marker.end = i as i64;
                break;
            }
        }
    }

    if marker.start > -1 && marker.end > -1 {
        let pairs: Vec<&str> = input[marker.start as usize + 1..marker.end as usize]
            .split("x")
            .collect();
        assert!(pairs.len() == 2);

        marker.chars = pairs[0].parse::<i64>().unwrap();
        marker.repeat = pairs[1].parse::<i64>().unwrap();

        return Some(marker);
    }

    None
}

fn decompress(input: &String) -> String {
    let mut pos = 0;

    let mut current: String = input.clone();
    loop {
        if let Some(marker) = find_next_marker(current.as_ref(), pos) {
            let pattern =
                &current[(marker.end + 1) as usize..(marker.end + 1 + marker.chars) as usize];

            let mut replacements = "".to_string();

            for _ in 0..marker.repeat {
                replacements.push_str(pattern);
            }

            current.replace_range(
                marker.start as usize..(marker.end + 1 + marker.chars) as usize,
                &replacements,
            );

            pos = marker.start as usize + replacements.len();
        } else {
            break;
        }
    }

    current
}

fn solve1(filename: &str) -> u64 {
    let mut length = 0;

    for line in lines_from_file(filename) {
        length += decompress(&line)
            .chars()
            .filter(|c| !c.is_whitespace())
            .collect::<String>()
            .len();
    }

    length as u64
}

fn solve2(filename: &str) -> u64 {
    0
}

fn lines_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

fn main() {
    println!("{}", solve1("input.txt"));
    println!("{}", solve2("input.txt"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_next_marker() {
        let m = find_next_marker("apa", 0);
        assert_eq!(m.is_none(), true);

        let m = find_next_marker("apa(2x32)", 0);
        assert_eq!(m.is_none(), false);
        let mu = m.unwrap();
        assert_eq!(mu.start, 3);
        assert_eq!(mu.end, 8);
        assert_eq!(mu.chars, 2);
        assert_eq!(mu.repeat, 32);

        let m = find_next_marker("apa(1x1", 0);
        assert_eq!(m.is_none(), true);

        let m = find_next_marker("apa(2x32)(32x2)", 0);
        assert_eq!(m.is_none(), false);
        let mu = m.unwrap();
        assert_eq!(mu.start, 3);
        assert_eq!(mu.end, 8);
        assert_eq!(mu.chars, 2);
        assert_eq!(mu.repeat, 32);

        let m = find_next_marker("apa(2x32)(32x2)", 9);
        assert_eq!(m.is_none(), false);
        let mu = m.unwrap();
        assert_eq!(mu.start, 9);
        assert_eq!(mu.end, 14);
        assert_eq!(mu.chars, 32);
        assert_eq!(mu.repeat, 2);
    }

    #[test]
    fn test_decompress() {
        assert_eq!(decompress(&"ADVENT".to_string()), "ADVENT".to_string());
        assert_eq!(decompress(&"A(1x5)BC".to_string()), "ABBBBBC".to_string());
        assert_eq!(decompress(&"(3x3)XYZ".to_string()), "XYZXYZXYZ".to_string());
        assert_eq!(
            decompress(&"A(2x2)BCD(2x2)EFG".to_string()),
            "ABCBCDEFEFG".to_string()
        );
        assert_eq!(decompress(&"(6x1)(1x3)A".to_string()), "(1x3)A".to_string());
        assert_eq!(
            decompress(&"X(8x2)(3x3)ABCY".to_string()),
            "X(3x3)ABC(3x3)ABCY".to_string()
        );
    }
}
