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
This module is the Flask blueprint for the cart page (/cart).
"""
import os
import requests

from flask import Blueprint, render_template, request

from helpers import courses, resources
from middlewares.auth import auth_required, auth_optional


course_page = Blueprint("course_page", __name__)
API_GATEWAY = "https://syscourse-gateway-4tq1q35x.uc.gateway.dev"

@course_page.route("/")
@auth_optional
def display(auth_context):
    """
    View function for displaying all of the course.

    Parameters:
        auth_context (dict): The authentication context of request.
                             See middlewares/auth.py for more information.
    Output:
        Rendered HTML page.
    """
    api_gateway_url = API_GATEWAY + "/courses"
    response = requests.get(api_gateway_url)

    course_items = response.json()
    resource_items = resources.list_resources()

    return render_template(
        "main.html",
        courses=course_items,
        resources=resource_items,
        auth_context=auth_context,
        bucket=courses.BUCKET,
    )


@course_page.route("/course", methods=["GET"])
@auth_required
def display_specific(auth_context):
    """
    View function for displaying the specifications of the course.

    Parameters:
        auth_context (dict): The authentication context of request.
                             See middlewares/auth.py for more information.
    Output:
        Rendered HTML page.
    """

    course_id = request.args.get("course_id")

    if course_id:
        # Fetch course details based on course_id
        api_gateway_url = API_GATEWAY + "/courses/" + course_id
        print(api_gateway_url)
        response = requests.get(api_gateway_url)
        course = response.json()
        
        resource_list = resources.list_resources_by_course(course_id=course_id)
        return render_template(
            "course.html",
            course=course,
            resources=resource_list,
            auth_context=auth_context,
            bucket=courses.BUCKET,
        )
    else:
        return "Course ID is required", 400


@course_page.route("/course", methods=["POST"])
@auth_required
def add_course(auth_context):
    """
    Endpoint for adding a course

    Parameters:
       auth_context (dict): The authentication context of request.
                            See middlewares/auth.py for more information.
    Output:
       Text message with HTTP status code 200.
    """
    # need to be implemented


@course_page.route("/course", methods=["DELETE"])
@auth_required
def remove(auth_context):
    """
    Endpoint for removing an item from cart.

    Parameters:
       auth_context (dict): The authentication context of request.
                            See middlewares/auth.py for more information.
    Output:
       Text message with HTTP status code 200.
    """

    # need to be implemented
