import csv
from github import Github

g = Github("your_token")

with open('data/sample.csv') as readFile:
    with open('data/result.csv', 'w') as writeFile:
        reader = csv.reader(readFile)
        writer = csv.writer(writeFile, lineterminator='\n')

        for row in reader:

            repo = g.get_repo(row[0] + '/repo_name')
            pull = repo.get_pull(number = int(row[1]))
            
            # print('◆　レビュー対象：' + row[0])

            count = 0
            for comment in pull.get_review_comments():
                if comment.user.login != row[0]:
                    count += 1
                    # print('レビュー指摘' + str(count) + '-----------')
                    # print(comment.user.login)
                    # print(comment.body)

            writer.writerow([row[0], row[1], str(count)])