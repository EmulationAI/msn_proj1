"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller

# from masonite.co import UploadContract

# def show(self, upload: UploadContract)
#     upload # <class masonite.drivers.UploadDiskDriver>
class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        dump(view)
        return "hello"
        return view.render("welcome")