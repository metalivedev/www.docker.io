# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import request
from mailchimp import utils as mailchimputils
from mailchimp.chimpy.chimpy import ChimpyException
from datetime import datetime
from forms import NewsSubscribeForm
from django.http import HttpResponseRedirect
# from .utils import get_app_auth_twitter
from utils import TwitterClient, ClientException
import json
from django.core.cache import cache
from base.models import TeamMember, NewsItem, Event, GenericPost

CONSUMER_KEY = 'aEtFq69wvzUAjlzwh9Tw'
CONSUMER_SECRET = 'o6mcmOLtp35loXfUbRBOVpyfzenFdOSwBV3jd4MMFSM'

#We are not using the intercom plugin because we use js instead
#from intercom import Intercom


def home(request):
    form = NewsSubscribeForm()

    ## The events
    events = Event.objects.all().order_by('date_and_time')
    upcoming_events = events.filter(date_and_time__gt=datetime.today())

    ## The news
    news_items = NewsItem.objects.filter(show=True).order_by('-publication_date')[0:6]

    ## The tweets
    twitter_client = TwitterClient(CONSUMER_KEY, CONSUMER_SECRET)
    try:
        favorite_tweets = twitter_client.get_favorite_tweets()
    except ClientException:
        favorite_tweets = None  # temporary error
    except Exception:
        favorite_tweets = None  # twitter client not set.

    return render_to_response("homepage.md", {
        "form": form,
        "events": events,
        "news_items": news_items,
        "upcoming_events": upcoming_events,
        "tweets": favorite_tweets

    }, context_instance=RequestContext(request))


def news(request):
    """
    News page
    """

    news_items = NewsItem.objects.all().order_by('-publication_date')

    return render_to_response("about/news.md", {
        "news_items": news_items,
    }, context_instance=RequestContext(request))

def press(request):
    """
    Press page
    """

    press_items = GenericPost.objects.all().order_by('-publication_date')

    return render_to_response("about/press.md", {
        "press_items": press_items,
    }, context_instance=RequestContext(request))


def team(request):
    """
    Team page
    """

    core_team = TeamMember.objects.all().filter(show_as_team=True).order_by('full_name')

    return render_to_response("about/team.md", {
        "core_team": core_team,
    }, context_instance=RequestContext(request))


def events(request):
    """
    events page
    """

    events = Event.objects.all().order_by('date_and_time')
    upcoming_events = events.filter(date_and_time__gt=datetime.today())
    past_events = events.filter(date_and_time__lt=datetime.today())

    return render_to_response("community/events.md", {
        "events": events,
        "upcoming_events": upcoming_events,
        "past_events": past_events
    }, context_instance=RequestContext(request))


def email_thanks(request):
    """
    Page for thanking the user for signup
    """

    if request.method == "POST":
        form = NewsSubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]

            list_id = 'c0995b6e8f'
            CACHE_TIMEOUT = 3600 * 24 * 3

            mailchimp_list = cache.get(list_id)

            if mailchimp_list:
                pass
            else:
                connection = mailchimputils.get_connection()
                mailchimp_list = connection.get_list_by_id(list_id)

                cache.set(list_id, mailchimp_list, CACHE_TIMEOUT)

            extra_text = None
            try:
                results = mailchimp_list.subscribe(
                    email,
                    {
                        'EMAIL': email,
                        'FNAME': '',
                        'LNAME': '',
                        'MMERGE3': '',
                        'MMERGE4': '',
                        'MMERGE5': 'www.docker.io/',
                    },
                    'html',
                    'true'
                )
            except ChimpyException as error:
                extra_text = "You are already subscribed to this list"
                print error
                pass

            intercom_extra = {
                'email': email,
                'news_signup_at': datetime.now().strftime("%Y-%m-%d"),
                'signup_location': "www.docker.io",
            }

            return render_to_response('base/email_thanks.html',
                                      {
                                          'form': form,
                                          'intercom_extra': intercom_extra,
                                          'extra_text': extra_text
                                      },
                                      context_instance=RequestContext(request))

        else:
            # form = NewsSubscribeForm()

            return render_to_response('base/email_form.html',
                                      {
                                          'form': form,
                                      },
                                      context_instance=RequestContext(request))

    else:
        form = NewsSubscribeForm()
        return render_to_response('base/email_form.html',
                                  {
                                      'form': form,
                                  },
                                  context_instance=RequestContext(request))
