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
A collection of helper functions for cart related operations.
"""


from dataclasses import asdict
import time
import os
import uuid

from google.cloud import firestore

from .data_classes import Resource

firestore_client = firestore.Client()

BUCKET = os.environ.get('GCS_BUCKET')

def add_resource(resource):
    """
    Helper function for adding a resource.

    Parameters:
       resource (Resource): A Resource object.

    Output:
       The ID of the resource
    """
    resource_id = uuid.uuid4().hex
    firestore_client.collection("resources").document(resource_id).set(asdict(resource))
    return resource_id


def get_resource(resource_id):
    """
    Helper function for getting a resource.

    Parameters:
       resource_id (str): The ID of the resource.

    Output:
       A Resource object.
    """
    resource = firestore_client.collection("resources").document(resource_id).get()
    return Resource.deserialize(resource)


def list_resources():
    """
    Helper function for listing resources.

    Parameters:
       None.

    Output:
       A list of Resource objects.
    """

    resources = firestore_client.collection("resources").order_by("title").get()
    resource_list = [Resource.deserialize(resource) for resource in list(resources)]
    return resource_list


def list_resources_by_course(course_id):
    """
    Helper function for listing resources base on course id.

    Parameters:
       course_id (str): The ID of the course.

    Output:
       A list of Resource objects.
    """
    resources_ref = firestore_client.collection("resources")
    query = resources_ref.where("course_id", "==", course_id)
    results = query.get()

    resources = []
    for doc in results:
        resource = Resource.deserialize(doc)
        if resource:
            resources.append(resource)

    return resources

def delete_resource(uid, resource_id):
    """
    Deletes a resource based on UID and resource ID.

    Parameters:
    - uid (str): The unique ID of the user who owns the resource.
    - resource_id (str): The ID of the resource to be deleted.

    Output:
    - A message indicating the outcome of the operation.
    """
    resource_ref = firestore_client.collection('resources').document(resource_id)
    resource_doc = resource_ref.get()

    if resource_doc.exists:
        resource_data = resource_doc.to_dict()
        if resource_data['uid'] == uid:
            resource_ref.delete()
            return "Resource successfully deleted."
        else:
            return "Unauthorized to delete this resource."
    else:
        return "Resource not found."