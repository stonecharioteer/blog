import os
import pathlib
import jinja2

problems = [
    # striver day 1
    ("Set Matrix Zeroes", "https://leetcode.com/problems/set-matrix-zeroes/", 73, "MEDIUM","striver-1","leetcode"),
    ("Pascal's Triangle", "https://leetcode.com/problems/pascals-triangle/", 118, "EASY","striver-1","leetcode"),
    ("Next Permutation", "https://leetcode.com/problems/next-permutation/", 31, "MEDIUM","striver-1","leetcode"),
    ("Kadane's Algorithm", "https://leetcode.com/problems/maximum-subarray/", 53, "EASY","striver-1","leetcode"),
    ("Sort an array of 0's 1's 2's", "https://leetcode.com/problems/sort-colors/", 75, "MEDIUM","striver-1","leetcode"),
    ("Stock Buy and Sell", "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/", 121, "EASY","striver-1","leetcode"),
    # striver day 2
    ("Rotate Matrix", "https://leetcode.com/problems/rotate-image/", 48, "MEDIUM", "striver-2", "leetcode"),
    ("Merge Overlapping Subintervals", "https://leetcode.com/problems/merge-intervals/", 56, "MEDIUM", "striver-2", "leetcode"),
    ("Merge two sorted Arrays without extra space", "https://leetcode.com/problems/merge-sorted-array/", 88, "EASY", "striver-2", "leetcode"),
    ("Find the duplicate in an array of N+1 integers", "https://leetcode.com/problems/find-the-duplicate-number/", 287, "MEDIUM", "striver-2", "leetcode"),
    # this is not on leetcode?
    ("Repeat and Missing Number", "https://www.interviewbit.com/problems/repeat-and-missing-number-array/", None, "MEDIUM", "striver-2", "interviewbit"),
    ("Inversion of Array (Pre-req: Merge Sort)", "https://www.codingninjas.com/codestudio/problems/count-inversions_615", None, "MEDIUM", "striver-2","codingninjas"), 
    # striver day 3
    ("Search in a 2d Matrix", "https://leetcode.com/problems/search-a-2d-matrix/", 74, "MEDIUM", "striver-3", "leetcode"),
    ("Pow(X,n)", "https://leetcode.com/problems/powx-n/", 50, "MEDIUM", "striver-3", "leetcode"),
    ("Majority Element (>N/2 times)", "https://leetcode.com/problems/majority-element/", 169, "EASY", "striver-3", "leetcode"),
    ("Majority Element (>N/3 times)", "https://leetcode.com/problems/majority-element-ii/", 229, "MEDIUM", "striver-3", "leetcode"),
    ("Grid Unique Paths", "https://leetcode.com/problems/unique-paths/", 62, "MEDIUM", "striver-3", "leetcode"),
    ("Reverse Pairs (Leetcode)", "https://leetcode.com/problems/reverse-pairs/", 493, "HARD", "striver-3", "leetcode" ),
    # Striver day 4
    ("2-Sum-Problem", "https://leetcode.com/problems/two-sum/", 1, "EASY", "striver-4", "leetcode"),
    ("4-sum-Problem", "https://leetcode.com/problems/4sum/", 18, "MEDIUM", "striver-4", "leetcode"),
    ("Longest Consecutive Sequence", "https://leetcode.com/problems/longest-consecutive-sequence/", 128, "MEDIUM", "striver-4", "leetcode"),
    # not leetcode?
    ("Largest Subarray with 0 sum","https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1", None, "EASY", "striver-4", "geeksforgeeks"),
    ("Count number of subarrays with given Xor K", "https://www.interviewbit.com/problems/subarray-with-given-xor/", None, "MEDIUM", "striver-4", "interviewbit"),
    ("Longest Substring without repeat", "https://leetcode.com/problems/longest-substring-without-repeating-characters/", 3, "MEDIUM", "striver-4", "leetcode"),
    # striver 5
    ("Reverse a LinkedList", "https://leetcode.com/problems/reverse-linked-list/", 206, "EASY", "striver-5", "leetcode"),
    ("Find the middle of LinkedList", "https://leetcode.com/problems/middle-of-the-linked-list/", 876, "EASY", "striver-5", "leetcode"),
    ("Merge two sorted Linked List (use method used in mergeSort)", "https://leetcode.com/problems/merge-two-sorted-lists/", 21, "EASY", "striver-5", "leetcode"),
    ("Remove N-th node from back of LinkedList", "https://leetcode.com/problems/remove-nth-node-from-end-of-list/", 19, "MEDIUM", "striver-5", "leetcode"),
    ("Add two numbers as LinkedList", "https://leetcode.com/problems/add-two-numbers/", 2, "MEDIUM", "striver-5", "leetcode"),
    ("Delete a given Node when a node is given. (0(1) solution)", "https://leetcode.com/problems/delete-node-in-a-linked-list/", 237, "EASY", "striver-5", "leetcode"),
    # striver 6
    ("Find intersection point of Y LinkedList", "https://leetcode.com/problems/intersection-of-two-linked-lists/", 160, "EASY", "striver-6", "leetcode"),
    ("Detect a cycle in Linked List", "https://leetcode.com/problems/linked-list-cycle/", 141, "EASY", "striver-6", "leetcode"),
    ("Reverse a LinkedList in groups of size k", "https://leetcode.com/problems/reverse-nodes-in-k-group/", 25, "HARD", "striver-6", "leetcode"),
    ("Check if a LinkedList is palindrome or not", "https://leetcode.com/problems/palindrome-linked-list/", 234, "EASY", "striver-6", "leetcode"),
    ("Find the starting point of the Loop of LinkedList", "https://leetcode.com/problems/linked-list-cycle-ii/", 142, "MEDIUM", "striver-6", "leetcode"),
    ("Flattening of a LinkedList", "https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1", None, "MEDIUM", "striver-6", "geeksforgeeks"),
    ("Rotate a LinkedList", "https://leetcode.com/problems/rotate-list/description/", 61, "MEDIUM", "striver-6", "leetcode"),
    # ("", "", , "", "striver-6", "leetcode"),

]

current_directory = pathlib.Path(os.path.realpath(__file__)).parent
with open("template.py", "r") as f:
    template = jinja2.Template(f.read())

with open("template-test.py", "r") as f:
    template_test = jinja2.Template(f.read())

with open("template-rst.txt", "r") as f:
    template_rst = jinja2.Template(f.read())

for (name, link, number, level, label, source) in problems:
    short_name = link[:-1][link[:-1].rfind("/") + 1 :].replace("-", "_")
    level = level.lower()
    if source != "leetcode":
        print(f"Skipping {name} from {source}")
        continue
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
                        solution_path=solution_path
                        )
                    )
            print("Created {} in {}".format(rst_file_path.name, rst_file_path.parent))
print("Done creating files")
