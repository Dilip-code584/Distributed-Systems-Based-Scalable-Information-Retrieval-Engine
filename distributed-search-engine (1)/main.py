# Main coordinator script
from crawler.crawler import crawl
from indexer.indexer import build_index
from ranker.ranker import compute_bm25
from utils.tokenizer import tokenize

urls = ["http://example.com", "https://example.org"]
crawl(urls)

index, doc_freq, doc_lengths = build_index()
avg_len = sum(doc_lengths.values()) / len(doc_lengths)
total_docs = len(doc_lengths)

query = "example search"
query_tokens = tokenize(query)
results = compute_bm25(query_tokens, index, doc_freq, doc_lengths, avg_len, total_docs)

print("Top results:")
for doc, score in results[:5]:
    print(doc, score)
