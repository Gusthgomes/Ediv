from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .upload_file import ChunkUploadedFile
from .utils import is_video
from tinymce.widgets import TinyMCE
from .choices import ServiceTags
from .models import Budgets
from datetime import datetime
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from django.utils.safestring import mark_safe

def request_budget(request):
    if request.method == "GET":
        HTML_FIELD = TinyMCE().render(name='descricao', value='', attrs={'id': 'id_descricao'})
        return render(request, 'request_budget.html', {'HTML_FIELD': HTML_FIELD, 'services': ServiceTags.choices})
    
    elif request.method == "POST":
        file = request.FILES.get("file")
        service = request.POST.get("service")
        descricao = request.POST.get("descricao")
        if not is_video(file):
            raise HttpResponseBadRequest()
        
        file_upload = ChunkUploadedFile(file)
        file_path = file_upload.save_disk()
        
        budget = Budgets(
            file_path = file_path,
            data = datetime.now(),
            description = descricao,
            client = request.user,
        )
        
        budget.save()
        messages.add_message(request, constants.SUCCESS, mark_safe('Orçamento solicitado com sucesso, <a href="#"> clique aqui</a> para ver o status!'))
        return redirect(reverse('request_budget'))
