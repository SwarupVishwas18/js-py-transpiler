import os
from converter import js_to_python
from colorama import Fore

# Test folder structure
test_dir = "sampleJS"

colors = [
    Fore.LIGHTBLUE_EX,
    Fore.CYAN,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX,
    Fore.YELLOW,
]

counter = 0

for subfolder in os.listdir(test_dir):
    print(Fore.LIGHTGREEN_EX)
    print("#" * 30)
    print(f"Converting subfolder: {subfolder}")
    print("#" * 30)

    subfolder_path = os.path.join(test_dir, subfolder)
    for js_file in os.listdir(subfolder_path):
        if js_file.endswith(".js"):
            js_path = os.path.join(subfolder_path, js_file)

            with open(js_path) as f:
                js_code = f.read()
            counter += 1
            factor = counter % len(colors)
            print(colors[factor])

            python_code = js_to_python(js_code)

            print(python_code)
            print()

print("Conversion complete!")
print(Fore.RESET)
