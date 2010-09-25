#!/usr/bin/python2.7 -O

# Run xychan as a CGI script.
# Ensure the path to the python2.7 binary above is correct.


import xychan
from xychan import app

# Uncomment and modify the next line to change the database xychan should use
# app.configure_db("sqlite:///test.db")

# Uncomment and modify this line to change where xychan stores images
# app.configure_image_dir("./_images")

from wsgiref.handlers import CGIHandler
CGIHandler().run(app)