# Bollocks Index
We've noticed that some courses at our university have a rather high amount of
bollocks in them, this is a place for us to figure out what that bollocks
actually means.

## Hacking
Models go in the models module. Pages go in the pages module, templates for
pages go in the templates directory inside the pages directory and are made
using [Plim](https://plim.readthedocs.org/en/latest/en/nutshell.html).

The existing code should be readable enough to figure out how to write your own.
Except for the templates. They can be a bit dense. Read the docs.

requirements.txt defines the virtualenv necessary, don't forget it.

If you want the facebook stuff to work you'll need to make a facebook dev
account and an application for this then whack the app key and secret into
`bollocksindex/config.py`.
