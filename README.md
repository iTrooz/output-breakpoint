# Output Breakpoint

This python script is a module for GDB that will trigger a breakpoint when a certain text is sent to stdout or stderr.
Then, you can run a backtrace (`bt` gdb command) to get the line of code that produced this text, or do anything else with the shell.

## Usage
`gdb --command=output_breakpoint.py --args <executable_file>`

## Others
Legacy version using a gdb script: https://gist.github.com/iTrooz/cc2b7e676fa7e73b5c089c81bf76ac45