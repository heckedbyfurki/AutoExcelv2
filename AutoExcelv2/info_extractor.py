import openai


async def get_values_async(text, keywords):
    
    prompt = f"""Extract from following in ["{'", "'.join(keywords)}"] format. \nInput: {text}\nOutput: """
    response = await openai.Completion.acreate(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return eval(response.choices[0].text)

