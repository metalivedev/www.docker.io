{% extends 'community/meetups.html' %}
{% load static %}
{% block title %} Events & Meetups - {% endblock %}
{% block meta-description %}Docker is an open-source project to easily create lightweight, portable, self-sufficient containers from any application. The same container that a developer builds and tests on a laptop can run at scale, in production, on VMs, bare metal, OpenStack clusters, public clouds and more.{% endblock %}
{% block meta-keywords %}Docker, linux containers, lxc, PaaS, dotCloud, introduction, about, how it works{% endblock %}

{% block copy_headline %}
# get involved with the Docker community by creating a Docker Meetup group and Meetup events
{% endblock %}



{% block copy_sidebar %}
{% endblock %}


{% block copy_introduction %}

# Docker meetups
Anyone can join or start a Docker Meetup. Simply click on the closest city to join the group and meet developers and
    ops engineers using Docker. If you want to create a new Docker Meetup in your city, we will are happy to help:
    <a href="{% url 'meetups-organize' %}">follow the guide</a>.

<iframe width="620" height="400" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps/ms?msa=0&amp;msid=202534187356482762121.0004e943a350c59ab3ca5&amp;ie=UTF8&amp;t=m&amp;ll=26.74561,-49.570312&amp;spn=108.630481,217.617188&amp;z=2&amp;output=embed"></iframe><br /><small>View <a href="https://maps.google.com/maps/ms?msa=0&amp;msid=202534187356482762121.0004e943a350c59ab3ca5&amp;ie=UTF8&amp;t=m&amp;ll=26.74561,-49.570312&amp;spn=108.630481,217.617188&amp;z=2&amp;source=embed" style="color:#0000FF;text-align:left">Docker Meetup Groups</a> in a larger map</small>

Do you want to be listed here? Email us at <strong>meetup@docker.io</strong> or ping us on <a href="https://twitter.com/docker/">twitter</a>.

### Currently active meetup groups:

#### North America
* <a href="http://www.meetup.com/Docker-Atlanta/">Atlanta, GA</a>
* <a href="http://www.meetup.com/Docker-Boston/">Boston, MA</a>
* <a href="http://www.meetup.com/Docker-Boulder/">Boulder, CO</a>
* <a href="http://www.meetup.com/Docker-Chicago/">Chicago, IL</a>
* <a href="http://www.meetup.com/Docker-Los-Angeles/">Los Angeles, CA</a>
* <a href="http://www.meetup.com/Docker-NewYorkCity/">New York, NY</a>
* <a href="http://www.meetup.com/Docker-Palo-Alto/">Palo Alto, CA</a>
* <a href="http://www.meetup.com/Docker-Portland-OR/">Portland, OR</a>
* <a href="http://www.meetup.com/Docker-San-Mateo-CA/">San Mateo, CA</a>
* <a href="http://www.meetup.com/Docker-meetups/">San Francisco, CA</a>
* <a href="http://www.meetup.com/Docker-Toronto/">Toronto, ON</a>

#### South America
* <a href="http://www.meetup.com/Docker-Sao-Paulo/">S&atilde;o Paulo, Brazil</a>

#### Europe
* <a href="http://www.meetup.com/Docker-London/">London, UK</a>
* <a href="http://www.meetup.com/Docker-Milano/">Milan, Italy</a>
* <a href="http://www.meetup.com/Docker-Paris">Paris, France</a>


{% endblock %}


