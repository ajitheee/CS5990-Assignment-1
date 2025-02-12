# -------------------------------------------------------------------------
# AUTHOR: Ajith Elumalai
# FILENAME: Similarity
# SPECIFICATION: description of the program
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy,
#pandas, or other sklearn modules.
#You have to work here only with standard dictionaries, lists, and arrays

# Importing some Python libraries
import csv

def tokenize(text):
    """Tokenize text by splitting on spaces."""
    return text.lower().split()

documents = []
doc_ids = []

file_path = 'cleaned_documents.csv'

try:
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        for row in reader:
            doc_ids.append(int(row[0]))  # Document ID
            documents.append(tokenize(row[1]))  # Tokenized text
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Ensure it is in the correct directory.")
    exit()

# Step 2: Build the document-term matrix
unique_words = set(word for doc in documents for word in doc)  # All unique words
unique_words = sorted(unique_words)  # Sort for consistency
word_index = {word: i for i, word in enumerate(unique_words)}  # Word to index mapping

#Building the document-term matrix by using binary encoding.
#You must identify each distinct word in the collection without applying any transformations, using
# the spaces as your character delimiter.
#--> add your Python code here

doc_term_matrix = []
for doc in documents:
    vector = [0] * len(unique_words)
    for word in doc:
        vector[word_index[word]] = 1  # Binary encoding
    doc_term_matrix.append(vector)

# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
# --> Add your Python code here
def sqrt(value):
    """Manual square root calculation using the Newton-Raphson method."""
    x = value
    y = (x + 1) / 2
    while abs(x - y) > 1e-10:
        x = y
        y = (x + value / x) / 2
    return x

def cosine_similarity(vec1, vec2):
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
    norm1 = sqrt(sum(v ** 2 for v in vec1))
    norm2 = sqrt(sum(v ** 2 for v in vec2))
    return dot_product / (norm1 * norm2) if norm1 and norm2 else 0

# Print the highest cosine similarity following the information below
# The most similar documents are document 10 and document 100 with cosine similarity = x
# --> Add your Python code here
max_similarity = 0
most_similar_docs = (None, None)

for i in range(len(doc_term_matrix)):
    for j in range(i + 1, len(doc_term_matrix)):
        sim = cosine_similarity(doc_term_matrix[i], doc_term_matrix[j])
        if sim > max_similarity:
            max_similarity = sim
            most_similar_docs = (doc_ids[i], doc_ids[j])

# Step 5: Print the result
print(f"The most similar documents are document {most_similar_docs[0]} and document {most_similar_docs[1]} with cosine similarity = {max_similarity:.4f}")
