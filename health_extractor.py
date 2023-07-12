import nltk
import re

def extract_health_sentences(file_path):
    # Download the 'punkt' resource for sentence tokenization
    nltk.download('punkt')

    # Read the text file
    with open(file_path, "r") as file:
        content = file.read()

    # Split the text into sentences
    sentences = nltk.sent_tokenize(content)

    # Filter relevant sentences and clean them up
    health_sentences = []
    keywords = ["health", "medical", "wellness", "disease", "treatment", "vitamins", "nutrition", "exercise"]  # Add more relevant keywords as needed

    for sentence in sentences:
        # Remove trailing spaces and strange characters
        cleaned_sentence = sentence.strip()

        # Remove blank lines
        if cleaned_sentence:
            # Remove specific patterns like "----------------------------------------"
            if not re.match(r'^[-—]+$', cleaned_sentence):
                # Check for health-related keywords
                for keyword in keywords:
                    if re.search(r"\b" + re.escape(keyword) + r"\b", cleaned_sentence, re.IGNORECASE):
                        health_sentences.append(cleaned_sentence)
                        break

    return health_sentences

# Example usage
file_path = "health-news.md"  # Replace with the path to your input text file
health_sentences = extract_health_sentences(file_path)

# Save the relevant sentences to a text file
output_file = "output.md"  # Replace with the desired output file path

with open(output_file, "w") as file:
    for sentence in health_sentences:
        file.write(f"- {sentence} \n\n")
