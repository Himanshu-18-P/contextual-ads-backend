# extract data from url , save the vectore locally  with a uuid 
from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup
from langchain.schema import Document
import re



class GetData:

    def __init__(self):
        pass
    

    def preprocess_text(self, raw_text):
        """
        Preprocess raw HTML content by:
        - Removing HTML tags
        - Cleaning newlines and spaces
        - Removing repetitive patterns and broken tokens
        """
        # Step 1: Parse HTML
        soup = BeautifulSoup(raw_text, "html.parser")
        cleaned_text = soup.get_text(separator=" ")

        # Step 2: Fix broken words (like StorageSelect → Storage Select)
        cleaned_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', cleaned_text)

        # Step 3: Remove extra newlines and spaces
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

        # Step 4: Remove word-level repetitions (e.g., "Select RAM Select RAM Select RAM")
        cleaned_text = re.sub(r'\b(\w+)( \1\b){3,}', r'\1', cleaned_text)

        # Step 6: Clean double spaces again
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

        return cleaned_text


    

    def extract_data(self, page_url):
        try:
            # Load the web page content
            loader = WebBaseLoader(web_paths=[page_url])
            docs = []
            
            for doc in loader.load():
                # Preprocess the document content
                cleaned_content = self.preprocess_text(doc.page_content)
                doc.page_content = cleaned_content  # Replace the original content with the cleaned version
                docs.append(doc)

            return docs

        except Exception as e:
            print(f"Error while extracting data from {page_url}: {e}")
            return []
    

if __name__ == '__main__':
    print('done')
