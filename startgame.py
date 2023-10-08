import random

from char_menus import set_char_name, set_char_race, set_char_class, set_char_pronoun, character_customize
from cheat_menu import toggle_cheats



class Character:
  name = "Bob"
  race = "Human"
  cclass = "Warrior"
  pronoun = "Male"
  inventory = {"Sword": 0, "Lockpicks": 0, "Magic Staff": 0, "Door Key": 0, "Exit Key": 0}
  trait = "Adaptable"
  cheats = {"All Items": False, "Invincible": False, "All Abilities": False}

Player = Character()



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
    character_customize(Player)
    continue
  elif (m_inp) == 3:
    toggle_cheats(Player)
    continue
  elif (m_inp) == 4:
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