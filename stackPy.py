from stackapi import StackAPI
import time

sites = ['stackoverflow','askubuntu','softwareengineering','gaming','cstheory','math','dba']

# currentSite = StackAPI('stackoverflow')
cotaTotal = 300

for site in sites: 

    currentSite = StackAPI('{}'.format(site))
    print(site)

    cotaGasta = 0
    while(cotaGasta <= 50):

        questions = currentSite.fetch('questions')

        cotaRestante = questions['quota_remaining']
        cotaGasta += (cotaTotal - cotaRestante)
        cotaTotal = cotaRestante


        questionItems = questions['items']

        idList = []
        userSet = set()
        tagsList = []

        for item in questionItems:

            owner = item['owner'] 
            ownerId = owner.get('user_id')
            userSet.add(ownerId)

            lastEditdate = item.get('last_edit_date')
            creationDate = item.get('creation_date')
            link = item.get('link')
            lastActivityDate = item.get('last_activity_date')
            score = item.get('score')
            questionId = item.get('question_id')
            title = item.get('title')
            answerCount = item.get('answer_count')
            isAnswered = item.get('is_answered')
            viewCount = item.get('view_count')

            tags = item.get('tags')
            for tag in tags:
                tagsList.append(tag)


            if(isAnswered):

                idList.append(questionId)
                
        print(len(idList))
        print(idList)
        
        time.sleep(10)
            

        # for idAnswer in range(0,500,100):
            

        answers = currentSite.fetch('questions/{ids}/answers', ids = idList[0:100])
        answersItems = answers['items']

        cotaRestante = answers['quota_remaining']
        cotaGasta = cotaTotal - cotaRestante
        cotaTotal = cotaRestante

        for item in answersItems:

            # print(item)
            # print(item['question_id'])

            lastEditdate = item.get('last_edit_date')
            creationDate = item.get('creation_date')
            link = item.get('link')
            lastActivityDate = item.get('last_activity_date')
            score = item.get('score')
            answerId = item.get('answer_id')
            isAccepted = item.get('is_accepted')
            questionId = item.get('question_id')

        time.sleep(10)

        userList = list(userSet) 
        users = currentSite.fetch('users/{ids}', ids = userList[0:100])
        usersItem = users['items']

        for item in usersItem:

            userId = item.get('user_id')
            reputation = item.get('reputation')
            userType = item.get('type')
            acceptRate = item.get('accept_rate')
            displayName = item.get('display_name')
            userLink = item.get('userLink')

            badges = item.get('bagde_counts')
            bronzeBadge = badges.get('bronze')
            silverBadge = badges.get('silver')
            goldBadge = badges.get('gold')


        time.sleep(10)


        

    
