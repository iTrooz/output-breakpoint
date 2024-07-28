# Output Breakpoint

This python script is a module for GDB that will trigger a breakpoint when a certain text is sent to stdout.
Then, you can run a backtrace (`bt` gdb command) to get the line of code that produced this text, or do anything else with the shell.

## Usage
`gdb --command=stdout_breakpoint.py --args <executable_file>`
