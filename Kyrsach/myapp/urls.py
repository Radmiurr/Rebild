from django.urls import path
from myapp.views import index, add_item, update_item,  ProductListView, ProductDetailView, ProductDeleteView, PaymentSuccessView, PaymentFailedView, create_checkout_session, AddReview


app_name = "myapp"

urlpatterns = [
    #http://127.0.0.1:8000/myapp/
    path("", index, name='index'),
    # path("", ProductListView.as_view(), name='index'),
    path("<int:pk>/", ProductDetailView.as_view(), name="detail"),
    # path("<int:my_id>/", indexItem, name="detail"),
    
    path("additem/", add_item, name="add_item"),
    path("updateitem/<int:my_id>/", update_item, name="update_item"),
    path("deleteitem/<int:pk>/", ProductDeleteView.as_view(), name="delete_item"),
    path("review/<int:my_id>", AddReview, name="AddReview"),
    path("success/", PaymentSuccessView.as_view(), name="success"),
    path("failed/", PaymentFailedView.as_view(), name="failed"),
    path("api/checkout-session/<int:id>/", create_checkout_session, name="api_checkout_session"),
    # path("deleteitem/<int:my_id>/", delete_item, name="delete_item"),
]