from typing import List
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from core.dataformat.output_format import *
from core.prompts.template import *
from dotenv import load_dotenv
import os
import time

load_dotenv('.env.secrets')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')


class PydenAnalytics:

    def __init__(self) -> None:
        self.llm = ChatGroq(api_key=GROQ_API_KEY,
            model= "llama-3.2-1b-preview",#"Llama3-70b-8192", llama-3.3-70b-specdec , llama-3.3-70b-versatile
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=3,
        )
        
        self.pydantic_parser_other = PydanticOutputParser(pydantic_object=PageContextualTags)
        self.prompt_other = ChatPromptTemplate.from_template(template=prompt_contextual)
        self.format_instructions_other = self.pydantic_parser_other.get_format_instructions()
    
    def genrate_response(self , dialogue):
        #print(dialogue)
        """
        Asynchronously generates a structured response from the LLM based on the input dialogue.

        Args:
            dailogue (str): The input dialogue or query for which a response is needed.

        Returns:
            res (BrandInfo): The structured response parsed into a Pydantic object.
        """
        
        messages = self.prompt_other.format_messages(page_text = f'{dialogue}' , format_instructions=self.format_instructions_other)
        output = self.llm.invoke(messages)
        res = self.pydantic_parser_other.parse(output.content)
        return res
    
if __name__ == '__main__':
    py = PydenAnalytics()
    input = "user_answer hello my answer is india , correct_answer india"
    start = time.time()
    res = py.genrate_response(input , '')
    end = time.time()
    print('total_time' , end - start)
    print(res.is_corr)
    print(res.response)
    print('-'*10)