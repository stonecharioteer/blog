"""Helper script to take the sorted json from leetcode and then convert it to a
neatly formatted toml file"""
import ast
import json

import toml

with open("data_sorted.json") as f:
    raw_data_lc = json.load(f)

data = {"problems": {"leetcode": raw_data_lc}}

for problem_id in data["problems"]["leetcode"]:
    row = data["problems"]["leetcode"][problem_id]
    row["questionId"] = int(row["questionId"])
    row["topicTags"] = [x["slug"] for x in row["topicTags"]]
    row["companyTagStats"] = json.loads(row["companyTagStats"])
    row["similarQuestions"] = json.loads(row["similarQuestions"])
    row["stats"] = json.loads(row["stats"])

with open("problems_1.toml", "w") as f:
    toml.dump(data, f)
