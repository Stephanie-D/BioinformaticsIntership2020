#Importing the random and FileIO package
import random # to randamize spidroin
import io # create a file

nucList = ['A','T','C','G'] # list of the four nuclotides

#DNA sequence function
def DNA_sequence(): # nameing the sequence function
  #Creating empty sub set
  subsetA = "" 
  subsetB = "" 
  # putting nuclutides in subset a
  for i in range(random.randint(1,76)):
    subsetA += nucList[random.randint(0,3)]

  # putting nuclutides in subset b
  for i in range(150 - len(subsetA)):
    subsetB += nucList[random.randint(0,3)]

  #making the large set
  largeset = subsetA + subsetB

  #making the full sequence 
  full_sequence =largeset + largeset

  return full_sequence #retuening the ful spidroin

spidroin = DNA_sequence() # making the return of the function into a variable

#makeing a fasta file for spidrion
filename = input("File Name Is: ")
file_header = input("File Header Is: ")
def spidroinFile(filname, file_header): # naming and putting perameter into the fasta file function
  try: #try block to help run if error found
    with open(filename + ".fasta","w") as spidroinFile_handel: # Creating the fasta file
      spidroinFile_handel.write(">"+ file_header + "\n" )# adding the headrer to the fasta file
      spidroinFile_handel.write(spidroin)# adding the spidroin to the fasta fiel
  except IOError as err:
     print("theres an error")

  return spidroinFile_handel

#Calling the fasta file fucnction
spidroinFile(filename, file_header)