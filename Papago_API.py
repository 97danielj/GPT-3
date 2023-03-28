import requests


def translate(text, o_lang, t_lang, honorific=False):
    data = {'text': text, 'source': o_lang, 'target': t_lang}

    if honorific and (o_lang == "en"):
        data['honorific'] = True

    client_id = "client_id"  # Client ID를 입력
    client_secret = "client_secret"  # Client Secret을 입력
    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if (rescode == 200):
        t_data = response.json()

        return t_data['message']['result']['translatedText']
    else:
        print('Error Code: ', rescode)


if __name__ == '__main__':
    #test
    text = input('번역하는 말을 입력하시오 :  ')
    print(translate(text, 'en', 'ko'))
