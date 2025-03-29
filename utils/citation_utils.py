from langchain_openai import ChatOpenAI

def format_citation(author: str, title: str, year: str, publisher: str) -> str:
    """
    Format citation details into APA format using GPT-4.
    """
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    prompt = (
        f"Create a properly formatted citation for the following details:\n\n"
        f"Author: {author}\n"
        f"Book Title: {title}\n"
        f"Publication Year: {year}\n"
        f"Publisher: {publisher}\n\n"
        f"Provide the citation in APA format."
    )

    return llm.predict(prompt)
