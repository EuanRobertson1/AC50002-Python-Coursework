



#main function
def main(): 
    #get letter values
    values = getValues()

    print(values)

    #define array abbr and call function to generate abbreviation 
    abbr = [] 
    abbr = generateAbbr(values)


#function for getting values. Creates dictionary
def getValues():
    letterValues = {}
    with open("values.txt", "r") as file:
        for line in file:
            key, value = line.strip().split()
            letterValues[key] = int(value)
    
    return(letterValues)



#function for generating abbreviations     
def generateAbbr(v):
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

    #process each name
    with open(f"{fileName}.txt", "r") as file:
        #create array containing each name in file
        names = [line.strip() for line in file]
    #iterate each name
    for name in names:
        #split name so we can check each word in the name
        words = name.split()
        #this dictionary contains the current word alongside the score for each of its letters
        word_scores = {}

        #get score of each character in a word
        for word in words:
            #this contains the scores for each letter
            scores = []
            #get length of current word
            length = len(word)

            #check each letter and update scores 
            for i in range(length):
                char = word[i].upper()

                #If the letter is the first letter
                if i == 0:
                    scores.append(0)

                #If the letter is the last letter
                elif i == length - 1:
                    if char == 'E':
                        scores.append(20)
                    else:
                        scores.append(5)

                #If letter isnt first or last
                else:
                    #2nd letter of word
                    if i == 1:
                        position_value = 1
                    elif i == 2:
                        position_value = 2
                    else:
                        position_value = 3
                
                #obtain frequecy value of letter
                letterFrequencyScore = v.get(char,0)
                #calculate total score
                totalScore = position_value + letterFrequencyScore
                #add this to scores
                scores.append(totalScore)
            
            #update word scores
            word_scores[word] = scores

        
        letters = []
        #extract letters from current word
        for word in words:
            for i in range(len(word)):
                letters.append(word[i].upper())
        
        
        #find best abbreviation using the highest score from before
        #initilise best score with infinity
        bestScore = float('inf')
        bestAbbreviation = None

        #loop though each letter
        for i in range(len(letters)):
            #loop though each letter that comes after i
            for j in range(i + 1, len(letters)):
                #loop though each letter that comes after j
                for k in range(j + 1, len(letters)):
                    #create a three letter abbreviation using i,j,k
                    abbreviation = letters[i] + letters[j] + letters[k]
                    #caluculate total score using letter_scores dictionary from earlier
                    totalScore = (letter_scores.get(letters[i], 0) +
                                letter_scores.get(letters[j], 0) +
                                letter_scores.get(letters[k], 0))
                    #update best score and best abbriviation if neccessary
                    if totalScore < bestScore:
                        bestScore = totalScore
                        bestAbbreviation = abbreviation

        #add to abbreviations array 
        allAbbreviations.append((name, bestAbbreviation))           
    
    
    return allAbbreviations
    
        

        
        


     


#call main
main()