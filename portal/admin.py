from django.contrib import admin

# Register your models here.
from import_export import resources
from .models import Test,AptQuestion,Student,Submit,Marked,Skip,Order,Finished,Answered
from import_export.admin import ImportExportModelAdmin

class AptQuestionResource(resources.ModelResource):

    class Meta:
        model = AptQuestion
        # import_id_fields = ('id',)
        # exclude = ('id', )
        fields = ('id','text','option1','option2','option3','option4','answer','section')

class AptQuestionAdmin(ImportExportModelAdmin):
	
	# raw_id_fields = ('questions',)
	list_filter = ('section',) 
	list_display = ('text',)

	resource_class = AptQuestionResource  

class TestAdmin(admin.ModelAdmin):
	filter_horizontal = ('questions',)
	list_filter = ('name',)


class StudentResource(resources.ModelResource):

    class Meta:
        model = Student
        import_id_fields = ('regno',)
        # exclude = ('id', )
        # fields = ('id','text','option1','option2','option3','option4','answer','section')

class StudentAdmin(ImportExportModelAdmin):
	
	list_filter = ('ugstream',)
	list_display = ('regno','QAscore','VRscore','LRscore',)



admin.site.register(Submit)
admin.site.register(Marked)
admin.site.register(Skip)
admin.site.register(Order)
admin.site.register(Finished)
admin.site.register(Answered)

admin.site.register(Student,StudentAdmin)    
admin.site.register(AptQuestion,AptQuestionAdmin)  	
