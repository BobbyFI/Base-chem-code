element = {
  "H": 1.008,
  "He": 4,
  "Li": 6.49

def weight1():
  if element1 == "H":
    element1 = 1.008
  if element1 == "He":
    element1 = 4.00
  if element1 == "Li":
    element1 = 6.49
  if element1 == "Be":
     element1 = 9.01
  if element1 == "B":
     element1 = 10.81

Be = 9.01
B = 10.81
C = 12.01
N = 14.01
O = 16.00
F = 19.00
Ne = 20.18
Na = 22.99
Mg = 24.30
Al = 26.98
Si = 28.09
P = 30.97
S = 32.06
Cl = 35.45
Ar = 39.95
K = 39.10
Ca = 40.08
Sc = 44.96
Ti = 47.87
V = 50.94
Cr = 52.00
Mn = 54.94
Fe = 55.85
import os
def clear():
  os.system('cls' if os.name == 'nt' else 'clear') 

def calc():
  tot = var1 + var2 + var3
  print(tot)

element = "a"
def equa():
  cat1 = cat1o
  cat2 = cat2o
Cont = '1'
cat1 = "0"
cat2 = "0"
cat3 = "0"
var1 = 0
var2 = 0
var3 = 0
cont = '1'

def search():
  equa()
  if cat1 == "0":
    while cont == '1':
      element1 = input("please enter the first element\n")
      num = int(input("Please enter the number of atoms\n"))
      
      var1 = element1 * num
      clear()
      cont = '2'
      cat1o = 1
  elif cat2 == 0:
    while cont == '2':
      element2 = input("please enter the second element or enter done\n")
      if element2 == "done":
        calc()
      else:
        num = int(input("Please enter the number of atoms\n"))
        weight()
        var2 = element2 * num
        clear()
        cat2 = "1"
  elif cat3 == "0":
    while cont == '3':
      element3 = input("please enter the third element or enter done")
      num = int(input("Please enter the number of atoms\n"))
      weight()
      var3 = element3 * num
      clear()
      cat3 = '1'

Cont = '1'
cat1o = "0"
cat2o = "0"
cat3o = "0"
tot = 0

element1 = 0
element

import time

job = input("Please select an operation by entering its corresponding number\n1.Calculate Formula Mass\n2.Molar convertions\n")
if job == "1":
  clear()
  time.sleep(.2)
  print("Formulas should be entered using their Symbol and\nQuantified with a following number. Ex. H2,C3")
  while tot == 0:
    search()
elif job == "2":
  clear()
  print("work in progress")