def room_0(plr):
  in_room_0 = True if plr.quit_game == False and plr.game_over == False else False
  
  def prompt1():
    print("""
  
  
  
  
  
| You wake in a square room.
|
| Shackles and cuffs attached by chains line the walls around you.
|
| A single torch fastened to the opposite wall provides the only light in this room.
  
  """)
    input("  Please press 'Enter' to continue...")
    print("""
  
  
  
  
  
| Your senses tell you that you're underground somewhere.
|
| On the opposite wall there is a single door, just to the left of the torch sconce.
|
| Lying on the floor before you is a note written on expensive stationary.

  """)
    input("  Please press 'Enter' to continue...")
    print("""
  
  
  
  
  
| "This should teach you to go snooping around in my treasure vault. Let's play a game. Escape this
|
| dungeon alive and you're free to go. Die and you will be forgotten like the others who learned this
|
| lesson the hard way."

  """)
    input("  Please press 'Enter' to continue...")
    plr.switch["wake"] = False
  
  
  def room_0_search():
    print("""
  
  
  
  
  
| In a pile of rubble in the corner, you find a sword with a small amount of rust on the blade.
|
| It looks functional.

    """)
    plr.switch["sword"] = True
    input("  Please press 'Enter' to continue...")
  
  while in_room_0 == True:
    if plr.quit_game == True or plr.game_over == True:
      break
    if plr.switch["wake"] == True:
      prompt1()
    print("""
  
  
  
  
  
| You are surrounded by the cold stonework of the square room. The only way forward lies ahead of you.
  
  
  What would you like to do?:
  ---------------------------
  1. Check the door.
  {second}
  ---------------------------
  9. Quit Game...
  
    """.format(second = "2. Search the room" if plr.switch["sword"] != True else " "))
    room_zero_choice = input("  Please select and option (1 - 4) and press 'Enter': ") or int(0)
    try:
      r0_inp = int(room_zero_choice)
    except:
      print("""
  ================================================================================
  Error: Please input a number...
  ================================================================================
      """)
      input("  Press 'Enter' to continue...")
      continue
    if r0_inp == 1:
      plr.switch["wake"] = False
      room_1(plr)
      continue
    elif r0_inp == 2 and plr.switch["sword"] != True:
      room_0_search()
    elif r0_inp == 9:
      plr.quit_game = True
      break
    else:
      print("""
  ================================================================================
  Error: Selection not recognized...
  ================================================================================
      """)
      input("  Please press 'Enter' to continue...")
      continue






