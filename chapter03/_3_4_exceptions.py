# Reraise caught exception
try:
    file = open("bar.txt", "rt")
except FileNotFoundError as e:
    print("=> Do some logging and re-raise the exception...")
    # raise  # Reraise current exception.


# Catch multiple exceptions.
try:
    print("=> Do something")
    nan = int("NaN")
except (TypeError, ValueError) as e:
    print("=> Handle Type or Value errors.")


# To ignore an exception.
try:
    nan = int("NaN")
except ValueError:
    pass  # <--


# To catch all exceptions except those related to program exit.
try:
    nan = int("NaN")
    raise SystemExit('"Exception" type don\'t catch exceptions related to program exit.')
except Exception as e:
    print(f"An error occurred: {e!r}")  # !r tells Python to use the __repr__.


# try-except-else
try:
    file = open("bar.txt", "rt")
except FileNotFoundError as e:
    print(f"Unable to open bar: {e}")
    data = ""
else:  # executed if the try block doesn't raise an exception.
    data = file.read()
    file.close()

