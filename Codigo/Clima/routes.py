from flet_route import path
from middlewares.url_middleware import UrlBasedMiddleware
from views.index_view import IndexView 
from views.next_view import NextView 



app_routes = [
    path(url="/",clear=True,view=IndexView().view), 
    path(url="/next_view/:my_id", clear=False, view=NextView().view ,middleware = UrlBasedMiddleware().call_me),
]

