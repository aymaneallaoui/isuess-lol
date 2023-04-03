from github import Github
import datetime

access_token = "fuck twitter"
g = Github(access_token)


repository_name = "username/repo-name"
repo = g.get_repo(repository_name)


troll_threshold = 10

for issue in repo.get_issues(state="open"):
    num_troll_comments = 0
    for comment in issue.get_comments():
        if "troll phrase" in comment.body:
            num_troll_comments += 1
    if num_troll_comments >= troll_threshold:

        message = "This issue has been automatically closed due to trolling you fucking nerd fat . Please contact stfu."
        issue.create_comment(message)
        issue.edit(state="closed")
