# Output Breakpoint

This python script is a module for GDB that will trigger a breakpoint when a certain text is sent to stdout or stderr.
Then, you can run a backtrace (`bt` gdb command) to get the line of code that produced this text, or do anything else with the shell.

This script uses syscalls to detect content written, so it should be compatible with all languages (Rust, Go, C++ were tested)

## Usage
`gdb --command=output_breakpoint.py --args <executable_file>`

## Licence
GPL-2-or-later

## Others
Legacy version using a gdb script: https://gist.github.com/iTrooz/cc2b7e676fa7e73b5c089c81bf76ac45 (only work with C/C++)
