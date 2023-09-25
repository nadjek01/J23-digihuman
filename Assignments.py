#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 2-1 Assignment
message = "Hello World"
print(message)


# In[4]:


#2-2 Assignment
message = "Hello World"
print(message)
message = "Wow it's nice here"
print(message)


# In[5]:


#2-3 Assignment
name = "Nana"
print("Hello " + name + " would you like to learn some Python today?")


# In[7]:


#2-4 Assignment
firstName = "Nana"
lastName = "Adjekum"
fullName = firstName + " " + lastName
print("Hello " + name + " would you like to learn some Python today?")
print("Hello " + name.lower() + " would you like to learn some Python today?")
print("Hello " + fullName.title() + " would you like to learn some Python today?")


# In[9]:


#2-5 Assignment
print("Albert Einstein once said, \"A person who never made a mistake never tried anything new.\"")


# In[10]:


#2-6 Assignment
famousPerson = "Albert Einstein"
message = "\"A person who never made a mistake never tried anything new.\""
print(famousPerson + " once said, " + message)


# In[11]:


#2-7 Assignment
name = "\tNana\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())


# In[14]:


#2-8 Assignment
print(5 + 3)
print(4 * 2)
print(12 - 4)
print(16 / 2)


# In[16]:


#2-9 Assignment
faveNum = 7
message = "My fave num is " + str(faveNum)
print(message)


# In[17]:


# 2-10 Assignment
# Nana A.
# 19-Sept
faveNum = 7
message = "My fave num is " + str(faveNum)
print(message)


# In[18]:


#3-1 Names
names = ["Bob", "Sally", "Roger"]
print(names[0])
print(names[1])
print(names[2])


# In[19]:


#3-2 Greetings
names = ["Bob", "Sally", "Roger"]
print("Hey " + names[0])
print("Hey " + names[1])
print("Hey " + names[2])


# In[20]:


#3-3 Your Own List
names = ["Balenciaga", "Maison Margiela", "Kapital"]
messageB = "I like the clothes from "
messageM = "I like the tabis from "
messageK = "I like the sweaters from "
print(messageB + names[0])
print(messageB + names[1])
print(messageB + names[2])


# In[26]:


#3-4 Guest List
guestList = ["Meryl Streep", "Anthony Bourdain", "Paris Hilton"]
invite = "come to Dinner"
print("Hey " + guestList[0] + ", " + guestList[1] + ", and " + guestList[2] + " " + invite)


# In[27]:


#3-5 Changing Guest List
guestList = ["Meryl Streep", "Anthony Bourdain", "Paris Hilton"]
invite = "come to Dinner"
print("Hey " + guestList[0] + ", " + guestList[1] + ", and " + guestList[2] + " " + invite)
print(guestList[2] + " can't come to dinner")
guestList[2] = "Queen Elizabeth"
print("Hey " + guestList[0] + ", " + guestList[1] + ", and " + guestList[2] + " " + invite)


# In[35]:


#3-6 More Guests
guestList = ["Meryl Streep", "Anthony Bourdain", "Paris Hilton"]
invite = "come to Dinner!"
guestList.insert(0, "Drake")
guestList.insert(2, "Julia Roberts")
guestList.append("Aubrey Plaza")
print("Hey, " + guestList[0] + " " + invite)
print("Hey, " + guestList[1] + " " + invite)
print("Hey, " + guestList[2] + " " + invite)
print("Hey, " + guestList[3] + " " + invite)
print("Hey, " + guestList[4] + " " + invite)
print("Hey, " + guestList[5] + " " + invite)


# In[59]:


#3-7 Shrinking Guest List
#3-6 More Guests
guestList = ["Meryl Streep", "Anthony Bourdain", "Paris Hilton"]
invite = "come to Dinner!"
guestList.insert(2, "Julia Roberts")
guestList.append("Aubrey Plaza")

print("Hey, " + guestList[0] + " " + invite)
print("Hey, " + guestList[1] + " " + invite)
print("Hey, " + guestList[2] + " " + invite)
print("Hey, " + guestList[3] + " " + invite)
print("Hey, " + guestList[4] + " " + invite)
#print("Hey, " + guestList[5] + " " + invite)

print("Hey, like actually only 2 people can come :(")

print("Hey " + guestList.pop() + " you can't " + invite)
print("Hey " + guestList.pop() + " you can't " + invite)
print("Hey " + guestList.pop() + " you can't " + invite)

print("Hey, " + guestList[0] + " you can " + invite)
print("Hey, " + guestList[1] + " you can " + invite)

del(guestList)
#print(guestList)    #wont print bc guestList DNE


# In[57]:


#3-8 Seeing the World
places = ["new york", "paris", "london", "rio de jianero", "morrocco"]
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
places.sort()
print(places)
places.sort()
print(places)


# In[6]:


#4-1 Pizzas
pizza = ["cheese", "vodka", "white"]
for pizza in pizza:
    print("I like " + pizza + " pizza")
print("I really love pizza!")


# In[7]:


#4-2 Animals
animals = ["tiger", "lion", "leopard"]
for animals in animals:
    print("A " + animals + " is cat")
print("All of these animals belong to the cat family!")


# In[9]:


#4-3 Counting to Twenty
for value in range(1,21):
    print(value)


# In[15]:


#4-4 One Million
allNums = list(range(1,1000001))
for allNums in allNums:
    print(allNums)


# In[13]:


#4-5 Summing a Million
allNums = list(range(1,1000001))
print(min(allNums))
print(max(allNums))
print(sum(allNums))


# In[20]:


#4-6 Odd Numbers
oddNums = list(range(1,21,2))
print(oddNums)


# In[22]:


#4-7 Threes
multThree = list(range(3, 31, 3))
for multThree in multThree:
    print(multThree)


# In[23]:


#4-8 Cubes
cubes = [value ** 3 for value in range(1,11)]
for cubes in cubes:
    print(cubes)


# In[25]:


#4-9 Cube Comprehension
cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)


# In[35]:


#4-10 Slices
pizza = ["cheese", "vodka", "white", "margherita"]
for pizza in pizza:
    print("I like " + pizza + " pizza")
print("I really love pizza!")

print("The first three items in the list are: ")
print(pizza[0:])
print("The middle three items in the list are: " + pizza[2:3])
print("The last three items in the list are: " + pizza[3:3])


# In[ ]:


#4-11 My Pizzas, Your Pizzas
favorite_pizzas = ["cheese", "vodka", "white"]
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("margherita")
friend_pizzas.append('pesto')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)


# In[ ]:




