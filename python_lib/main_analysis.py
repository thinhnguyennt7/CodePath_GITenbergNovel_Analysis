from heapq import heappush, heappop
import re
class Frankenstein:

    def __init__(self, fileName):
        self.num_words = 0
        self.frankText = open(fileName, 'r')
        self.wordMap = {}
        self.frequenceWords = []
        if self.frankText.mode == 'r':
            while True:
                # Read the line
                line = self.frankText.readline()
                # If no line then break
                if not line:
                    break
                words = self.splitString(line)
                for word in words:
                    if word in self.wordMap:
                        self.wordMap[word] += 1
                    else:
                        self.wordMap[word] = 1

    def getTotalNumberOfWord(self, textFile):
        count = 0
        for val in self.wordMap.values():
            count += val
        return count

    def getTotalUniqueWords(self):
        return len(self.wordMap.keys())

    def splitString(self, sentence):
        wordList = []
        temp = ''
        # Remove new line character and avoid white empty white space
        sentence = sentence.replace('\n', '')
        sentence = sentence.replace('\r', '')
        sentence = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", sentence)
        for char in sentence:
            if char == ' ' and (temp != ' '):
                if (temp != ''):
                    wordList.append(temp)
                temp = ''
            else:
                temp += char
        if temp and (temp != '\n' or '' or ' '):
            wordList.append(temp)
        return wordList

    def get20MostFrequentWords(self, mostFreq):
        arr = []
        for key in self.wordMap:
            # Push to arr using min heap
            heappush(self.frequenceWords, [-self.wordMap[key], key])
            heappush(arr, [-self.wordMap[key], key])
        out = [heappop(arr) for _ in range(mostFreq)]
        return self.reformatOutput(out)

    def get20MostInterestingFrequentWords(self, textFile, filterVal, mostFreq):
        commonList = []
        values = []
        commandText = open(textFile, 'r')
        while True:
            line = commandText.readline().replace('\n', '')
            if not line:
                break
            if len(commonList) == filterVal:
                break
            commonList.append(line.lower())

        for ele in self.frequenceWords:
            if len(values) == mostFreq:
                break
            if ele[1].lower() not in commonList:
                values.append(ele)
        return self.reformatOutput(values)

    def reformatOutput(self, array):
        output = []
        for ele in array:
            ele[0] = ele[0]*(-1) # CHANGE VALUE TO POSITIVE
            output.append([ele[1], ele[0]])
        return output

    def get20LeastFrequentWords(self, mostFreq):
        out = []
        for ele in self.frequenceWords:
            if len(out) == mostFreq:
                break
            if ele[0] == -1:
                out.append(ele)
        return self.reformatOutput(out)

    def splitByChapter(self, file):
        text = open(file, 'r')
        currLine = 1
        texts = ''
        chapter = []
        soLama = {
            "I": 1,
            "II": 2,
            "III": 3,
            "IV": 4,
            "V": 5,
            "VI": 6,
            "VII": 7,
            "VIII": 8,
            "IX": 9,
            "X": 10
        }
        while True:
            line = text.readline()
            # If no line then break
            if not line:
                break
            texts += line
        return texts
            # if 'CHAPTER I.' in line:
            #     print (currLine)
            # currLine += 1

    def getFrequencyOfWord(self, word):
        return

    def getChapterQuoteAppears(self, quote):
        return

    def generateSentence(self, oldSentence):
        return

    def getAutocompleteSentence(self, startOfSentence):
        return

    def findClosestMatchingQuote(self, str):
        return


# DRIVER
if __name__ == "__main__":
    # Initilize intial value
    # text = "frankenstein.txt"
    text = 'test.txt'
    common = 'commonUS.txt'
    filterVal = 100
    mostFreq = 20
    word = 'promise'

    # Instantiated
    analysis = Frankenstein(text)

    # Number of words in the text file
    print ("Total Words: ", analysis.getTotalNumberOfWord(text))

    # Number total of unique words
    print ("Total Unique Words: ", analysis.getTotalUniqueWords())

    # Most 20 frequent words
    print ("Most 20 Frequency Words: ", analysis.get20MostFrequentWords(mostFreq))

    # Most 20 interesting frequent words
    print ("Most 20 Interesting Frequence Words: ", analysis.get20MostInterestingFrequentWords(common, filterVal, mostFreq))

    # Least 20 Frequence Words
    print ("Least 20 Frequence Words: ", analysis.get20LeastFrequentWords(mostFreq))

    # Get Frequence Of Word in each chapter
    print ("Frequence Words Chapters: ", analysis.splitByChapter(text))