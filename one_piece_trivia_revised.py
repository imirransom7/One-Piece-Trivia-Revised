print("Welcome to One Piece Trivia!")
input("Hello contestant! Ready to play? ")

name = input("\nAwesome To start off, what is your name? ")
print(f"Nice to meet you {name}!")
print("\nNow, let us get started with our first question")

def trivia_stack(question, choices, answer, answer2, answer3 = "0"):
  print(question)
  for choice in choices:
    print(choice)
    score = 0
  ans = input("\n")
  if ans == answer or ans == answer2 or ans == answer3:
    print("\nAwesome! Here are 10 points.")
    score += 10
  else:
    print(f"\nSorry, that is incorrect. The answer is {answer}")
  return score

trivia_stack('\nWho ate the "Chop-Chop" devil fruit?', ["A. Bon Clay", "B. Buggy the Clown", "C. Daz Bones", "D. Clawador"], "B", "b")


trivia_stack("\nWho was the 3rd person to become member of the Straw Hat Pirates?", ["A. Sanji", "B. Nami", "C. Ussop", "D. Zoro"], "B", "b")

trivia_stack("\nWhat is White Beard's full name?", ["A. Edward Newgate", "B. Marshal D. Teach", "C. Basil Hawkins", "D. Demoaro Black"], "A", "a")

trivia_stack("\nWho was the first person Luffy fought in the beginning of One Piece?", ["A. Alvida", "B. Buggy the Clown", "C. Clawador", "D. Don Kreig"], "A", "a")

trivia_stack("\nWhat is this highest position within the Marines?", ["A. Admiral", "B. Fleet Admiral", "C. Vice Admiral", "D. Grand Admiral"], "B", "b")

trivia_stack("\nWhat sound did the Skyipeans hear when the Shandia were sent into the sky via 'the Knock Up Stream'", ["A. Bird", "B. Thunder", "C. Bell", "D. Explosion"], "C", "c")

trivia_stack("\nWhat animal is Chopper constantly mistaken for?", ["A. Dog", "B. Squirell", "C. Reindeer", "D. Raccoon"], "D", "d")

trivia_stack("\nThere are 10 CP9 agents. How many went undercover at the Galley La shipwright place?", ["A. 4", "B. 6", "C. 5", "D. 3"], "D", "d", "3")

trivia_stack("\nHow old is Luffy after the time-skip?", ["A. 17", "B. 19", "C. 21", "D. 23"], "B", "b", "19")

trivia_stack("\nWhat is Katakuri's devil fruit type?", ["A. Paramecia", "B. Logia", "C. Zoan", "D. Smile"], "A", "a")

trivia_stack("\nWho gave Luffy his scar under his eye?", ["A. Shanks", "B. Black Beard", "C. Demaoro Black", "D. Luffy"], "D", "d")