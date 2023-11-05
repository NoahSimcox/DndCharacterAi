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
pRace = DndAi.dnd_race_var
gearArmor = DndAi.dnd_armor_var
gearWeapon = DndAi.dnd_weapon_var
gearMisc = ["Adventurer's Pack", "Ball Bearings"]
possibleSkills = DndAi.dnd_profs_list


# ability score determining
statRanks = DndAi.refined_stat_rankings_list
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
expertiseCount = 0
expertiseSkills = []
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
        profArmor = "light, medium, & heavy armor, as well as shields"
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
        profLanguages += ", Thieves' Cant"
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
for i in range(expertiseCount):
    expertiseSkills += skills[i]
    
pAcrobatics = pDexMod + profBonus*("Acrobatics" in skills)*(1 + "Acrobatics" in expertiseSkills)
pAnimalHandling = pWisMod + profBonus*("Animal Handling" in skills)*(1 + "Animal Handling" in expertiseSkills) 
pArcana = pIntMod + profBonus*("Arcana" in skills)*(1 + "Arcana" in expertiseSkills)
pAthletics = pStrMod + profBonus*("Athletics" in skills)*(1 + "Athletics" in expertiseSkills)
pDeception = pChaMod + profBonus*("Deception" in skills)*(1 + "Deception" in expertiseSkills)
pHistory = pIntMod + profBonus*("History" in skills)*(1 + "History" in expertiseSkills)
pInsight = pWisMod + profBonus*("Insight" in skills)*(1 + "Insight" in expertiseSkills)
pIntimidation = pChaMod + profBonus*("Intimidation" in skills)*(1 + "Intimidation" in expertiseSkills)
pInvestigation = pIntMod + profBonus*("Investigation" in skills)*(1 + "Investigation" in expertiseSkills)
pMedicine = pWisMod + profBonus*("Medicine" in skills)*(1 + "Medicine" in expertiseSkills)
pNature = pIntMod + profBonus*("Nature" in skills)*(1 + "Nature" in expertiseSkills)
pPerception = pWisMod + profBonus*("Perception" in skills)*(1 + "Perception" in expertiseSkills)
pPerformance = pChaMod + profBonus*("Performance" in skills)*(1 + "Performance" in expertiseSkills)
pPersuasion = pChaMod + profBonus*("Persuasion" in skills)*(1 + "Persuasion" in expertiseSkills)
pReligion = pWisMod + profBonus*("Religion" in skills)*(1 + "Religion" in expertiseSkills)
pSleightOfHand = pDexMod + profBonus*("Sleight of Hand" in skills)*(1 + "Sleight of Hand" in expertiseSkills)
pStealth = pDexMod + profBonus*("Stealth" in skills)*(1 + "Stealth" in expertiseSkills)
pSurvival = pWisMod + profBonus*("Survival" in skills)*(1 + "Survival" in expertiseSkills)

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
        featTraits += "Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.\nDwarven Resilience: You resist poison damage and have advantage on saving throws against poison.\nStonecunning: If you make an Intelligence (History) check related to stonework, you add double your proficiency bonus to the check.\n"
        profTools += "smith's tools, brewer's supplies, mason's tools, "
        profLanguages += ", Dwarvish"
    case "Elf":
        featTraits += "Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.\nFey Ancestry: You have advantage on saving throws against being charmed, and magic can't put you to sleep.\nTrance: You only need to sleep for 4 hours to get the benefits of a long rest.\nYou can attempt to hide when you are lightly obscured by some natural phenomena.\n"
        profLanguages += ", Elvish"
        skills += "Perception"
    case "Gnome":
        featTraits += "Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.\nGnome Cunning: you have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic.\nTinker: Using tinker's tools, you can spend 1 hour and 10 gp to make a Tiny clockwork device (AC 5, 1 hp) that lasts for up to 24 hours, unless you spend 1 hour repairing it to keep it working. You can have up to 3 of these active at once, and when you make one choose one of the following options:\n\tClockwork Toy: The toy looks like a creature of your choice, and when placed on the ground it moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents.\n\tFire Starter: You can use an action to cause the device to make a small fire that you can use to light a candle, torch, or campfire.\n\tMusic Box: When opened, the box plays a single song at a moderate volume. It stops playing when the song ends or when it is closed.\n"
        profLanguages += ", Gnomish"
        profTools += "tinker's tools, "
    case "Half-Elf":
        featTraits += "Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.\nFey Ancestry: You have advantage on saving throws against being charmed, and magic can't put you to sleep.\n"
        profLanguages += ", Elvish"
    case "Half-Orc":
        featTraits += "Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.\nRelentless Endurance. Once per long rest when you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead.\nSavage Attacks: When you score a critical hit with a melee weapon attack, you can add one additional damage die and add it to the total damage.\n"
        skills += "Intimidation"
        profLanguages += ", Orcish"
    case "Halfling":
        featTraits += "Lucky: When you roll a 1 on a d20 roll, you can reroll the die and must use the new result, even if it is a 1.\nBrave: You have advantage on saving throws against being frightened.\nNimble: You can move through the space of any creature that is a larger size than you. \nNaturally Stealthy: You can attempt to hide if you are obscured by a creature that is a larger size than you.\n"
        profLanguages += ", Halfling"
    case "Human":
        profLanguages += ", Elvish, Dwarvish"
    case "Tiefling":
        featTraits += "Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.\nHellish Resistance: You resist fire damage.\n"
        profLanguages += ", Infernal"
        # ADD THAT TIEFLINGS GET THE THAUMATURGY CANTRIP

