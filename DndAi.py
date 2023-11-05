import openai
import HahaCantGetMySecretKey

openai.api_key = HahaCantGetMySecretKey.openai.api_key

prompt = "A mysterious cloacked figure whose eyes glow an intimidating red. While physically frail, his eldritch magic proves him threatening."

keywords = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

dnd_armor_var = ""
dnd_weapon_var = ""
dnd_raw_spell_list = ""
dnd_raw_cantrip_list = ""


#gold pieces
gp = 125

#figuring out the class
dnd_class_prompt = f"Interpret the following level one Dungeons and Dragons character description: '{prompt}' determine a suitable class, from Dnd 5e, for this character and output just that class name. It must only be one word."

dnd_class = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": dnd_class_prompt}]
)

dnd_class_var = dnd_class.choices[0].message["content"].strip(".")
print(dnd_class_var)

#decrementing gold based on class
if dnd_class_var in ["Wizard", "Warlock", "Rogue", "Artificer"]:
    gp -= 25
elif dnd_class_var in ["Sorcerer"]:
    gp -= 50
elif dnd_class_var in ["Barbarian", "Druid"]:
    gp -= 75
elif dnd_class_var in ["Monk"]:
    gp -= 112


#figuring out the raw stats
raw_stat_rankings_prompt = f"Using this prompt: '{prompt}' rank these skills numerically from 1 to 6. 1 being the most relevent skill for the description of the character and 6 being the least relevent [{', '.join(keywords)}]. Keep in mind that the class is {dnd_class_var}"

raw_stat_rankings = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": raw_stat_rankings_prompt}]
)

raw_stat_rankings_response = raw_stat_rankings.choices[0].message["content"]


#figuring out the refined stats
refined_stat_rankings_prompt = f"Take this text:{raw_stat_rankings_response} and only output the ability names, in order, on one line, with no numbers."

refined_stat_rankings = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": refined_stat_rankings_prompt}]
)

refined_stat_rankings_list = refined_stat_rankings.choices[0].message["content"].split(",")
j = 0
while j < len(refined_stat_rankings_list):
    refined_stat_rankings_list[j] = refined_stat_rankings_list[j].strip()
    j += 1
print(refined_stat_rankings_list)


#figuring out the race
dnd_race_prompt = f"Using this prompt: '{prompt}' determine a common race, from Dnd 5e, and output just that race name."

dnd_race = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": dnd_race_prompt}]
)

dnd_race_var = dnd_race.choices[0].message["content"].strip(".")
print(dnd_race_var)


#figuring out the skill proficiencies
dnd_profs_prompt = f"Using this prompt: '{prompt}' determine 6 suitable skill proficiencies, from Dnd 5e, for this character and output only those 6 skill proficeincies on one line. Do not include saving throws, armor, or weapon proficiencies."

dnd_profs = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": dnd_profs_prompt}]
)

dnd_profs_list = dnd_profs.choices[0].message["content"].split(",")
i = 0
while i < len(dnd_profs_list):
    dnd_profs_list[i] = dnd_profs_list[i].strip()
    i += 1
print(dnd_profs_list)


#figuring out the armor
if dnd_class_var not in ["Wizard", "Warlock", "Sorcerer", "Monk"]:
    dnd_armor_prompt = f"Based on this class '{dnd_class_var}' choose an armor that costs less than or equal to {gp/2} from Dnd 5e. The output must only be the armor name."

    dnd_armor = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": dnd_armor_prompt}]
    )
    dnd_armor_var = dnd_armor.choices[0].message["content"].strip()
    print(dnd_armor_var)


#figuring out the weapons
if  dnd_class_var in ["Fighter", "Barbarian", "Rogue", "Monk", "Paladin", "Ranger"]:
    dnd_weapon_prompt = f"Based on this class '{dnd_class_var}' choose a weapon that costs less than or equal to {gp/2} from Dnd 5e. The output must only be the weapon name."

    dnd_weapon = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": dnd_weapon_prompt}]
    )
    dnd_weapon_var = dnd_weapon.choices[0].message["content"].strip()
    print(dnd_weapon_var)


#figuring out the raw spells
if  dnd_class_var in ["Warlock", "Wizard", "Bard", "Cleric", "Artificer", "Sorcerer", "Druid"]:
    dnd_raw_spell_prompt = f"Using this prompt: '{prompt}' determine 4 spells a level one {dnd_class_var} would have in Dnd 5e. The output must only be the spell names. No cantrips."

    dnd_raw_spell = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": dnd_raw_spell_prompt}]
    )
    
    dnd_raw_spell_list = dnd_raw_spell.choices[0].message["content"].split(",")
    k = 0
    while k < len(dnd_raw_spell_list):
        dnd_raw_spell_list[k] = dnd_raw_spell_list[k].strip()
        k += 1
    print(dnd_raw_spell_list)
 

#figuring out the raw cantrips
    dnd_raw_cantrip_prompt = f"Using this prompt: '{prompt}' determine 4 cantrips a level one {dnd_class_var} would have in Dnd 5e. The output must only be the cantrip names. No spells."

    dnd_raw_cantrip = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": dnd_raw_cantrip_prompt}]
    )
    
    dnd_raw_cantrip_list = dnd_raw_cantrip.choices[0].message["content"].split(",")
    l = 0
    while l < len(dnd_raw_cantrip_list):
        dnd_raw_cantrip_list[l] = dnd_raw_cantrip_list[l].strip()
        l += 1
    print(dnd_raw_cantrip_list)
    

# # personality traits
# dnd_personality_traits_prompt = f"Using the prompt: '{prompt}' create a one sentence descriction of two personality traits."

# dnd_personality_traits = openai.ChatCompletion.create(
#     model = "gpt-4",
#     messages=[{"role": "user", "content": dnd_personality_traits_prompt}]
# )

# dnd_personality_traits_var = dnd_personality_traits.choices[0].message["content"]
# print(dnd_personality_traits_var)


# #ideals
# dnd_ideals_prompt = f"Using the prompt: '{prompt}' create an ideal and give it a one sentence description."

# dnd_ideals = openai.ChatCompletion.create(
#     model = "gpt-4",
#     messages=[{"role": "user", "content": dnd_ideals_prompt}]
# )

# dnd_ideals_var = dnd_ideals.choices[0].message["content"]
# print(dnd_ideals_var)


# #bonds
# dnd_bonds_prompt = f"Using the prompt: '{prompt}' make up a bond this charcter has and describe it in one sentence."

# dnd_bonds = openai.ChatCompletion.create(
#     model = "gpt-4",
#     messages=[{"role": "user", "content": dnd_bonds_prompt}]
# )

# dnd_bonds_var = dnd_bonds.choices[0].message["content"]
# print(dnd_bonds_var)


# #flaws
# dnd_flaws_prompt = f"Using the prompt: '{prompt}' make up two flaws and describe them each in one sentence."

# dnd_flaws = openai.ChatCompletion.create(
#     model = "gpt-4",
#     messages=[{"role": "user", "content": dnd_flaws_prompt}]
# )

# dnd_flaws_var = dnd_flaws.choices[0].message["content"]
# print(dnd_flaws_var)