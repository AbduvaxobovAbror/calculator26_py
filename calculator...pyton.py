# -*- coding: utf-8 -*-
"""
Created on Sat May 30 21:05:22 2026

@author: Abror
"""
print("a new postcode will have been created by @author: Abror!")
        
print("1-qo'shish")
print("2-ayirish")
print("3-ko'paytirish")
print("4-bo'lish")

opinion = int(input("qaysi amalni bajarmoqchisiz, tanlang >>>"))
if(opinion in [1,2,3,4]):
    raqam2 = int(input("1-raqamni kiriting >>>"))
    raqam1 = int(input("2-raqamni kiriting >>>"))
    
if (opinion == 1):
    natija = raqam2 + raqam1
    
elif(opinion == 2):
    natija = raqam2 - raqam1
    
elif(opinion == 3):
    natija = raqam2 * raqam1
    
elif(opinion == 4):
    natija = raqam2 // raqam1
    
print("natija {}".format(natija))




