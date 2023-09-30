#Game Layout:
#  Main Menu:
#    1. Play Game
#    2. Character Customization
#    3. Cheats
#    4. Quit Game
#  
#  Play Game:
#    (Game Starts)
#
#  Character Customization:
#    (Displays Current Character Info)
#    1. Change Character Name
#    2. Change Character Race
#    3. Change Character Class
#    3. Choose Character Pronouns
#  
#  Cheats Menu:
#    (Displays currently enabled cheats)
#    1. All Items
#    2. Invincible
#    3. All Abilities
#  
#  Quit Game:
#    (Displays "Thanks you for playing.")

import random






class Character:
  name = "Bob"
  race = "Human"
  cclass = "Warrior"
  pronoun = "Male"
  inventory = {"Sword": 0, "Lockpicks": 0, "Magic Staff": 0, "Door Key": 0, "Exit Key": 0}
  trait = "Adaptable"
  
  
  
  
  
Player = Character()








def set_char_name():
  print("""
  ================================================================================
  Please input the name of your character!
  ================================================================================
  """)
  c_name = input("What is your name?: ")
  return c_name








def set_char_race():
  char_race = True
  def character_selection(race, trait):
    Player.race = race
    Player.trait = trait
    if Player.race == "Elf":
      an_a = "an"
    else:
      an_a = "a"
    print("""
  ================================================================================
  Your character is {a} {race}!
  ================================================================================
    """.format(race = Player.race, a = an_a))
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
    """.format(race = Player.race, trait = Player.trait))
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












def set_char_class():
  char_class = True
  def character_selection(cclass, item):
    Player.cclass = cclass
    Player.inventory.update({}.fromkeys(Player.inventory, 0))
    Player.inventory[item] = 1
    print("""
  ================================================================================
  Your character is a {cclass}!
  ================================================================================
    """.format(cclass = Player.cclass))
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
    """.format(cclass = Player.cclass))
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





def set_char_pronoun():
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
    """.format(pronoun = Player.pronoun))
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
      Player.pronoun = "Male"
      continue
    elif c_pro_inp == 2:
      Player.pronoun = "Female"
      continue
    elif c_pro_inp == 3:
      Player.pronoun = "Non-binary"
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









def character_customize():
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
    """.format(name = Player.name))
    cc_menu = input("Please select an option (1 - 4) and press 'Enter': ") or int(0)
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
      Player.name = set_char_name()
      continue
    elif cc_inp == 2:
      set_char_race()
      continue
    elif cc_inp == 3:
      set_char_class()
      continue
    elif cc_inp == 4:
      set_char_pronoun()
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







game_on = True
while game_on == True:
  print("""
  ================================================================================
  Main Menu:
    1. Play Game
    2. Character Customization
    3. Cheats
    4. Quit Game
  ================================================================================
  """)
  
  m_menu = input("Please select an option (1 - 4) and press 'Enter': ") or int(0)
  try:
    m_inp = int(m_menu)
  except:
    print("""
  ================================================================================
  Please input a number...
  ================================================================================
    """)
    input("Please press 'Enter' to continue...")
    continue
  
  if (m_inp) == 1:
    continue
  elif (m_inp) == 2:
    character_customize()
    continue
  elif (m_inp) == 3:
    continue
  elif (m_inp) == 4:
    print(" ")
    print("""
  ================================================================================
  Thank you for playing!
  ================================================================================
  """)
    input("Press Enter to continue...")
    break
  else:
    print("Error: selection not recognized.")
    continue
    
  game_on = False