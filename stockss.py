# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:37:26 2021

@author: User
"""

days = 2

initial = 6000
oneDay = initial / 5
interest = 0
totalInterest = 0
percent = .1

amount = [(oneDay * 2), (oneDay * 2), (oneDay)]


for x in range(3,50):
    interest = amount[x-3] * percent
    totalInterest += interest
    amount.append(amount[x-3] + interest)
    


days  = []

ordered = []
for y in range(0, len(amount), 5):
    days.append(amount[y:y+5])
  
    



for z in days:
    ordered.append({'Mon': round(z[0],1), 'Tues': round(z[1],1), 'Wed': round(z[2],1), 'Thurs': round(z[3],1), 'Fri': round(z[4],1)})
    

for a in ordered:
    print(a)
    


print("\n\n Interest: {}".format(round(totalInterest,2)))
