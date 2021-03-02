from google_play_scraper import reviews_all
from app_store_scraper import AppStore
from google_play_scraper import app
import csv

package_name = 'com.netcompany.smittestop_exposure_notification'


def play_store_scraper(package):
    results = reviews_all(package)

    # Creates or updates the CSV with this name
    with open(r'google_reviews.csv', 'w', newline='') as file:
        fieldnames = ['username', 'review', 'score']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        # Adds the fields to the CSV
        for x, item in enumerate(results):
            username = item['userName']
            score = item['score']
            review = item['content']

            try:
                print(f'{x}: {username} says: {review}')
                writer.writerow({'username': username, 'review': review, 'score': score})
            except:
                print('Failed to add entry XXX')


def app_store_scraper(app_name):
    app = AppStore(country="dk", app_name=app_name)
    app.review(how_many=1000)

    # Creates or updates the CSV with this name
    with open(r'appstore_reviews.csv', 'w', newline='') as file:
        fieldnames = ['username', 'review', 'score']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for review in app.reviews:
            score = review['rating']
            username = review['userName']
            review = review['review']

            try:
                print(f'{username} says: {review}')
                writer.writerow({'username': username, 'review': review, 'score': score})
            except:
                print('Failed to add entry XXX')


play_store_scraper(package_name)
app_store_scraper('smittestop')
