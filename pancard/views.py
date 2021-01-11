from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

from .forms import UploadPancard
from .utils import handle_uploaded_file




class PancardActions(View):
    
    def get(self, request):
        """
        Display the form for uplaoding the pancard
        Args: Request django request 
        Returns:
            Form Django template
        """
        return render(request, "pancard_upload.html")
    
    def post(self, request):
        """
        To process the uploaded pamcard using tessaract
        """
        data = handle_uploaded_file(request.FILES['file'])
        if data:
            return render(request, "pancard_details.html", {
                "results": data
            })
        else:
            return render(request, 'error.html', status=400)
