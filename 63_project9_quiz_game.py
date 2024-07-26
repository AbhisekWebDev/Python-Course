print("**************************")
print("!!!Welcome to qiuz game!!!")

question_bank = [
    {
        "text" : "The ability to acquire methods and attributes fromm another class is called?",
        "answer" : "A"
    },
    {
        "text": "What is the process of hiding the internal details and showing only the functionality called?",
        "answer": "D"
    },
    {
        "text": "Which OOP concept allows one interface to be used for a general class of actions?",
        "answer": "C"
    },
    {
        "text": "Which of the following is not a feature of OOP?",
        "answer": "D"
    },
    {
        "text": "Which keyword is used to create a class in Python?",
        "answer": "B"
    },
    {
        "text": "Which function is used to initialize an object in a class?",
        "answer": "A"
    },
    {
         "text": "What is it called when an object of one class is stored within another object?",
         "answer": "B"
    },
    {
        "text": "In Python, which method is automatically called to destroy an object?",
        "answer": "C"
    }
]

options = [
    ["A. Inheritance", "B. Encapsulation", "C. Polymorphism", "D. Abstraction"],
    ["A. Inheritance", "B. Encapsulation", "C. Polymorphism", "D. Abstraction"],
    ["A. Inheritance", "B. Encapsulation", "C. Polymorphism", "D. Abstraction"],
    ["A. Encapsulation", "B. Abstraction", "C. Inheritance", "D. Compilation"],
    ["A. def", "B. class", "C. create", "D. new"],
    ["A. __init__", "B. __create__", "C. __start__", "D. __new__"],
    ["A. Encapsulation", "B. Composition", "C. Aggregation", "D. Inheritance"],
    ["A. __init__", "B. __delete__", "C. __del__", "D. __destroy__"]
]

score = 0

def check_answer(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True

for question_num in range(len(question_bank)):
    print("**************************")
    print(question_bank[question_num]["text"])

    for i in options[question_num]:
        print(i)

    guess = input("Enter the answer (A/B/C/D) : ").upper()
    
    is_correct = check_answer(guess, question_bank[question_num]["answer"])

    if is_correct:
        print("Correct answer")
        score += 1
    else:
        print("Incorrect answer")
        print(f"The correct option is {question_bank[question_num]['answer']}")

    print(f"Your current score is {score}/{question_num+1}")

print(f"Your score = {score}")

print(f"Youve answered {score/(len(question_bank))*100}% questions correctly")