1)
num = float(input())  
print(f"Original float: {num}")  
print(f"Converted to integer: {int(num)}")  
print(f'Converted to string: "{str(num)}"')  

2)
name = input()  
first, last = name.split()  
print(f"Your initials are: {first[0].upper()}.{last[0].upper()}")  

3)
text = input()  
print(text[::-1])  

4)
word = input()  
index = int(input())  
print(f'Substring from index {index}: "{word[index:]}"')  

5)
email = input()  
print(f"Domain: {email.split('@')[-1]}")  

6)
word = input()  
print(word[-1] + word[1:-1] + word[0] if len(word) > 1 else word)  
