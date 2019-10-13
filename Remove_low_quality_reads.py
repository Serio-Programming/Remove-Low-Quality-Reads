#Remove Low Quality Reads
#This program removes sequences from a FASTQ file that have 5 or more bases that
#Have a quality score less than 15
#A program by Tyler Serio
#Python 3.7
#Circa October 2018

#import relevant libraries
import numpy
import os.path
from os import path

#create variables
running = 1

#define the function
def remove_low_quality_reads():
    #create variables
    readcount = 0
    totalreadcount = 0
    milreadcount = 0
    linecount = 0
    badbasecount = 0

    #each sequence in a FASTQ file has 4 lines, thus 4 variables are created
    line1 = "blah"
    line2 = "blah"
    line3 = "blah"
    line4 = "blah"
    opening = 1

    #ask the user what file they would like to open
    while opening == 1:
        print ("What file would you like to remove low quality reads from?")
        print ("Example: 'results.fastq'")
        print ("Type the exact name of the file you would like to remove low quality reads from,")
        ofile = input ("or type [0] to retrun to the menu. ")
        print ("")

        #return to the menu
        if ofile == "0":
            naming = 0
            removing = 0
            opening = 0
            break

        #check to see if the file exists
        path.exists(ofile)

        #if the file exists move on to the next step
        if path.exists(ofile) == True:
            print ("I will retrieve your file.")
            print ("I have found your file.")
            ofile = open(ofile, "r")
            cutoff = 0
            opening = 0
            removing = 0
            naming = 1
            break

        #if the file doesn't exist, ask the user for another
        if path.exists(ofile) == False:
            print("I will retrieve your file.")
            print("I cannot find this file. Make sure to type the file name exactly,")
            print("Try again, or type [0] to return to the menu.")
            print("")
            opening = 1
            removing = 0
            naming = 0

    #ask the user what they would like to name their output file
    while naming == 1:
        outputfilename = input ("The high-quality reads will be written to an output file. What would you like to name your output file? ")
        outputfilename =str(outputfilename)
        outputfilename2 = (outputfilename + "(low_quality_reads)" + ".txt.")
        outputfilename = (outputfilename + ".txt.")
        outputfile = open (outputfilename, "w")
        outputfile2 = open (outputfilename2, "w")
        print ("Your new file name is " + outputfilename)
        naming = 0
        removing = 1
        break

    #begin removing low quality reads
    while removing == 1:
        cutoff += 1

        #if all lines of the file have been read, end this section of the program
        if cutoff == 2:
            ofile.close()
            outputfile.close()
            outputfile2.close()
            print ("That's it!")
            print ("We're done!")
            print ("Total numbers of reads examined: " + str(totalreadcount))
            removing = 0
            break

        #step through each line of the file
        for line in ofile:
            if readcount == 100000:
                readcount = 0
                milreadcount = milreadcount + 100000
                print (str(milreadcount) + " reads examined.")
            linecount += 1
            if linecount == 1:
                line1 = str(line)
            if linecount == 2:
                line2 = str(line)
            if linecount == 3:
                line3 = str(line)
            if linecount == 4:
                line4 = str(line)
                readcount += 1
                totalreadcount += 1

                #define low quality scores
                characters = ("!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/")

                #check the fourth line for low quality scores
                for i in line4:
                    if i in characters:
                        badbasecount += 1
                    else:
                        badbasecount += 0

                #write better quality reads to a file
                if badbasecount < 5:
                    outputfile.write(line1)
                    outputfile.write(line2)
                    outputfile.write(line3)
                    outputfile.write(line4)

                #write lower quality reads to a different file
                else:
                    outputfile2.write(line1)
                    outputfile2.write(line2)
                    outputfile2.write(line3)
                    outputfile2.write(line4)

                #reset the variables
                badbasecount = 0
                line1 = "blah"
                line2 = "blah"
                line3 = "blah"
                line4 = "blah"
                linecount = 0    

#begin the program
while running == 1:
    #ask the user what they want to do
    print ("Hello, what would you like to do?")
    print ("")
    print ("[1] - Remove low quality reads from a paired file.")
    print ("[2] - Exit")
    print ("")
    selecting = 1
    
    while selecting == 1:
        selection = 0
        selection = input ("Which do you choose? ")
        print ("")
        
        if selection != "1" and selection != "2":
            if selection == "":
                selection == ("Nothing")
                
            print ("You have chosen [" + selection + "].")
            print ("That is not a proper selection.")
            print ("Please choose from the list of selections.")
            
        else:
            selecting = 0

        #run the function
        if selection == "1":
            remove_low_quality_reads()
            selection = 0
            
        if selection == "2":
            selecting = 2
            selection = 0

            #exit the program
            while selecting == 2:
                print ("Goodbye. Are you sure you want to exit?")
                print ("")
                print ("[y] - Yes")
                print ("[n] - No")
                print ("")
                selection = input ("Which do you choose? ")
                print ("")

                #make sure the user really wants to exit the program
                if (selection != "y" and selection != "n"):
                    if selection == "":
                        selection == ("Nothing")
                        
                    print ("You have chosen [" + selection + "].")
                    print ("That is not a proper selection.")
                    print ("Please choose from the list of selections.")
                    
                if selection == "y":
                    exit()
                    
                if selection == "n":
                    print ("Oops. Nevermind then.")
                    selecting = 0
                
    
