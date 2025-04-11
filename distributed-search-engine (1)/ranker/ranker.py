# BM25-based ranking of documents
import math

def compute_bm25(query_tokens, index, doc_freq, doc_lengths, avg_len, total_docs, k1=1.5, b=0.75):
    scores = {}
    for token in query_tokens:
        if token not in index:
            continue
        idf = math.log((total_docs - doc_freq[token] + 0.5) / (doc_freq[token] + 0.5) + 1)
        for doc_id, freq in index[token]:
            tf = freq
            len_d = doc_lengths[doc_id]
            score = idf * ((tf * (k1 + 1)) / (tf + k1 * (1 - b + b * len_d / avg_len)))
            scores[doc_id] = scores.get(doc_id, 0) + score
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
