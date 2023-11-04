import openai


openai.api_key = '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'

keywords = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]


raw_stat_rankings_prompt = f"Interpret the following level one Dungeons and Dragons character description: 'Spending all his time in the libraries this man is old and has the knowledge of 1000 sages.' rank these skills numerically from 1 to 6. 1 being the most relevent skill for the description and 6 being the least relevent [{', '.join(keywords)}]."

raw_stat_rankings = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": raw_stat_rankings_prompt}]
)

raw_stat_rankings_response = raw_stat_rankings.choices[0].message["content"]


refined_stat_rankings_prompt = f"Take this text:{raw_stat_rankings_response} and only output the ability names, in order, on one line"

refined_stat_rankings = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": refined_stat_rankings_prompt}]
)

refined_stat_rankings_list = refined_stat_rankings.choices[0].message["content"].split()
print(refined_stat_rankings_list)




#dnd_class = openai.ChatCompletion.create(
    #model="gpt-3.5-turbo",
    #messages=[{"role": "user", "content": refined_stat_rankings_prompt}]
#)




