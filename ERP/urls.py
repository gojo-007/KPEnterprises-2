from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('CallEntry',views.CallEntry,name="Call Entry"),
    path('AddCallEntry',views.AddCallEntry,name="Add Call Entry"),
    path('Cluster',views.Cluster,name="Cluster"),
    path('EditCluster/<int:id>',views.EditCluster,name="Edit Cluster"),
    path('DeleteCluster/<int:id>',views.DeleteCluster,name="Delete Cluster"),
    path('CostCode',views.CostCode,name="Cost Code"),
    path('EditCostCode/<int:id>',views.EditCostCode,name="Edit Cost Code"),
    path('DeleteCostCode/<int:id>',views.DeleteCostCode,name="Delete Cost Code"),
    path('GST',views.GST,name="GST"),
    path('EditGST/<int:id>',views.EditGST,name="Edit GST"),
    path('DeleteGST/<int:id>',views.DeleteGST,name="Delete GST"),
    path('Party',views.Party,name="party"),
    path('AddParty',views.AddParty,name="Add party"),
    path('EditParty/<int:id>',views.EditParty,name="Edit Party"),
    path('DeleteParty/<int:id>',views.DeleteParty,name="Delete Party"),
    path('Labour',views.Labour,name="Labour"),
    path('EditLabour/<int:id>',views.EditLabour,name="Edit Labour"),
    path('DeleteLabour/<int:id>',views.DeleteLabour,name="Delete Labour"),
    path('AddLabour',views.AddLabour,name="Add Labour"),
    path('Rate',views.Rate,name="Rate"),
    path('AddRate',views.AddRate,name="Add Rate"),
    path('EditRate/<int:id>',views.EditRate,name="Edit Rate"),
    path('DeleteRate/<int:id>',views.DeleteRate,name="Delete Rate"),
    path('Invoice',views.Invoice,name="Invoice"),
    path('AddInvoice',views.AddInvoice,name="Add Invoice"),
    path('login',views.Login,name='Login'),
    path('logout',views.Logout,name='Logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
