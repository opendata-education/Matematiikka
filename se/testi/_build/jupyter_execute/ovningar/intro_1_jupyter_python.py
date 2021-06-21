#!/usr/bin/env python
# coding: utf-8

# # Intro 1: Använd Jupyter Notebooks

# Om du inte har använt Jupyter Notebooks eller Python tidigare är detta ett bra ställe att börja.
# 
# Detta är en Jupyter Notebook. Notebook är en typ av dokument som är interaktiva. Du kan läsa instruktionerna och göra egna ändringar i dokumentet. För att detta ska fungera behöver du öppna dokumentet online med hjälp av webbapplikationen MyBinder (detta kan göras med hjälp av raketsymbolen uppe i kanten. Det kan ta någon minut att öppna.) eller genom att ladda ned filen (filformat.ipynb) och öppna den lokalt med programmet Jupyter Notebook.

# ## Jupyter-övningar

# ### 1. Köra celler

# Ett Jupyter-dokument består av textceller och kodceller. Detta är en textcell, även kallad *markdown*. Du kan öppna en cell i *edit mode* genom att dubbelklicka den. Du kan **köra** (run) en cell genom att trycka **Ctrl + Enter**, eller **Run**-knappen i menybalken.
# 
# När du öppnar cellen ser du också hur olika typer av formatering fungerar, t.ex. hur man skriver **fet** och *kursiv* stil. 
# 
# - Testa att öppna och ändra denna cell
# - Kör cellen.

# ### 2. Nya celler och celltyp

# Denna cell är en textcell. När du markerar en sådan ser du texten "Markdown" i en ruta i övre kanten. Du kan ändra cellens typ till "Code" om du vill. Denna cell innehåller dock ingen fungerande python-kod, så det är inte till någon nytta.
# 
# Man kan sätta in nya celler om det behövs. Se i den övre menybalken, och välj **Insert** $\rightarrow$ **Insert cell below**. En ny cell är automatiskt en kodcell.
# 
# - Skapa en ny cell.
# - Ändra den nya cellen till *Markdown*.

# ### 3. Matematiska uttryck

# I textceller i Jupyter kan man använda $\LaTeX$-text. Om du inte har använt LaTeX är du kanske bekant med något annat program som använder det språket, till exempel MAOLs [Läksyvihko](https://xn--lksyvihko-v2a.fi/).
# 
# Genom att skriva `$`-tecken före och efter koden kan man få ekvationer mitt i en textrad, så här:  $\frac{d}{dx}e^x = e^x$
# 
# Om man skriver dubbla `$$`-tecken syns formeln på en egen rad. (öppna denna cell och se hur det ser ut)
# 
# $$P\left(\text{"k av n lyckas"}\right)\ =\ \binom{n}{k}\cdot p^k\cdot q^{n-k}$$
# 
# - Här syns deriveringsregeln för en naturlig exponentialfunktion och formeln för binomialsannolikhet. Skapa en ny textcell nedan och skriv in någon annan av dina favoritformler. Om du inte har använt LaTeX tidigare kan du använda Läksyvihko för att översätta din ekvation till kod.

# ### 4. Bilder och länkar

# Om man skriver en artikel i en notebook vill man kanske lägga in bilder. kommandot för att göra detta är ``<img src= bildlänk   >`` eller ``![titel](bildlänk)``
# 
# Efter Istället för **"bildlänk"** fyller man i en webbadress till en bild. Då hämtar Jupyter automatiskt in bilden.
# 
# Om du har sparat denna notebook på din dator och öppnat den med Jupyter Notebooks kan du också skriva filnamnet på en bild som ligger i samma mapp som denna notebook på din dator.
# 
# - Skapa en ny cell, eller använd den nya cellen du skapade i uppgift 2.
# - Använd någotdera kommandot för att lägga till en bild.
# - Kör cellen. Syns bilden? Kom ihåg att det måste vara en Markdown-cell.

# ## Python-uppgifter

# ### 1. Obligatoriskt "Hello World!"-program

