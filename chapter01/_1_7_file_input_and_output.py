# Once control leaves the with statement block, the file is automatically closed.
print('-> with')

with open("data.txt") as file:
    for line in file:
        print(line, end='')  # end='' omits the extra newline

# If you don't use the with statement...
print('-> w/o with')

file = open('data.txt')
for line in file:
    print(line, end='') # end='' omits the extra newline
file.close()

# Use read() to read the entire file as a string.
print('-> read()')

with open('data.txt') as file:
    data = file.read()

print(data, end='')

# To read in chunks
print('-> chunk')

with open('data.txt') as file:
    while (chunk := file.read(10000)): # 10,000 bytes per chunk
        print(chunk, end='')

# To read in chunks (Alternative)
print('-> chunk (alternative)')

with open('data.txt') as file:
    while True:
        chunk = file.read(10000)
        if not chunk:
            break
        print(chunk, end='')

# Print to file stream.
print('-> Write to file')

year = 1
num_years = 10
principal = 12345.6789
rate = 0.06

with open('out.txt', 'wt') as out:
    while year <= num_years:
        principal = principal * (1 + rate)
        # print(f'{year:>3d} {principal:0.2f}', file=out)
        out.write(f'{year:3d} {principal:0.2f}\n')
        year += 1

# To work with a file that use a different encoding (default: UTF-8).
print('-> diff encoding')

with open('data.txt', encoding='latin-1') as file:
    data = file.read()

# To read the user input.
name = input('Enter your name: ')
print('Hello', name)