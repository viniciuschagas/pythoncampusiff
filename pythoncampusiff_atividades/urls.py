from django.conf.urls.defaults import *

urlpatterns = patterns('pythoncampusiff_atividades.views',
    (r'^minicursos_da_manha$', 'gerar_minicursos_da_manha'),
    (r'^minicursos_da_tarde$', 'gerar_minicursos_da_tarde'),
)