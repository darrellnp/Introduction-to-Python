# -*- coding: utf-8 -*-
"""109006239_Darrell Nathaniel Prayogi楊輝_hw3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JzKRjEAcnTxUJAyq9HmKkYM5R5ryTuFV
"""

import sys
import os
def printRed(text): print("\033[91m {}\033[00m" .format(text)) 
def printGreen(text): print("\033[92m {}\033[00m" .format(text)) 


class Record:
    def __init__(self, category , description, amount):
        
        self._category = category
        self._description = description
        self._amount = str(amount)

    @property
    def category(self):
        
        return self._category
    @property
    def description(self):
        
        return self._description
    @property
    def amount(self):
        
        return self._amount


class Records:
    def __init__(self):                                         
          filename = "records.txt"
          if os.path.exists(filename):
              try:
                  with open(filename) as f:
                      files = f.readlines()
                      self._records = []
                      self._initial_money = 0
                      welcome_balance = 0
                      flag = 0
                      for i in range(0,len(files)):
                          line = files[i]
                          if line == files[0]:
                              self._initial_money = int(line.strip())
                          else:
                              category,desc,amt = line.strip().split()
                              self._records.append(Record(category, desc, int(amt)))
                              if flag == 0 :
                                  welcome_balance = self._initial_money + int(amt)
                                  flag = 1
                              else : 
                                  welcome_balance = welcome_balance + int(amt)
                      print(f"Welcome back! Your balance is {self._initial_money} dollars.\n")
              except:
                  printRed("Invalid format in records.txt. Deleting the contents.")
                  with open(filename, 'w') as f:
                      f.write('')
                  self._records = []
                  self._initial_money = 0
                  try:
                    self._initial_money = int(input("How much money do you have? "))
                  except ValueError:
                    self._initial_money = str(0)
                    printRed("Invalid value for money. Set to 0 by default")
          else:
              self._records = []
              self._initial_money = 0
              try:
                self._initial_money = int(input("How much money do you have? "))
              except ValueError:
                self._initial_money = str(0)
                printRed("Invalid value for money. Set to 0 by default")
    def add(self,new_record,categories):
        
        new_record = new_record.split()                                 
        if len(new_record)==3:
            new_record = Record(new_record[0],new_record[1],new_record[2])      
            if categories.is_category_valid(new_record.category):
                try:
                    
                    self._initial_money += int(new_record.amount)
                    
                    self._records.append(new_record)                
                except ValueError:                                  
                    printRed('Invalid value for money.\nFail to add a record.')
            else:       
                printRed('The specified category is not in the category list.\nYou can check the category list by command "view categories".\nFail to add a record.')
        else:
            printRed('Invalid format, The format of a record should be like this: meal breakfast -50.\nFail to add a record.')
    	
 
    def view(self):
        
        print("Here's your expense and income records:")
        print('Category        Description          Amount')
        print('=============== ==================== ========')
        for item in self._records:
            print(f'{item.category :<15} {item.description:<20} {item.amount:<8}')    
        print('=============== ==================== ========')
        printGreen(f'Now you have {self._initial_money} dollars.')
    	
 
    def delete(self,delete_record):
        if self._records == []:                          
            printRed("There's no records in file. Fail to delete a record.")
        else:
            delete_record = delete_record.split()
            if len(delete_record)==3:
                name = delete_record[0]
                
                try:
                    price = int(delete_record[1])
                    index = int(delete_record[2])
                except ValueError:
                    printRed('Invalid format. Fail to delete a record.')
                    return
                for i in range(0,len(self._records)):
                    if (name == self._records[i].description) and (str(price) == self._records[i].amount) and (index == i+1):
                        self._initial_money -= price
                        self._records.pop(i)
                        return
                printRed(f"There's no record with {' '.join(delete_record)}. Fail to delete a record.")
            else:
                printRed('Invalid format, The format of a record should be like this: breakfast -50 1. \nFail to delete a record.')
    	
 
    def find(self,non_nested_list):

        global category             
       
        def check_inside(record):
            
            if record.category in non_nested_list:
                return True
        sub_list =[]
        sub_list.extend(list(filter( lambda x: check_inside(x),self._records )))        

        total = 0
        for i in range(0,len(sub_list)):
            total += int(sub_list[i].amount)
        
        if sub_list != []:
            print(f"Here's your expense and income records under category \"{category}\":")
            print('Category        Description          Amount')
            print('=============== ==================== ========')
            for item in sub_list:
                print(f'{item.category:<15} {item.description:<20} {item.amount:<8}')    
            print('=============== ==================== ========')
            printGreen(f'The total amount above is {total}.')
        else:
            printRed(f'There is no records under category "{category}".')


    def save(self):
        
        with open('records.txt','w+') as fh_record:
            fh_record.write(f'{str(self._initial_money)}\n')
            for item in self._records :
                fh_record.write(f"{' '.join([item.category,item.description,item.amount])}\n")
    

class Categories:
    
    def __init__(self):
       
        categories = ['expense', ['food', ['meal', 'snack', 'drink'], \
            'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
        self._categories = categories
   
 
    def view(self):
        
        def view_categories(categories,level):
           
            for i in categories:
                if type(i) == list:            
                    view_categories(i,level+1)
                else:                          
                    print(f'{"  "*level}- {i}')
        view_categories(self._categories,0)
    	
 
    def is_category_valid(self,category):
        
        def is_valid(category,categories):
            if type(categories) == list:
                for i in categories:
                    flag = is_valid(category,i)
                    if flag == -1:                          
                        continue                            
                    elif flag ==  True:                     
                        return True
            else:                                           
                if category == categories:
                    return True 
                else:
                    return -1
            return False                                    
        return is_valid(category,self._categories)
    	
 
    def find_subcategories(self,target_categories):
       
        def find_subcategories_gen(target, categories, found=False):
            
            if found == True:                       
                for i in categories:                
                    if type(i) == list:
                        yield from find_subcategories_gen(target, i, True)
                    else:
                        yield i
            elif type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(target, child, False)
                    if child == target and index + 1 < len(categories) and type(categories[index + 1]) == list:
                        yield from find_subcategories_gen(target, categories[index + 1], True)      
            else:         
                if categories == target:            
                    yield categories

        return [i for i in find_subcategories_gen(target_categories,self._categories)]  


records = Records()
categories = Categories()

while True:
    command = input('\nWhat do you want to do (add / view / delete / view categories / find / exit)? ')
    if command == 'add':     
        record = input("Add an expense or income record with category, description, and amount (separate by spaces): ")
        records.add(record, categories)     
    elif command == 'view':
        records.view()
    elif command == 'delete':
        delete_record = input("Which record do you want to delete? ")
        records.delete(delete_record)
    elif command == 'view categories':
        categories.view()
    elif command == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        records.find(target_categories)
    elif command == 'exit':
        records.save()
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')

