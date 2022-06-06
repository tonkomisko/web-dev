
# todo: 1 asking for a question


# todo: 2 check the answer if it was correct


# todo: 3 check to see if we're at the end of the quiz


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    def still_has_questions(self):
        """Returns true if the question number is less than length of the list of questions"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Gets the text of the question, increases question number for the next iteration and asks for user answer"""
        current_question = self.question_list[self.question_number]
        current_question_text = self.question_list[self.question_number].text
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question_text} (True or False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Compares the user answer with the correct answer and increases the score"""
        if user_answer.lower() == correct_answer.lower():
            self.user_score += 1
            print("You got it right!")
        else:
            self.user_score -= 1
            print("You got it wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.user_score}/{len(self.question_list)}")
