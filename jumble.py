#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 09:48:47 2021

@author: eniolaosineye
"""
import nltk

from nltk.corpus import words
word_list = words.words()
# prints 236736


  
# Function to print permutations of string 
# This function takes three parameters: 
# 1. String 
# 2. Starting index of the string 
# 3. Ending index of the string. 

  
# Driver program to test the above function 
word = 'jnuier'


#print(permutations);

def binary_search(arr, low, high, x): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1



def permute(a, l, r, permutations): 
    if l == r: 
        #print (''.join(a)) 
        temp = ''.join(a)
        permutations.append(' '.join(temp[0].upper() + temp[1:] for word in temp.split()))
    else: 
        for i in range(l, r + 1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l + 1, r, permutations) 
            a[l], a[i] = a[i], a[l] # backtrack 
            
            
#Big 0(n to the power 2) 
def jumbleUsingLinearSearch(string):
    stringLength = len(string) 
    listOfLetters = list(string) 
    permutations = []
    possibleWords = [];
    permute(listOfLetters, 0, stringLength-1, permutations) 

    for word in word_list:
        for permutation in permutations:
            if(permutation.upper() == word.upper()):
                possibleWords.append(word)
    return possibleWords

    #print(possibleWords)
def jumbleUsingBinarySearch(string):
    stringLength = len(string) 
    listOfLetters = list(string) 
    permutations = []
    possibleWords = [];
    permute(listOfLetters, 0, stringLength-1, permutations) 
    for permutation in permutations:
        print(permutation)
        
        
        index = binary_search(word_list, 0, len(word_list)-1, permutation)
        print(index)
        if(index != -1):
            possibleWords.append(word_list[index])
        
            
    return possibleWords
            
        
    
    

    
word = 'jurein'
#jumbleUsingLinearSearch(word);
#print(word_list)
#print(jumbleUsingBinarySearch(word))
print(binary_search(word_list, 0, len(word_list)-1, 'monday') )
print(word_list[0])