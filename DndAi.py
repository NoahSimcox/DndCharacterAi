import openai
import HahaCantGetMySecretKey

openai.api_key = HahaCantGetMySecretKey.openai.api_key

prompt = "This short woman has a long beard with heavy armor. Her convictions come from the gods. She is clumsy, but is very resialnt to damage."

keywords = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

gp = 135


dnd_class_prompt = f"Interpret the following level one Dungeons and Dragons character description: '{prompt}' determine a suitable class, from Dnd 5e, for this character and output just that class name. It must only be one word."

dnd_class = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": dnd_class_prompt}]
)

dnd_class_var = dnd_class.choices[0].message["content"]
print(dnd_class_var)

if dnd_class_var == "Wizard" or "Warlock" or "Rogue" or "Artificer":
    gp -= 25
elif dnd_class_var == "Sorcerer":
    gp -= 50
elif dnd_class_var == "Barbarian" or "Druid":
    gp -= 75
elif dnd_class_var == "Monk":
    gp -= 112


raw_stat_rankings_prompt = f"Using this prompt: '{prompt}' rank these skills numerically from 1 to 6. 1 being the most relevent skill for the description of the character and 6 being the least relevent [{', '.join(keywords)}]. Keep in mind that the class is {dnd_class_var}"

raw_stat_rankings = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": raw_stat_rankings_prompt}]
)

raw_stat_rankings_response = raw_stat_rankings.choices[0].message["content"]


refined_stat_rankings_prompt = f"Take this text:{raw_stat_rankings_response} and only output the ability names, in order, on one line."

refined_stat_rankings = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": refined_stat_rankings_prompt}]
)

refined_stat_rankings_list = refined_stat_rankings.choices[0].message["content"].split()
print(refined_stat_rankings_list)


dnd_race_prompt = f"Using this prompt: '{prompt}' determine a suitable race, from Dnd 5e, for this character and output just that race name. It must only be one word."

dnd_race = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": dnd_race_prompt}]
)

dnd_race_var = dnd_race.choices[0].message["content"]
print(dnd_race_var)


dnd_profs_prompt = f"Using this prompt: '{prompt}' determine 6 suitable skill proficiencies, from Dnd 5e, for this character and output just those 6 skill proficeincies on one line. Do not include saving throws, armor, or weapon proficiencies."

dnd_profs = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": dnd_profs_prompt}]
)

dnd_profs_list = dnd_profs.choices[0].message["content"].split()
print(dnd_profs_list)


dnd_armor_prompt = f"Using this prompt: '{prompt}' determine an armor, from Dnd 5e, for this character. The armor must be less then {gp} gold coins to buy. Output just the armor name and nothing else."

dnd_armor = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": dnd_armor_prompt}]
)

dnd_armor_var = dnd_armor.choices[0].message["content"]
print(dnd_armor_var)

