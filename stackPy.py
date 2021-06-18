from stackapi import StackAPI

sites = ['stackoverflow','askubuntu','softwareengineering']

# currentSite = StackAPI('stackoverflow')
cotaRestante = 300

currentSite = StackAPI('askubuntu')

while(cotaRestante >= cotaRestante - 50):

    questions = currentSite.fetch('questions')

    cotaRestante = questions['quota_remaining']

    questionItems = questions['items']



    idList = []

    for item in questionItems:

        idList.append(item['question_id'])
        
        # reputation = item['owner']['reputation']
        # print(item)
        
    #for 0 -- 100 = 500

    answers = currentSite.fetch('questions/{ids}/answers', ids = idList[0:100])
    answersItems = answers['items']

    for item in answersItems:

        # print(item)
        print(item['question_id'])
