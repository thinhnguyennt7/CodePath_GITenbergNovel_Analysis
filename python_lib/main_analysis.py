from heapq import heappush, heappop
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
            print ("List word")
            print (self.wordMap)
            print ("################")

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
        # Remove new line character
        sentence = sentence.replace('\n', '')
        for char in sentence:
            if char == ' ' and temp != '':
                wordList.append(temp)
                temp = ''
            else:
                temp += char
        if temp and temp != '\n':
            wordList.append(temp)
        return wordList

    def get20MostFrequentWords(self):
        mostFreq = 20
        arr = []
        output = []
        for key in self.wordMap:
            # Push to arr using min heap
            # heappush(arr, [-self.wordMap[key], key])
            heappush(self.frequenceWords, [-self.wordMap[key], key])
        out = [heappop(self.frequenceWords) for _ in range(mostFreq)]
        # Reformat the output
        for i in out:
            i[0] = i[0]*(-1) # Change to positive value
            output.append([i[1], i[0]])
        return output

    def get20MostInterestingFrequentWords(self, textFile, filterVal):
        mostFreq = 20
        commonList = []
        values = []
        commandText = open(textFile, 'r')
        while True:
            line = commandText.readline().replace('\n', '')
            if not line:
                break
            if len(commonList) == filterVal:
                break
            commonList.append(line)

        for ele in self.frequenceWords:
            if (ele[1] not in commonList):
                values.append(ele)

        return values


    def get20LeastFrequentWords(self):
        return

    def getFrequencyOfWord(self):
        return

    def getChapterQuoteAppears(self, quote):
        return

    def generateSentence(self, oldSentence):
        return

    def getAutocompleteSentence(self, startOfSentence):
        return

    def findClosestMatchingQuote(self, str):
        return

# Driver
if __name__ == "__main__":
    # Initilize intial value
    # text = "frankenstein.txt"
    text = 'test.txt'
    common = 'commonUS.txt'
    filterVal = 100

    # Instantiated
    analysis = Frankenstein(text)

    # Number of words in the text file
    print ("Total Words: ", analysis.getTotalNumberOfWord(text))

    # Number total of unique words
    print ("Total Unique Words: ", analysis.getTotalUniqueWords())

    # Most 20 frequent words
    print ("Most 20 Frequency Words: ", analysis.get20MostFrequentWords())

    # Most 20 interesting frequent words
    print ("Most 20 Interesting Frequence Words: ", analysis.get20MostInterestingFrequentWords(common, filterVal))