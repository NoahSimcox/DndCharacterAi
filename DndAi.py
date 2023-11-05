import openai
import HahaCantGetMySecretKey

openai.api_key = HahaCantGetMySecretKey.openai.api_key

prompt = "a gnome with bright blue hair and a mischievous twinkle in her eye. She specializes in illusion magic, creating intricate and realistic illusions to confound and deceive her foes. Her spellbook is adorned with colorful drawings and secret notes, reflecting her creative and curious nature as she delves into the world of arcane magic."

keywords = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

gp = 125


dnd_class_prompt = f"Interpret the following level one Dungeons and Dragons character description: '{prompt}' determine a suitable class, from Dnd 5e, for this character and output just that class name. It must only be one word."

dnd_class = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": dnd_class_prompt}]
)

dnd_class_var = dnd_class.choices[0].message["content"]
print(dnd_class_var)

if dnd_class_var in ["Wizard", "Warlock", "Rogue", "Artificer"]:
    gp -= 25
elif dnd_class_var in ["Sorcerer"]:
    gp -= 50
elif dnd_class_var in ["Barbarian", "Monk"]:
    gp -= 75
elif dnd_class_var in ["Monk"]:
    gp -= 112


raw_stat_rankings_prompt = f"Using this prompt: '{prompt}' rank these skills numerically from 1 to 6. 1 being the most relevent skill for the description of the character and 6 being the least relevent [{', '.join(keywords)}]. Keep in mind that the class is {dnd_class_var}"

raw_stat_rankings = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": raw_stat_rankings_prompt}]
)

raw_stat_rankings_response = raw_stat_rankings.choices[0].message["content"]


refined_stat_rankings_prompt = f"Take this text:{raw_stat_rankings_response} and only output the ability names, in order, on one line, with no numbers."

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


dnd_profs_prompt = f"Using this prompt: '{prompt}' determine 6 suitable skill proficiencies, from Dnd 5e, for this character and output only those 6 skill proficeincies on one line. Do not include saving throws, armor, or weapon proficiencies."

dnd_profs = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": dnd_profs_prompt}]
)

dnd_profs_list = dnd_profs.choices[0].message["content"].split()
print(dnd_profs_list)

if dnd_class_var not in ["Wizard", "Warlock", "Rogue", "Artificer", "Monk"]:
    dnd_armor_prompt = f"Using this prompt: '{prompt}' determine an armor, from Dnd 5e, for this character. The armor must be less then {gp} gold coins to be a valid output and the output must only be the armor name."

    dnd_armor = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": dnd_armor_prompt}]
    )

    if len(dnd_armor.choices[0].message["content"].split()) > 3:
        count = 5
        dnd_armor_var = dnd_armor.choices[0].message["content"]
        while len(dnd_armor_var.split()) > 3 and count > 0:
            dnd_armor_var = dnd_armor.choices[0].message["content"]
            count -= 1
            print(count)
    else:
        dnd_armor_var = dnd_armor.choices[0].message["content"]
    print(dnd_armor_var)


if  dnd_class_var in ["Fighter", "Barbarian", "Rogue", "Monk", "Paladin", "Ranger"]:
    dnd_weapon_prompt = f"Using this prompt: '{prompt}' determine a weapon, from Dnd 5e, for this character. The weapon must be less then {gp} gold coins and the output must only be the weapon name, no other words."

    dnd_weapon = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": dnd_weapon_prompt}]
    )

    if len(dnd_weapon.choices[0].message["content"].split()) > 3:
        count = 5
        dnd_weapon_var = dnd_weapon.choices[0].message["content"]
        while len(dnd_weapon_var.split()) > 3 and count > 0:
            dnd_weapon_var = dnd_weapon.choices[0].message["content"]
            count -= 1
            print(count)
    else:
        dnd_weapon_var = dnd_weapon.choices[0].message["content"]
    print(dnd_weapon_var)


if  dnd_class_var in ["Warlock", "Wizard", "Bard", "Cleric", "Artificer", "Sorcerer", "Druid"]:
    dnd_spell_prompt = f"Using this prompt: '{prompt}' determine the spells a level one {dnd_class_var} would have in Dnd 5e. The output must only be the spell names. No cantrips."

    dnd_spell = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": dnd_spell_prompt}]
    )
    
    dnd_spell_var = dnd_spell.choices[0].message["content"]
    print(dnd_spell_var)
   