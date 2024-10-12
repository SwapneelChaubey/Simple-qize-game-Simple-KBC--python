# Project 3
# Simple Quiz game /  Simple KBC
questions = [
  [
    "Q1. Which of these devices is used to point at things on the monitor",
     "a) CPU", "b) Keyboard", "c) Mouse", "d) Speakers", 3
  ],
  [
    "Q2. What does GB stand for in the world of computers? ","a) Gigabyte"," b) Game boy"," c) General Business"," d) None of the above", 1
  ],
  [
    "Q3. Which of these devices cannot be carried around? ","a) Desktop computer"," b) Smartphone"," c) Tablets"," d) Laptops",1
  ],
  [
    "Q4. Which of these computer devices runs on a battery? ","a) Desktop computer"," b) Laptop"," c) Tablet"," d) Both b and c",4
  ],
  [
    "Q5. Which one of these is the smallest computer? ","a) Mainframe computer"," b) Laptop"," c) Tablet"," d) Desktop computer",3
 ],
]

levels = [10000, 20000, 30000, 40000, 50000,]
money = 0
for i in range(0, len(questions)):
  question = questions[i]
  print(f"\n{[i+1]} Question for Rs.{levels[i]}\n")
  print(f"{question[0]}")
  print(f"{question[1]}          {question[2]} ")
  print(f"{question[3]}          {question[4]} ")
  reply = int(input("Enter your answer (1-4) or 0 to quit:\n" ))
  if (reply == 0):
    print("You quit the game, Thanks for playing!")
    money = levels[i-1]
    break
  if(reply == question[5]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 0):
      money = 10000
    elif(i == 1):
      money = 20000
    elif(i == 2):
      money = 30000
    elif(i == 3):
      money = 40000
    elif(i == 4):
      money = 50000
  else:
    print("Wrong answer!")
    break 

print(f"Your take money for home is {money}")