finalProfLang = "Proficient in " + profArmor + "\nProficient in " + profWeapon + "\nFluent in " + profLanguages + "\n"

match pClass: # class traits
    case "Artificer":
        featTraits += "Spellcasting: you are a Charisma-based spellcaster, and have cantrips & spells listed in the spellcasting page of your character sheet. Cantrips can be cast repeatedly, but each use of a first level spell expends a first level spell slot, which regenerate when you complete a long rest.\nMagical Tinkering: If you're holding thieves' or artisan's tools, you can use an action to touch a Tiny object and give it one of the following properties:\n\t1) The object sheds bright light in a 5-foot radius and dim light for another 5 feet.\n\t2) When tapped by a creature, the object replays a 6-second message that you record when you tinker with the object. This can be heard up to 10 feet away.\n\t3) The object continuously emits a single odor or nonverbal sound that you choose, observable up to 10 feet away.\n\t4) A static visual effect appears on one of the object's surfaces. This effect can be a picture, up to 25 words of text, lines and shapes, or a mixture of these elements, as you like.\nThese properties last indefinitely and you can have up to " + pIntMod + " active at a time. You can cancel one effect as an action.\n"
    case "Barbarian":
        featTraits += "Rage: You have 2 rages per long rest, and can enter one as a bonus action. While raging, you are unable to cast spells but gain:\n\t1) Advantage on Strength checks/saving throws\n\t2) +2 damage to Strength-based melee weapon attacks\n\t3) Resistance to piercing, bludgeoning, and slashing damage.\nRage ends after 1 minute, you spend 1 round without taking or dealing damage, or you end it as a bonus action.\nUnarmored Defense: If you aren't wearing any armor (a shield is fine), your AC equals " + str(10+pDexMod+pConMod) + ".\n"
    case "Bard":
        featTraits += "Spellcasting: you are a Charisma-based spellcaster, and have cantrips & spells listed in the spellcasting page of your character sheet. Cantrips can be cast repeatedly, but each use of a first level spell expends a first level spell slot, which regenerate when you complete a long rest.\nBardic Inspiration: You have " + pChaMod + " uses of bardic inspiration per long rest. You can use a bonus action to give a d6 'bardic inspiration die' to an ally within 60 feet of you. Once within the next 10 minutes, that ally can roll the die and add the result to one d20 roll it makes. A creature can only have 1 bardic inspiration die at a time.\n"
    case "Cleric":
        featTraits += "Spellcasting: you are a Wisdom-based spellcaster, and have cantrips & spells listed in the spellcasting page of your character sheet. Cantrips can be cast repeatedly, but each use of a first level spell expends a first level spell slot, which regenerate when you complete a long rest.\nDisciple of Life: Your healing spells each heal an additional 3 health.\n"
        # ADDITIONAL SPELLS: BLESS & CURE WOUNDS
    case "Druid":
        featTraits += "Spellcasting: you are a Wisdom-based spellcaster, and have cantrips & spells listed in the spellcasting page of your character sheet. Cantrips can be cast repeatedly, but each use of a first level spell expends a first level spell slot, which regenerate when you complete a long rest.\n"
    case "Fighter":
        featTraits += "Fighting Style (Defense): You gain +1 AC while wearing armor.\nSecond Wind: Once per long rest, you can use a bonus action to regain 1d10+1 health.\n"
    case "Monk":
        featTraits += "Martial Arts: While you don't wear armor or a shield, you gain mastery over unarmed combat and monk weapons, which are shortswords and simple melee weapons without the two-handed or heavy properties. This allows you to use Dexterity instead of Strength for the attack/damage rolls of unarmed strikes & monk weapons, allows your unarmed strikes to deal 1d4 damage, and when you attack with an unarmed strike or monk weapon you can make one unarmed strike as a bonus action. \nUnarmored Defense: If you aren't wearing any armor or shield, your AC equals " + str(10+pDexMod+pWisMod) + ".\n"
    case "Paladin":
        featTraits += "Divine Sense: " + str(1+pChaMod) + " times per long rest, you can use an action to learn the locations of any celestial, fiend, or undead within 60 feet of you that is not behind total cover. You know the type (celestial, fiend, or undead) of any being whose presence you sense, but not its identity.\nLay on Hands: you have a pool of 5 healing points that recharge on a long rest. You can use an action to spend some of these healing points to heal a creature you touch an amount of health equal to the points spent. Alternatively, you can spend all 5 healing points at once to cure one disease/poison afflicting a creature you touch.\n"
    case "Ranger":
        featTraits += "Favored Foe: Twice per long rest when you hit a creature with an attack roll, you can mark them as your favored foe for one minute or until you lose your concentration (as if concentrating on a spell). The first time you damage your favored foe on each turn, including when you mark it, you deal +1d4 damage.\nCanny: You become fluent in Elvish and Gnomish if you are not already fluent in them. Additionally, gain expertise in one skill.\n"
        expertiseCount += 1
    case "Rogue":
        featTraits += "Expertise: Gain expertise in 2 skills.\nSneak Attack: Once per turn when you hit with a Dexterity-based attack roll, you can do +1d6 damage if you either 1) have advantage on the attack roll or 2) if you have an ally adjacent to the target and the attack doesn't have disadvantage.\n"
        expertiseCount += 2
    case "Sorcerer":
        featTraits += "Spellcasting: you are a Charisma-based spellcaster, and have cantrips & spells listed in the spellcasting page of your character sheet. Cantrips can be cast repeatedly, but each use of a first level spell expends a first level spell slot, which regenerate when you complete a long rest.\nWild Magic Surge: whenever you cast a levelled spell, roll a d20. On a 1, roll on the Wild Magic table.\nTides of Chaos: You can use this ability to gain advantage on one d20 roll. You are then unable to use it until you cast a levelled spell, upon which you regain use of the feature and immediately roll on the wild magic table.\n"
    case "Warlock":
        featTraits += "Spellcasting: you are a Charisma-based spellcaster, and have cantrips & spells listed in the spellcasting page of your character sheet. Cantrips can be cast repeatedly, but each use of a first level spell expends a first level spell slot, which regenerate when you complete a short rest.\nDark One's Blessing: when you kill an enemy, you immediately gain " + str(pChaMod+pLevel) + " temporary hit points.\n" 
        # ADDITIONAL SPELLS: BURNING HANDS & COMMAND SPELLS
    case "Wizard":
        featTraits += "Spellcasting: you are an Intelligence-based spellcaster, and have cantrips & spells listed in the spellcasting page of your character sheet. Cantrips can be cast repeatedly, but each use of a first level spell expends a first level spell slot, which regenerate when you complete a long rest.\nArcane Recovery: Once per long rest, you can regain 1 levels worth of expended spell slots when you complete a short rest.\n"

