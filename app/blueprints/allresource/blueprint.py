from helpers import courses, resources
from middlewares.auth import auth_required, auth_optional

from flask import Blueprint, render_template

all_resource_page = Blueprint('all_resource_page', __name__)

@all_resource_page.route('/all_resource')
@auth_optional
def display(auth_context):
    """
    View function for displaying the resources page.
    """
    resource_items = resources.list_resources()
    return render_template(
        "all_resource_page.html",
        resources=resource_items,
        auth_context=auth_context,
        bucket=courses.BUCKET,
    )
