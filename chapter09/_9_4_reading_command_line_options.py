# Example 1: Manually process command-line arguments.
def main_1(argv):
    if len(argv) != 3:
        raise SystemExit(f"Usage: python {argv[0]} input_file output_file\n")
    input_file = argv[1]
    output_file = argv[2]
    print(f"{input_file=}, {output_file=}")


# Example 2: Use `argparse` module for more complicated command-line handling.
import argparse


def main_2(argv):
    arg_parser = argparse.ArgumentParser(description="This is some program.")

    # A positional argument.
    arg_parser.add_argument("in_file")

    # An option taking an argument.
    arg_parser.add_argument("-o", "--output", action="store")

    # An option that sets a Boolean flag.
    arg_parser.add_argument("-d", "--debug", action="store_true", default=False)

    # Parse the command line.
    args = arg_parser.parse_args(args=argv)

    # Retrieve the option settings.
    in_file = args.in_file
    output = args.output
    debug_mode = args.debug

    print(in_file, output, debug_mode)


if __name__ == "__main__":
    import sys

    # main_1(sys.argv)  # Example 1
    main_2(sys.argv[1:])