def room_1(plr):
  in_room_1 = True if plr.quit_game == False and plr.game_over == False else False
  
  def prompt1():
    print("""
  
  
  
  
  
| The room before you resembles a wide hallway, about 10 feet wide and about 30 feet long.
|
| There is a door on far side of the hall leading further into the dungeon.

    """)
    input("  Please press 'Enter' to continue...")
    print("""
  
  
  
  
  
| However, after the first 10 foot section of this room, which is a safe
|
| zone, there are spouts jutting from the walls on either side of the room that 
|
| spew fire, making the rest of the room impassable.

    """)
    input("  Please press 'Enter' to continue...")
    plr.switch["room1intro"] = False
  
  prompt2 = "The fire spouts block your passage."
  
  prompt3 = "The path formed by the spell cuts through the fire in front of you."
  
  def skeleton():
    print("""
  
  
  
  
  
| At first there doesn't seem to be anything notable about this skeleton.
|
| However, as you are about to walk away, you notice the rock the skeleton is leaning against.
|
| Between it and the wall is a small satchel.

  """)
    input("  Please presss 'Enter' to continue...")
    print("""
  
  
  
  
  
| Inside is a surprisingly well preserved journal.
|
| The journal's owner was close to deciphering the code written on the opposite wall,
|
| but succombed to a wound before he could finish his work.

    """)
    plr.switch["book"] = True
    plr.switch["skeleton"] = False
    input("  Please press 'Enter' to continue...")
  
  def use_wallspell():
    print("""
  
  
  
  
  
| Following the instructions for the arcane formula, you move your hands through
|
| a series of motions and utter a set of arcane words.

    """)
    input("  Please press 'Enter' to continue...")
    print("""
    
    
    
    
    
| Suddenly walls of force form a square corridor that cuts through the fire,
|
| allowing passage through it.

    """)
    input("  Please press 'Enter' to continue...")
    plr.switch["wallspell"] = False
  
  def wall_spell():
    print("""
  
  
  
  
  
| You are able to finish the decoding work of the journal and descover what
|
| the text on the wall actually says.
|
| It's instructions for a magic spell that will get you past the spouts of fire. 

    """)
    input("  Please press 'Enter' to continue...")
    print("""
    
    
    
    
    
| You quickly record the work you've done in the journal and leave it 
|
| for the next victim of the dungeon, just in case.

    """)
    plr.switch["wallspell"] = True
    plr.switch["scratches"] = False
    input("Please press 'Enter' to continue...")
  
  def wall_scratches():
    wall_scratches = True
    while wall_scratches == True:
      print("""
  
  
  
  
  
| Scratched into the wall is a bunch of text that doesn't seem to make any sense to you.
|
| It could be written in code, but you're unsure how to even begin deciphering it.

  ---------------------------
  What would you like to do?:
    {first}
    2. Go back.
  ---------------------------
    9. Quit Game...
  
      """.format(first = "1. Decipher the code" if plr.switch["book"] == True else " "))
      wall_scratch_choice = input("Please select an option (1 - 4) and press 'Enter': ") or int(0)
      try:
        wc_inp = int(wall_scratch_choice)
      except:
        print("""
  ================================================================================
  Error: Please input a number...
  ================================================================================
        """)
        input("Press 'Enter' to continue...")
        continue
      if wc_inp == 1 and plr.switch["book"] == True:
        wall_spell()
        break
      elif wc_inp == 2:
        break
      elif wc_inp == 9:
        plr.quit_game = True
        break
      else:
        print("""
  ================================================================================
  Error: Selection not recognized...
  ================================================================================
      """)
        input("  Please press 'Enter' to continue...")
        continue
  
  while in_room_1 == True:
    if plr.quit_game == True or plr.game_over == True:
      break
    if plr.switch["room1intro"] == True:
      prompt1()
    print("""
  
  
  
  
  
| {prompt}
|
| There seems to be something scratched into the wall just to the left of 
|
| the entrace, and to the right there is a skeleton of one of the dungeon's victims.

  ---------------------------
  What would you like to do?:
    {first}
    {second}
    {third}
    {fourth}
    5. Go back.
  ---------------------------
    9. Quit to Main Menu...

    """.format(prompt = prompt3 if plr.switch["scratches"] == False and plr.switch["wallspell"] == False else prompt2, first = "1. Investigate the scratches on the wall." if plr.switch["scratches"] == True else " ", second = "2. Investigate the skeleton." if plr.switch["skeleton"] == True else " ", third = "3. Use the spell." if plr.switch["wallspell"] == True else " ", fourth = "4. Continue forward." if plr.switch["scratches"] == False and plr.switch["wallspell"] == False else " "))
    room_one_choice = input("Please select an option (1 - 4) and press 'Enter': ") or int(0)
    try:
      r1_inp = int(room_one_choice)
    except:
      print("""
  ================================================================================
  Error: Please input a number...
  ================================================================================
      """)
      input("Press 'Enter' to continue...")
      continue
    if r1_inp == 1:
      wall_scratches()
      continue
    elif r1_inp == 2 and plr.switch["skeleton"] == True:
      skeleton()
      continue
    elif r1_inp == 3 and plr.switch["wallspell"] == True:
      use_wallspell()
      continue
    elif r1_inp == 4 and plr.switch["wallspell"] == False and plr.switch["scratches"] == False:
      room_2(plr)
    elif r1_inp == 5:
      room_0(plr)
    elif r1_inp == 9:
      plr.quit_game = True
      break
    else:
      print("""
  ================================================================================
  Error: Selection not recognized...
  ================================================================================
      """)
      input("  Please press 'Enter' to continue...")
      continue






