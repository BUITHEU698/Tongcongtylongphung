from django.contrib import admin
from .models import contactModel
from .models import postBlog
from .models import UserModel
from .models import CartModel
from .models import CartItemModel
from .models import OrderModel

admin.site.register(contactModel)
admin.site.register(postBlog)
admin.site.register(UserModel)
admin.site.register(CartModel)
admin.site.register(CartItemModel)
admin.site.register(OrderModel)
