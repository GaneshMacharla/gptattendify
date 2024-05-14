# delete_expired_objects.py

# Import necessary modules
from datetime import datetime
from .models import UserDetails  # Import your UserDetails model

# Define the function to delete expired objects
def delete_expired_objects():
    # Perform logic to delete expired objects from the database
    expired_objects = UserDetails.objects.filter(expiry_date=datetime.now())
    expired_objects.delete()
    print("Expired objects deleted successfully")

# Call the function to delete expired objects
delete_expired_objects()
    