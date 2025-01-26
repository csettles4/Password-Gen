#1/24/2025 ---- Password Strength Checking ----
#Takes a string and analyzes it and returns a rating for your password.
#Uses CISA.gov Guidelines for a strong password.



def PWStrengthCheck():

    PW = input("Input password for strenght check: ")
    
    # Variables for checking conditions of PW variable
    OOE_16_Chars = False
    OOE_16_Upper = False
    OOE_16_Num = False
    OOE_16_Symbol = False

    OOE_8LT_16_Chars = False
    OOE_8LT_16_Upper = False
    OOE_8LT_16_Num = False
    OOE_8LT_16_Symbol = False

    LT_8_GT_6_Chars = False
    LT_8_GT_6_Upper = False
    LT_8_GT_6_Num = False
    LT_8_GT_6_Symbol = False

    LT_6_Chars = False

#-------------------------------------------------------------------------------------------------

    if len(PW) >= 16:
        OOE_16_Chars = True
        for char in PW:
            if char.isupper():  #Checks if the character in the string is capital
                OOE_16_Upper = True

            if char.isdigit():  #Checks if the character in the string is a number
                OOE_16_Num = True

            if not char.isalnum(): #Checks if the character in the string is a symbol
                OOE_16_Symbol = True

        if not any([OOE_16_Upper, OOE_16_Num, OOE_16_Symbol]): #Checks if all three of them are false
            print("STRONG: Try adding capital letters, numbers, and symbols for a higher rating.")

        if any([OOE_16_Symbol, OOE_16_Num, OOE_16_Upper]): #Checks if at least one of them is true.
            print("VERY STRONG")

#-------------------------------------------------------------------------------------------------
   
    if len(PW) >= 8 and len(PW)< 16:
        OOE_8LT_16_Chars = True
        for char in PW:
            if char.isupper():  #Checks if the character in the string is capital
                OOE_8LT_16_Upper = True

            if char.isdigit():  #Checks if the character in the string is a number
                OOE_8LT_16_Num = True

            if not char.isalnum(): #Checks if the character in the string is a symbol
                OOE_8LT_16_Symbol = True

        if not any([OOE_8LT_16_Upper, OOE_8LT_16_Num, OOE_8LT_16_Symbol]):
            print("WEAK: Add more Characters, Symbols, Capital Letters, and Numbers")

        if any([OOE_8LT_16_Symbol, OOE_8LT_16_Num, OOE_8LT_16_Upper]):
            if all([OOE_8LT_16_Num, OOE_8LT_16_Symbol, OOE_8LT_16_Upper]):
                print("VERY STRONG")
            else:
                print("STRONG: Try adding capital letters, numbers, and symbols for a higher rating.")

#-----------------------------------------------------------------------------------------------------
  
    if len(PW) < 8 and len(PW) > 6:
        LT_8_GT_6_Chars = True
        for char in PW:
            if char.isupper():  #Checks if the character in the string is capital
                LT_8_GT_6_Upper = True

            if char.isdigit():  #Checks if the character in the string is a number
                LT_8_GT_6_Num = True

            if not char.isalnum(): #Checks if the character in the string is a symbol
                LT_8_GT_6_Symbol = True

        if not any([LT_8_GT_6_Upper, LT_8_GT_6_Num, LT_8_GT_6_Symbol]):
            print("WEAK: Add more Characters, Symbols, Capital Letters, and Numbers")

        if any([LT_8_GT_6_Symbol, LT_8_GT_6_Num, LT_8_GT_6_Upper]):
            if all([LT_8_GT_6_Num, LT_8_GT_6_Symbol, LT_8_GT_6_Upper]):
                print("STRONG: Try adding capital letters, numbers, and symbols for a higher rating.")
            else:
                print("MEDIUM: Try adding capital letters, numbers, and symbols for a higher rating.")

#-----------------------------------------------------------------------------------------------------

    if len(PW) <= 6: #If the length is less than or equal to six it defaults to Super Weak. No need to check further in the string.
        print("SUPER WEAK: Add a lot more characters along with symbols, capital letters, and numbers so that this password is acceptable.")   

PWStrengthCheck()