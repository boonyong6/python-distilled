import atexit


def cleanup():
    print("Cleaning up...")
    print("Program terminated.")


atexit.register(cleanup)

print("Program started.")

raise SystemExit("Exit on error.")
