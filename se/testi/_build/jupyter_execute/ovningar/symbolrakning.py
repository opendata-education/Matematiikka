#!/usr/bin/env python
# coding: utf-8

# # Symbolräkning med Python

# Vanligen utförs beräkningar i program med hjälp av numeriska metoder och algoritmer, och då kan endast närmevärden fås, men om man implementerar ett CAS (Computer Algebra System), kan man få exakta, symboliska svar.
# 
# Python kan utföra symbolräkning med hjälp av funktionspaketet [SymPy](https://docs.sympy.org/). I denna Notebook hittar du en del exempel på hur SymPy kan användas. Om du vill ha fler exempel utöver denna introduktion kan du söka bland [SymPy:s instruktioner](https://docs.sympy.org/latest/tutorial/index.html).

# ## Att definiera en funktion

# In[1]:


# Vi börjar med att importera paketet sympy.
# Genom att skriva import kommandot som "from ____ import *" gör vi så att inget funktionsprefix behövs
# (vi kan då skriva Symbol istället för sympy.Symbol och sin istället för sympy.sin)
from sympy import *

# I Python har variabler ingen betydelse innan de är definierade. SymPy är inget undantag.
# För att använda x som en symbolvariabel behöver vi definiera den med SymPy-funktionen Symbol.
x = Symbol('x')

# Vi definierar några funktioner och namnger dem f(x), g(x) och h(x).
def f(x):
    return x**2 + x + 1

def g(x):
    return sin(x) + cos(x) - 1

def h(x):
    return 5*exp(x) + 1


# In[2]:


# Vi kontrollerar att funktionerna kan skrivas ut symboliskt.
f(x)


# In[3]:


g(x)


# In[4]:


h(x)


# In[5]:


# Vi substituerar x med 1 i funktionen f(x)

f(x).subs(x, 1)


# In[6]:


# Vi beräknar summan av g(0) och h(1).
# Vi gör detta med ett mellansteg där vi beräknar de båda funktionsvärdena.

g0 = g(x).subs(x, 0)
h1 = h(x).subs(x, 1)

g0 + h1


# In[7]:


# Vi definierar en sammansatt funktion, g(f(x))

def c(x):
    return g(f(x))

c(x)


# ## Derivator och integraler

# In[8]:


# Vi deriverar f med hjälp av sympys funktion "diff".

df = diff(f(x))
df


# In[9]:


# Vi beräknar h'(5)

dh = diff(h(x))
dh5 = dh.subs(x, 5)
dh5


# In[10]:


# Vi integrerar f med avseende på x

F = integrate(f(x),x)
F


# In[11]:


# Vi beräknar den bestämda integralen av f, då x går från 0 till 5.

F0_5 = integrate(f(x),(x,0,5))
F0_5

