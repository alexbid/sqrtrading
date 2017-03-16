from django.contrib import admin

#from .models import Question
#from .models import Choice
from .models import signals
from .models import calendar
from .models import batch_run

#admin.site.register(Question)
#admin.site.register(Choice)
admin.site.register(signals)
admin.site.register(calendar)
admin.site.register(batch_run)