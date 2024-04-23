import requests

def fetch_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("Failed to fetch the website.")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

def main():
    url = input("Enter the website URL: ")
    website_data = fetch_website(url)
    if website_data:
        # Process the fetched website data here
        with open("web_data.txt",'w') as file:
            file.write(website_data)
            print("web site code successfully extracted and saved in wed_data.txt")

