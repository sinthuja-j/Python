'''
Author: Sinthuja Jeevarajhan
Course: CS 1026, Professor Sarlo
Assignment 4: Country Classes
Purpose: Return an updated version of user's data input that executed a series of updates specified by the user. Invalid
updates are outputted to a file and the new data file is saved to a new file.
'''
#import the Country class from country.py and CountryCatalogue class from catalogue.py
from country import Country
from catalogue import CountryCatalogue
#function that takes in three paramaters; the data file, file containing updates; file to output bad updates
def processUpdates(cntryFileName, updateFileName,badUpdateFile):
    #open the output data file with final information
    output= open("output.txt", "w")
    #open the output data file with bad updates
    bad_output= open(badUpdateFile, "w")
    #try to open the country data file
    try:
        file_countrydata = open(cntryFileName, "r", encoding= "utf-8")
    #if the file doesnt exist it prompts the user to decide if they would like to exit program or enter new file name
    except:
        while True:
            quit_response= input("Would you like to quit 'Y' (yes) or 'N' (no): ")
            if quit_response.upper() == "Y":
                output.write("Update Unsuccessful\n")
                return (False,None)
            else:
                cntryFileName= input("Please enter the file with country data: ")
                file_countrydata= cntryFileName
                #if the file exists the program quits the while loop
                if file_countrydata != None:
                    break
    #create the country object using CountryCatalogue with the data file
    country_object= CountryCatalogue(cntryFileName)
    #try to open the country update file
    try:
        file_update= open(updateFileName, "r")
    #if the file doesnt exist it prompts the user to decide if they would like to exit program or enter new file name
    except:
        while True:
            quit_response= input("Would you like to quit 'Y' (yes) or 'N' (no): ")
            if quit_response.upper() == "Y":
                output.write("Update Unsuccessful\n")
                return (False,None)
            else:
                updateFileName= input("Please enter the file with update data: ")
                file_update= open(updateFileName, "r")
                #if the file exists the program quits the while loop
                if file_update != None:
                    break
    #open the file containing the list of updates
    file_update= open(updateFileName, "r")
    #iterate through the update file
    for i in file_update:
        i= i.strip()
        data= i.split(';')
        country_updatename= data[0]
        country_updatename= country_updatename.strip()
        #create a country object with the name of the country
        cntry1= Country(country_updatename)
        #checks if the country already exists
        obj= country_object.findCountry(cntry1)
        exit= False
        #checks if the country name contains only letters and underscores
        if not country_updatename.isalpha() or country_updatename.__contains__("_"):
            bad_output.write(i)
            bad_output.write("\n")
            exit= True
        #checks if the file begins with an uppercase
        elif not country_updatename[0].isupper():
            bad_output.write(i)
            bad_output.write("\n")
            exit= True

        p_counter=0
        a_counter= 0
        c_counter= 0
        if exit == False:
            for elem in data[1:]:
                elem= elem.strip()
                if elem[0]== "P":
                    p_counter+=1
                if elem[0]== "A":
                    a_counter+=1
                if elem[0]== "C":
                    c_counter+=1
                    value= elem[2:]
                    #checks if the contient is one of the 7 valid contients, if its not the update is skipped and added to the bad update file
                    if (value != "North_America") and (value != "South_America") and (value != "Asia") and (value != "Africa") and (value != "Antartica") and (value != "Australia") and  (value != "Europe"):
                        bad_output.write(i)
                        bad_output.write("\n")
                        exit= True
        if exit == False:
            #if there is more than one population update, it is skipped and added to the bad update file
            if p_counter > 1:
                bad_output.write(i)
                bad_output.write("\n")
                exit = True
            #if there is more than one area update, it is skipped and added to the bad update file
            elif a_counter > 1:
                bad_output.write(i)
                bad_output.write("\n")
                exit = True
            #if there is more than one continent update, it is skipped and added to the bad update file
            elif c_counter > 1:
                bad_output.write(i)
                bad_output.write("\n")
                exit = True

        if exit== False:
            #if the country does not exist
            if obj == None:
                for elem in data[1:]:
                    #try statement in case there is not enough data- index error
                    try:
                        #checks if there are commas every 3 #'s, if not update is skipped and added to bad update else it is valid
                        if elem[0]== "P":
                            check_value = elem[2:]
                            check_value = check_value[::-1]
                            count= 0
                            for letter in check_value:
                                count+= 1
                                #checks if every 4th character going back is a comma
                                if count == 4:
                                    if letter == ",":
                                        exit==False
                                    else:
                                        exit == True
                                    count= 0
                            if exit == False:
                                #if the update is valid the country is added to the catalogue with its population
                                cntry1.setPopulation(elem[2:])
                            #invalid update
                            elif exit == True:
                                bad_output.write(i)
                                bad_output.write("\n")
                        #checks that there are commas every 3 #'s if not then update is skipped and added to bad update file, else it is valid
                        elif elem[0]== "A":
                            check_value = elem[2:]
                            check_value = check_value[::-1]
                            count= 0
                            for letter in check_value:
                                count+= 1
                                #checks if every 4th character going back is a comma
                                if count == 4:
                                    if letter == ",":
                                        exit==False
                                    else:
                                        exit == True
                                    count= 0
                            if exit == False:
                                #if the country is valid the country is added to the catalogue with its area
                                cntry1.setArea(elem[2:])
                                print(elem[2:])
                            #invalid update
                            elif exit == True:
                                bad_output.write(i)
                                bad_output.write("\n")
                        #for the continent
                        elif elem[0]== "C":
                            cntry1.setContinent((elem[2:]))
                    #except runs if there is not enough data, it only adds the exisiting data
                    except:
                        country_object.addCountry(cntry1.getName(), cntry1.getPopulation(), cntry1.getArea(),cntry1.getContinent())
                country_object.addCountry(cntry1.getName(), cntry1.getPopulation(), cntry1.getArea(),cntry1.getContinent())
            #if the country exists
            else:
                for elem in data[1:]:
                    elem= elem.strip()
                    #try statement in case there isnt enough data- index error
                    try:
                        #for population update
                        if elem[0]== "P":
                            check_value = elem[2:]
                            check_value = check_value[::-1]
                            count= 0
                            #checks if every 4th character going back is a comma
                            for letter in check_value:
                                count+= 1
                                if count == 4:
                                    #if it is then the file is valid, else it is invalid
                                    if letter == ",":
                                        exit= False
                                    else:
                                        exit= True
                                    count= 0
                            #if the update is valid the country is updates with the pop value
                            if exit == False:
                                country_object.setPopulation(cntry1, elem[2:])
                            #if the update is invalid the country is skipped and added to the bad updates file
                            elif exit == True:
                                bad_output.write(i)
                                bad_output.write("\n")
                        #for area update
                        elif elem[0]== "A":
                            check_value = elem[2:]
                            check_value = check_value[::-1]
                            count= 0
                            for letter in check_value:
                                count+= 1
                                #checks that every 4th character going back is a comma
                                if count == 4:
                                    #if it is then the update is valid, else its invalid
                                    if letter == ",":
                                        exit= False
                                    else:
                                        exit = True
                                    count= 0
                            #if the update is valid the country is updated with the area
                            if exit == False:
                                country_object.setArea(cntry1, elem[2:])
                            #if the update if invalid the country is skipped and added to the bad updates file
                            elif exit == True:
                                bad_output.write(i)
                                bad_output.write("\n")
                        #for the continent
                        elif elem[0]== "C":
                            country_object.setContinent(cntry1, elem[2:])
                    except:
                        None
    file_update.close()
    #save the catalogue to the file output.txt
    country_object.saveCountryCatalogue("output.txt")
    #return True that the update is successful and return the count
    return (True, country_object)

