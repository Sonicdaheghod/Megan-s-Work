#Purpose of this program is to create a fun, interactive game for high school chemistry students to test their general chemistry vocabulary

#credit for hangman and wordbank template: <script src="https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c"
#Hangman game code based on: https://www.youtube.com/watch?v=cJJTnI22IF8
#timestamp:https://youtu.be/cJJTnI22IF8?t=246

#Here, I want to create a storage space for the images of hangman and chemistry terms
nanoputian  = ['''
+-------------------------------+
              |                 |
     \|/     _|_     \|/        |
      \     /   \    /          |
      \\\   O   O  ///          |
       \\\   \ /  ///           |
         \    |   /             |
          \ //  \/              |
          | /    ||             |
          |      ||             | 
          \\      /             | 
            \\  /               |
              |                 |
              |                 |
            /   \               |
           /     \              |
     ____/        \____         |
                                |
                                |
                                |
                                |
========================================


''']


chemHangmanIcons = ['''
+-------------------------------+
              |                 |
              |                 |
                                |
                                |
                                |
                                |
                                |
                                |
                                | 
                                | 
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
========================================''', '''
+-------------------------------+
              |                 |
             _|_                |
            /   \               |
            O   O               |
             \ /                |
                                |
                                |
                                |
                                | 
                                | 
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
========================================''', '''
+-------------------------------+
              |                 |
             _|_                |
            /   \               |
            O   O               |
             \ /                |
              |                 |
            //  \               |
          | /    ||             |
          |      ||             | 
          \\      /             | 
            \\  /               |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
========================================''', '''
+-------------------------------+
              |                 |
     \|/     _|_                |
      \     /   \               |
      \\\   O   O               |
       \\\   \ /                |
         \    |                 |
          \ //  \               |
          | /    ||             |
          |      ||             | 
          \\      /             | 
            \\  /               |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
========================================''', '''
+-------------------------------+
              |                 |
     \|/     _|_     \|/        |
      \     /   \    /          |
      \\\   O   O  ///          |
       \\\   \ /  ///           |
         \    |   /             |
          \ //  \/              |
          | /    ||             |
          |      ||             | 
          \\      /             | 
            \\  /               |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
========================================''', '''
+-------------------------------+
              |                 |
     \|/     _|_     \|/        |
      \     /   \    /          |
      \\\   O   O  ///          |
       \\\   \ /  ///           |
         \    |   /             |
          \ //  \/              |
          | /    ||             |
          |      ||             | 
          \\      /             | 
            \\  /               |
              |                 |
              |                 |
            /                   |
           /                    |
     ____/                      |
                                |
                                |
                                |
                                |
                                |
                                |
========================================''', '''
+-------------------------------+
              |                 |
     \|/     _|_     \|/        |
      \     /   \    /          |
      \\\   O   O  ///          |
       \\\   \ /  ///           |
         \    |   /             |
          \ //  \/              |
          | /    ||             |
          |      ||             | 
          \\      /             | 
            \\  /               |
              |                 |
              |                 |
            /   \               |
           /     \              |
     ____/        \____         |
                                |
                                |
                                |
                                |
========================================


''']

#Word bank of General Chemistry terms, this is made in a different python file
#genChemWords = ("acid, Arrhenius, base, Bronsted, chemistry, dissociation, density, electron, element"
         # "Freezing, functional group, Gibbs free energy, Gamma emission, Half-reaction, Halogens, indicator, Ionic bond" 
          #"Kinetic energy, kinetic theory, Le Châtelier's principle, Lattice energy, molarity, molality, nitrogen, Neutron"
          #"osmotic pressure, Oxidation, peroxide, Periodic table, Radioactive decay, Raoult's law"
          #"Supersaturated, Salt bridge, Thermodynamics, temperature, Uncertainty principle, Unimolecular reaction"
          #"VSPER theory, valence electron, Wavelength").split()

#setting up game

#1-getting random word from list for user to guess
import random
from GeneralChemistryTerms import genChemWords
import string

def useWord(genChemWords):
  genChemWord = random.choice(genChemWords)
  while "-" in genChemWord or " " in genChemWord:
    genChemWord = random.choice(genChemWords)

  return genChemWord

#2-setting up the hangman game
def chemHangman():
  genChemWords = useWord(genChemWords)
  letters.genChemWords = set(genChemWords) #depicts the seperate letters of a word
  chemAlphabet = set(string.ascii_uppercase)

  #storing letters user already guessed 
  lettersGuessed = set()

  #need to have somethign that asks the user to type in a letter
userAttempt = input("Make a guess:")
print(userAttempt)



 
