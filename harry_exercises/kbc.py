questions=["who is the prime minister of india ? ", "which is longest river in india ? ", "2+5/5=?", "How many icc world cup india has ?"]
answers=["Narendra Damodar Das Modi", "Ganga", "2.4", "2"]

won_amount=0
for question in questions:
 ans=input(question)
 for answer in answers:
  if(answer.lower()==ans.lower()):
   won_amount+=5000

print(f"You have won {won_amount}")  
