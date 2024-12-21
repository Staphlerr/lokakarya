from django.urls import path
from forumandreviewpage.views import show_forum, create_forum_entry, show_xml, show_json, show_json_by_id, show_xml_by_id, detail_post, upvote_post, delete_post, edit_post, edit_post_ajax
from forumandreviewpage import views

app_name = 'forumandreviewpage'

urlpatterns = [
    path('forumandreviewpage/', views.show_forum, name='show_forum'),
    path('post/<uuid:post_id>/', views.detail_post, name='detail_post'),
    path('create/', views.create_forum_entry, name='create_forum_entry'),
    path('post/<uuid:post_id>/upvote/', views.upvote_post, name='upvote_post'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('delete_post/<uuid:post_id>/', views.delete_post, name='delete_post'),
    path('post/<uuid:post_id>/edit/', views.edit_post, name='edit_post'),
    path('edit_post_ajax/<uuid:post_id>/', views.edit_post_ajax, name='edit_post_ajax'),
]