from stackapi import StackAPI

currentSite = StackAPI('stackoverflow')

questions = currentSite.fetch('questions')

questionItems = questions['items']



idList = []

for item in questionItems:

    idList.append(item['question_id'])

    # reputation = item['owner']['reputation']

    
#for 0 -- 100 = 500

answers = currentSite.fetch('questions/{ids}/answers', ids = idList[0:100])
answersItems = answers['items']

for item in answersItems:

    # print(item)
    print(item['question_id'])
