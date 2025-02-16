# Google Maps API

## Maps Static

https://developers.google.com/maps/documentation/maps-static/start

```bash
runme(){
    local object_name=static-image-api-$(@@timestamp)

    local zoom
    for zoom in {1..19}; do
        @gmaps get_static_image - \
            $object_name \
            --lat $ROOFAI_TEST_GOOGLE_MAPS_LAT \
            --lon $ROOFAI_TEST_GOOGLE_MAPS_LON \
            --filename $(printf "%03d.png" $zoom) \
            --zoom $zoom
    done

    local scale
    for scale in 1 2 4; do
        @gif ~download,~upload \
            $object_name \
            --frame_duration 1000 \
            --scale $scale
    done

    @upload - $object_name

    @assets publish \
        extensions=gif+png,push \
        $object_name
}

runme
```

![image](https://github.com/kamangir/assets/blob/main/static-image-api-2025-02-15-wnfsd9/static-image-api-2025-02-15-wnfsd9-2X.gif?raw=true)

## Geocoding

https://developers.google.com/maps/documentation/geocoding/start

```python
from roofai.google_maps.api.geocoding import geocode

success, lat, lon, metadata = geocode(address="Vancouver Art Gallery", verbose=True)
assert success
```

> 🏛️  roofai.roofai.google_maps.api.geocoding.geocode(Vancouver Art Gallery): lat:49.282961, lon:-123.120471

<details>
<summary>metadata</summary>

```json
{'results': [{'address_components': [{'long_name': '750',
                                      'short_name': '750',
                                      'types': ['street_number']},
                                     {'long_name': 'Hornby Street',
                                      'short_name': 'Hornby St',
                                      'types': ['route']},
                                     {'long_name': 'Central Vancouver',
                                      'short_name': 'Central Vancouver',
                                      'types': ['neighborhood', 'political']},
                                     {'long_name': 'Vancouver',
                                      'short_name': 'Vancouver',
                                      'types': ['locality', 'political']},
                                     {'long_name': 'Metro Vancouver',
                                      'short_name': 'Metro Vancouver',
                                      'types': ['administrative_area_level_2',
                                                'political']},
                                     {'long_name': 'British Columbia',
                                      'short_name': 'BC',
                                      'types': ['administrative_area_level_1',
                                                'political']},
                                     {'long_name': 'Canada',
                                      'short_name': 'CA',
                                      'types': ['country', 'political']},
                                     {'long_name': 'V6Z 2H7',
                                      'short_name': 'V6Z 2H7',
                                      'types': ['postal_code']}],
              'formatted_address': '750 Hornby St, Vancouver, BC V6Z 2H7, '
                                   'Canada',
              'geometry': {'location': {'lat': 49.2829607, 'lng': -123.1204715},
                           'location_type': 'ROOFTOP',
                           'viewport': {'northeast': {'lat': 49.28409063029149,
                                                      'lng': -123.1195870697085},
                                        'southwest': {'lat': 49.2813926697085,
                                                      'lng': -123.1222850302915}}},
              'navigation_points': [{'location': {'latitude': 49.2824154,
                                                  'longitude': -123.1213573}},
                                    {'location': {'latitude': 49.28307419999999,
                                                  'longitude': -123.1210837}}],
              'place_id': 'ChIJwXz9f39xhlQRT3qxXAPDlbU',
              'plus_code': {'compound_code': '7VMH+5R Vancouver, BC, Canada',
                            'global_code': '84XR7VMH+5R'},
              'types': ['art_gallery',
                        'establishment',
                        'museum',
                        'point_of_interest',
                        'tourist_attraction']}],
 'status': 'OK'}
```

</details>
