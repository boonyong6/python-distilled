import tempfile

with tempfile.TemporaryFile() as temp_file:
    print(f"Temp file location: {temp_file.name}")
    temp_file.write(b"Hello World")
    temp_file.seek(0)
    data = temp_file.read()
    print("Got:", data)

with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Temp dir location: {temp_dir}")
