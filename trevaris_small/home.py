from flask import (
    Blueprint, render_template
)

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def home():
    projects = get_projects()
    return render_template('index.html', projects=projects)

def get_projects():
    import json
    import os

    path = os.path.dirname(__file__)
    
    with open(f"{path}/projects.json", "r") as f:
        projects = json.load(f)
    
    return projects