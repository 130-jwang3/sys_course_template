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


import os
import time

from flask import Blueprint, redirect, render_template, url_for

from helpers import resources, courses, eventing
from middlewares.auth import auth_required
from middlewares.form_validation import (
    ResourceUploadForm,
    resource_form_validation_required,
)

PUBSUB_TOPIC_NEW_PRODUCT = os.environ.get("PUBSUB_TOPIC_NEW_PRODUCT")


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
    form = ResourceUploadForm()
    form.course_id.choices = [
        (course.course_id, course.title) for course in courses.list_course()
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
    form.course_id.choices = [
        (course.course_id, course.title) for course in courses.list_course()
    ]

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

    resource_id = resources.add_resource(upload_resource)

    # Publish an event to the topic for new products.
    # Cloud Function detect_labels subscribes to the topic and labels the
    # product using Cloud Vision API upon arrival of new events.
    # Cloud Function streamEvents (or App Engine service stream-event)
    # subscribes to the topic and saves the event to BigQuery for
    # data analytics upon arrival of new events.
   #  eventing.stream_event(
   #      topic_name="new-product",
   #      event_type="email",
   #      event_context={"resource_id": resource_id, "resource_url": upload_resource.url},
   #  )

    return redirect(url_for("course_page.display"))
