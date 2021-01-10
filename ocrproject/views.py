from django.views import View
from django.http import HttpResponse


class Index(View):
    
    def get(self, request):
        """
        Display the form for uplaoding the pancard
        Args: Request django request 
        Returns:
            Form Django template
        """
        return HttpResponse("Welcome to OCR Project")
    
    def post(self, request):
        """
        To process the uploaded pamcard using tessaract
        """
        return HttpResponse("Welcome to OCR Project")
