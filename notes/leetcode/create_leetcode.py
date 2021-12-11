import os
import pathlib
import jinja2

problems = [
    (
        "Set Matrix Zeroes",
        "https://leetcode.com/problems/set-matrix-zeroes/",
        73,
        "MEDIUM",
    ),
    (
        "Pascal's Triangle",
        "https://leetcode.com/problems/pascals-triangle/",
        118,
        "EASY",
    ),
    (
        "Next Permutation",
        "https://leetcode.com/problems/next-permutation/",
        31,
        "MEDIUM",
    ),
    (
        "Kadane's Algorithm",
        "https://leetcode.com/problems/maximum-subarray/",
        53,
        "EASY",
    ),
    (
        "Sort an array of 0's 1's 2's",
        "https://leetcode.com/problems/sort-colors/",
        75,
        "MEDIUM",
    ),
    (
        "Stock Buy and Sell",
        "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/",
        121,
        "EASY",
    ),
]

current_directory = pathlib.Path(os.path.realpath(__file__)).parent
with open("template.py", "r") as f:
    template = jinja2.Template(f.read())

with open("template-test.py", "r") as f:
    template_test = jinja2.Template(f.read())

for (name, link, number, level) in problems:
    level = level.lower()
    short_name = link[:-1][link[:-1].rfind("/") + 1 :].replace("-", "_")
    folder_name = current_directory / "solutions" / f"{number:04}_{short_name}"
    filename = folder_name / "solution.py"
    # make the solution file
    os.makedirs(folder_name, exist_ok=True)
    if not filename.exists():
        with open(filename, "w") as f:
            f.write(
                template.render(
                    link=link,
                    number=number,
                    short_name=short_name,
                    level=level,
                    name=name,
                )
            )
        print("Created {} in {}".format(filename.name, filename.parent))
    # make the test file
    test_path = current_directory / "tests" / level.lower()
    test_import_directory = filename.parent.relative_to(current_directory)
    test_file = test_path / f"test_{number:04}.py"
    os.makedirs(test_path, exist_ok=True)
    if not test_file.exists():
        with open(test_file, "w") as f:
            f.write(
                template_test.render(
                    link=link,
                    number=number,
                    level=level,
                    name=name,
                    short_name=short_name,
                    code_folder_path=test_import_directory,
                )
            )
        print("Created {} in {}".format(test_file.name, test_file.parent))

print("Done creating files")
