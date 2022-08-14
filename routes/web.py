from masonite.authentication import Auth
from masonite.routes import Route

ROUTES = [
    Route.get("/", "auth.HomeController@show"),
]

ROUTES += Auth.routes()