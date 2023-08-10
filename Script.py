import pickle
import os
import shutil
import PyPDF2
import nltk
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import argparse





def main(input_dir):
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

    

    model_filename = 'svm_model.pkl'
    # Loading trained model
    with open(model_filename, 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    # Loading vectorizer for processing input    
    with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
        loaded_vectorizer = pickle.load(vectorizer_file)
    
    # Data pipeline for input preprocessing
    def preprocess_text(text):
        # Lowercase the text
        text = text.lower()

        # Removing non-alphanumeric characters and extra spaces
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

        # Tokenizing the text
        tokens = word_tokenize(text)

        # Removing stopwords
        tokens = [word for word in tokens if word not in stop_words]

        # Joining tokens back to form a clean text string
        clean_text = ' '.join(tokens)

        return clean_text
    
    # Reading pdf files from directory
    for filename in os.listdir(input_dir):
        # Reading pdf
        if filename.endswith('.pdf'):
            pdf_reader = PyPDF2.PdfReader(f'{input_dir}{filename}')
        text = ''
        # Converting pdf's content to string
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
        
        # Preprocessing recived text from the pdf file
        processed_txt = preprocess_text(text)

        # Vectorizing the preprocessed text
        resume_vector = loaded_vectorizer.transform([processed_txt])


        # Predicting the category using the trained model
        predicted_category = loaded_model.predict(resume_vector)[0]
   
        # Creating the output category folder if it doesn't exist
        output_folder = os.path.join('D:/python/ML PROJECT/Resume_Categorizer/OUTPUT', predicted_category)
        os.makedirs(output_folder, exist_ok=True)
        
        # Moveing the resume to the output folder
        shutil.move(os.path.join(input_dir, filename), os.path.join(output_folder, filename))
         
        # Creating a CSV file and appending filename and category of the CV
        with open('categorized_resumes.csv', 'a') as csv_file:
            csv_file.write(f'{filename},{predicted_category}\n') 





if __name__ == '__main__':
    # Creating the parser
    parser = argparse.ArgumentParser(
        description="path of the CV's"
    )
    # Adding an argument
    parser.add_argument('path', help="enter the path", type=str)
    # Parsing the argument
    args = parser.parse_args()
    
    # Sending the given path to main 
    main(args.path)