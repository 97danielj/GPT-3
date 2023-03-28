# 1. OpenAI key 설정
My_OpenAI_key = '나만의 키'

import openai
openai.api_key = My_OpenAI_key
completion = openai.Completion()


# 2. GPT3 config 설정(매개변수 설정)
# max_tokens = 생성된 글의 길이
# temperature, top_p로 생성될 다음 단어의 샘플링 방법을 지정
# config
temperature = 0.7
max_tokens = 150
top_p = 1.0
best_of = 1
frequency_penalty = 0.0
presence_penalty = 0.0

# stop = ["You:"]
stop = ["\n"]


# 4. chatbot building
# question : 질문을 입력
def run_openai_chatbot(question='What time is it?', history=''):
    prompt_initial = f'Human:%s\nAI:' % (question)

    #history : 대화 기록
    #prompt :이전 대화 기반 + 시작 prompt
    prompt = history + '\n' + prompt_initial

    response = completion.create(
        prompt=prompt,
        engine="davinci",
        max_tokens=max_tokens,
        stop=stop,
        temperature=temperature,
        top_p=top_p,
        best_of=best_of,
    )
    answer = response.choices[0].text.strip()

    history = prompt + answer

    return answer, history

history = ''
for turn in range(100):
    question = input(">> User: ")
    answer, history = run_openai_chatbot(question=question, history=history)
    print("AI : ", answer)