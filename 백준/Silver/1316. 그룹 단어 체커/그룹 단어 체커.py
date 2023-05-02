def is_con(word):
   for i in range(len(word)-1):
      if word[i]==word[i+1]:
         continue
      elif word[i] in word[i+1:]:
         return int(False)
   return int(True)



result=0
for test_case in range(int(input())):
   result+=is_con(input())
print(result)