# money
gp = 125
if pClass in ["Wizard", "Warlock", "Rogue", "Artificer"]:
    gp -= 25
elif pClass in ["Sorcerer"]:
    gp -= 50
elif pClass in ["Barbarian", "Druid"]:
    gp -= 75
elif pClass in ["Monk"]:
    gp -= 112

cp = random.randint(100, 300)
sp = int((1000 - cp) / 10)
ep = 0
pp = 0

# armor
ac = 10 + (pClass == "Fighter")
match gearArmor:
    case "Padded Armor" | "Leather Armor":
        ac += 1 + pDexMod
        gp -= 10
    case "Studded Leather":
        ac += 2 + pDexMod
        gp -= 45
    case "Hide Armor":
        ac += 2 + min(pDexMod, 2)
        gp -= 10
    case "Chain Shirt":
        ac += 3 + min(pDexMod, 2)
        gp -= 50
    case "Scale Mail":
        ac += 4 + min(pDexMod, 2)
        gp -= 50
    case "Breastplate":
        ac += 4 + min(pDexMod, 2)
        gp -= 400
    case "Halfplate" | "Half Plate":
        ac += 5 + min(pDexMod, 2)
        gp -= 750
    case "Ring Mail":
        ac += 4
        gp -= 30
    case "Chain Mail":
        ac += 6
        gp -= 75
    case "Splint" | "Splint Armor":
        ac += 7
        gp -= 200
    case "Plate" | "Plate Mail" | "Plate Armor":
        ac += 8
        gp -= 1500


# weapons
weaponB = pStrMod
if(gearWeapon in ["Dagger", "Shortsword", "Rapier", "Scimitar", "Whip", "Light Crossbow", "Dart", "Shortbow", "Sling", "Hand Crossbow", "Heavy Crossbow", "Longbow"]):
    weaponB = pDexMod
wAtkB = weaponB + profBonus 

