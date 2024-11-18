



#main function
def main(): 
    #get letter values
    values = getValues()

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
        print(f"names in file: {names}")
    #iterate each name
    word_scores = []

    for name in names:
        #split name so we can check each word in the name
        words = name.split()
        print(f"current name: {words}")
        
        #get score of each character in a word
        for word in words:
            #this contains the scores for each letter
            scores = []
            #get length of current word
            length = len(word)

            #check each letter and update scores 
            for i in range(length):
                position_value = 0
                char = word[i].upper()
                print(f"current letter: {char}")
                #If the letter is the first letter
                if i == 0:
                    scores.append(0)
                #If the letter is the last letter
                elif i == length - 1:
                    if char == 'E':
                       scores.append(0)
                    else:
                       scores.append(5)
                    
                #If letter isnt first or last
                else:
                    #2nd letter of word
                    if i == 1:
                        position_value = 1
                    elif i == 2:
                        position_value = 2
                    elif i > 2:
                        position_value = 3
                    
                    #obtain frequecy value of letter
                    letterFrequencyScore = v.get(char,0)
                    #calculate total score
                    totalScore = position_value + letterFrequencyScore
                    #add this to scores
                    scores.append(totalScore)
                    
            #update word scores
            word_scores.extend(scores)
            print(f"word score: {word_scores}")

    bestAbbreviations = []
    #calculate best abbreviation
    bestAbbreviationScore = float('inf')
    bestAbbreviation = None
   
    


       
    
    
    
        

        
        


     


#call main
main()