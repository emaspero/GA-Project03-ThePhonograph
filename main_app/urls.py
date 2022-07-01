from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    #  Record Model Related Paths 
    path('records/', views.RecordList.as_view(), name='records_index'),
    path('records/<int:pk>/', views.RecordDetail.as_view(), name='records_detail'),
    path('records/create/', views.RecordCreate.as_view(), name='records_create'),
    path('records/<int:pk>/update', views.RecordUpdate.as_view(), name='records_update'),
    path('records/<int:pk>/delete', views.RecordDelete.as_view(), name='records_delete'),

    # Crate Model Related Paths
    path('crates/<int:pk>/', views.CrateDetail.as_view(), name='crates_detail'),
    path('crates/create/', views.CrateCreate.as_view(), name='crates_create'),
    path('crates/<int:pk>/update', views.CrateUpdate.as_view(), name='crates_update'),
    path('crates/get_crate', views.get_crate, name='get_crate'),



    # Associate & Un-associate a record with a Crate
    path('records/<int:record_id>/assoc_record/', views.assoc_record, name='assoc_record'),
    path('crates/<int:pk>/unassoc_record/<int:record_id>/', views.unassoc_record, name='unassoc_record'),


    # # Add Track List
    path('records/<int:pk>/add_tracklist/', views.add_tracklist, name='add_tracklist'),


    # Artists Display All
    path('artists/', views.ArtistList.as_view(), name='artists_index'),
    # # Artist Display Detail 
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name = 'artists_detail'),
    # # Artist Creation 
    path('artists/create', views.ArtistCreate.as_view(), name = 'artists_create'),
    # # Artist Update
    path('artists/<int:pk>/update', views.ArtistUpdate.as_view(), name = 'artists_update'),
    # # Artist Delete
    path('artists/<int:pk>/delete', views.ArtistDelete.as_view(), name = 'artists_delete'),



    # Associate and Unassociate an Artist with a Record (M:M)
    path('records/<int:record_id>/assoc_artist/<int:artist_id>/', views.assoc_artist, name='assoc_artist'),
    path('records/<int:record_id>/unassoc_artist/<int:artist_id>/', views.unassoc_artist, name='unassoc_artist'),



    # Signup Route/URL
    path('accounts/signup/', views.signup, name='signup'),

    path("password_reset/", views.password_reset_request, name="new_password_reset"),


]

urlpatterns += staticfiles_urlpatterns()