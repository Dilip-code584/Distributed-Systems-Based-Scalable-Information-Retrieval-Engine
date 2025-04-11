# Indexer for building inverted index using TF-IDF and BM25
import os, math, json
from collections import defaultdict
from utils.tokenizer import tokenize

def build_index(doc_dir="data/raw_html"):
    index = defaultdict(list)
    doc_freq = defaultdict(int)
    doc_lengths = {}

    for file in os.listdir(doc_dir):
        with open(os.path.join(doc_dir, file), encoding="utf-8") as f:
            text = f.read()
            tokens = tokenize(text)
            tf = defaultdict(int)
            for token in tokens:
                tf[token] += 1
            doc_id = file
            doc_lengths[doc_id] = len(tokens)
            for token, freq in tf.items():
                index[token].append((doc_id, freq))
                doc_freq[token] += 1

    return index, doc_freq, doc_lengths
