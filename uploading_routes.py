from flask import Blueprint


uploading_routes = Blueprint("uploading", __name__)



@uploading_routes.route('/upload_excel')
def upload_excel():
    # code is here
    return "excel uploaded succfully"


@uploading_routes.route('/upload_pdf')
def upload_pdf():
    return "pdf uploaded succfully"


@uploading_routes.route('/upload_image')
def upload_image():
    return "image uploaded succfully"
