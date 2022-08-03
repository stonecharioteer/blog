---
author: Vinay Keerthi - Merkle Science
date: 22 March 2022
---
```bash
$ python -m this | head -n 4 | tail -n 1
```
# Explicit is Better than Implicit

## Rust for Pythonistas

This talk was delivered on 26 Mar, 2022, at the BangPypers monthly meetup. This
was a virual talk, and the video is hosted here and [the slides are available
here.](https://docs.google.com/presentation/d/1iYmAtGr7jrhYmXe6E8DgXMe-C9j4096WiNEcZSX8wXY)

## Running the examples

All examples shown in the video are available here. Note that you'll need to
[install Rust and Cargo](https://rustup.rs/) to use them.

Some sections of the code will be commented out, in order to allow them to
compile, but if you want to see the errors, uncomment any code that is
commented out. To make this easier to find, I'll add a comment above these
blocks with `// ERROR IF UNCOMMENTED`.

To run the examples, you can just run `cargo run -- --number <Example number>`.

To read the examples, ignore the `src/main.rs` and other files, focus only on
the files within `src/examples/exNN` folders. Each of these files will have a
`run` function that contains the main logic.

When reading the examples, note that the line that reads `pub fn run()` is
*usually* going to be in a `main.rs` file, and it will instead be `fn main()`.
I've had to change this because I'm shipping this as a command-line interface.
