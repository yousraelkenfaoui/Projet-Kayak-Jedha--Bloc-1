import os 
import logging
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import json

import pandas as pd

class BookingSpider(scrapy.Spider):
    name = "Booking"
    start_urls = ['https://www.booking.com']
    top_5_villes = ['Collioure', 'Aigues Mortes', 'Saintes Maries de la mer', 'Nimes', 'Avignon']

    # récupérer la page des hotels pour chaque ville :
    def start_requests(self):
        checkin_date = "2024-05-16"
        checkout_date = "2024-05-20"
        
        url_villes = 'https://www.booking.com/searchresults.fr.html?ss={}&checkin={}&checkout={}&group_adults=2&no_rooms=1&group_children=0&nflt=ht_id%3D204' 
    
        for ville in self.top_5_villes:
            url_ville = url_villes.format(ville,checkin_date,checkout_date)
            yield scrapy.Request(url_ville, callback=self.parse_hotels, meta={'Ville':ville, 'url_ville': url_ville})
    
    # Récupérer l'url des hotels de chaque ville :
    def parse_hotels(self, response):
        
        hotels = response.xpath("//h3[@class='aab71f8e4e']") 
       
        for hotel in hotels:
            nom_hotel = hotel.xpath(".//div[contains(@class, 'f6431b446c a15b38c233')]/text()").get()
            url_hotel = hotel.xpath(".//@href").get()
            yield response.follow(url_hotel, callback=self.parse_hotels_details, meta={'Ville': response.meta['Ville'], 'nom_hotel': nom_hotel, 'url_hotel': url_hotel})
    
        # Récupérer d'autres hotels qui n'aparaissent pas sur la première page :
        hotel_par_page = 25
        while hotel_par_page < 500:
            url_ville_page_suivante = response.meta['url_ville'] + f"&offset={hotel_par_page}"
            yield response.follow(url_ville_page_suivante, callback=self.parse_hotels, meta=response.meta)
            hotel_par_page += 25

    # Récupérer les informations de chaque hotel : 
    def parse_hotels_details(self, response):
         yield {
              'Ville':response.meta['Ville'],
              'nom_hotel': response.meta['nom_hotel'],
              'url_hotel': response.meta['url_hotel'],
              'GPS': response.xpath("//@data-atlas-latlng").get(),
              'score': response.xpath("//div[@class='c624d7469d eb03ae5461 dab7c5c6fa a937b09340 a3214e5942 d5fd510f01 dc7f26e57f']/div[1]/text()").get(),
              'voters':response.xpath("//div[@class='c624d7469d eb03ae5461 dab7c5c6fa a937b09340 a3214e5942 d5fd510f01 dc7f26e57f']/div[2]/div[2]/text()").get(),
              'description': Selector(response).css('div.hp_desc_main_content').xpath('string()').get().strip(),
              'address': response.xpath("//span[contains(@class, 'hp_address_subtitle')]/text()").get()

         }
         
filename = "scraping_booking.json"


process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        filename : {"format" : "json"}
    }
})

process.crawl(BookingSpider)
process.start()