from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator

class PageContextualTags(BaseModel):
    category: str = Field(..., description="The main topic or category of the page, ideally following IAB taxonomy, e.g., 'Sports > Running'")
    sentiment: str = Field(..., description="Overall sentiment of the content: Positive, Neutral, or Negative")
    keywords: list[str] = Field(..., description="Important keywords or named entities from the page content")
    summary: str = Field(..., description="A one-paragraph summary of the page content")


if __name__ == '__main__':
    print('done')