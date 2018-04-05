from django.conf import settings
from django.http import HttpResponse
from django.template import loader
from twython import Twython, TwythonError


def _get_tweets(latitude, longitude):

    twitter = Twython(
        settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET,
        settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)

    geocode = '{0},{1},50km'.format(latitude, longitude)

    # 100 is the max num of tweets you can get from a search
    tweets = twitter.search(count=100, geocode=geocode)

    # Remove from tweets, the ones without coordinates
    # It seems that only around 1% of tweets have coordinates
    geo_tweets = []

    for t in tweets['statuses']:
        if t['coordinates'] is not None:
            geo_tweets.append({
                "coordinates": t['coordinates']['coordinates'],
                "url": "https://twitter.com/{0}/status/{1}".format(t['user']['screen_name'], t['id_str'])
            })
    print(geo_tweets)
    return geo_tweets


def index(request):

    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')

    template = loader.get_template('index.html')
    context = {
        'tweets': _get_tweets(latitude, longitude) if latitude and longitude else [],
        'gmaps_api_key': settings.GMAPS_API_KEY,
        'latitude': latitude,
        'longitude': longitude
    }

    return HttpResponse(template.render(context, request))
