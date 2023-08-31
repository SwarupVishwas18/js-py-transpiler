import openai
import re

openai.api_key = "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"


def avg(a, b):
    return (a + b) / 2


prompt = f"Give me python docstring for given function :\n\n{avg.__name__}{avg.__doc__}"

# print(prompt)
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
)

documentation = response.choices[0].text
documentation = re.sub(r"\n", " ", documentation).strip()

print(documentation)
