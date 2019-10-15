---
layout: page
title: "Publications"
---

{% for yr in (2000..2019) reversed %}
## {{yr}}
{% include publications.html year=yr %}
{% endfor %}

{% assign yr = 1998 %}
## {{yr}}
{% include publications.html year=yr %}
