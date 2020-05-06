# Table of Contents
---

<!--ts-->
   * [Binary Search](#binary-search)
      * [Challenge](#challenge)
      * [Approach And Efficiency](#approach-And-efficiency)
      * [Solution](#solution)
<!--te--> 



# Binary Search
Write a python function to search and find the given element's position in a given sorted list

---

## Challenge
Do not use any inbuit function in python.  

---

## Approach And Efficiency

First find a length of a source list wihout using any inbuilt functions.  
Write a python function to accept the arguments as source list, search key to be searched and identified the position.  
Define and initialize the low number and middle number as zero and high number as length - 1.  
Iterate through while loop until the low number less than or equal to high number.  
Identify the middle number by finding mid point((high_number + low_number) / 2).  
Check whether the middle number of the list is equal to search key then return the middle number position.  
Otherwise check whether search key less than middle number of the list then re initialize high number as mid number - 1.  
Otherwise check whether search key greater than middle number of the list then re inittialize low number as mid number + 1.  
Iterate through remaning of the list to identify the position of the search key.  
If position of the search key not found inside the while loop, the function will return position as -1

---

## Solution
[White Board](assets/binary-search.jpg)

---