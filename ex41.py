import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# dictionary
PHRASES = {
    "class %%%(%%%):":
     "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
     "class has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
     "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
     "Set *** to an instance of class %%%.",
    "***.***(@@@)":
     "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
     "From *** get the *** attirbute set it to '***'."
}

# do they want to drill phrases first
#for doing the inverse
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())
# snippet contains the key of PHRASES (snippets = PHRASES.keys())
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    #print class_names
    #for w in random.sample(WORDS, snippet.count("%%%")):
    #    class_names = [w.capitalize()]
    other_names = random.sample(WORDS, snippet.count("***"))
    #print other_names
    results = []
    param_names = []

    # check if @@@ exists; if exists = 1 , not = 0
    for i in range(0, snippet.count("@@@")):
        #print i
    #if snippet.count("@@@") == 1:
        param_count = random.randint(1,3)
        param_names.append(','.join(random.sample(WORDS, param_count)))
    #print param_names

    for sentence in snippet, phrase:
        result = sentence[:]
        #print result
        #fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        #fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        #fake para names
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
    return results
    #print results

# keep going on until they hit Ctrl-C
try:
    while True:
        snippets = PHRASES.keys()
        #print snippets
        random.shuffle(snippets)
        #print snippets

        for snippet in snippets:
            #choose a key
            phrase = PHRASES[snippet]
            #print snippet.count("%%%") # class_names
            #print snippet.count("***") # other_names
            #print snippet.count("@@@") # param_names = 0 or 1
            question, answer = convert (snippet, phrase)
            if PHRASE_FIRST:
                question, answer =answer, question

            print question

            raw_input("> ")
            print "ANSWER: %s\n\n" % answer
            #print sys.argv, len(sys.argv)

except EOFError:
    print "\nBye"
