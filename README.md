# 🔍 Distributed Search Engine with Scalable Ranking Algorithms

A scalable and fault-tolerant distributed search engine built using **Python**, **MapReduce-style architecture**, and **TCP/IP socket programming**, optimized for real-time web crawling, indexing, and retrieval with high efficiency.

## 🚀 Features

- **Parallel Crawling & Indexing**: Efficient Unix-based crawling pipelines powered by Python's multiprocessing.
- **Distributed Ranking Algorithms**: Implements scalable document ranking using **TF-IDF** and **BM25** models.
- **Fault Tolerance**: Node communication via **TCP/IP sockets** with recovery support.
- **Information Retrieval Optimized**: Achieved 45% improvement in search response and document relevance.
- **Unix/Linux Compatible**: Built and tested on Linux systems for optimal performance.

## 📦 Architecture Overview

- **Crawler**: Fetches and stores HTML pages concurrently.
- **Indexer**: Processes and tokenizes documents to build an inverted index.
- **Ranker**: Uses BM25 algorithm to rank results based on search queries.
- **Socket Layer**: Ensures communication between distributed components using TCP/IP.

## 🛠️ Tech Stack

- Python, BeautifulSoup, Requests
- Multiprocessing, Socket Programming
- UNIX/Linux Environments
- Information Retrieval: TF-IDF, BM25
- TCP/IP Networking

## 📁 Project Structure

