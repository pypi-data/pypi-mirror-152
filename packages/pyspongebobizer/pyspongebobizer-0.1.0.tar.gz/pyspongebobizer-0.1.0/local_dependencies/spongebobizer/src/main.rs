#![allow(unused_parens)]
use std::io;
use std::io::Read;

use spongebobizer::process_string;

fn main() {
	let mut buf = [0; 65536];
	let mut stdin = io::stdin();
	// TODO:  Test for correctness when processing large input that includes multibyte chars; I have a sneaking suspicion that this will fail if a char spans the boundary between reads.
	loop {
		let count = stdin.read(&mut buf).unwrap();
		if(count == 0) {
			break;
		}
		print!("{}", process_string(std::str::from_utf8(&buf[0..count]).unwrap()));
	}
	println!();
}

