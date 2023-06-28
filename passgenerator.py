import random
import time

keys = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
  'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
  '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+',
  '=', '{', '}', '[', ']', '|', ':', ';', ',', '.', '<', '>', '/', '?'
]

print("Quartzz/Egzoz Password Generator-Şifre Oluşturucu")
time.sleep(2)

reqLenght = input("Şifre Kaç Haneli Olsun ? ")
reqLenght = int(reqLenght)

reqPass = ""

i = 0

if (reqLenght <= 0):
  print("something is wrong")
else:
  while (i < reqLenght):
    reqPass += random.choice(keys)
    i += 1
    if (i == reqLenght):
      print(reqPass)
