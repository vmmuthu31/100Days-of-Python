student_score=input("Enter the scores: ").split()
for n in range(0,len(student_score)):
  student_score[n]=int(student_score[n])
print (f"The scores are  {student_score}")
high_score=0
for score in student_score:
  if score>high_score:
    high_score=score
print(f"The Highest score is: {high_score}")
