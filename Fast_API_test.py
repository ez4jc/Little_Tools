import requests
url_api = "http://"


def call_with_prompt(word_input):
    url = url_api

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    data = {
        "model": "qwen_turbo",
        "messages": [
            {
                "role": "user",
                "content": word_input
            }
        ],
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
        ret = result["choices"][0]["message"]["content"]
        return ret
    else:
        print(f"请求失败，状态码：{response.status_code}")


if __name__ == '__main__':
    words = input("")
    content = call_with_prompt(words)
    print(content)
