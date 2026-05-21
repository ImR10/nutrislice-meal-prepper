# class responsible for fetching Nutrislice API and cleaning items
import os
import requests
from dotenv import load_dotenv
from flask import request
from extensions import db
from models import CachedMenu
from datetime import date


class Nutrislice():
    ns = Nutrislice()

    def buildURI(self, meal_type):
        load_dotenv()

        school = os.getenv("SCHOOL")
        base_url = "api.nutrislice.com/menu/api/weeks/school/"
        dining_hall = "dining-hall-2"
        meals = meal_type
        year, month, day = 2026, 5, 20

        url = f"{school.lower()}.{base_url}{dining_hall}/menu-type/{meals[0]}/{year}/{month:02d}/{day:02d}/?format=json"

        return url

    def get_raw_menu(self, URI):
        data = requests.get(URI)
        return data


    def fetch_menu(self):
        meals = ["breakfast", "lunch", "dinner"]

        breakfast_URI = ns.buildURI(meals[0])
        lunch_URI = ns.buildURI(meals[1])
        dinner_URI = ns.buildURI(meals[2])

        breakfast_raw_data = ns.get_raw_menu(breakfast_URI)
        lunch_raw_data = ns.get_raw_menu(lunch_URI)
        dinner_raw_data = ns.get_raw_menu(dinner_URI)

        






        

    def clean_items(self):
        pass


if __name__ == "__main__":
    from nutrislice import Nutrislice
    ns = Nutrislice()
    print(ns.buildURI())