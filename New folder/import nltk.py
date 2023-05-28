import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def calculate_similarity(text1, text2):
    # Tokenize the texts
    tokens1 = word_tokenize(text1)
    tokens2 = word_tokenize(text2)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens1 = [word for word in tokens1 if word.lower() not in stop_words]
    filtered_tokens2 = [word for word in tokens2 if word.lower() not in stop_words]

    # Calculate the similarity using the Jaccard similarity coefficient
    set1 = set(filtered_tokens1)
    set2 = set(filtered_tokens2)
    similarity = len(set1.intersection(set2)) / len(set1.union(set2))

    return similarity

def check_plagiarism(text1, text2, threshold=0.5):
    similarity = calculate_similarity(text1, text2)
    if similarity >= threshold:
        print("Plagiarism detected!")
        print(f"Similarity: {similarity}")
    else:
        print("No plagiarism detected.")
        print(f"Similarity: {similarity}")

# Example usage
text1 = "This is the original text."
text2 = "This is some copied text."
check_plagiarism(text1, text2)
