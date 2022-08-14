from masonite.controllers import Controller
from masonite.request import Request
from masonite.views import View

from app.models.User import User


class HomeController(Controller):
    def show(self, view: View, request : Request):
        return view.render("auth.home", {"user": request.user()})
