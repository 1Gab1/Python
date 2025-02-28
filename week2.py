1) 
nums = list(map(int, input().split()))  # Input list  
for num in nums:  
    if num > 50:  # Stop if > 50  
        break  
    if num % 5 == 0:  # Skip multiples of 5  
        continue  
    print(num, end=" ")  # Print number  

2)
pwd = input()  # Input password  
if len(pwd) < 6 or pwd.isalpha():  # Weak check  
    print("Weak")  
elif any(c.isdigit() for c in pwd) and any(c.isalpha() for c in pwd):  # Moderate check  
    if len(pwd) >= 8 and any(c in "@#$%&" for c in pwd):  # Strong check  
        print("Strong")  
    else:  
        print("Moderate")  
else:  
    print("Weak")  

3)
words = input().split()  # Input words  
print(" ".join(word[::-1] if i % 2 else word for i, word in enumerate(words)))  # Reverse alt words  

4)
words = input().split()  # Input list  
freq = {}  # Dictionary init  
for word in words:  
    freq[word] = freq.get(word, 0) + 1  # Count words  
print({k: v for k, v in freq.items() if v > 1})  # Print duplicates  

5)
books = {'Book1': 5, 'Book2': 6, 'Book3': 10}  # Book data  
book = input("Enter book name: ")  # Input book  
while True:  
    copies = input("Enter copies: ")  # Input copies  
    if copies.isdigit():  # Validate number  
        copies = int(copies)  
        break  
    print("Invalid input. Enter a number.")  
if book in books:  # Check book  
    if books[book] >= copies:  
        print("Available")  
    else:  
        print("Partially Available")  
else:  
    print("Unavailable")  

6)
words = input().split()  # Input words  
freq = {}  # Dictionary init  
for word in words:  
    freq[word.lower()] = freq.get(word.lower(), 0) + 1  # Count words  
print(freq)  # Print result  
