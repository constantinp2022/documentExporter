from django.shortcuts import render, redirect
from django.conf import settings
from django.db.models import F
from django.contrib import messages
from .forms import DeafaultTemplateForm, NewTemplateForm
from .models import Default_Templates
from user.models import Profile
from io import BytesIO
import sys
import subprocess
import re

from django.http import HttpResponse
#from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

#Change path to parent directory for aneasier acces to files
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from employee.models import Employees

#Convert from docx to pdf
def convert_to(folder, source, timeout=None):
    args = ['libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', folder, source]

    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    filename = re.search('-> (.*?) using filter', process.stdout.decode())

    if filename is None:
        raise LibreOfficeError(process.stdout.decode())
    else:
        return filename.group(1)


def default_tmpl_home(request):
    employee = Employees.objects.all()
    default_tmpl = Default_Templates.objects.all()

    if request.method == 'POST':
        form = DeafaultTemplateForm(data=request.POST)
        if form.is_valid():
            doctype = form.cleaned_data['format']

            employee_id = form.data['employee']
            default_tmpl_id = form.data['default_tmpl']

            employee = Employees.objects.get(pk=employee_id)
            default_tmpl = Default_Templates.objects.get(pk=default_tmpl_id)

            context_data = {
                'employee': employee,
            }

            docx_title = 'generated_document' + '.docx'
            pdf_title = 'generated_document' + '.pdf'

            # Update the number of documents exported
            logged_user = request.user
            logged_profile = Profile.objects.get(user_id=logged_user.id)
            logged_profile.nr_documents = logged_profile.nr_documents + 1
            logged_profile.save()

            # Take the template
            template = DocxTemplate(default_tmpl.template_file.path)

            template.render(context_data)

            template.save('document-generat.docx')

            if doctype == 'docx':
                #response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                f = BytesIO()
                template.save(f)
                length = f.tell()
                f.seek(0)
                response = HttpResponse(
                    f.getvalue(),
                    content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                )
                response['Content-Disposition'] = 'attachment; filename=' + docx_title
                response['Content-Length'] = length
                return response
            if doctype == 'pdf':
                convert_to(settings.BASE_DIR + '/media/wip/','document-generat.docx')

                file = open(settings.BASE_DIR + '/media/wip/' + 'document-generat.pdf', "rb")
                f = BytesIO(file.read())

                length = f.tell()
                f.seek(0)

                response = HttpResponse(
                    f.getvalue(),
                    content_type='application/pdf'
                )
                response['Content-Disposition'] = 'attachment; filename=' + pdf_title
                #response['Content-Length'] = length
                return response
    else:
        form = DeafaultTemplateForm()

    template_name = "default_tmpl-home.html"
    context = {
        'form': form,
        'employee': employee,
        'default_tmpl': default_tmpl,
    }
    return render(request, template_name, context)


def new_default_tmpl(request):
    if request.method == 'POST':
        template_form = NewTemplateForm(request.POST,
                                    request.FILES)
        if  template_form.is_valid():
            template_form.save()
            messages.success(request, f'Template stored!')
            return redirect('default_tmpl:home')

    else:
        template_form = NewTemplateForm()

    context = {
        'template_form': template_form,
    }

    return render(request, "new_default_tmpl.html", context)