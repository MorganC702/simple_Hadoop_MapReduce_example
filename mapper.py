#!/usr/bin/env python
import sys
import re
import nltk
from nltk.corpus import stopwords

nltk.data.path.append("/root/simple_Hadoop_MapReduce_example/nltk_data")
stop_words = set(stopwords.words("english"))

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    words = re.findall(r'\w+', line)
    for word in words:
        word = word.lower()
        if word and word not in stop_words and word.isalpha():
            print(f"{word}\t1")
