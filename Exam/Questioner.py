
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return f"{self.question}\n{self.answer}\n"
    
    def print_question(self):
        print(self.question)

    def print_answer(self):
        print(self.answer)

from random import randint
import os
import pandas as pd


def main():
    # get the folder path automatically
    f_path = os.path.dirname(os.path.abspath(__file__))

    # File path
    file_path = os.path.join(f_path, "KeyWordAssoluto.md")

    # Open the file
    f = open(file_path, "r", encoding="utf-8")
    lines = f.readlines()
    f.close()

    # 72.  Feature extraction for speech classification, which region of analysis is not used | Invariant
    questions = []

    for l in lines:
        s = l.split("|")
        q = s[0].strip()
        a = s[1].strip()
        questions.append(Question(q, a))

    errors = 0
    correct = 0

    while True:
        if len(questions) == 0:
            print("No more questions")
            # check if there is a file with the results
            if os.path.exists("results.csv"):
                df = pd.read_csv("results.csv")
                # append the results to csv without using append
                df.loc[len(df)] = [correct, errors]
                df.to_csv("results.csv", index=False)
            else:                
                df = pd.DataFrame({"Correct": [correct], "Errors": [errors]})
                df.to_csv("results.csv", index=False)
            break


        q_index = randint(0, len(questions)-1)
        q = questions[q_index]
        q.print_question()
        input("Press Enter to show the answer")
        q.print_answer()
        i=input("y: correct, q: quit\n")
        if i == 'q':
            break
        elif i == 'y':
            correct += 1
            questions.pop(q_index)
        else:
            errors += 1

        # clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
if __name__ == '__main__':
    main()