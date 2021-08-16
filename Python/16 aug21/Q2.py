def checkvowel(s):
  for i in s:
    if(i=="a"):
      s=s.replace("a","g")
    elif(i=="e"):
      s=s.replace("e","g")
    elif(i=="i"):
      s=s.replace("i","g")
    elif(i=="o"):
      s=s.replace("o","g")
    elif(i=="u"):
      s=s.replace("u","g")
  print(s)
print("Use small letters only...!")
sentence = input("Enter a sentence: ")
checkvowel(sentence)