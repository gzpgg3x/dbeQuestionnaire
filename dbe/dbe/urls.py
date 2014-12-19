from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from dbe.questionnaire.views import *
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dbe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    # (r"^done/$", "simple.direct_to_template", dict(template="questionnaire/done.html"), "done"),
    # (r"^done/$", "simple.direct_to_template", dict(template="questionnaire/done.html"), "done"),
    (r'^$', TemplateView.as_view(template_name="questionnaire/done.html")),
)

urlpatterns += patterns("dbe.questionnaire.views",
    (r"^$", login_required(Questionnaires.as_view()), {}, "questionnaires"),

    (r"^questionnaire/(?P<dpk>\d+)/(?P<section>\d+)/$",
     login_required( ViewQuestionnaire.as_view() ), {}, "questionnaire"),

    (r"^questionnaire/(?P<dpk>\d+)/$",
     login_required( ViewQuestionnaire.as_view() ), {}, "questionnaire"),

    (r"^user-questionnaires/(?P<dpk>\d+)/$",
     login_required( UserQuests.as_view() ), {}, "user_questionnaires"),

    (r"^user-questionnaire/(?P<dpk>\d+)/$",
     login_required( UserQuest.as_view() ), {}, "user_questionnaire"),

    (r"^quest-stats/(?P<dpk>\d+)/$",
     login_required( QuestStats.as_view() ), {}, "quest_stats"),
)