def room_2(plr):
  in_room_2 = True if plr.quit_game == False and plr.game_over == False else False
  
  def prompt1():
    print("""
  
  
  
  
  
| All across this room are scattered corpses and piles of bones.
|
| Standing in the center of the room is the creature that struck them all down:
|
| a walking skeleton with glowing red motes of light where it's eyes should be.

    """)
    input("  Please press 'Enter' to continue...")
    print("""
  
  
  
  
  
| It wields a sword and wears the remains of armor that has almost rusted away completely,
|
| offering very little in the way of protection.
|
| Across the room is the next door that leads further into the dungeon.

    """)
    input("  Please press 'Enter' to continue...")
  
  prompt2 = "The skeleton stands in the room before you."
  
  prompt3 = "The room appears empty, other than the scattered remains scattered about."
  
  def skel_attack():
    print("""
  
  
  
  
  
| You rush up behind the skeleton, using the element of surprise to gain the advantage.
|
| With a single strong swing of your sword, you send the skeleton toppling
|
| to the floor in a heap of scattering bones. The way is now safe for you to traverse.

    """)
    plr.switch["enemy"] = False
    input("Please press 'Enter' to continue...")
    
  
  def skel_sneak():
    print("""
  
  
  
  
  
| You attempt to sneak by the skeleton, but his undead senses detect your presence
|
| before you can make it to the other side of the room.
|
| The skeleton, faster than you expected, is upon you before you can even react.

    """)
    input("  Please press 'Enter' to continue...")
    print("""
  
  
  
  
  
| It cuts you down and returns to its post, 
|
| leaving you to die from your wounds and join the rest of the fallen here.

    """)
    input("Please press 'Enter' to continue...")
    print("""
  
  
  
  
  =============
  Game over....
  =============

    """)
    plr.game_over = True
    input("Please press 'Enter' to continue...")
  
  while in_room_2 == True:
    if plr.quit_game == True or plr.game_over == True:
      break
    if plr.switch["enemy"] == True:
      prompt1()
    print("""
  
  
  
  
  
  {prompt}
  
  
  What would you like to do?:
  ---------------------------
    {first}
    {second}
    {third}
    4. Go back.
  ---------------------------
    9. Quit Game...

    """.format(prompt = prompt2 if plr.switch["enemy"] == True else prompt3, first = "1. Attack him from behind." if plr.switch["sword"] == True and plr.switch["enemy"] == True else " ", second = "2. Sneak past him." if plr.switch["enemy"] == True else " ", third = "3. Continue forward." if plr.switch["enemy"] != True else " "))
    room_two_choice = input("Please select an option (1 - 4) and press 'Enter': ") or int(0)
    try:
      r2_inp = int(room_two_choice)
    except:
      print("""
  ================================================================================
  Please input a number...
  ================================================================================
      """)
      input("Press 'Enter' to continue...")
      continue
    if r2_inp == 1 and plr.switch["sword"] == True and plr.switch["enemy"] == True:
      skel_attack()
    elif r2_inp == 2 and plr.switch["enemy"] == True:
      skel_sneak()
      break
    elif r2_inp == 3:
      room_3(plr)
      pass
    elif r2_inp == 4:
      break
    elif r2_inp == 9:
      plr.quit_game = True
      break
    else:
      print("Error: selection not recognized.")
      continue






