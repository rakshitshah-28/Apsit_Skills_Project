def currencyConvertor(count1,count2,amt):
    ans = 0
    if (count2 == "india") or (count2 == "ind"):
        if ((count1 == "europe") or (count1 == "eu")):
            ans = amt * 85.89
            print(amt,"Euro/s is equal to",ans,"Indian Rupee/s")
        elif ((count1 == "us") or (count1 == "usa") or (count1 == "united states") or (count1 == "united states of america")):
            ans = amt * 75.31
            print(amt,"American Dollar/s is equal to",ans,"Indian Rupee/s")
        elif (count1 == "japan") or (count1 == "jp") or (count1 == "jpn"):
            ans = amt * 0.70
            print(amt,"Japanese Yen is equal to",ans,"Indian Rupee/s")
        elif ((count1 == "switzerland") or (count1 == "confoederatio helvetica") or (count1 == "ch") or (count1 == "che")):
            ans = amt * 80.01
            print(amt,"Swiss Franc/s is equal to",ans,"Indian Rupee/s")
        elif ((count1 == "uk") or (count1 == "united kingdom") or (count1 == "United Kingdom of Great Britain") or (count1 == "gbr") or (count1 == "great britain")):
            ans = amt * 94.68
            print(amt,"British Pound/s is equal to",ans,"Indian Rupee/s")

        else:
            print("Please pick from an option from the given list only!! ")

    elif (count1 == "india") or (count1 == "ind"):
        if (count2 == "europe") or (count2 == "eu"):
            ans = amt * 0.012
            print(amt,"Indian Rupee/s is equal to",ans,"Euro/s")
        elif (count2 == "us") or (count2 == "usa") or (count2 == "united states") or (count2 == "united states of america"):
            ans = amt * 0.013
            print(amt,"Indian Rupee/s is equal to",ans,"American Dollar/s")
        elif (count2 == "japan") or (count2 == "jp") or (count2 == "jpn"):
            ans = amt * 1.42
            print(amt,"Indian Rupee/s is equal to",ans,"Japanese Yen")
        elif (count2 == "switzerland") or (count2 == "confoederatio helvetica") or (count2 == "ch") or (count2 == "che"):
            ans = amt * 0.012
            print(amt,"Indian Rupee/s is equal to",ans,"Swiss Franc/s")
        elif (count2 == "uk") or (count2 == "united kingdom") or (count2 == "united kingdom of great britain") or (count2 == "gbr") or (count2 == "great britain"):
            ans = amt * 0.011
            print(amt,"Indian Rupee/s is equal to",ans,"British Pound/s")
        else:
            print("Please pick from an option from the given list only!! ")

    else:
        print("Please check your inputs!!")

    return ans
#while True:
def converter():
        print("CURRENCY CONVERTER:")    
        print("THE CONVERTER WORKS FOR \n INR TO US/UK/EUROPE/JAPAN/SWITZERLAND\n \t\tOR \n US/UK/EUROPE/JAPAN/SWITZERLAND TO INR ")
        while True:
            while True:
                country1 = input("Enter the country's name you to convert:")
                country1 = country1.lower()
                if not ((country1 == "europe") or (country1 =="eu") or (country1 == "us") or (country1 == "usa") or (country1 == "united states") or (country1 == "united states of america") or (country1 == "japan") or (country1 == "jp") or (country1 == "jpn") or (country1 == "switzerland") or (country1 == "confoederatio helvetica") or (country1 == "ch") or (country1 == "che") or (country1 == "uk") or (country1 == "united kingdom") or (country1 == "united kingdom of great britain") or (country1 == "gbr") or (country1 == "great britain") or (country1 == "india") or (country1 =="ind")):
                    print("Please check your inputs!!")
                    continue

                else:

                    while True:
                        if not ((country1 == "india") or (country1 == "ind")):
                            country2 = "india"
                            print("country2: India")
                        else:
                            country2 = input("Enter the country's name into which you want it to be converted:")
                            country2 = country2.lower()

                            if ((country2 == "india") or (country2 == "ind")):
                                print("You've entered the same country. Please Try again!")
                                continue

                        if not ((country2 == "europe") or (country2 =="eu") or (country2 == "us") or (country2 == "usa") or (country2 == "united states") or (country2 == "united states of america") or (country2 == "japan")  or (country2 == "jp") or (country2 == "jpn") or (country2 == "switzerland") or (country2 == "confoederatio helvetica") or (country2 == "ch") or (country2 == "che") or (country2 == "uk") or (country2 == "united kingdom") or (country2 == "united kingdom of great britain") or (country2 == "gbr") or (country2 == "great britain") or (country2 =="india") or (country2 =="ind")):

                            print("Please check your inputs!!")
                            continue


                        #elif ((country2 == "india") or (country2 == "ind")):
                            #print("You've entered the same inputs. Please Try again!")
                        else:
                            amount = float(input("Enter amount:"))
                            print("\n")
                            currencyConvertor(country1,country2,amount)
                            print("\n")

                            #break
                            while True:
                                choice = int(input("Press 0 to go back and 1 to continue\n"))
                                if not ((choice == 0 ) or (choice == 1)):
                                    print("Invalid")
                                    continue
                                else:
                                    break
                        break
                break



            if(choice == 0):
                break
            elif(choice == 1):
                continue
