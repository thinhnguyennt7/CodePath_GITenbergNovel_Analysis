# def getTotalNumberOfWord(textFile):
#     # Read the text file
#     frankText = open(textFile,"r")
#     num_words = 0
#     while True:
#         # Read the line
#         line = frankText.readline()
#         # If no line then break
#         if not line:
#             break
#         words = line.split()
#         num_words += len(words)
#     return num_words


# if __name__ == "__main__":
#     text = "frankenstein.txt"
#     # text = 'test.txt'
#     getTotalNumberOfWord(text)