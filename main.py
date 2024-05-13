import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from patterns import patterns 

nltk.download('punkt')
nltk.download('stopwords')

def process_input(input_text):
    tokens = word_tokenize(input_text)
    
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    return filtered_tokens

def handle_command(command):
    for pattern, responses in patterns.items():
        if re.search(pattern, command, re.IGNORECASE):
            return responses[0] 
    return "Sorry, I don't understand that."

def main():
    print("Hi I am Maya!")
    
    while True:
        user_input = input("You: ")
        response = handle_command(user_input)
        print("Maya:", response)
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
