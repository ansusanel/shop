from django.urls import path
from.import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('addcategories',views.addcategories,name='addcategories'),
    path('viewcategories',views.viewcategories,name='viewcategories'),
    path('addproducts',views.addproducts,name='addproducts'),
    path('viewproducts',views.viewproducts,name='viewproducts'),
    path('registeredusers',views.registeredusers,name='registeredusers'),
    path('feeback',views.feeback,name='feeback'),
    path('viewoders',views.viewoders,name='viewoders'),
    path('categorydata',views.categorydata,name='categorydata'),
    path('editcategory',views.editcategory,name='editcategory'),
    path('editcat/<int:id>',views.editcat,name='editcat'),
    path('updatecategory/<int:id>',views.updatecategory,name='updatecategory'),
    path('delete/<int:id>',views.delete,name='delete'),  
    path('editproduct',views.editproduct,name='editproduct'), 
    path('editcategory',views.editcategory,name='editcategory'),
    path('editprod/<int:id>',views.editprod,name='editprod'),
    path('updateproduct/<int:id>',views.updateproduct,name='updateproduct'),
    path('deleteprod/<int:id>',views.deleteprod,name='deleteprod'),  
]