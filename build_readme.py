import os
import re
import requests


def get_work_info():
    """Get user's info from leetcode"""
    url = "https://alfa-leetcode-api.onrender.com/userProfile/tadod"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: ", response.status_code)
        return None


def get_ranking():
    url = "https://alfa-leetcode-api.onrender.com/tadod"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["ranking"]
    else:
        print("Error: ", response.status_code)
        return None


def get_badges():
    """Get user's badges from leetcode"""
    url = "https://alfa-leetcode-api.onrender.com/tadod/badges"
    response = requests.get(url)
    if response.status_code == 200:
        if response.json()["badgesCount"] == 0:
            return None
        return response.json()["badges"]
    else:
        print("Error: ", response.status_code)
        return None


def get_problems():
    """Get all problems from solutions directory"""
    dir = "./solutions"
    problems = {}

    for root, _, filenames in os.walk(dir):
        for filename in filenames:
            if filename.endswith('.py'):
                match = re.match(r"(\d+)_([a-zA-Z0-9_]+)\.py", filename)
                if match:
                    problem_id = int(match.group(1))
                    problem_name = match.group(2).replace('_', ' ').title()
                    topic = os.path.basename(root)
                    file_path = os.path.join(root, filename)

                    problems[problem_id] = {
                        'name': problem_name,
                        'topic': topic,
                        'path': file_path
                    }
    return problems


def build_readme():
    """Build README.md"""
    # Get information
    ranking = get_ranking()
    w = get_work_info()
    badges = get_badges()
    problems = get_problems()

    with open("README.md", "w") as f:
        # Repo badge
        badges = "<div align=\"center\">\n" + \
            "[![CI](https://github.com/fastify/fastify/workflows/ci/badge.svg)](https://github.com/fastify/fastify/actions/workflows/ci.yml)\n" + \
            "[![py-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://standardjs.com/)\n" + \
            "</div>\n\n"
        f.write(badges)

        # Heading 1
        f.write("# Daily solving LeetCode problems\n\n")

        # User
        if ranking is not None:
            f.write(f"### Ranking: {ranking}\n\n")

        if w is not None:
            f.write("### Progress: ")
            f.write(f"{w["totalSolved"]}/{w["totalQuestions"]}\n\n")
            f.write("| Difficulty | Solved | Total |\n")
            f.write("|------------|--------|-------|\n")
            f.write(f"| Easy | {w["easySolved"]} | {w["totalEasy"]} |\n")
            f.write(f"| Medium | {w["mediumSolved"]} | {w["totalMedium"]} |\n")
            f.write(f"| Hard | {w["hardSolved"]} | {w["totalHard"]} |\n\n")

        # Badges
        if badges is not None:
            f.write("## Badges\n\n")
            for badge in badges:
                img = "<img " + \
                    f"src=\"{badge["icon"]}\" " + \
                    "style=\"width: 100px;\" " + \
                    f"title=\"{badge["displayName"]}\" />"
                f.write(img)
            f.write("\n\n")

        # Problems
        f.write("## Problems solved\n\n")
        f.write("| Problem ID | Problem Name | Topic | Solution |\n")
        f.write("|------------|--------------|-------|------|\n")

        for problem_id, problem in sorted(problems.items()):
            problem_info = f"| {problem_id} | " + \
                f"[{problem["name"]}](https://leetcode.com/problems/{problem['name'].replace(' ', '-').lower()}) | " + \
                f"{problem["topic"]} | " + \
                f"[Solution]({problem["path"]}) |"
            f.write(problem_info + "\n")


if __name__ == "__main__":
    build_readme()
    print("README.md is built successfully!")
