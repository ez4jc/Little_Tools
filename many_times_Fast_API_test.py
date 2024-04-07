from http import HTTPStatus
import requests
url = "http://111.19.168.149:8197/v1/chat/completions"

content_init = input()

messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': content_init}]


headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

data = {
    "model": "qwen_turbo",
    "messages":  messages,
    "do_sample": True,
    "temperature": 0,
    "top_p": 0,
    "n": 1,
    "max_tokens": 0,
    "stream": False
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print(result["choices"][0]["message"]["content"])
    messages.append({'role': result["choices"][0]['message']['role'],
                     'content': result["choices"][0]['message']['content']})

else:
    print(f"请求失败，状态码：{response.status_code}")

for _ in range(10):
    words = input()
    messages.append({'role': 'user', 'content': words})
    data["messages"] = messages

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print(result["choices"][0]["message"]["content"])

    else:
        print(f"请求失败，状态码：{response.status_code}")

# if __name__ == '__main__':
#     conversation_with_messages()
