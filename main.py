from github import Github


g = Github("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")

user = "Open-Bootcamp"
try:
    for repo in g.get_user(user).get_repos():
        print("========",repo.name,"========")
        for commit in repo.get_commits():
            print(commit.commit.message)

except:
    print("repositorio vacío")