import hashlib

def generate_fingerprint(request):
    # Generate device fingerprint based on request information
    fingerprint = ""

    # Extract relevant information from the request object
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    ip_address = request.META.get('REMOTE_ADDR', '')
    accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')
    screen_resolution = request.META.get('HTTP_RESOLUTION', '')  # Assuming you have a custom header for screen resolution
    timezone = request.META.get('TIMEZONE', '')  # Assuming you have a custom header for timezone
    browser_plugins = request.META.get('BROWSER_PLUGINS', '')  # Assuming you have a custom header for browser plugins
    device_type = request.META.get('DEVICE_TYPE', '')  # Assuming you have a custom header for device type
    platform = request.META.get('PLATFORM', '')  # Assuming you have a custom header for platform
    operating_system = request.META.get('HTTP_USER_AGENT', '').split('(')[1].split(';')[0].strip()  # Extracting operating system from user agent
    # Add more parameters as needed.
    # Create a fingerprint using the extracted information
    fingerprint = hashlib.md5(f"{user_agent}{ip_address}{accept_language}{screen_resolution}{timezone}{browser_plugins}{device_type}{platform}{operating_system}".encode()).hexdigest()
    return fingerprint

