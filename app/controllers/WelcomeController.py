"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller


# from masonite.co import UploadContract

class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        dd(view)
        return view.render("welcome")
