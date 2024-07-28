import gdb


# ----- CONFIG
SEARCH_DATA = b"Hello" # Modify this to change the text to search for

# ----- CODE


gdb.execute("catch syscall write")

is_syscall_exit = True
def handle_breakpoint(event: gdb.BreakpointEvent):
    if event.breakpoint.number != 1: # Only handle the our catchpoint set above (the first defined)
        return

    # We only care about syscall exits, not both calls and exits
    # (Could also be just calls I guess)
    global is_syscall_exit
    is_syscall_exit = not is_syscall_exit
    if not is_syscall_exit:
        gdb.execute("continue")
        return
    
    written_fd = int(gdb.parse_and_eval("$rdi"))
    written_ptr = int(gdb.parse_and_eval("$rsi"))
    written_len = int(gdb.parse_and_eval("$rdx"))

    # Disable if you program copies the stdout or stderr fd
    # Check for stdout or stderr fd
    if written_fd != 1 and written_fd != 2:
        return
    
    print(f"Found write at fd {written_fd}")

    # Read data written to fd
    memory = gdb.selected_inferior().read_memory(written_ptr, written_len)
    b = memory.tobytes()

    # Check if it is what we are looking for
    if b.find(SEARCH_DATA) != -1:
        print("Found requested data !")
        # no "continue", so drops to shell
    else:
        gdb.execute("continue")
    

gdb.events.stop.connect(handle_breakpoint)

gdb.execute("run")