def room_3(plr):
  in_room_3 = True if plr.quit_game == False and plr.game_over == False else False
  
  def prompt1():
    print("""
  
  
  
  
  
| This room is divided into two parts by a large portcullis. 
|
| On your side of the room, there is a pedistal with writing carved into it.

    """)
    input("  Please press 'Enter' to continue...")
    print("""
    
    
    
    
  
| "The wealthy want it. The poor have it. Either will die if they eat it."
|
| You must speak your answer aloud to answer the riddle.

    """)
    input("  Please press 'Enter' to continue...")
    plr.switch["room3intro"] = False
  
  prompt2 = '"The wealthy want it. The poor have it. Either will die if they eat it."'
  
  prompt3 = "The portcullis that divides this room in half is open. The next door awaits you."
  
  def riddle_success():
    print("""
  
  
  
  
  
| The porcullis shakes and grinds upward as the way is opened to you.
|
| You have given the correct answer to the riddle.
|
| On the other side of the portcullis is the next door that leads into the unknown.

    """)
    input("Please press 'Enter' to continue...")
    plr.switch["riddle"] = False
  
  def riddle_trap():
    print("""
  
  
  
  
  
| The walls tremble around you as if the dungeon itself has grown angry
|
| and the room begins to fill with poisonous gas.
|
| You choke on your own breath as the poison takes effect and your vision fades to blackness.

    """)
    input("Please press 'Enter' to continue...")
    print("""
  
  
  
  
  =============
  Game over....
  =============

    """)
    input("Please press 'Enter' to continue...")
    plr.game_over = True
  
  
  def riddle_ans():
    riddle_counter = 3
    while riddle_counter >= 1:
      print("""
  
  
  
  
  
| You step up to the pedistal. You have {count} attempts remaining. 
|
| "The wealthy want it. The poor have it. Either will die if they eat it."
|
| What is the answer to the riddle?
|
| (Tip: Type your answer with no spaces and no punctuation.)

      """.format(count = riddle_counter))
      riddle_answer = input("What do you say?: ")
      riddle_answer = riddle_answer.lower()
      if riddle_answer == "nothing":
        riddle_success()
        break
      else:
        print("""
  
  
  
  
  
|That was not the correct answer. You feel the floor shake angrily.

        """)
        riddle_counter += -1
        input("Please press 'Enter' to continue...")
    if riddle_counter < 1:
      riddle_trap()
  
  while in_room_3 == True:
    if plr.quit_game == True or plr.game_over == True:
      break
    if plr.switch["room3intro"] == True:
      prompt1()
    print("""
  
  
  
  
  
| {prompt}
  
  
  What would you like to do?:
  ---------------------------
    {first}
    {second}
    3. Go back.
  ---------------------------
    9. Quit Game...

    """.format(prompt = prompt2 if plr.switch["riddle"] == True else prompt3, first = "1. Try to answer the riddle." if plr.switch["riddle"] == True else " ", second = "2. Continue forward." if plr.switch["riddle"] != True else " "))
    room_three_choice = input("Please select an option (1 - 4) and press 'Enter': ") or int(0)
    try:
      r3_inp = int(room_three_choice)
    except:
      print("""
  ================================================================================
  Please input a number...
  ================================================================================
      """)
      input("Press 'Enter' to continue...")
      continue
    if r3_inp == 1 and plr.switch["riddle"] == True:
      riddle_ans()
      continue
    elif r3_inp == 2 and plr.switch["riddle"] != True:
      dungeon_end(plr)
      continue
    elif r3_inp == 3:
      break
    elif r3_inp == 9:
      plr.quit_game = True
      break
    else:
      print("""
  Error: selection not recognized.
      """)
      input("Please press 'Enter' to continue...")






def dungeon_end(plr):
  print("""
  
  
  
  
  
| As you pass through the door, your eyes are met with bright sunlight and fresh air.
|
| You are out in the wilderness, but at least you are out.
|
| You have survived the dungeon and will live to see another day.

  """)
  input("Please press 'Enter' to continue...")
  print("""
  
  
  
  
  
  ===================================
  Well done! Thank you for playing...
  ===================================

  """)
  input("Please press 'Enter' to continue...")
  plr.game_over = True





class Character:
  switch = {}
  switch = {"skeleton": True, "scratches": True, "enemy": True, "sword": False, "book": False, "wallspell": False, "riddle": True, "wake": True, "room1intro": True, "room3intro": True}
  quit_game = False
  game_over = False
  def reset(self):
    self.switch["skeleton"] = True
    self.switch["scratches"] = True
    self.switch["enemy"] = True
    self.switch["sword"] = False
    self.switch["book"] = False
    self.switch["wallspell"] = False
    self.switch["riddle"] = True
    self.game_over = False
    self.quit_game = False
Player = Character()






game_on = True
while game_on == True:
  if Player.quit_game == True:
    break
  print("""
  ==============
  Main Menu:
    1. Play Game
    2. Quit Game
  ==============
  """)
  m_menu = input("Please select an option (1 - 4) and press 'Enter': ") or int(0)
  try:
    m_inp = int(m_menu)
  except:
    print("""
  
  
  
  
  
  ========================
  Please input a number...
  ========================

    """)
    input("Please press 'Enter' to continue...")
  if (m_inp) == 1:
    Player.reset()
    room_0(Player)
  elif (m_inp) == 2:
    print("""
  
  
  
  
  
  ======================
  Thank you for playing!
  ======================

    """)
    input("Press Enter to continue...")
    break
  else:
    print("Error: selection not recognized.")