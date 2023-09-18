import streamlit as st
import folium
from streamlit_folium import folium_static
import requests
import random  

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You need to log in to access this page!")
    st.stop()

st.title('Mental Health Specialists')

# Your Google API Key here, we removed for privacy
API_KEY = " "

# Geocode the location entered by user using Google Maps Geocoding API
def get_lat_lon_from_location(location):
    endpoint_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={API_KEY}"
    response = requests.get(endpoint_url).json()
    if response['status'] == 'OK':
        lat = response['results'][0]['geometry']['location']['lat']
        lon = response['results'][0]['geometry']['location']['lng']
        return lat, lon
    else:
        st.error("Unable to geocode the entered location. Please try a different one.")
        return 37.76, -122.42  # Default coordinates

# Function to get phone details
def get_place_details(place_id):
    endpoint_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=formatted_phone_number&key={API_KEY}"
    response = requests.get(endpoint_url).json()
    if response.get("status") == "OK":
        details = response.get("result", {})
        return details.get("formatted_phone_number")  # gets phone number
    else:
        return None

# Mock function to get availability from your appointment system
def get_specialist_availability(specialist_id):
    return random.choice([True, False])  



# Pull data from Google Places API
def get_specialists_from_google_places(lat, lon, keyword="mental health specialist"):
    endpoint_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lon}&radius=5000&keyword={keyword}&key={API_KEY}"
    response = requests.get(endpoint_url).json()
    results = response.get('results', [])
    
    specialists = []
    for result in results:
        phone_number = get_place_details(result.get("place_id"))
        availability = get_specialist_availability(result.get("place_id"))  # Mocked availability
        specialists.append({
            "lat": result['geometry']['location']['lat'],
            "lon": result['geometry']['location']['lng'],
            "name": result.get('name', 'Unknown Name'),
            "address": result.get('vicinity', 'Unknown Address'),
            "phone": phone_number or "Not available",
            "type": result.get("types", ["Unknown"])[0],
            "rating": result.get("rating", 0),
            "open_now": result.get("opening_hours", {}).get("open_now", False),
            "available": availability  # Add availability to specialist data
        })
    return specialists


# User Input
location = st.text_input("Enter a location:")
specialization_type = st.selectbox("Type of Specialization", ["mental_health", "psychiatrist", "therapist", "counselor"], index=0)  
min_rating = st.slider("Minimum Rating", 0.0, 5.0, 3.0, 0.1)
max_distance = st.slider("Maximum Distance (in meters)", 100, 50000, 5000)
only_open = st.checkbox("Show only currently open specialists")

# Geocode user location or use default
if location:
    lat, lon = get_lat_lon_from_location(location)
else:
    lat, lon = 37.76, -122.42

# Fetch and filter specialists
specialists = get_specialists_from_google_places(lat, lon, keyword=specialization_type)
filtered_specialists = [
    s for s in specialists if s["rating"] >= min_rating
    and (only_open == False or s["open_now"] == True) 
    
]

# Map creation and display
map_width, map_height = 1400, 800 
m = folium.Map(location=[lat, lon], zoom_start=10, tiles="http://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}", attr="google")

for specialist in filtered_specialists:
    availability_status = "Available" if specialist["available"] else "Not Available"
    booking_link = "#dummy_booking_link"  # Replace with actual link
    folium.Marker(
        location=[specialist["lat"], specialist["lon"]],
        popup=f"Name: {specialist['name']}<br>Phone: {specialist['phone']}<br>Address: {specialist['address']}<br>Availability: {availability_status}<br><a href='{booking_link}'>Book Now</a>",
    ).add_to(m)

folium_static(m, width=map_width, height=map_height)
