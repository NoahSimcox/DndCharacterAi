import openai


openai.api_key = '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'

Keywords = ["strength", "dexterity", "constitution", "intelligence", "speed", "wisdom", "charisma"]

response = openai.Completion.create(
    engine="4K context",  # the engine in use
    prompt="Interpret the following Dungeons and Dragons character description: 'A strong and fast warrior with great knowledge of nature.' Output the words on this list that pertain to the character description.",
    max_tokens=1000
)