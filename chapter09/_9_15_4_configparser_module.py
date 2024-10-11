import configparser

# Create a config parser and read a file.
cfg = configparser.ConfigParser()
cfg.read("config.ini")

# Extract values
a = cfg.get("section1", "name1")
b = cfg.get("section2", "name2")

print(a, b)