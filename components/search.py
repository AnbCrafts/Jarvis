import webbrowser

def search(request):
    try:
        query = request.replace("search on google", "").strip()
        webbrowser.open("https://www.google.com/search?q=" + query)
        response = f"Searching on Google {query}"
    except Exception as e:
        response = f"An unexpected error occurred: {e}"
    return response
