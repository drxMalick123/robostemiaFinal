from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='home'),
    path('order-confirmed/', views.order_confirmed, name='order_confirmed'),
    path('order-tracking/', views.order_tracking, name='order_tracking'),
    path('product-detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('services-open/', views.services_open, name='services_open'),
    path('services/', views.services, name='services'),
    path('advisorycommittee/', views.advisory_committee, name='advisory-committee'),
    path('shop/', views.shop, name='shop'),
    path('your-cart/', views.your_cart, name='your_cart'),
    path('cart/update/', views.update_cart_quantity, name='update_cart_quantity'),
    path('cart/remove/', views.remove_from_cart, name='remove_from_cart'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urls.py
handler404 = 'robot.views.custom_404'