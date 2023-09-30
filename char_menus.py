def set_char_name():
  print("""
  ================================================================================
  Please input the name of your character!
  ================================================================================
  """)
  c_name = input("What is your name?: ")
  return c_name

def set_char_race(plyrname):
  char_race = True
  def character_selection(race, trait):
    plyrname.race = race
    plyrname.trait = trait
    if plyrname.race == "Elf":
      an_a = "an"
    else:
      an_a = "a"
    print("""
  ================================================================================
  Your character is {a} {race}!
  ================================================================================
    """.format(race = plyrname.race, a = an_a))
    input("Please press 'Enter' to continue...")
    return char_race == False
  while char_race == True:
    print("""
  ================================================================================
  Character Race: {race}
  Character Trait: {trait}
  ================================================================================
  Select a race for your character:
    1. Human
    2. Elf
    3. Hobbit
    4. Back to Character Customization
  ================================================================================
    """.format(race = plyrname.race, trait = plyrname.trait))
    c_race = input("Please select an option (1 - 3) and press 'Enter': ") or int(0)
    try:
      c_race_inp = int(c_race)
    except:
      print("""
  ================================================================================
  Please input a number...
  ================================================================================
      """)
      input("Please press 'Enter' to continue...")
      continue
    if c_race_inp == 1:
      character_selection("Human", "Adaptable")
    elif c_race_inp == 2:
      character_selection("Elf", "Elvish")
    elif c_race_inp == 3:
      character_selection("Hobbit", "Nimble")
    elif c_race_inp == 4:
      break
    elif c_race_inp == 42:
      character_selection("Cat-Folk", "All")
    else:
      print("""
  ================================================================================
  Error: selection not recognized.
  ================================================================================
      """)
      input("Please press 'Enter' to continue...")
      continue

def set_char_class(plyrname):
  char_class = True
  def character_selection(cclass, item):
    plyrname.cclass = cclass
    plyrname.inventory.update({}.fromkeys(plyrname.inventory, 0))
    plyrname.inventory[item] = 1
    print("""
  ================================================================================
  Your character is a {cclass}!
  ================================================================================
    """.format(cclass = plyrname.cclass))
    input("Please press 'Enter' to continue...")
    return char_class == False
  while char_class == True:
    print("""
  ================================================================================
  Character Class: {cclass}
  ================================================================================
  Select a class for your character:
    1. Warrior
    2. Burglar
    3. Sorcerer
    4. Back to Character Customization
  ================================================================================
    """.format(cclass = plyrname.cclass))
    c_class = input("Please select an option (1 - 3) and press 'Enter': ") or int(0)
    try:
      c_class_inp = int(c_class)
    except:
      print("""
  ================================================================================
  Please input a number...
  ================================================================================
      """)
      input("Please press 'Enter' to continue...")
      continue
    if c_class_inp == 1:
      character_selection("Warrior", "Sword")
    elif c_class_inp == 2:
      character_selection("Burglar", "Lockpicks")
    elif c_class_inp == 3:
      character_selection("Sorcerer", "Magic Staff")
    elif c_class_inp == 4:
      break
    else:
      print("""
  ================================================================================
  Error: selection not recognized.
  ================================================================================
      """)
      input("Please press 'Enter' to continue...")
      continue

def set_char_pronoun(plyrname):
  char_pro = True
  while char_pro == True:
    print("""
  ================================================================================
  Current Pronoun Setting: {pronoun}
  ================================================================================
  Select pronouns for your character:
    1. Male: He/Him/His
    2. Female: She/Her/Her
    3. Nonbinary: They/Them/Their
    4. Back to Character Customization
  ================================================================================
    """.format(pronoun = plyrname.pronoun))
    c_pronoun = input("Please select an option (1 - 3) and press 'Enter': ") or int(0)
    try:
      c_pro_inp = int(c_pronoun)
    except:
      print("""
  ================================================================================
  Please input a number...
  ================================================================================
      """)
      input("Please press 'Enter' to continue...")
      continue
    if c_pro_inp == 1:
      plyrname.pronoun = "Male"
      continue
    elif c_pro_inp == 2:
      plyrname.pronoun = "Female"
      continue
    elif c_pro_inp == 3:
      plyrname.pronoun = "Non-binary"
      continue
    elif c_pro_inp == 4:
      break
    else:
      print("""
  ================================================================================
  Error: selection not recognized.
  ================================================================================
      """)
      input("Please press 'Enter' to continue...")
      continue

def character_customize(plyrname):
  character_menu = True
  while character_menu == True:
    print("""
  ================================================================================
  Character Customization:             Player name: {name}
    1. Choose Character Name
    2. Choose Character Race
    3. Choose Character Class
    4. Choose Character Pronouns
    5. Back to Main Menu
  ================================================================================
    """.format(name = plyrname.name))
    cc_menu = input("Please select an option (1 - 5) and press 'Enter': ") or int(0)
    try:
      cc_inp = int(cc_menu)
    except:
      print("""
  ================================================================================
  Please input a number...
  ================================================================================
      """)
      input("Please press 'Enter' to continue...")
      continue
    if cc_inp == 1:
      plyrname.name = set_char_name()
      continue
    elif cc_inp == 2:
      set_char_race(plyrname)
      continue
    elif cc_inp == 3:
      set_char_class(plyrname)
      continue
    elif cc_inp == 4:
      set_char_pronoun(plyrname)
      continue
    elif cc_inp == 5:
      break
    else:
      print("""
  ================================================================================
  Error: selection not recognized.
  ================================================================================
      """)
      input("Please press 'Enter' to continue...")
      continue
    continue