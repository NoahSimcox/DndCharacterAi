import PyPDF2
import random
import DndAi

pdfFileObj = open('DnDDefault.pdf', 'rb')

# creating reader and writer objects
pdfReader = PyPDF2.PdfReader(pdfFileObj)
pdfWriter = PyPDF2.PdfWriter()
formFields = pdfReader.get_form_text_fields()

# copying page over to the writer, clear old PDF
pdfWriter.add_page(pdfReader.pages[0])
pdfWriter.add_page(pdfReader.pages[1])
pdfWriter.add_page(pdfReader.pages[2])
with open("GeneratedCharacter.pdf", "wb") as output_stream:
    pdfWriter.write(output_stream)

# temp variables for now
name = "Bob D. Builder"
pLevel = 1
profBonus = int((pLevel+7)/4)
pClass = DndAi.dnd_class_var
# pSubclass = "None"
pRace = "Dwarf"
pBackground = "Acolyte"
gearArmor = "Splint"
gearWeapon = "Greatsword"
gearMisc = ["Adventurer's Pack", "Ball Bearings"]
possibleSkills = ["Athletics", "Religion", "Intimidation", "Medicine", "Performance"]

# ability score determining
statRanks = ["Strength", "Charisma", "Constitution", "Wisdom", "Intelligence", "Dexterity"]
scoreVals = [0,0,0,0,0,0]
scoreMods = [0,0,0,0,0,0]
match pRace:
    case "Human":
        scoreVals = [16,15,14,13,12,10]
        scoreMods = [3,2,2,1,1,0]
    case "Dwarf": # assume all dwarves are mountain dwarves
        scoreVals = [17,15,14,12,10,8]
        scoreMods = [3,2,2,1,0,-1]
    case "Half-Elf" | "Half Elf": 
        scoreVals = [17,16,14,10,10,8]
        scoreMods = [3,3,2,0,0,-1]
    case _: 
        scoreVals = [17,14,14,12,10,8]
        scoreMods = [3,2,2,1,0,-1]

pStrVal = scoreVals[statRanks.index("Strength")]
pStrMod = scoreMods[statRanks.index("Strength")]
pDexVal = scoreVals[statRanks.index("Dexterity")]
pDexMod = scoreMods[statRanks.index("Dexterity")]
pConVal = scoreVals[statRanks.index("Constitution")]
pConMod = scoreMods[statRanks.index("Constitution")]
pIntVal = scoreVals[statRanks.index("Intelligence")]
pIntMod = scoreMods[statRanks.index("Intelligence")]
pWisVal = scoreVals[statRanks.index("Wisdom")]
pWisMod = scoreMods[statRanks.index("Wisdom")]
pChaVal = scoreVals[statRanks.index("Charisma")]
pChaMod = scoreMods[statRanks.index("Charisma")]

# class information
profSaves = "XXX,YYY"
hitDie = 0
profArmor = ""
profWeapon = ""
profTools = ""
profLanguages = "Common"
skillsKnown = 3 # start with 3 from BG/the other stuff you'd be losing from BG
match pClass: 
    case "Artificer":
        hitDie = 8
        profSaves = "INT,CON"
        profArmor = "light & medium armor, as well as shields"
        profWeapon = "simple weapons"
        profTools += "thieves' tools, tinker's tools, alchemist's supplies, "
        skillsKnown += 2
    case "Barbarian":
        hitDie = 12
        profSaves = "STR,CON"
        profArmor = "light & medium armor, as well as shields"
        profWeapon = "simple & martial weapons"
        skillsKnown += 2
    case "Bard":
        hitDie = 8
        profSaves = "DEX,CHA"
        profArmor = "light armor"
        profWeapon = "simple weapons, hand crossbows, longswords, rapiers, shortswords"
        profTools += "musical instruments, "
        skillsKnown += 3
    case "Cleric":
        hitDie = 8
        profSaves = "WIS,CHA"
        profArmor = "light & medium armor, as well as shields"
        profWeapon = "simple weapons"
        skillsKnown += 2
    case "Druid":
        hitDie = 8
        profSaves = "INT,WIS"
        profArmor = "light & medium armor, as well as shields"
        profWeapon = "clubs, daggers, darts, javelins, maces, quarterstaffs, scimitars, sickles, slings, spears"
        profTools += "herbalism kit, "
        profLanguages += ", Druidic"
        skillsKnown += 2
    case "Fighter":
        hitDie = 10
        profSaves = "STR,CON"
        profArmor = "light, medium, & heavy armor, as well as shields"
        profWeapon = "simple & martial weapons"
        skillsKnown += 2
    case "Monk":
        hitDie = 8
        profSaves = "STR,DEX"
        profWeapon = "simple weapons and shortswords"
        skillsKnown += 2
    case "Paladin":
        hitDie = 10
        profSaves = "WIS,CHA"
        profArmor = "light, medium, & heavy armor, as well as shields"
        profWeapon = "simple & martial weapons"
        skillsKnown += 2
    case "Ranger":
        hitDie = 10
        profSaves = "STR,DEX"
        profArmor = "light & medium armor, as well as shields"
        profWeapon = "simple & martial weapons"
        skillsKnown += 3
    case "Rogue":
        hitDie = 8
        profSaves = "DEX,INT"
        profArmor = "light armor"
        profWeapon = "simple weapons, hand crossbows, longswords, rapiers, shortswords"
        profTools += "thieves' tools,"
        profLanguages.append([", Thieves' Cant"])
        skillsKnown += 4
    case "Sorcerer":
        hitDie = 6
        profSaves = "CON,CHA" 
        profWeapon = "daggers, darts, slings, quarterstaffs, light crossbows"
        skillsKnown += 2
    case "Warlock":
        hitDie = 8
        profSaves = "WIS,CHA"
        profArmor = "light armor"
        profWeapon = "simple weapons"
        skillsKnown += 2
    case "Wizard":
        hitDie = 6
        profSaves = "INT,WIS" 
        profWeapon = "daggers, darts, slings, quarterstaffs, light crossbows"
        skillsKnown += 2