# Cellen nedan är en kodcell. Man känner igen kodceller på Index-markeringen ``In [ ]`` och den pilformade *run*-knappen i vänstra kanten. Detta dokument är inställt på Python-kod
# 
# Det hör till traditionen att man börjar vägen mot programmering med att göra ett program som skriver ut meddelandet "Hello World!".
# 
# - skriv följande kod i cellen nedan.
# 
# ````python
# print("Hello World!")
# ````
# - Kör kodcellen. Den borde skriva ut meddelandet.

# In[ ]:





# ### 2. Error

# Det sägs att det enda som är säkert i livet är döden och skattebetalningen, men för en programmerare är inget mer säkert än att koden förr eller senare avger ett felmeddelande.
# 
# Ibland fungerar inte koden, och det kan vara så lite som ett enda tecken som är fel. Python innehåller inte någon funktion som rättar din kod, men felmeddelandet pekar ut **var** i koden felet finns. Seda får man lov att söka och testa tills man lyckas få koden att fungera.
# 
# - Kör koden nedan. Den avger ett felmeddelande.
# - Hitta felet i koden och fixa den.

# In[1]:


print(Att fela är mänskligt.)


# ### 3. Variabler

# Beräkningar i Python använder vanligen variabler. En variabel kan definieras med hjälp av ett =-tecken.
# 
# Man kan använda de 4 räknesätten med +, -, \* och /, och potens med \*\*.
# 
# - Läs exempelkoden så att du förstår hur den fungerar. Kör den.

# In[2]:


# Rader som börjar med # påverkar inte koden.
# Använd gärna sådana kommentarer för att förklara vad koden gör.

manader = 12         # Variabeln månader har nu värdet 12.
dagar = 365.25       # Variabeln dagar har värdet 365.25
kvot = dagar/manader

print("En månad är i medeltal", kvot, "dagar lång")


# - Skriv en kod som definierar variablerna **a** och **b** (vilka siffervärden du vill), multiplicerar dem och skriver ut svaret.

# In[ ]:





# ### 4. Funktionspaket 

# Pythons egna funktioner är ganska begränsade, men det finns många tilläggsmoduler, så kallade *paket* med funktioner som man kan importera till sin kod för att få fler möjligheter. Det är också möjligt för python-användare att skapa sina egna moduler.
# 
# Vi testar här att importera paketet **numpy**, som innehåller många funktioner för beräkningar.
# När vi har importerat numpy kan vi använda numpys funktioner om vi kallar på dem med prefixet **numpy.** Ett funktionspaket behöver bara hämtas en gång per dokument, men import-kommandot måste köras igen varje gång man startar om dokumentet.
# 
# Vi kan också importera numpy med ett kortnamn och på så sätt förenkla prefixet.
# ````python
# import numpy as np
# ````

# In[3]:


import numpy as np

np.sin(0)  # sinusfunktionen ingår i numpy-paketet. Vi beräknar sinus av vinkeln 0 rad. 


# ### 5. Listor

# En lista är en serie värden. De kan vara siffervärden, text eller andra variabler.
# Man kan spara listan som ett variabelvärde.
# 
# ````python
# lista = [2, 3, "banan", "äpple", 5]
# ````
# 
# Om listan bara innehåller siffervärden kan du använda numpys funktioner för att beräkna lägesmått för det statistiska materialet.
# 
# np.mean(lista) beräknar medelvärde
# 
# np.std(lista) beräknar standardavvikelse
# 
# np.var(lista) beräknar varians
# 
# - Samla in minst 5 statistiksiffror - exempelvis 5 vänners längd - och skriv in dem en lista nedan.
# - Beräkna medeltal och standardavvikelse för listan. Du måste ha kört en cell som importerar numpy först.

# In[ ]:





# ## Bra jobbat!

# Du kom genom introduktionen. Hoppas den har varit lärorik och klar, och att du minns funktionerna vi gick igenom.
# 
# Om du har frågor kan du fråga din instruktör eller maila oss på avoin-data-apua@cern.ch
# 
# I nästa Notebook ritar vi diagram.
