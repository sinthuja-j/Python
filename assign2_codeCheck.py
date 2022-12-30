#3 functions to be used in teh program Assign2.py
#function to test if the value basic code
def basicCodeCheck(code):
        #Initiate the basicCodeList and noneList that would be outputted to the user
        basicCodeList= []
        noneList= []
        i = 0
        totalSum= 0
        for i in range(0, len(code)-1):
                tempDigit= int(code[i])
                totalSum = totalSum + tempDigit
        checkDigit= totalSum % 10
        x= len(code)-1
        #checl if the last digit is equal to the check digit if true then the function is basic
        if checkDigit == int(code[x]):
                basicCodeList.append(True)
                basicCodeList.append(code)
                return basicCodeList
        else:
                noneList.append(False)
                noneList.append(code)
                return noneList
#function to test if the value is a positional code
def posititonalCodeCheck(code):
        positionalCodeList= []
        noneList= []
        i = 0
        totalProduct= 0
        for i in range(0,len(code)-1):
                tempDigit= int(code[i])
                totalProduct = totalProduct + ((i+1) * tempDigit)
        checkDigit= totalProduct % 10
        x= len(code)

        #if the check digit is equal to the last digit then the code is positional
        if checkDigit == int(code[x-1]):
                positionalCodeList.append(True)
                positionalCodeList.append(code)
                return positionalCodeList

        else:
                noneList.append(False)
                noneList.append(code)
                return noneList
#function to test if the value is a universal code
def universalPCode(code):
        universalCodeList= []
        noneList = []
        i = 0
        totalSum = 0
        for i in range (0,len(code)-1):
                tempDigit= int(code[i])

                #if i is an even index then you multiply the value by 1
                if ((i+1) % 2 == 0):
                        j= tempDigit * 1
                        #print(j)
                #if i an off index then you multiply the value by 3
                elif ((i+1) % 2 == 1):
                        j= tempDigit * 3
                        #print(j)
                totalSum+= j

        tempCheckDigit= totalSum % 10
        checkDigit = 0
        #if the value is 0 then that becomes the check digit
        if tempCheckDigit == 0:
                checkDigit == tempCheckDigit
       #if the value is between 1 and 10 then you subtract it by 10 to get the new check digit
        elif tempCheckDigit > 0 and tempCheckDigit < 10:
                checkDigit= 10-tempCheckDigit
        x= len(code)

        if checkDigit == int(code[x-1]):
                universalCodeList.append(True)
                universalCodeList.append(code)
                return universalCodeList
        else:
                noneList.append(False)
                noneList.append(code)
                return noneList




