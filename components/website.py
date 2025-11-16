import webbrowser

def website(request):
    try:
        query = request.replace("open", "").replace("website", "").replace(" ", "").strip()
        webbrowser.open("https://www." + query + ".com")
        response = f"Opening {query} website"
    except Exception as e:
        response = f"An unexpected error occurred: {e}"
    return response
