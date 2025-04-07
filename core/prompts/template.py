prompt_contextual = '''
You will be provided with the textual content of a web page (including its title, meta description, and main content). Your task is to analyze the content and extract structured information for contextual advertising.

Your response must include the following:

1. **Category**: Identify the main topic of the page, ideally following a structured format (e.g., "Sports > Running", "Finance > Personal Loans").
2. **Sentiment**: Determine the overall tone of the content (Positive, Neutral, or Negative).
3. **Keywords**: List 3 to 7 key terms or named entities that represent the main themes or subjects in the content.
4. **Summary**: Provide a 1-2 sentence summary of the page in natural language.

Instructions:

1. Focus only on the page content provided. Avoid assumptions or external data.
2. Use clear and concise language.
3. Your analysis must be suitable for use in contextual ad targeting systems.
4. Return the result strictly in **JSON format** using the structure provided.
5. Do not include any extra commentary, headers, or explanation outside the JSON.

{page_text}

{format_instructions}
'''
