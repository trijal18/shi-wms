from owslib.wms import WebMapService

def wms_images(url):
    i = 0
    wms = WebMapService(url, version='1.3.0')
    layers = list(wms.contents)
    for layer in layers:
            try:
                img = wms.getmap(
                            layers=[layer],
                            srs='EPSG:4326',
                            bbox=wms[layer].boundingBoxWGS84,
                            size=(500, 500),
                            format='image/jpeg',
                            transparent=True
                )
                
                img_link = f'images/img{i}.jpg'
                with open(img_link, 'wb') as out:
                    out.write(img.read())
                
                i += 1

            except Exception as e:
                print(f"Error with layer '{layer}': {e}")
    
if __name__=="__main__":            
    wms_link="https://map.bgs.ac.uk/arcgis/services/GeoIndex_Onshore/geophysics_midlands_hires/MapServer/WmsServer?service=WMS&version=1.3.0&request=GetCapabilities&_ga=2.166723898.508089590.1725200503-887682611.1725200503"
    wms_images(wms_link)
