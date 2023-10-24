'''
- Aise multiline comment likhte hain, aur # se single line comments.
- print("Hello") is function se hai terminal me print karate hain.
- Python me curly brackets nahi hote hain, indentation hoota hai.
- pip ke help se ham packages download karte hain.
- import math, aise ham modules import karte hain.
- math ek builtin module hai python me.
- math.gcd(3, 6)
- Rules for creating variables:
    - Should start with a letter or an underscore
    - Cannot start with a number
    - The name can only contain alpha numeric characters
    - Variable names are case sensetive
- Variables dynamic type ke hote hai by default python me, fix type ke banasakte hai ya nahi ye dekhna rahega.
- Variables data store karne ke liye containers hote hain.
- type-casting:
    - int(e): e ko integer me convert karega
    - float(e): e ko float me convert karega
    - str(e): e ko string me convert karega
- strings:
    - Strings ko bhi ham triple quotes me break karke likh sakte hain.
    - 
'''

# Aise ham variables declare karte hai python me.
# a = 34
# b = "Harry"
# c = 45.36

# typeA = type(a)
# typeB = type(b)

# print("addition", a + c)
# print("addition", a - c)
# print("multiplication", a * c)
# print("division", a / c)

# print("typeA", typeA)
# print("typeB", typeB)

# Strings

# Aise strings ko break karke bhi likh sakte hain.
# name = '''Manikant 
# Jha'''

# name = "  Manikant  "
# print(name[0])
# print(name[2:4]) # 2 include hoga 4 include hoga nahi, aise ham strings ko slice karte hain.
# print(name.strip()) # Ye leading aur trailing white spaces ko remove karta hai. JS me trim ke barabar hai.
# print(len(name)) # Ye string ki length dega hame.
# print(name.lower()) # Ye sare characters ko lowercase me convert karta hai.
# print(name.upper()) # Ye sare characters ko uppercase me convert karta hai.
# print(name.replace("a", "@")) # Yaha mai a ko @ se replace kar raha hun.

# str1 = "My name is "
# str2 = "Manikant Jha"
# concat = str1 + str2 # Aise string concatination karte hain.
# print(concat)

# template = "My name is {1}. I am a {0}.".format("Manikant Jha", "Full Stack Developer")
# print(template) # Aise template strings bana sakte hai python me. By default jo starting me bracket hota hai wo 0 index pe hota hai aur dusre hon to unka accordingly index hoga, ham number de ke ye index change karsakte hai, to fir hamare arguments wo hisab se map honge.

# template2 = f"Hello {str1} and {str2}" # Aise bhi python me template strings likh sakte hain. 

# ** Exponetitation operator
# // Floor division operator
# %  Modulo division operator

''' 
Python Collections 
1. List
2. Tuple
3. Set
4. Dictionary
'''

lst = [2, 4, 6, 8, 10]
# print(lst, type(lst), lst[2]) # Apparently python me bhi harchiz ek object hai aur wo object kisi class ka hota hai.
# print(lst[1:4]) # 1 to 4 index ke elements print kara raha hun, 1 included par 4 included nahi.
# lst[1] = 66 # Ye ham list ko mutate karrahe hain.
# lst.append(100) # Ye method list ke end me elements ko add karta hai.
# print(lst)
# lst.insert(1, 20) # Ye mai 1 index pe 100 add karraha hun, baki ke elements accordingly khisak jaaenge.
# print(lst)
# lst.remove(100) # Ye jobhi item specify kiya hai usko list mese nikal dega.
# print(lst)
# lst.pop() # Ye list me se last index ke item ko nikal dega.
# print(lst)
# del lst[3] # Ye list me se 3 index ke elememnt ko remove kardega.
# del lst # Ye pure lst variable ko hi delete kardega
# print(lst)
# lst.clear() # Ye list ko clear yane khali kardega.
# Inke alwa bhi aur methods hai jo mujhe khud dekhne rahenge.







