import requests
import json



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

for items in responseQuestionItems:
    questionId = items['question_id']
    # print(items['is_answered'])
    newUrl = BASEURL+'/'+str(questionId)+'/answers'

    responseAnswer = requests.get(newUrl,params=params)
    responseAnswerItems = responseAnswer.json()['items']

    # print(responseAnswerItems[0]['owner']['user_id'])
    
    if(items['is_answered'] == True):

        for aitems in responseAnswerItems:
            print(aitems['is_accepted'])








