import re


js_code = """
// program to find the factorial of a number

// take input from the user
const number = parseInt(prompt('Enter a positive integer: '));

// checking if number is negative
if (number < 0) {
    console.log('Error! Factorial for negative number does not exist.');
}

// if number is 0
else if (number === 0) {
    console.log(`The factorial of ${number} is 1.`);
}

// if number is positive
else {
    let fact = 1;
    for (i = 1; i <= number; i++) {
        fact *= i;
    }
    console.log(`The factorial of ${number} is ${fact}.`);
}
"""


def js_to_python(js):
    python = js
    # Replace let and const with variable assignments
    python = re.sub(r"let (.*) = (.*);", r"\1 = \2", python)
    python = re.sub(r"const (.*) = (.*);", r"\1 = \2", python)

    # Replace function definition with def
    python = re.sub(r"function (.*)\((.*)\)", r"def \1(\2)", python)

    # Replace return with return
    python = re.sub(r"return (.*);", r"return \1", python)

    # Replace console.log with print
    python = re.sub(r"console\.log\((.*)\)", r"print(\1)", python)
    # label = False
    lines = python.splitlines()
    counter = 0
    label = False
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = ("    " * counter) + lines[i]
        if "{" in lines[i]:
            lines[i] = re.sub("{", ":", lines[i])
            counter += 1
        if "}" in lines[i]:
            lines[i] = re.sub("}", "", lines[i])
            counter -= 1
        # print(lines[i])

    updatePython = ""
    for i in lines:
        updatePython += i + "\n"

    return updatePython


python_code = js_to_python(js_code)
print(python_code)
