{% extends 'live.html' %}
{% load static %}
{% block title %}Docker Hack Day #7 - {% endblock %}
{% block meta-description %}Docker is an open-source project to easily create lightweight, portable, self-sufficient containers from any application. The same container that a developer builds and tests on a laptop can run at scale, in production, on VMs, bare metal, OpenStack clusters, public clouds and more.{% endblock %}
{% block meta-keywords %}Docker, linux containers, lxc, PaaS, dotCloud, introduction, about, how it works{% endblock %}


{% block copy_headline %}
# Docker Meetup San Mateo @ Edmodo - Oct. 22nd - LIVE #
{% endblock %}

{% block copy_introduction %}

## Schedule

Streaming starts at around 6:15pm PST

* 6:15pm PST: Docker: What? Why? by <a href="https://twitter.com/nickstinemates">Nick Stinemates</a>
* 6:30pm PST: How to build a SaaS in 10 minutes by <a href="https://twitter.com/nickstinemates">Nick Stinemates</a>
* 7:00pm PST: Docker + OpenStack by <a href="https://twitter.com/sam_alba">Sam Alba</a>
* 7:30pm PST: Q&A

{#<img src="{% static 'img/live/docker-meetup-waiting.jpg' %}" title="LIVE">#}
<iframe width="625" height="380" src="http://www.youtube.com/embed/6RzQB0XbTrQ" frameborder="0" allowfullscreen></iframe>

<i>Note: There can be up to 1 minute delay with Google Hangout On Air.</i>

### Backchannel

In addition, we have a special IRC channel: <strong>#docker-meetup</strong>, where you'll be able to ask questions during the meetup.

{% endblock copy_introduction %}

    {# NOTE: Link to online chat here, cannot be in markdown #}

{% block copy_1 %}

We start the Docker Meetup broadcast at around 6:15pm PST.

Back channel: IRC #docker-hackday

Twitter: #dockermeetup

{% endblock %}
