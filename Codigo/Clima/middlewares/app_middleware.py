import flet as ft
from flet_route import Params,Basket

class AppBasedMiddleware:
    def __init__(self):
        ...

    async def call_me(self,page:ft.Page,params:Params,basket:Basket):

        print("App Based Middleware Called")
        #page.route = "/another_view" # If you want to change the route for some reason, use page.route
