import csv
from github import Github
import time

g = Github("your_token")

repo = g.get_organization('org').get_repo('repo')
print(repo.name)

for project in repo.get_projects(state='open'):
    with open('data/' + project.name + '.csv', 'w') as writeFile:
        writer = csv.writer(writeFile, lineterminator='\n')

        for column in project.get_columns():
            print(project.name + '：' + column.name)
            if(column.get_cards().totalCount > 0):
                for card in column.get_cards():
                    issue = card.get_content()
                    time.sleep(1)
                    writer.writerow([column.name, issue.get_labels()[0].name])

