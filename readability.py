import re
from typing import List


def get_readability_score(code: str) -> float:
    # Calculate score as before
    score = 0

    lines = len(code.split("\n"))
    score += lines

    chars = len(code)
    score += chars

    spaces = len(re.findall(r"\s", code))
    score += spaces

    comments = len(re.findall(r"#.*?\n", code, re.DOTALL))
    score += comments * 2

    classes = len(re.findall(r"^class .*?:", code, re.MULTILINE))
    score += classes * 3

    functions = len(re.findall(r"^def .*?:", code, re.MULTILINE))
    score += functions * 4

    # Determine total possible score
    total_possible = (lines + chars) * 2

    # Calculate percentage
    percentage = score / total_possible * 100
    # percentage = min(percentage, 100)

    return percentage


file = input("Enter the path of file : ")

with open(file, "r") as f:
    code = f.read()

percentage = get_readability_score(code)
print(f"Readability score: {percentage:.2f}%")
