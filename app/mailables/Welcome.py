from masonite.facades import Mail
from masonite.mail import Mailable
from masonite.environment import env

class Welcome(Mailable):
    def build(self):
        return (
            self.to("shehbaz.bsee1395@gmail.com")
            .subject("Masonite 4")
            .text("Hello from Masonite!")
            .html("<h1>Hello from Masonite!</h1>")
        )

# from masonite.environment import env
# from app.mailables.Welcome import Welcome
# Mail.mailable(Welcome().to("shehbaz.bsee1395@gmail.com")).send()
#