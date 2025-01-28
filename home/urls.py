from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ValidVoteViewSet,ConstituencyViewSet,DistrictViewSet

router = DefaultRouter()
router.register(r'valid-vote', ValidVoteViewSet)
router.register(r'constituency', ConstituencyViewSet)
router.register(r'district', DistrictViewSet)

urlpatterns = [
    # Party URLs
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('admin_page', views.admin_page, name='admin_page'),
    path('party_result/', views.party_result, name='party_result'),
    path('party_activity/', views.party_activity, name='party_activity'),
    
    path('parties/', views.party_list, name='party_list'),
    path('parties2/', views.party_list2, name='party_list2'),
    path('party/<int:pk>/', views.party_detail, name='party_detail'),
    path('party/create/', views.party_create, name='party_create'),
    path('party/<int:pk>/update/', views.party_update, name='party_update'),
    path('party/<int:pk>/delete/', views.party_delete, name='party_delete'),

    # District URLs
    path('districts/', views.district_list, name='district_list'),
    path('district/create/', views.district_create, name='district_create'),
    path('district/<int:pk>/update/', views.district_update, name='district_update'),
    path('district/<int:pk>/delete/', views.district_delete, name='district_delete'),
    
    path('khayines/', views.khayine_list, name='khayine_list'),
    path('khayine/create/', views.khayine_create, name='khayine_create'),
    path('khayine/<int:pk>/update/', views.khayine_update, name='khayine_update'),
    path('khayine/<int:pk>/delete/', views.khayine_delete, name='khayine_delete'),

    path('townships/', views.township_list, name='township_list'),
    path('township/create/', views.township_create, name='township_create'),
    path('township/<int:pk>/update/', views.township_update, name='township_update'),
    path('township/<int:pk>/delete/', views.township_delete, name='township_delete'),

    path('constituencies/', views.constituency_list, name='constituency_list'),
    path('constituencies/create/', views.constituency_create, name='constituency_create'),
    path('constituencies/<int:pk>/update/', views.constituency_update, name='constituency_update'),
    path('constituencies/<int:pk>/delete/', views.constituency_delete, name='constituency_delete'),
    
    path('number_of_voters1/', views.number_of_voters_list1, name='number_of_voters_list1'),
    path('number_of_voters1/create/', views.number_of_voters_create1, name='number_of_voters_create1'),
    path('number_of_voters1/<int:pk>/update/', views.number_of_voters_update1, name='number_of_voters_update1'),
    path('number_of_voters1/<int:pk>/delete/', views.number_of_voters_delete1, name='number_of_voters_delete1'),
    
    path('valid-vote/', views.valid_vote_list, name='valid_vote_list'),
    path('valid-vote/create/', views.valid_vote_create, name='valid_vote_create'),
    path('valid-vote/update/<int:id>/', views.valid_vote_update, name='valid_vote_update'),
    path('valid-vote/delete/<int:id>/', views.valid_vote_delete, name='valid_vote_delete'),
]
