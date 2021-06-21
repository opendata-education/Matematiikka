#!/usr/bin/env python
# coding: utf-8

# # Intro 2: Statistik i Python

# I denna notebook ska vi se på hur man importerar statistik till Python och presenterar den visuellt som en tabell, graf eller diagram.
# 
# Vi kommer att använda **numpy**, som från tidigare är bekant, samt **pandas** och **matplotlib.pyplot**. Vi börjar med att importera paketen. Kör kodcellen, så att paketen är tillgängliga i resten av dokumentet.

# In[1]:


import matplotlib.pyplot as plt  # matplotlib.pyplot innehåller verktyg för att rita grafer och diagram.
import pandas as pd              # pandas låter oss läsa in en datafil och spara den som en variabel i python.
import numpy as np               


# ### CSV-filer

# Många datafiler är i .csv-format (comma separated values). En tabell i ett kalkylblad kan sparas som .csv, och ser då ut ungefär så här:
# 
# <img src="files/csvstudentexempel.PNG" width=250>
# 
# Csv-filer kan importeras till python, och blir då till en typ av tabellvariabel som kallas DataFrame.
# Eftersom största delen av open data-filer är tillgängliga som .csv, ska vi här se på hur man hanterar sådana tabeller.

# ### Statistik: Världens energiproduktion

# Den Notebook som du läser nu finns online på GitHub. I samma system av mappar på GitHub finns en csv-fil med information om världens energiproduktion 1800-2019. På GitHub, såväl som lokalt på din dator, kan du hänvisa till en fil med en *relativ sökväg*. Tillsammans med denna notebook finns mappen **files** och i den finns filen **global-energy-substitution.csv**. Vi kan alltså hitta filen med sökvägen "files/global-energy-substitution.csv", och vi kan importera den till python med pandas-funktionen **pd.read_csv()**.
# 
# Vi sparar csv-filen som en DataFrame-variabel med namnet **energi**. Därefter kan vi se de första raderna av tabellen med hjälp av kommandot **energi.head()**, bara så vi vet om den lästes in rätt.

# In[2]:


energi = pd.read_csv("files/global-energy-substitution.csv")
energi.head()


# Nu vill vi kunna sålla ut information ur tabellen. Här följer några metoder:
# 
# #### Kolumn
# Vi kan välja ut en kolumn med värden. Detta kommer att behövas när vi ska föra in data i en graf. 
# ````python
# energi["Oil (TWh)"]  # Återger kolumnen med rubriken Oil (TWh)
# 
# # Vi kan förstås också spara kolumnen som en variabel:
# oil = energi["Oil (TWh)"]
# ````
# 
# #### Värdesökning
# Vi kan söka de rader som innehåller ett bestämt värde. I python använder vi = för att definiera en variabel och == för att kontrollera en variabel.
# ````python
# energi[energi["Year"]==2015]   # Kontrollerar tabellen och återger de rader som innehåller årtalet 2015
# 
# energi[energi["Wind (TWh)"]>0] # Återger de rader där vindkraftsproduktionen är större än 0 TWh.
# 
# energi[(energi["Year"]<1990) & (energi["Wind (TWh)"]>0)] # Flera krav kan kombineras med & ("och").
# ````
# 
# #### Index
# Vi kan välja ut rader med hjälp av index. Varje rad i tabellen har ett index längst till vänster, och indexering i python fungerar så att den första raden/elementet alltid har index 0. 
# 
# ````python
# energi[67:69] # Hänvisar till raderna 67 och 68 (år 2015 och 2016), men inte slutgränsen 69.
# ````
# #### Enskild cell
# Vi kan använda kommandon loc och iloc för att hänvisa till en viss cell.
# ````python
# energi.iloc[[67],[2]]          # iloc söker en cell med hjälp av radindex och kolumnindex
# 
# energi.loc[[67],["Oil (TWh)"]] # loc söker en cell med hjälp av radindex och kolumntitel
# ````
# 
# 
# ````python
# 
# ````

# ### Övning: Informationssökning

# Med hjälp av tipsen ovan kan du utföra följande övningar:
# 
# #### Värdesökning
# 
# Skriv ett kommando som återger de rader i tabellen där produktionen för vindkraft överstiger 1000 TWh. Från och med vilket årtal skedde det här?
# 
# Skriv ett kommando för att välja ut de rader i tabellen där produktionssiffran för oljeenergi är högre än för biomassa. Från och med vilket årtal skedde det här?
# 
# #### Index
# 
# Skriv ett kommando som väljer ut raderna med årtalen 2000-2005. Vilken form av energiproduktion var störst under den tiden?
# 
# #### Enskild cell
# 
# Hur hög var produktionen av vattenkraft år 1977? Skriv ett kommando som enbart återger den cellen.

# In[3]:


# Skriv din kod här. Skapa fler kodceller vid behov.
# Kom ihåg att du måste köra de tidigare kodcellerna så att funktionspaketen och datafilen är tillgängliga.

