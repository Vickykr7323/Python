# Python Code Written By Vicky Kumar 

# In[1]:

a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=a+b
print("sum of {} and  {} = {}".format(a,b,c))


# In[2]:


a=float(input("Enter first number"))
b=float(input("Enter second number"))
c=a+b
print("sum of {} and  {} = {}".format(a,b,c))


# In[3]:


l=float(input("Enter Length : "))
b=float(input("Enter breath : "))
area = l*b
print("area of rectangle {} and  {} = {}".format(l,b,area))


# In[4]:


a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("Before Swapping value of a {} and b {}".format(a,b))
a=a+b
b=a-b;
a=a-b;
print("After Swapping value of  a {} and b {}".format(a,b,c))


# In[5]:


b=float(input("Enter Length : "))
h=float(input("Enter breath : "))
area = 0.5*b*h
print("area of triangle {} and  {} = {}".format(b,h,area))


# In[6]:


import random
print(random.random())
l=int(input("Enter lower bound"))
u=int(input("Enter Upper bound"))
print("random number between {} and {} = {}".format(l,u,random.randint(l,u)))
li=[20,30,40,50,60,70]
print("given List")
print(li)
print("Random number with in given list = {}".format(random.choice(li)))


# In[7]:


no=int(input("Enter number "))
if no>0:
    print(no, " is positive nuber")
elif no<0:
    print(no," is negative no")
else:
    print("it is zero")






