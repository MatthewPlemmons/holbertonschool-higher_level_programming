#!/usr/bin/python3


def write_file(filename="", text=""):
    char_written = 0
    with open(filename, mode="w", encoding="utf-8") as f:
        for char in text:
            f.write(char)
            char_written += 1
    return char_written
