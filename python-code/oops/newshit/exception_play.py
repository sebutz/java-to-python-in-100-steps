# exceptions

# in Python there are no checked exceptions
# all the exceptions are unchecked
# when an exception occurred we don't want to throw to the outside world

i = 0
j = 10
try:
    k = j/i
except ZeroDivisionError:
    print("Exception")
    k = 0
finally:
    print("for sure it will be executed")

print(k)

# catching multiple exceptions
try:
    k = j/i
    j.length = 4
except (ZeroDivisionError, AttributeError):
    print("Exception")
    k = 0
finally:
    print("for sure it will be executed")
print("k")

# try - except - else
i = 4
try:
    k = j/i
except ZeroDivisionError:
    print("Exception")
else:
    print("Just in case there is no exception")
finally:
    print("for sure it will be executed")


# you want to use that exception info to log it for example
i = 0  # type: int
try:
    k = j/i
except ZeroDivisionError as error:
    print("Exception was", error)   # Exception was division by zero
else:
    print("Just in case there is no exception")
finally:
    print("for sure it will be executed")


# you want to use that exception info to log it for example
# let's go up in hierarchy: ArithmeticError
i = 0  # type: int
try:
    k = j/i
except ArithmeticError as error:
    print("Exception was", error)   # still the same message:  Exception was division by zero
else:
    print("Just in case there is no exception")
finally:
    print("for sure it will be executed")


# you want to use that exception info to log it for example
# let's go up in hierarchy: Exception
i = 0  # type: int
try:
    k = j/i
except Exception as error:
    print("Exception was", error)   # still the same message:  Exception was division by zero
else:
    print("Just in case there is no exception")
finally:
    print("for sure it will be executed")


'''
 object
        BaseException
            Exception
                ArithmeticError
                    FloatingPointError
                    OverflowError
                    ZeroDivisionError
                AssertionError
                AttributeError
                BufferError
                EOFError
                ImportError
                    ModuleNotFoundError
                LookupError
                    IndexError
                    KeyError
                MemoryError
                NameError
                    UnboundLocalError
                OSError
                    BlockingIOError
                    ChildProcessError
                    ConnectionError
                        BrokenPipeError
                        ConnectionAbortedError
                        ConnectionRefusedError
                        ConnectionResetError
                    FileExistsError
                    FileNotFoundError
                    InterruptedError
                    IsADirectoryError
                    NotADirectoryError
                    PermissionError
                    ProcessLookupError
                    TimeoutError
                ReferenceError
                RuntimeError
                    NotImplementedError
                    RecursionError
                StopAsyncIteration
                StopIteration
                SyntaxError
                    IndentationError
                        TabError
                SystemError
                TypeError
                ValueError
                    UnicodeError
                        UnicodeDecodeError
                        UnicodeEncodeError
                        UnicodeTranslateError
                Warning

'''

