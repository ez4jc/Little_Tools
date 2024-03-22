from http import HTTPStatus
import dashscope

dashscope.api_key = "sk-693317d6d8374702a086ea955b885c76"


def call_with_stream(word_input):
    responses = dashscope.Generation.call(
        model=dashscope.Generation.Models.qwen_turbo,
        prompt=word_input,
        result_format='message',  # set the result to be "message" format.
        stream=True,
        incremental_output=True  # get streaming output incrementally
    )
    full_content = ''  # with incrementally we need to merge output.
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            full_content += response.output.choices[0]['message']['content']
            print(response.output.choices[0]['message']['content'])
        else:
            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))
    print('Full response:\n' + full_content)


if __name__ == '__main__':
    words = input("")
    call_with_stream(words)
