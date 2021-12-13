class HumanService(object):
    def say(self, string: str) -> None:
        print(string)

    def ask(self, question: str) -> str:
        return input(question + " ")