pMaxHP = int(pLevel*(hitDie/2 + 1 + pConMod)+(hitDie/2-1))
pSTStr = pStrMod + profBonus*("STR" in profSaves)
pSTDex = pDexMod + profBonus*("DEX" in profSaves)
pSTCon = pConMod + profBonus*("CON" in profSaves)
pSTInt = pIntMod + profBonus*("INT" in profSaves)
pSTWis = pWisMod + profBonus*("WIS" in profSaves)
pSTCha = pChaMod + profBonus*("CHA" in profSaves)

# determine skills known
skills = possibleSkills # limit this by the number of skills you can have
pAcrobatics = pDexMod + profBonus*("Acrobatics" in skills)
pAnimalHandling = pWisMod + profBonus*("Animal Handling" in skills)
pArcana = pIntMod + profBonus*("Arcana" in skills)
pAthletics = pStrMod + profBonus*("Athletics" in skills)
pDeception = pChaMod + profBonus*("Deception" in skills)
pHistory = pIntMod + profBonus*("History" in skills)
pInsight = pWisMod + profBonus*("Insight" in skills)
pIntimidation = pChaMod + profBonus*("Intimidation" in skills)
pInvestigation = pIntMod + profBonus*("Investigation" in skills)
pMedicine = pWisMod + profBonus*("Medicine" in skills)
pNature = pIntMod + profBonus*("Nature" in skills)
pPerception = pWisMod + profBonus*("Perception" in skills)
pPerformance = pChaMod + profBonus*("Performance" in skills)
pPersuasion = pChaMod + profBonus*("Persuasion" in skills)
pReligion = pWisMod + profBonus*("Religion" in skills)
pSleightOfHand = pDexMod + profBonus*("Slight of Hand" in skills)
pStealth = pDexMod + profBonus*("Stealth" in skills)
pSurvival = pWisMod + profBonus*("Survival" in skills)

# speed calcs
pSpeed = 30
match pRace:
    case "Dwarf" | "Gnome" | "Halfling":
        pSpeed -= 5
    case "Elf" | "Half Elf" | "Half-Elf" | "Air Genasi" | "Satyr": # assume all elves are wood elves, and all half-elves are wood half-elves
        pSpeed += 5
    case "Centaur":
        pSpeed += 10

# Proficiencies & Languages
if(pRace == "Dwarf" and "medium" not in profArmor):
    profArmor = "light & medium armor"

if(pRace == "Elf" and "martial" not in profWeapon):
    if("shortsword" not in profWeapon): profWeapon += "shortswords, "
    if("short" not in profWeapon): profWeapon += "shortbows, "
    if("longsword" not in profWeapon): profWeapon += "longswords, "
    profWeapon += "longbows"

