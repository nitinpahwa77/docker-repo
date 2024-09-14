import datetime
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Extract the name parameter from the query string
    name = req.params.get('name')
    
    # Get the current date and time in UTC
    current_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

    # Create the response message
    if name:
        message = f"Hello, {name}! The current UTC time is {current_time}."
    else:
        message = f"Hello! The current UTC time is {current_time}. Provide a name for a personalized message."

    # Return the response as an HTTP response
    return func.HttpResponse(message, status_code=200)
