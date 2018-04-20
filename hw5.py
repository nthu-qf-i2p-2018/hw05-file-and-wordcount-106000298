from collections import Counter
import string
import csv
import pickle
import json


def main(filename):
    # read file into lines
    txtfile = open("i_have_a_dream.txt")
    lines = txtfile.readlines()

    # declare a word list
    all_words = []

    # extract all words from lines
    for line in lines:
        # split a line of text into a list words
        # "I have a dream." => ["I", "have", "a", "dream."]
        words = line.split()
        for word in words:
            # then, remove (strip) unwanted punctuations from every word
            # "dream." => "dream"
            word = word.strip().strip(string.punctuation)
            # check if word is not empty
            if word:
               word is not None
                # append the word to "all_words" list
               all_words.append(word)

    # compute word count from all_words
    counter = Counter(all_words)

    counter = counter.most_common()


    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...
    with open("wordcount.csv","w",newline="") as csv_file:
        # create a csv writer from a file object (or descriptor)
        writer = csv.writer(csv_file)
        # write table head
        writer.writerow(['word', 'count'])
        # write all (word, count) pair into the csv writer
        for word,count in counter:
             writer.writerow([word,count])
        #writer.writerrows(counter.most_common())


    # dump to a json file named "wordcount.json"
    f = open("wordcount.json","w")
    json.dump(counter,f)
    json.dump(counter,open("wordcount.json","w"))

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly
    pickle.dump(counter,open("wordcount.pkl","wb"))

if __name__ == '__main__':
    main("i_have_a_dream.txt")


