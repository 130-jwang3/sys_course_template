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
A collection of helper functions for courses related operations.
"""


from dataclasses import asdict
import time
import uuid
import os

from google.cloud import firestore

from .data_classes import Course

BUCKET = os.environ.get('GCS_BUCKET')

firestore_client = firestore.Client()


def add_course(course):
    """
    Helper function for adding a course.

    Parameters:
       course (Course): A Course object.

    Output:
       The ID of the course.
    """
    course_id = uuid.uuid4().hex
    firestore_client.collection("courses").document(course_id).set(asdict(course))
    return course_id

def get_course(course_id):
    """
    Helper function for getting a course.

    Parameters:
       course_id (str): The unique ID of a course.

    Output:
       A Course Object.
    """

    course = firestore_client.collection("courses").document(course_id).get()
    return Course.deserialize(course)


def list_course():
    """
    Helper function for listing courses base on ratings

    Parameters:
       None.

    Output:
       A list of Course objects.
    """
    courses = firestore_client.collection("courses").order_by("ratingsAverage").get()
    course_list = [Course.deserialize(course) for course in list(courses)]
   #  course_list.sort(key=lambda x: (x.ratingsAverage, x.ratingsCount))
    course_list.sort(key=lambda x: (float(x.ratingsAverage) if x.ratingsAverage is not None else 0, 
                                int(x.ratingsCount) if x.ratingsCount is not None else 0))
    return course_list


def remove_course(uid, course_id):
    """
    Helper function for deleting a course based on user ID and course ID.

    Parameters:
       uid (str): The unique ID of a user.
       course_id (str): The ID of the course to be deleted.

    Output:
       A message indicating whether the course was successfully deleted or not.
    """
    # Reference to the specific course document
    course_ref = firestore_client.collection('courses').document(course_id)
    course_doc = course_ref.get()

    # Check if the course exists and belongs to the user
    if course_doc.exists:
        course_data = course_doc.to_dict()
        if course_data['uid'] == uid:
            # Delete the course
            course_ref.delete()
            return "Course successfully deleted."
        else:
            return "Unauthorized to delete this course."
    else:
        return "Course not found."

def update_course(uid, course_id, updates):
    """
    Helper function for updating specific attributes of a course.

    Parameters:
       uid (str): The unique ID of a user authorized to update the course.
       course_id (str): The ID of the course to be updated.
       updates (dict): A dictionary of the attributes to be updated and their new values.

    Output:
       A message indicating whether the course was successfully updated or not.
    """
    # Reference to the specific course document
    course_ref = firestore_client.collection('courses').document(course_id)
    course_doc = course_ref.get()

    # Check if the course exists and belongs to the user
    if course_doc.exists:
        course_data = course_doc.to_dict()
        if course_data['uid'] == uid:
            # Update the specified attributes of the course
            course_ref.update(updates)
            return "Course successfully updated."
        else:
            return "Unauthorized to update this course."
    else:
        return "Course not found."