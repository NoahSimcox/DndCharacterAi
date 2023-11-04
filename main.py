import openai


openai.api_key = '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'

Keywords = ["strength", "dexterity", "constitution", "intelligence", "speed", "wisdom", "charisma"]

def generate_Dnd_character(messages):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # the engine in use
        messages=messages
    )

    return response.choices[0].message["content"]

prompt = [{"role": "user", "content": "Interpret the following Dungeons and Dragons character description: 'A strong and fast warrior with great knowledge of nature.' Output the words on this list [" + ', '.join(Keywords) + "] that pertain to the character description."}]

response = generate_Dnd_character(prompt)

print(response)