from stackapi import StackAPI

currentSite = StackAPI('stackoverflow')

questions = currentSite.fetch('questions')

questionItems = questions['items']



idList = []

for item in questionItems:

    idList.append(item['question_id'])



answers = currentSite.fetch('questions/{ids}/answers',ids = idList)

print(answers)