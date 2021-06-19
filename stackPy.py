from stackapi import StackAPI
import time

# def calculaCota(cotaTotal,cotaGasta):

#     return 


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
        cotaGasta = cotaTotal - cotaRestante
        cotaTotal = cotaRestante


        questionItems = questions['items']

        idList = []
        userSet = {}
        for item in questionItems:

            # reputation = item['owner']['reputation']
            questionOwner = item['owner']
            userId = questionOwner['user_id']

            userSet.add(userId)

            if(item['is_answered'] == True):

                idList.append(item['question_id'])
                
        # print(len(idList))
        # print(idList)
        
        time.sleep(31)
            

        for idAnswer in range(0,500,100):
            

            answers = currentSite.fetch('questions/{ids}/answers', ids = idList[idAnswer:idAnswer+100])
            answersItems = answers['items']

            cotaRestante = answers['quota_remaining']
            cotaGasta = cotaTotal - cotaRestante
            cotaTotal = cotaRestante

            for item in answersItems:

                # print(item)
                print(item['question_id'])
        
            time.sleep(31)
        

    
