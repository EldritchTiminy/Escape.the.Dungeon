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

def character_customize():
  character_menu = True
  while character_menu == True:
    print("""
  ================================================================================
  Character Customization:
    1. Choose Character Name
    2. Choose Character Race
    3. Choose Character Class
    4. Choose Character Pronouns
  ================================================================================
    """)
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
    if cc_menu == 1:
      #continue
      pass
    elif cc_menu == 2:
      #continue
      pass
    elif cc_menu == 3:
      #continue
      pass
    elif cc_menu == 4:
      #continue
      pass
    else:
      print("Error: selection not recognized.")
      #continue
    character_menu = False

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