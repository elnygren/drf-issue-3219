# drf-issue-3219
A small demo of DRF issue 3219 that might cause dataloss in a multipart PATCH request when a nested serializer is present.

[Issue link](https://github.com/tomchristie/django-rest-framework/issues/3219)

The Demo has a "Startup" class because that was the one present in my larger project where I discovered this issue.

The issue itself is described at the link above, and on the code level see:
https://github.com/elnygren/drf-issue-3219/blob/master/DRFerror/views.py#L33

Short description of the problem:

* see the `views.py` above first
* validated_data is populated with an empty OrderedDict() object for `admin`
* serializer.save() is usually implemented in a way that could then null this relationship to `admin` as an OrderedDict is not a admin object, but an empty object. 
* like described at the link, this issue could be present in other DRF Fields.


Dependencies

* Python 3.4.3
* requirements.txt:
  * Django 1.7.4
  * Django Rest Framework 3.1.3
  * Pillow (for file uploads)

Database state:
* create a root user and another user
* see dumpdata for Startup

PATCH request:

![POSTMAN PATCH](https://github.com/elnygren/drf-issue-3219/blob/master/multpart_PATCH.png)
