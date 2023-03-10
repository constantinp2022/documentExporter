from django.db import models

class Default_Templates(models.Model):
	template_name = models.CharField(max_length=255)
	template_file = models.FileField(default='default.docx', upload_to='template_files')
	template_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.template_name
