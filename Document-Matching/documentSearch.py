import numpy as np
import math

def getQueries():
    queriesList = []
    with open("queries.txt", "r") as queries:
        queriesList = queries.read().splitlines()
    return queriesList

def getDocuments():
    documentList = []
    with open("docs.txt", "r") as docs:
        documentList = docs.read().splitlines()
    return documentList

def buildDict():
    dictCount = 0
    dictionairy = []
    documents = open("docs.txt", "r")
    for document in documents:
        uniqueWords = []
        words = document.split()
        for w in words:
            #Only using the the unique words
            if w not in uniqueWords:
                uniqueWords.append(w)
        dictionairy.append(uniqueWords)
        dictCount += len(uniqueWords)
    return dictionairy

def buildIndex():
    invIndex = {}
    documents = {}
    dict = buildDict()
    for x in range(len(dict)):
        documents[x + 1] = dict[x]
    for num, doc in documents.items():
        for w in doc:
            if w not in invIndex.keys():
                invIndex[w] = [str(num)]
            else:
                invIndex[w].append(str(num))
    return invIndex

def calcAngle(x, y):
    x = np.array(x)
    y = np.array(y)
    normX = np.linalg.norm(x)
    normY = np.linalg.norm(y)
    #Calculating the angle
    cos_theta = np.dot(x, y) / (normX * normY)
    theta = math.degrees(math.acos(cos_theta))
    theta = round(theta, 5) #Rounding the result to 5dp
    return theta

def run():
    #Gathering all the variables from the functions
    docRelevanceValue = {}
    queryList = getQueries()
    invIndex = buildIndex()
    documentList = getDocuments()
    dictionairy = invIndex.keys()
    print("Words in dictionairy: " + str(len(invIndex)))
    for query in queryList:
        #Initialising variables only used within the query loop
        dictVector = {}
        docValues = {}
        allDocs = []
        relevantDocs = []
        print("Query: " + query)
        #Finding all the relevant documnets
        queryWords = query.split()
        for w in queryWords:
            for docNum in invIndex[w]:
                allDocs.append(docNum)
        for i in range(len(invIndex)):
            #If the document appears in both the query words
            if len(queryWords) == allDocs.count(str(i)):
                relevantDocs.append(str(i))
        print("Relevant documents: " + " ".join(relevantDocs))
        #Building the query vector
        queryFreq = {i : 0 for i in dictionairy}
        for w in queryWords:
            if w in queryFreq:
                queryFreq[w] += 1 #The frequency the words appear
        queryVector = list(queryFreq.values())
        #Building the document vector
        for docs in relevantDocs:
            wordFreq = {i : 0 for i in dictionairy}
            for w in documentList[int(docs)-1].split():
                if w in wordFreq:
                    wordFreq[w] += 1
            dictVector[docs] = list(wordFreq.values())
        for doc in relevantDocs:
            angle = calcAngle(queryVector, dictVector[str(doc)])
            docValues[doc] = angle
        #Ordering the dictionairy into a list of tuples for output
        docValues = sorted(docValues.items(), key = lambda kv:(kv[1], kv[0]))
        for doc in docValues:
            print(str(doc[0]) + " " + str(doc[1]))


run()
