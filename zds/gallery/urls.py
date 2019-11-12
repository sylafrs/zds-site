from django.urls import re_path

from zds.gallery.views import NewGallery, NewImage, DeleteImages, EditImage, ImportImages, GalleryDetails, \
    EditGallery, ListGallery, DeleteGalleries, EditGalleryMembers, NewGalleryGroup, EditGalleryGroup, \
    GalleryGroupDetails


urlpatterns = [
    # Index
    re_path(r'^$', ListGallery.as_view(), name='gallery-list'),

    # Gallery operation
    re_path(r'^nouveau/$', NewGallery.as_view(), name='gallery-new'),
    re_path(r'^(?P<pk>\d+)/(?P<slug>.+)/$',
            GalleryDetails.as_view(), name='gallery-details'),
    re_path(r'^editer/(?P<pk>\d+)/(?P<slug>.+)/$',
            EditGallery.as_view(), name='gallery-edit'),
    re_path(r'^membres/(?P<pk>\d+)/$',
            EditGalleryMembers.as_view(), name='gallery-members'),
    re_path(r'^supprimer/$', DeleteGalleries.as_view(),
            name='galleries-delete'),

    # Gallery items operations

    re_path(r'^item/supprimer/(?P<pk_gallery>\d+)/$',
            DeleteImages.as_view(), name='gallery-item-delete'),

    # Group operations
    re_path(r'^groupe/voir/(?P<pk>\d+)/(?P<slug>.+)/(?P<pk_group>\d+)/(?P<slug_group>.+)/$',
            GalleryGroupDetails.as_view(), name='gallery-group-details'),
    re_path(r'^groupe/ajouter/(?P<pk_gallery>\d+)/$',
            NewGalleryGroup.as_view(), name='gallery-group-new'),
    re_path(r'^groupe/editer/(?P<pk_gallery>\d+)/(?P<pk>\d+)/$',
            EditGalleryGroup.as_view(), name='gallery-group-edit'),


    # Image operations
    re_path(r'^image/ajouter/(?P<pk_gallery>\d+)/$',
            NewImage.as_view(), name='gallery-image-new'),
    re_path(r'^image/editer/(?P<pk_gallery>\d+)/(?P<pk>\d+)/$',
            EditImage.as_view(), name='gallery-image-edit'),
    re_path(r'^image/importer/(?P<pk_gallery>\d+)/$',
            ImportImages.as_view(), name='gallery-image-import'),
]
