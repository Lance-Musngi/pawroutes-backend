from django.http import JsonResponse

def home_api(request):
    """
    A simple API endpoint to check if backend is working.
    """
    return JsonResponse({"message": "Backend API is running!"})
