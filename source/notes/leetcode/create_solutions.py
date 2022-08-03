import os
import pathlib

import jinja2
import toml

current_directory = pathlib.Path(os.path.realpath(__file__)).parent
with open("template.py", "r") as f:
    template = jinja2.Template(f.read())

with open("template-test.py", "r") as f:
    template_test = jinja2.Template(f.read())

with open("template-rst.txt", "r") as f:
    template_rst = jinja2.Template(f.read())

with open("problems.toml", "r") as f:
    problems = toml.load(f)

assert "problems" in problems.keys(), (
    "There are no problems in the problems.toml file, or the definition is"
    "not as expected."
)
assert (
    "leetcode" in problems["problems"].keys()
), "There are no leetcode problems in the problems list"

lc_problems = problems["problems"]["leetcode"]

for problem_definition in lc_problems:
    link = problem_definition["url"]
    level = problem_definition["level"]
    number = problem_definition["number"]
    name = problem_definition["name"]
    short_name = link[:-1][link[:-1].rfind("/") + 1 :].replace("-", "_")
    level = level.lower()
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

    rst_file_path = current_directory / f"lc_{number:04}.rst"
    if not rst_file_path.exists():
        with open(rst_file_path, "w") as f:
            solution_path = filename.relative_to(current_directory)
            f.write(
                template_rst.render(
                    level=level,
                    link=link,
                    number=number,
                    short_name=short_name,
                    name=name,
                    solution_path=solution_path,
                )
            )
            print("Created {} in {}".format(rst_file_path.name, rst_file_path.parent))
print("Done creating files")
