# Nicholas Larsen, Tracing Notes

# What is tracing?

    #A debugging method that allows you to see things about your functions such as what called them, what they did, etc.

    #Syntax:
        # python -m trace --trace C:\Users\nick.larsen\Documents\CS2-Projects\Notes\Tracing\tracing.py
        # --trace (displays function lines as they are executed)
        # --count (displays the number of times each function is executed)
        # --listfuncs (displays the functions in the project)
        # --trackcalls (displays when functions are called)

# What are some ways we can debug by tracing?

    #Make a function that lets us see how our functions are interacting and runnning

# How do you access the debugger in VS Code?

    #F5
    #Litle bug by the arrow
    #Play button, run debug python file

# What is testing?

    #going through code and trying to break it

# What are boundary conditions?

    # User inputs that are strange, and may cause problems, highs, lows, or things most likely to be coded improperly.

# How do you handle when users give strange inputs?

    # try-except statements, conditionals, loops



import trace
import sys
tracer = trace.Trace(count=False,trace=True)
#frame has access to the current function, event has access to the event such as call, return, etc. Arg provides additional information about the event, such as the value of a return event.
def trace_calls(frame, event, arg):
    if event == 'call':
        print(f'Calling function: {frame.f_code.co_name}')
    elif event == 'line':
        print(f'Executing line: {frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'return':
        print(f'{frame.f_code.co_name} returned {arg}')
    elif event == 'exception':
        print(f'Exception in {frame.f_code.co_name}: {arg}')
    return trace_calls

sys.settrace(trace_calls)

"""
Event Types:

call - When the function is called
line - when a new line is executed
return - when the function returns a value
exception - when there is an exception raised
"""

def sub(num_one, num_two):
    return num_one - num_two

def add(num_one, num_two):
    print(sub(num_one, num_two))
    return num_one + num_two

print(add(5342, 4))

# tracer.run('sub(5342, 4)')