import wikipedia

def search_wikipedia(request):
    try:
        query = request.replace("search on wikipedia", "").replace("wikipedia", "").strip()
        response = wikipedia.summary(query, sentences=2)
    except Exception as e:
        response = f"An unexpected error occurred: {e}"
    return response
