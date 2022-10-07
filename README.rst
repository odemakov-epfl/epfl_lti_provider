Sample LTI Provider for Flask
=============================

This is an edxtended version of https://github.com/mitodl/mit_lti_flask_sample repo

Super Quick Start
-----------------

You can try out the sample app for free by deploying it to your Heroku account
simply by clicking the deploy button:

|Deploy|

.. |Deploy| image:: https://www.herokucdn.com/deploy/button.png
   :target: https://heroku.com/deploy

Quick Start
-----------

Open your terminal and navigate to the directory you want to contain your
working directory.  Execute these commands:

.. code-block:: bash

   git clone https://github.com/odemakov-epfl/epfl_lti_provider.git
   cd epfl_lti_provider
   virtualenv venv
   . venv/bin/activate
   pip install -r requirements.txt
   export FLASK_APP=mit_lti_flask_sample.py
   export FLASK_DEBUG=1
   flask run [--host=127.0.0.1]

Then navigate to `http://localhost:5000/is_up <http://localhost:5000/is_up>`_

If you see a page containing the words, "I'm up", you have verified that you
can run the sample app locally.

1. Deploy the sample app to a server accessible from your LTI consumer, edX or
   another LMS.  (These instructions presume you're using edX, but they are
   similar for any LTI consumer.)
#. In edX Studio, navigate to ``Settings\Advanced Settings`` and enter these
   values for the specified keys.

======================= ========================
Keys                    Values
======================= ========================
Advanced Module List    ``[ lti ]``
----------------------- ------------------------
LTI Passports           ``[ "lti_starx_add_demo:__consumer_key__:__lti_secret__" ]``
======================= ========================

3. Still in edX Studio, navigate to the content page that will contain your LTI
   tool and create an LTI Advanced Component.
#. Enter the LTI ID for the external LTI provider.
#. Enter the URL of the external tool that this component launches.

======================= ========================
Keys                    Values
======================= ========================
LTI ID                  ``lti_starx_add_demo``
----------------------- ------------------------
LTI URL                 ``THE_URL_OF_YOUR_DEPLOYED_LTI_PROVIDER``
----------------------- ------------------------
Open in New Page        ``False``
----------------------- ------------------------
Request user's username ``True``
----------------------- ------------------------
Scored                  ``True``
----------------------- ------------------------
Weight                  ``10``
======================= ========================

Test to update to heroku-22 stack