dmgDie = "1d8"
match gearWeapon:
    case "Blowgun":
        dmgDie = "1"
        gp -= 10
    case "Club" | "Dagger" | "Light Hammer" | "Sickle" | "Dart" | "Sling":
        dmgDie = "1d4"
        gp -= 2
    case "Handaxe" | "Javelin" | "Mace" | "Quarterstaff" | "Spear" | "Shortbow" | "Scimitar" | "Shortsword" | "Trident" | "Hand Crossbow":
        dmgDie = "1d6"
        gp -= 10
    case "Glaive" | "Halberd" | "Pike" | "Heavy Crossbow":
        dmgDie = "1d10"
        gp -= 20
    case "Greataxe" | "Lance":
        dmgDie = "1d12"
        gp -= 20
    case "Greatsword" | "Maul":
        dmgDie = "2d6"
        gp -= 30

if(gp <= 0): gp = 0

dmgType = "s"
match gearWeapon:
    case "Club" | "Greatclub" | "Light Hammer" | "Mace" | "Quarterstaff" | "Flail" | "Maul" | "Warhammer":
        dmgType = "b"
    case "Dagger" | "Javelin" | "Spear" | "Light Crossbow" | "Dart" | "Shortbow" | "Sling" | "Lance" | "Morningstar" | "Pike" | "Rapier" | "Shortsword" | "Trident" | "War Pick" | "Blowgun" | "Hand Crossbow" | "Heavy Crossbow" | "Longbow":
        dmgType = "p"

weaponTags = gearWeapon + " has the following tags: "
if(gearWeapon in ["Dagger", "Rapier", "Scimitar", "Shortsword", "Whip"]):
    weaponTags += "\nFinesse (Attacks with Dexterity, not Strength)"
if(gearWeapon in ["Club", "Handaxe", "Light Hammer", "Sickle", "Scimitar", "Shortsword", "Hand Crossbow"]):
    weaponTags += "\nLight (Can be dual wielded effectively)"
if(gearWeapon in ["Glaive", "Halberd", "Lance", "Pike", "Whip"]):
    weaponTags += "\nReach (Range is 10 feet, not 5 feet)"
if(gearWeapon in ["Greatclub", "Light Crossbow", "Shortbow", "Glaive", "Greataxe", "Greatsword", "Halberd", "Maul", "Pike", "Heavy Crossbow", "Longbow"]):
    weaponTags += "\nTwo-Handed (Requires two hands to attack with)"
if(gearWeapon in ["Quarterstaff", "Spear", "Battleaxe", "Longsword", "Trident", "Warhammer"]):
    weaponTags += "Versatile (If you wield this weapon with two hands, increase the damage die by 1 stage. Ex: 1d8 -> 1d10)"

if(gearWeapon in ["Dagger", "Handaxe", "Light Hammer", "Spear", "Dart", "Trident"]):
    weaponTags += "\nThrown 20/60 (Can be thrown as a ranged attack using the same modifier you usually would. Within 20 feet is a normal roll, within 60 feet has disadvantage)"
if(gearWeapon in ["Javelin"]):
    weaponTags += "\nThrown 30/120 (Can be thrown as a ranged attack using the same modifier you usually would. Within 30 feet is a normal roll, within 120 feet has disadvantage)"
if(gearWeapon in ["Light Crossbow", "Shortbow"]):
    weaponTags += "\nRanged 80/320 (Must be used for a Dexterity-based ranged attack. Aiming within 80 feet is a normal roll, within 320 feet has disadvantage)"
if(gearWeapon in ["Sling", "Hand Crossbow"]):
    weaponTags += "\nRanged 30/120 (Must be used for a Dexterity-based ranged attack. Aiming within 30 feet is a normal roll, within 120 feet has disadvantage)"
if(gearWeapon in ["Blowgun"]):
    weaponTags += "\nRanged 25/100 (Must be used for a Dexterity-based ranged attack. Aiming within 25 feet is a normal roll, within 100 feet has disadvantage)"
if(gearWeapon in ["Longbow"]):
    weaponTags += "\nRanged 150/600 (Must be used for a Dexterity-based ranged attack. Aiming within 150 feet is a normal roll, within 600 feet has disadvantage)"
if(gearWeapon in ["Heavy Crossbow"]):
    weaponTags += "\nRanged 100/400 (Must be used for a Dexterity-based ranged attack. Aiming within 100 feet is a normal roll, within 400 feet has disadvantage)"


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
        "AC": ac,
        "AttacksSpellcasting": weaponTags,
        "Wpn Name": gearWeapon,
        "Wpn1 AtkBonus": wAtkB,
        "Wpn1 Damage": dmgDie + "+" + weaponB + " " + dmgType,
        
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

output_stream.close()