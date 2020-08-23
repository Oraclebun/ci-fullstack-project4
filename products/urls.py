from django.urls import path
import products.views


urlpatterns = [
    path('', products.views.IndexView.as_view(),
         name="home_page_route"),
    path('directory', products.views.DirectoryView.as_view(),
         name="product_directory_route"),
    path('create', products.views.input_product,
         name="create_product_route"),
    path('update/<int:product_id>', products.views.update_product,
         name="update_product_route"),
    path('delete/<int:product_id>', products.views.delete_product,
         name="delete_product_route"),
    path('details/<int:pk>', products.views.ProductDetailView.as_view(),
         name="product_detail_route"),
    path('breakfast', products.views.CategoryView.as_view(),
         name="category_product_route"),
    path('biscuits-and-cookies', products.views.CategoryView.as_view(),
         name="category_product_route"),
    path('grains-and-dried-beans', products.views.CategoryView.as_view(),
         name="category_product_route"),
    path('nuts', products.views.CategoryView.as_view(),
         name="category_product_route"),
    path('baking-ingredients', products.views.CategoryView.as_view(),
         name="category_product_route"),
    path('fresh-produce', products.views.CategoryView.as_view(),
         name="category_product_route")
]