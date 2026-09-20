class StringHandler:
    def getString(self):
        self.text = input()

    def printString(self):
        print(self.text.upper())


text = StringHandler()
text.getString()
text.printString()
