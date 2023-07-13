from django.urls import path
# from main.views.dashboard_view import Dashboard
from shop_template.views.home_view import HomeView
from shop_template.views.store_view import store, product_detail, search, submit_review
from shop_template.views.cart_view import cart, add_cart, remove_cart, remove_cart_item, checkout

from shop_template.views.order_view import place_order, payments, order_complete, create_checkout_session, successView,cancelledView, stripe_config

from shop_template.views.auth_view import MyaccountView, register, login, logout, activate, dashboard, forgotPassword,resetpassword_validate, resetPassword, my_orders, edit_profile, change_password, order_detail

urlpatterns = [
    path('', HomeView, name='home'),
    path('store/', store, name='store'),
    path('category/<slug:category_slug>/', store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/',product_detail, name='product_detail'),
    path('search/',search, name='search'),
    path('submit_review/<int:product_id>/', submit_review, name='submit_review'),

    path('cart/', cart, name='cart'),
    path('add_cart/<int:product_id>/', add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/',remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/',remove_cart_item, name='remove_cart_item'),

    path('checkout/', checkout, name='checkout'),

    path('place_order/', place_order, name='place_order'),
    path('payments/', payments, name='payments'),
    path('order_complete/', order_complete, name='order_complete'),

    path('create-checkout-session/', create_checkout_session, name="create_checkout_session"),
    path('success/', successView, name="success"), # new
    path('cancelled/', cancelledView), # new
    path('config/', stripe_config),
    path('account/', MyaccountView, name="my_account"),


## account url
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),

    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('forgotPassword/', forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', resetPassword, name='resetPassword'),

    path('my_orders/', my_orders, name='my_orders'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change_password/', change_password, name='change_password'),
    path('order_detail/<int:order_id>/', order_detail, name='order_detail'),

]