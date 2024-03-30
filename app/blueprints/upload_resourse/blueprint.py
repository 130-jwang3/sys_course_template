# Copyright 2018 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
This module is the Flask blueprint for the upload resource page (/upload_resource).
"""


from dataclasses import asdict
import os
import time
import requests

from flask import Blueprint, redirect, render_template, url_for

from helpers import resources, courses, eventing
from middlewares.auth import auth_required
from middlewares.form_validation import (
    ResourceUploadForm,
    resource_form_validation_required,
)

PUBSUB_TOPIC_NEW_PRODUCT = os.environ.get("PUBSUB_TOPIC_NEW_PRODUCT")
API_GATEWAY = "https://syscourse-gateway-4tq1q35x.uc.gateway.dev"
GATEWAY_KEY = "?key=AIzaSyB2PRCa87u1VsFXMw65lDgI03Y5HRFj9C4"

upload_resource_page = Blueprint("upload_resource_page", __name__)


@upload_resource_page.route("/upload_resource", methods=["GET"])
@auth_required
def display(auth_context):
    """
    View function for displaying the upload resource page.

    Parameters:
       auth_context (dict): The authentication context of request.
                            See middlewares/auth.py for more information.
    Output:
       Rendered HTML page.
    """

    # Prepares the upload resourse form.
    # See middlewares/form_validation.py for more information.
    api_gateway_url = API_GATEWAY + "/courses" + GATEWAY_KEY
    response = requests.get(api_gateway_url)
    list_course = response.json()
    
    form = ResourceUploadForm()
    form.course_id.choices = [
        (course["course_id"], course["title"]) for course in list_course
    ]
    return render_template("upload_resource.html", auth_context=auth_context, form=form)


@upload_resource_page.route("/upload_resource", methods=["POST"])
@auth_required
@resource_form_validation_required
def process(auth_context, form):
    """
    View function for processing upload resource requests.

    Parameters:
       auth_context (dict): The authentication context of request.
                            See middlewares/auth.py for more information.
       form (SellForm): A validated upload_resource form.
                        See middlewares/form_validation.py for more
                        information.
    Output:
       Rendered HTML page.
    """
    api_gateway_url = API_GATEWAY + "/courses" + GATEWAY_KEY
    response = requests.get(api_gateway_url)
    list_course = response.json()
    
    form.course_id.choices = [
        (course["course_id"], course["title"]) for course in list_course
    ]

    api_gateway_url = API_GATEWAY + "/resources" + GATEWAY_KEY
    upload_resource = resources.Resource(
        title=form.title.data,
        description=form.description.data,
        # url=form.resourceFile.data.filename,
        url="resource_1",
        # type=form.resourceFile.data.content_type,
        type="png",
        uid=auth_context.get("uid"),
        course_id=form.course_id.data,
    )
    new_upload_resource = asdict(upload_resource)
    response = requests.post(api_gateway_url, json=new_upload_resource)

    if response.ok:
        email = auth_context.get('email')
        eventing.stream_event(
            topic_name=PUBSUB_TOPIC_NEW_PRODUCT,
            event_type='new-product-sub',
            event_context={
                'to': email,
                'subject': 'Successfully Uploaded Resource to Syscourse',
                'text': 'resource uploaded to syscourse.'
            }
        )
        return redirect(url_for("course_page.display"))
    else:
        # Handle the case where the request to the API Gateway fails
        return "Error: Failed to add course", 500
