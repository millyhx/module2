# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:57:38 2019

@author: milly
"""

import requests


def postcode_locator():
    postcode_input = input("Enter a postcode: ")
    postcode = postcode_input
    
    
    endpoint = 'https://api.postcodes.io/postcodes/'
    response = requests.get(endpoint + postcode)
    data = response.json()
    
    country = data['result']['country']
    region = data['result']['region']
    admin_district = data['result']['admin_district']
    parliamentary_constituency = data['result']['parliamentary_constituency']
    parish = data['result']['parish']
    latitude = data['result']['latitude']
    longitude = data['result']['longitude'] 
    
    
    
    print("Country: {}".format(country))
    print("Region: {}".format(region))
    print("District: {}".format(admin_district))
    print("Town: {}".format(parliamentary_constituency))
    print("Parish: {}".format(parish))
    print("Latitude: {}".format(latitude))
    print("Longitude: {}".format(longitude))
    

    
    
postcode_locator()

"""
{"status":200,"result":{"postcode":"TA4 1AY","quality":1,"eastings":315334,"northings":125768,"country":"England","nhs_ha":"South West","longitude":-3.208599,"latitude":51.025023,"european_electoral_region":"South West","primary_care_trust":"Somerset","region":"South West","lsoa":"Taunton Deane 013A","msoa":"Taunton Deane 013","incode":"1AY","outcode":"TA4","parliamentary_constituency":"Taunton Deane","admin_district":"Taunton Deane","parish":"Oake","admin_county":"Somerset","admin_ward":"Bradford-on-Tone","ced":"Upper Tone","ccg":"NHS Somerset","nuts":"Somerset","codes":{"admin_district":"E07000190","admin_county":"E10000027","admin_ward":"E05006861","parish":"E04008805","parliamentary_constituency":"E14000988","ccg":"E38000150","ced":"E58001328","nuts":"UKK23"}}}

"""