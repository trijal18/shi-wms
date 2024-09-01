from modules.wms_images import wms_images
from modules.combine import create_video

def generate_video(url):
    wms_images(url)
    return create_video('images', 'output_video.mp4', 4)

if __name__=="__main__":
    wms_url="https://firms.modaps.eosdis.nasa.gov/mapserver/wms/fires/YourMapKey/fires_viirs_24/?REQUEST=GetMap&WIDTH=1024&HEIGHT=512&BBOX=-180,-90,180,90"
    wms_images(wms_url)
    create_video('images', 'output_video.mp4', 4)
