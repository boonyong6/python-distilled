# Not using `with` statement as it can't handle detached buffer.
f = open("filename.txt", "rt")  # Text-mode file
fb = f.detach()                 # Detach underlying binary mode file.
data = fb.read()                # Return bytes.
print(data)