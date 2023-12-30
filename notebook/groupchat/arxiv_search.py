# filename: arxiv_search.py
import arxiv

# Search for papers on Llama
result = arxiv.query(query='Llama', max_results=1)

# Print the title and link of the first result
print("Title:", result[0]['title'])
print("Link:", result[0]['pdf_url'])