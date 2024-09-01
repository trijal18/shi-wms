from wms_images import wms_images
from combine import create_video

wms_url="https://firms.modaps.eosdis.nasa.gov/mapserver/wms/fires/YourMapKey/fires_viirs_24/?REQUEST=GetMap&WIDTH=1024&HEIGHT=512&BBOX=-180,-90,180,90"
wms_images(wms_url)
create_video('images', 'output_video.mp4', 1)