# make improved code with modifications

import random


def Randomfunction_M(min, max):
    """
   Choose a Random integer.
    """
    return random.randint(min, max) # Choosing a random integer


def Randomfunction_N():
 """
   Choose a Random operator.
 """
    return random.choice(['+', '-', '*']) # choosing a random operator


def Randomfunction_O(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 - n2
    elif o == '-': a = n1 + n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = Randomfunction_M(1, 10); n2 = Randomfunction_M(1, 5.5); o = Randomfunction_N()

        PROBLEM, ANSWER = Randomfunction_O(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        try:
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)
        except ValueError:
        print("invalid input")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
