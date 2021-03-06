from django.urls import path
import products.views


urlpatterns = [
    path('', products.views.IndexView.as_view(),
         name="home_page_route"),
    path('directory', products.views.DirectoryView.as_view(),
         name="product_directory_route"),
    path('create', products.views.CreateProduct.as_view(),
         name="create_product_route"),
    path('update/<int:pk>', products.views.UpdateProduct.as_view(),
         name="update_product_route"),
    path('delete/<int:pk>', products.views.DeleteProduct.as_view(),
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
         name="category_product_route"),
    path('brands', products.views.BrandListView.as_view(),
         name="view_brand_route"),
    path('create-brands', products.views.BrandAdd.as_view(),
         name="create_brand_route"),
    path('update-brands/<int:pk>', products.views.BrandUpdate.as_view(),
         name="update_brand_route"),
    path('delete-brands/<int:pk>', products.views.BrandDelete.as_view(),
         name="delete_brand_route"),
    path('subcategory', products.views.SubcategoryListView.as_view(),
         name="view_subcategory_route"),
    path('add-subcategory', products.views.AddSubcategory.as_view(),
         name="add_subcategory_route"),
    path('update-subcategory/<int:pk>',
         products.views.UpdateSubcategory.as_view(),
         name="update_subcategory_route"),
    path('delete-subcategory/<int:pk>',
         products.views.DeleteSubcategory.as_view(),
         name="delete_subcategory_route"),
    path('usage', products.views.UsageListView.as_view(),
         name="view_usage_route"),
    path('add-usage', products.views.AddUsage.as_view(),
         name="add_usage_route"),
    path('update-usage/<int:pk>',
         products.views.UpdateUsage.as_view(),
         name="update_usage_route"),
    path('delete-usage/<int:pk>',
         products.views.DeleteUsage.as_view(),
         name="delete_usage_route")
]
