import requests
import json
import urllib





BASEURL = "https://api.stackexchange.com/2.2/questions"


params = {
    "site":"stackoverflow"
}



# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
# )



responseQuestion = requests.get(BASEURL,params=params)

responseQuestionItems = responseQuestion.json()['items']

for itemsQuestion in responseQuestionItems:

    #dados do usuario
    user_rep = itemsQuestion['owner']['reputation']
    # print(user_rep)


    #dados da pergunta

    questionId = itemsQuestion['question_id']
    # print(itemsQuestion['is_answered'])


    # print(responseAnswerItems[0]['owner']['user_id'])
    
    if(itemsQuestion['is_answered'] == True):

        newUrl = BASEURL+'/'+str(questionId)+'/answers'

        responseAnswer = requests.get(newUrl,params=params)
        responseAnswerItems = responseAnswer.json()['items']

        for answerItem in responseAnswerItems:
            
            print(answerItem['is_accepted'])








