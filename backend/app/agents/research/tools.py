import os
from tavily import TavilyClient
from agents import function_tool

# Tavily Client
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@function_tool
def web_search(query: str) -> str:
    """ Etsii tietoa netistä Tavilylla (AI-optimoitu haku). """
    print(f"--- Suoritetaan ammattilais-haku: {query} ---")
    try:
        # Hakee ja tiivistää sisällön automaattisesti
        response = tavily.search(query=query, search_depth="advanced", max_results=5)
        
        combined_results = ""
        for i, r in enumerate(response['results'], 1):
            combined_results += f"TULOS {i}:\nOtsikko: {r['title']}\nLinkki: {r['url']}\nSisältö: {r['content']}\n\n"
        
        print(f"--- Tavily löysi {len(response['results'])} laadukasta lähdettä ---")
        return combined_results
    except Exception as e:
        print(f"Tavily-virhe: {e}")
        return f"Hakua ei voitu suorittaa: {e}"