# Features & Traits
featTraits = ""
match pRace: # racial traits, also has languages
    case "Dragonborn":
        featTraits += "Draconic Resistance: you resist fire damage\nBreath Weapon: Twice per long rest, you can exhale fire in a 30-foot long line that is 5-feet wide. Each creature in the area must make a DC " + str(10+pConMod) + " Dexterity saving throw. On a failed save, they take 1d10 damage, or half as much on a success.\n"
        profLanguages += ", Draconic"
    case "Dwarf":
        featTraits += "Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.\nDwarven Resilience: You resist poison damage and have advantage on saving throws against poison.\nStonecunning: If you make an Intelligence (History) check related to stonework, you add double your proficiency bonus to the check."
        profTools += "smith's tools, brewer's supplies, mason's tools, "
        profLanguages += ", Dwarvish"
    case "Elf":
        featTraits += "Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.\nFey Ancestry: You have advantage on saving throws against being charmed, and magic can't put you to sleep.\nTrance: You only need to sleep for 4 hours to get the benefits of a long rest.\nYou can attempt to hide when you are lightly obscured by some natural phenomena."
        profLanguages += ", Elvish"
        skills += "Perception"
    case "Gnome":
        featTraits += "Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.\nGnome Cunning: you have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic.\nTinker: Using tinker's tools, you can spend 1 hour and 10 gp to make a Tiny clockwork device (AC 5, 1 hp) that lasts for up to 24 hours, unless you spend 1 hour repairing it to keep it working. You can have up to 3 of these active at once, and when you make one choose one of the following options:\n\tClockwork Toy: The toy looks like a creature of your choice, and when placed on the ground it moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents.\n\tFire Starter: You can use an action to cause the device to make a small fire that you can use to light a candle, torch, or campfire.\n\tMusic Box: When opened, the box plays a single song at a moderate volume. It stops playing when the song ends or when it is closed."
        profLanguages += ", Gnomish"
        profTools += "tinker's tools, "
    case "Half-Elf":
        featTraits += "Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.\nFey Ancestry: You have advantage on saving throws against being charmed, and magic can't put you to sleep."
        profLanguages += ", Elvish"
    case "Half-Orc":
        featTraits += "Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.\nRelentless Endurance. Once per long rest when you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead.\nSavage Attacks: When you score a critical hit with a melee weapon attack, you can add one additional damage die and add it to the total damage."
        skills += "Intimidation"
        profLanguages += ", Orcish"
    case "Halfling":
        featTraits += "Lucky: When you roll a 1 on a d20 roll, you can reroll the die and must use the new result, even if it is a 1.\nBrave: You have advantage on saving throws against being frightened.\nNimble: You can move through the space of any creature that is a larger size than you. \nNaturally Stealthy: You can attempt to hide if you are obscured by a creature that is a larger size than you."
        profLanguages += ", Halfling"
    case "Human":
        profLanguages += ", Elvish, Dwarvish"
    case "Tiefling":
        featTraits += "Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.\nHellish Resistance: You resist fire damage.\n"
        profLanguages += ", Infernal"
        # ADD THAT TIEFLINGS GET THE THAUMATURGY CANTRIP

finalProfLang = "Proficient in " + profArmor + "\nProficient in " + profWeapon + "\nFluent in " + profLanguages + "\n"

# match pClass: # class traits

# money
cp = random.randint(100, 300)
sp = int((1000 - cp) / 10)
ep = 0
gp = 999
pp = 0

# place everything in the writer object
pdfWriter.update_page_form_field_values(
    pdfWriter.pages[0], {
        "CharacterName": name,
        "ClassLevel": (pClass + " " + str(pLevel)),
        "Race ": pRace,
        "Background": "Custom",
        "Alignment": "N/A",
        "XP": "N/A",
        "ProfBonus": profBonus,
        "Speed": pSpeed,
        "STR": pStrVal,
        "STRmod": pStrMod,
        "DEX": pDexVal,
        "DEXmod ": pDexMod,
        "CON": pConVal,
        "CONmod": pConMod,
        "INT": pIntVal,
        "INTmod": pIntMod,
        "WIS": pWisVal,
        "WISmod": pWisMod,
        "CHA": pChaVal,
        "CHamod": pChaMod,
        "Initiative": pDexMod,
        "ST Strength": pSTStr,
        "ST Dexterity": pSTDex,
        "ST Constitution": pSTCon,
        "ST Intelligence": pSTInt,
        "ST Wisdom": pSTWis,
        "ST Charisma": pSTCha,
        "Acrobatics": pAcrobatics,
        "Animal": pAnimalHandling,
        "Arcana": pArcana,
        "Athletics": pAthletics,
        "Deception ": pDeception,
        "History ": pHistory,
        "Insight": pInsight,
        "Intimidation": pIntimidation,
        "Investigation ": pInvestigation,
        "Medicine": pMedicine,
        "Nature": pNature,
        "Perception ": pPerception,
        "Performance": pPerformance,
        "Persuasion": pPersuasion,
        "Religion": pReligion,
        "SleightofHand": pSleightOfHand,
        "Stealth ": pStealth,
        "Survival": pSurvival,
        "Passive": str(10+pPerception),
        "HDTotal": (str(pLevel) + "d" + str(hitDie)),
        "HPMax": pMaxHP,
        "Features and Traits": featTraits,
        "ProficienciesLang": finalProfLang,
        
        # Stuff to comment out if you are printing it out
        "HD": (str(pLevel) + "d" + str(hitDie)),
        "HPCurrent": pMaxHP,
        "CP": cp,
        "SP": sp,
        "EP": ep,
        "GP": gp,
        "PP": pp
    }
)


# put everything in the new PDF
with open("GeneratedCharacter.pdf", "wb") as output_stream:
    pdfWriter.write(output_stream)

pdfFileObj.close()