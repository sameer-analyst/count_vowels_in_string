# This function counts the number of vowels in a given string
def count_vowels(string,vowels):
  count = 0
  for char in string:
      if char in vowels:
          count+=1
  return count
      
string = input("Enter the sentence:")
vowels = "AEIOUaeiou"
print("Number of vowels:",count_vowels(string,vowels))