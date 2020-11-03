import inspect

my_frame = inspect.currentframe()

print(my_frame) #<frame object at MEMORY_LOCATION>

print(my_frame.f_lineno) #this is line 7 so it prints 7
print(my_frame.f_code.co_filename) #filename of this code executing or '<pyshell#1>' etc.
print(my_frame.f_lineno) #this is line 9 so it prints 9


print(list('Hello, world!'.partition('w')))

print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')