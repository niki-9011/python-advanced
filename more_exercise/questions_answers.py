import random


questions_answers = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the largest mammal in the world?": "Blue whale",
    "How many continents are there?": "Seven",
    "What is the chemical symbol for water?": "H2O",
    "What is the capital of Japan?": "Tokyo",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the tallest mountain in the world?": "Mount Everest",
    "What is the chemical symbol for gold?": "Au",
    "Who is known as the father of modern physics?": "Isaac Newton",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote the novel 'Pride and Prejudice'?": "Jane Austen",
    "What is the square root of 144?": "12",
    "What is the chemical formula for table salt?": "NaCl",
    "Who discovered penicillin?": "Alexander Fleming",
}


def play_game():
    print("Welcome to the Question Game!")
    print("Answer the following questions:\n")


    questions = list(questions_answers.keys())
    random.shuffle(questions)

    score = 0

    for question in questions:
        answer = input(question + "\nYour answer: ")
        correct_answer = questions_answers[question]

        if answer.lower() == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.\n")

    print("Game Over!")
    print(f"Your final score is {score}/{len(questions)}")


def main():
    play_game()
    while True:
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            play_game()
        else:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
