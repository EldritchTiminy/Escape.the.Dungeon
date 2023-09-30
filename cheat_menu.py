def toggle_cheats(plyrname):
  cheat_menu = True
  while cheat_menu == True:
    print("""
  ================================================================================
  Cheats Menu:
    1. Invincible:          {inv}
    2. All Starting Items   {items}
    3. All Abilities        {abi}
    4. Back to Main Menu
  ================================================================================
    """.format(inv = "ON" if plyrname.cheats["Invincible"] == True else "OFF", items = "ON" if plyrname.cheats["All Items"] == True else "OFF", abi = "ON" if plyrname.cheats["All Abilities"] == True else "OFF"))
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
      plyrname.cheats["Invincible"] = True if plyrname.cheats["Invincible"] == False else False
      continue
    elif cc_inp == 2:
      plyrname.cheats["All Items"] = True if plyrname.cheats["All Items"] == False else False
      continue
    elif cc_inp == 3:
      plyrname.cheats["All Abilities"] = True if plyrname.cheats["All Abilities"] == False else False
      continue
    elif cc_inp == 4:
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