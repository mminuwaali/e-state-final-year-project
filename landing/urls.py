from . import views
from django.urls import path

app_name, urlpatterns = "landing", [
    path("category/<id>/", views.category_detail_view, name="category-detail-view"),
    path("category/", views.category_view, name="category-view"),
    path("contact/", views.contact_view, name="contact-view"),
    path("<id>/", views.detail_view, name="detail-view"),
    path("about/", views.about_view, name="about-view"),
    path("", views.index_view, name="index-view"),
]
