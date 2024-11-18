
#main function
def main(): 
    #get letter values
    values = getValues()

    #define array abbr and call function to generate abbreviation 
    abbr = [] 
    names = getNames()
    abbr = generateBestAbbr(values, names)

    #write to file
    with open("testOutput.txt", "w") as file:
        for x in range(len(abbr)):
            file.write(f"Name: {names[x]} \n {abbr[x]} \n")


#function for getting frequency values. Creates dictionary
def getValues():
    letterValues = {}
    with open("values.txt", "r") as file:
        for line in file:
            key, value = line.strip().split()
            letterValues[key] = int(value)
    
    return(letterValues)

#function for reading in names
def getNames():
    correctFileName = False

    while not correctFileName:
       
       fileName = input("please enter the name of the .txt file you wish to open: \n"); 

       #try opening the file
       try:
        #read in file
        file = open(f"{fileName}.txt", "r")
        
        #set correct name to true
        correctFileName = True

       except FileNotFoundError as e:
        #print error
        print(f"Error: {e}")

    #Get Names
    with open(f"{fileName}.txt", "r") as file:
        #create array containing each name in file
        names = [line.strip() for line in file]
    
    return names

#function for generating abbreviations     
def generateBestAbbr(v,names):
    word_scores = []#this will contain the scores for each name
    combined_names = []# this will be used in tandem with word_scores later
    for name in names:
        #split name
        words = name.split()
        combo = "".join([w.upper() for w in words])
        combined_names.append(combo)

        scores = []
        for word in words:#check each word of the name
                #get score of each character in a word
                #this will contain the scores for each letter
                #get length of current name
                length = len(word)

                #check each letter and update scores 
                for i in range(length):
                    position_value = 0
                    char = word[i].upper()
                    #If the letter is the first letter
                    if i == 0:
                        scores.append(0)
                    #If the letter is the last letter
                    elif i == length - 1:
                        if char == 'E':#if letter is 'E'
                            scores.append(0)
                        else:#otherwise if not 'E'
                            scores.append(5)
                        
                    #If letter isnt first or last
                    else:
                        if i == 1:#2nd letter of word
                            position_value = 1
                        elif i == 2:#3rd letter of word
                            position_value = 2
                        elif i > 2:#any other letter
                            position_value = 3
                        #obtain frequecy value of letter
                        letterFrequencyScore = v.get(char,0)
                        #calculate total score
                        totalScore = position_value + letterFrequencyScore
                        #add this to scores
                        scores.append(totalScore)
                
        #update word scores
        word_scores.append(scores)
        
            
    bestAbbreviations = []
    #calculate best abbreviation

    for n in range(len(combined_names)):#iterate through each row in combined_names
        bestAbbreviationScore = float('inf')
        bestAbbreviation = None
        sameScoreAbreviation = []
        row = combined_names[n]

        for i in range(len(row)):#iterate through each letter
            for j in range(i + 1, len(row)):#iterate through each letter that comes after i
                for k in range(j + 1, len(row)):#iterate through each letter that comes after j
                    #create 3 letter abbreviation
                    abbreviation = row[i] + row[j] + row[k]

                    if (not abbreviation.isalpha()):#skip abbreviation if it contains non letters i.e. symbols or apostrophes
                        break

                    totalAScore = (word_scores[n][i] + word_scores[n][j] + word_scores[n][k])
                    
                    #update best abreviation if applicable
                    if totalAScore < bestAbbreviationScore:
                        bestAbbreviation = abbreviation
                        bestAbbreviationScore = totalAScore
                    
                    
        bestAbbreviations.append(bestAbbreviation)
    
    return bestAbbreviations


#call main
main()