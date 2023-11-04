import openai


openai.api_key = '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'

Keywords = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

message_content = f"Interpret the following Dungeons and Dragons character description: 'A strong and fast warrior with great knowledge of nature.' only output the words on this list [{', '.join(Keywords)}] that pertain to the character description."
message_content2 = f"Interpret the following level one Dungeons and Dragons character description: 'A strong and fast warrior with great knowledge of nature.' only output a possible ability score based on the prompt for each of the following abilities [{', '.join(Keywords)}]."

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # the engine in use
    messages=[{"role": "user", "content": message_content2}]
)


print(response.choices[0].message["content"])