#create a dictionary  and take a input from the user and the return the meaning of the words

#1
word_meanings = {"apparent":"visible","catastrophic":"destructive","fete":"event","annoyed":"angry","pretend":"to show off"}

name  = input("enter word: ")
print(word_meanings[name])

#2
make_sentences = {"apparent":"This was quite apparent to be caught.",
                  "catastrophic":"The landslide that occured in Manali was a catastrophic event happened recently.",
                  "fete":"A fete was organised by the Jiwaji Club."}
name = input(" enter word for sentence: ")
print(make_sentences[name])