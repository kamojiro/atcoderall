# Usage

## Requirements
Please install a compiler for Rust language (see https://www.rust-lang.org).

## Input Generation
`in` directory contains 50 pre-generated input files, which are different from the inputs for the provisional tests or system tests.
If you want more inputs, prepare `seeds.txt` which contains a list of random seeds (unsigned 64bit integers) and execute the following command.
```
cargo run --release --bin gen < seeds.txt
```

This will output input files into `in` directory.

## Visualization
```
cargo run --release --bin vis <input_file> <output_file>
```
Given an input file and an output file, the above command writes a visualization result to `out.svg`.
It also outputs the score to standard output.
You can open the svg file using image viewers, web browsers, or via `vis.html` file.

In `out.svg`, each rectangle is colored according to the ratio of the desired area to the actual area.
The larger the actual area is, the redder the color is, and the smaller the area is, the bluer the color is.
If the desired area and the actual area are almost equal, the color is purple.
The correspondence between a rectangle and a company is shown by a line segment connecting the desired position and the center of the rectangle.
The number written in the center of the rectangle indicates the ID of the company.
