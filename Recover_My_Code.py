# Description
# I lost my source code! All I have left are the tokens. Help me recover the source.

# Tokens
# Each token is represented as an array in the following format:

# {command, arg1, arg2}

# Example:

# {"set", "x", "5"}

# Commands
# Each valid command translates to a line of source code:

# {"set", "x", "5"} -> x = 5
# {"add", "y", "3"} -> y += 3
# {"sub", "a", "4"} -> a -= 4

# Rules
# The first argument is always a variable.
# The second argument is either a number or a variable.
# Task
# Given an array of tokens, return a string containing the reconstructed source code.

# Constraints
# Tokens are given in the order they should appear in the source code.
# Each command must be separated by a newline character (\n).
# Invalid commands should be ignored.
# Only set, add, and sub are valid commands.
# Variables consist only of letters [a-zA-Z] and may be longer than one character.
# Spaces in the output do not matter (a=5, a =5 and a = 5 are all valid).
# There should not be any empty lines in the output.
# If there are no valid commands, return an empty string.

from typing import Sequence


def restore_code(tokens: Sequence[Sequence[str]]) -> str:
    lines = []
    for token in tokens:
        if len(token) != 3:
            continue
        cmd, arg1, arg2 = token
        if cmd not in ("set", "add", "sub"):
            continue
        if not arg1.isalpha():
            continue
        if arg2.isalpha():
            pass
        elif arg2.isdigit():
            pass
        elif arg2 and arg2[0] == '-' and arg2[1:].isdigit():
            pass
        else:
            continue
        if cmd == "set":
            lines.append(f"{arg1} = {arg2}")
        elif cmd == "add":
            lines.append(f"{arg1} += {arg2}")
        elif cmd == "sub":
            lines.append(f"{arg1} -= {arg2}")
    return "\n".join(lines)s