__author__ = 'NBUCHINA'

from django.conf.urls import patterns, url
from ToyController import views


urlpatterns = patterns('',
    # ex: /polls/
     url(r'^control/$', views.control),
     url(r'^$', views.control_page),
    # url(r'^editor-substep-actions/$', views.get_components_list,name="substep-actions"),
    # url(r'^editor-substep-params/$', views.get_component_params,name="substep-params"),
    # url(r'^editor-class-params/$', views.get_component_class_params,name="substep-class"),
    # url(r'^editor-substep-update/$', views.update_state,name="update-substep"),
)