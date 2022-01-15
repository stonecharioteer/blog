import json
import os

import requests

# Fill in these details to be able to send a request, more details in README

HEADERS = {
    "x-csrftoken": os.environ["LC_X_CSRF_TOKEN"],
    "Referer": "https://leetcode.com/problems",
    "Cookie": os.environ["LC_COOKIE"],
}

graphql_url = "https://leetcode.com/graphql"

final_data = {}


# Get a list of all questions on Leetcode,
# we will query details for these question


def get_question_list():

    response = requests.get("https://leetcode.com/api/problems/all")
    raw_data = response.json()

    stat_status_pairs = raw_data["stat_status_pairs"]

    question_title_slug = [i["stat"]["question__title_slug"] for i in stat_status_pairs]

    return question_title_slug


# Post a GraphQL request for a given question,
# Query has the description of all the details we want,
# Query can be modified according to needs


def leech(question):
    query = """query questionData {
        question(titleSlug: "%s") {
          questionId
          title
          titleSlug
          content
          isPaidOnly
          difficulty
          likes
          dislikes
          similarQuestions
          exampleTestcases
          categoryTitle
          topicTags {
            slug
            }
          companyTagStats
          stats
          hints
          status
          sampleTestCase
          mysqlSchemas
          challengeQuestion {
              id
              date
              incompleteChallengeCount
              streakCount
              type
              __typename
          }
          }
        }""" % (
        question
    )
    r = requests.post(
        graphql_url,
        json={"query": query},
        headers=HEADERS,
    )

    r = r.json()
    r = r["data"]["question"]
    r["url"] = "https://leetcode.com/problems/" + str(r["titleSlug"])
    question_id_formatted = "{:04d}".format(int(r["questionId"]))
    final_data[question_id_formatted] = r


question_list = get_question_list()


# Call the leech function for all questions,
# Prints progress
import progressbar

with progressbar.ProgressBar(max_value=len(question_list)) as bar:
    for i, question in enumerate(question_list):
        leech(question)
        bar.update(i)


# Dump our Python dictionary to a JSON file

with open("data_1.json", "w") as file:
    json.dump(final_data, file)
