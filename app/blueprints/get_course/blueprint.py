from helpers import courses, resources
from middlewares.auth import auth_required, auth_optional

from flask import Blueprint, render_template

all_course_page = Blueprint('all_course_page', __name__)

@all_course_page.route('/all_course')
@auth_optional
def display(auth_context):
    """
    View function for displaying the courses page.
    """
    course_items = courses.list_course()
    return render_template(
        "all_course_page.html",
        courses=course_items,
        auth_context=auth_context,
        bucket=courses.BUCKET,
    )
