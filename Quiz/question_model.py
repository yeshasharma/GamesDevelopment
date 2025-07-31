class Question:

    def __init__(self, q_text, answer):
        self.text = q_text
        self.answer = answer

if __name__ == "__main__":
    new_q = Question("2+3=5", True)
    print(new_q.text)

