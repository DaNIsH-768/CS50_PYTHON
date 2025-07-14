import requests
from PIL import Image
from io import BytesIO
import json

Artist_API = "https://api.artic.edu/api/v1/artworks/search?q="
Image_API = "https://www.artic.edu/iiif/2/#/full/800,600/0/default.jpg"

def main():
    artist = input("Artist: ")

    try:
        artist_data = fetch_data(artist)
    except requests.HTTPError:
        print("Error fetching `Artist` data.")
    else:
        try:
            data = fetch_image_data(artist_data)
        except requests.HTTPError:
            print("Error fetching `Image` data.")
        else:
            images = []

            for image_id in data:
                try:
                    images.append(Image.open(fetch_image(image_id)))
                except requests.HTTPError:
                    print(f"Error fetching image: {image_id}")
        
        

# Save the images as an animated GIF
            images[0].save(
                f"{artist}.gif",
                append_images=images[1:],
                duration=3000,  # duration of each frame in milliseconds
                loop=0,  # loop forever
            )

def fetch_image_data(artist_data : list) -> list:
    """
    Fetch image_id for the images of the artist requested

    @accepts: artist_data => [{data}, {data}, {data}]
    @returns: list containing image id's => ['id', 'id', 'id']
    """
    data = []

    for image in artist_data:
        try:
            response = requests.get(image['api_link']).text
        except requests.HTTPError:
            print("Error fetching image data.")
        else:
            parsed = json.loads(response)
            data.append(parsed['data']['image_id'])
        

    return data

def fetch_data(artist : str) -> list:
    '''
    Fetches 3 painting data for the requested artist

    @accepts -> artist name
    @returns -> list of 3 dicts where each dict is info about 1 artwork
    '''
    URL = f"{Artist_API}{artist}&limit=3"
    
    response = requests.get(URL)
    data = response.json()

    return data['data']


def fetch_image(id : str) -> BytesIO:
    '''
    Fetches image data based on the id given

    @accepts : Id of the image
    @returns : Bytes containing the image data
    '''
    first, last = Image_API.split("#")
    URL = f"{first}{id}{last}"

    response = requests.get(URL)
    return BytesIO(response.content)



if __name__ == "__main__":
    main()
