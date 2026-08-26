import os
from tavily import TavilyClient
from agents import function_tool  # type: ignore[import-untyped]

# Tavily Client
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@function_tool
def web_search(query: str) -> str:
    """Etsii ajankohtaista ja reaaliaikaista tietoa netistä Tavilylla."""
    print(f"--- [Meeting Prep] Suoritetaan verkkohaku: {query} ---")
    try:
        response = tavily.search(query=query, search_depth="advanced", max_results=5)
        
        combined_results = ""
        for i, r in enumerate(response.get('results', []), 1):
            combined_results += f"LÄHDE {i}:\nOtsikko: {r.get('title', '')}\nLinkki: {r.get('url', '')}\nSisältö: {r.get('content', '')}\n\n"
        
        print(f"--- [Meeting Prep] Tavily löysi {len(response.get('results', []))} lähdettä ---")
        return combined_results if combined_results else "Ei suoria hakutuloksia löytynyt."
    except Exception as e:
        print(f"[Meeting Prep] Tavily-virhe: {e}")
        return f"Hakua ei voitu suorittaa: {e}"
