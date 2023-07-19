#Project Name: WASTE CATAG 
#Project Details: A “ Waste randomizer” Python program was used to select the precise cell within each load for extraction and categorization. 
#Python program aims to seamlessly simplify waste management processes by automating the classification of items into appropriate waste categories 
#computes the sum of percentages based on sorting quantity. 
#

#using python is get way to manipulate data and analyze it python 
#First imported the data:
import pandas as pd
import csv
import numpy as np


#(a) prompt user
#(b) input scanner 
#3. group by category

#print function method 

#note: figure out how to take a specific percentage of a paper/glass/
#declare a catergory called mainWasteCat
#insert new columm using in a dataframe
#with open("data.csv", 'r') as csvfile:
#1.read file
df = pd.read_csv('data1.csv')
#2.add catergory called waste catag
#df.insert(3, "wasteCATAG", np.nan)
df.head()
print(df.head)

#need another catalog before we can group because we need the catalog to group them by catalog
#group by to group the materials
#find the catalog there are missing (NA filled to know what catalog belong too) prompt the user with that 
#add catalog data to missing values 
#take that input put it back into the catalog
#group by category 





#(a) prompt user using printf
#print("what category does:" + df['Materials'] + "belong to？")

#prompt the user for missing values in WASTECATAG (comeback)
#access the index based , range the column

#figure out the range and the sum
for i, value in enumerate(df['wasteCATAG']):
   #if condition for parsing materials into segments
    if ( 2 <= i <= 10):
         new_value = input(f"What CAT is this {df.loc[i, 'Materials']}: ")
         df.loc[i, 'wasteCATAG'] = str(new_value) 

#key error
print(df['Materials'])
#print(wasteCATAG)

# Blockchain

#add catalog data to missing values 

#prompt (b)  input scanner 
#print(f"Welcome to this catalog is {Materials}")
#Material = input("what material does this belong to?")

#ask for the input
# do a group by method by fips, years, material 

#Using GroupBy multiple column
#how to display the percentage 
#df = df.groupby('Materials')['percentage'].sum()
#temp = df.groupby(['FIPS', 'Year', 'wasteCATAG'])['Percentage'].sum()
temp = df['Percentage'].sum()
print(f"This is the total waste quantity:{temp}");

#Create a block class
#run each cell 
class Block:
    #Create a constructor for the block class
   def _init_(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()
    
#create a method that calculates the hash using SHA-256
   def calc_hash(self):
       sha = hashlib.sha256()
       sha.update(self.data.encode('utf-8'))
       return sha.hexdigest()


#Create the blockchain class
class Blockchain:
     #create a constructor for the Blockchain class
   def __init__(self):
      self.chain = [self.create_genesis_block(self)]
  return Block(data, prev_hash)


  #Create a method that creates the first block in the blockchain also known as the "Genesis Block"
def create_genesis_block(self):
#previous hash 
return Block("Original Block", "0")
#Create a method that creates a new block and adds it to the Block chain(aka the list)
def add_block(self, data):
   prev_block = self.chain[-1]
   new_block = Block(data,          prev_block.hash)
   self.chain.append(new_block)

   #Test the BlockChain
#create variable object
blockchain = Blockchain()
