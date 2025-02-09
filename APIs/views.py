from django.shortcuts import render
import requests

def get_client_ip(request):
    # Retrieve the client's IP address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    ip = '59.96.113.192'
    api_token = '4c4e0a58424fe1'  # Your IPInfo API token

    # IPInfo API request
    response = requests.get(f"https://ipinfo.io/{ip}?token={api_token}")

    if response.status_code == 200:
        location_data = response.json()
        city = location_data.get('city', 'Unknown City')
        region = location_data.get('region', 'Unknown Region')
        country = location_data.get('country', 'Unknown Country')
        loc = location_data.get('loc', 'Unknown Location')
        org = location_data.get('org', 'Unknown Organization')
        postal = location_data.get('postal', 'Unknown Postal Code')
        timezone = location_data.get('timezone', 'Unknown Timezone')
    else:
        city = region = country = loc = org = postal = timezone = "Unknown"

    context = {
        'ip': ip,
        'city': city,
        'region': region,
        'country': country,
        'loc': loc,
        'org': org,
        'postal': postal,
        'timezone': timezone,
    }
    return render(request, 'index.html', context)
