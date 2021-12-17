import os


def get_file_to_move():
    source = input("Enter path to file (path to user catalog redundant): ")
    return source


def get_target():
    destination = input("Enter path to destination: (path to user redundant): ")
    return destination


def main():
    source = get_file_to_move()
    destination = get_target()
    # remove %USERPROFILE% if necessary
    os.system(fr"move %USERPROFILE%\{source} %USERPROFILE%\{destination}")
    print("Done!")


if __name__ == "__main__":
    main()
