# StealMyStuff
Every year a special time comes around, thousands of students move into thousands of flats around the country and wayward furniture, technology and the occasional pet is cast out onto the curb. StealMyStuff is dedicated to rehoming these items, users can post a picture, description and map reference of their stuff for others to browse and, if they like what they see, come and steal it. 

## Hacking
Models go in the models module. Pages go in the pages module, templates for
pages go in the templates directory inside the pages directory and are made
using Mako.

The existing code should be readable enough to figure out how to write your own.
Except for the templates. They can be a bit dense. Read the docs.

requirements.txt defines the virtualenv necessary, don't forget it.

If you want the facebook stuff to work you'll need to make a facebook dev
account and an application for this then whack the app key and secret into
`bollocksindex/config.py`.
