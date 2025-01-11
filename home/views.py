from django.shortcuts import render
from django.http import HttpResponse
from docx import Document
from io import BytesIO
import pypandoc
from docx import Document
from io import BytesIO
from docx2pdf import convert
from django.http import HttpResponse
import os
import tempfile
# Create your views here.

datavar = [
    {
        "firstName": "pratham",
        "lastName": "kubetkar",
        "age": 30,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 1000,
        "AmountPaid" : 500,
        "PlotType" : "Square"
    },
    {
        "firstName": "aniket",
        "lastName": "chavan",
        "age": 25,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 2000,
        "AmountPaid" : 1000,
        "PlotType" : "Rectangle"
    },
    {
        "firstName": "ritesh",
        "lastName": "bhagat",
        "age": 20,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 3000,
        "AmountPaid" : 1500,
        "PlotType" : "Circle"
    },
    {
        "firstName": "omkar",
        "lastName": "unde",
        "age": 35,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 4000,
        "AmountPaid" : 2000,
        "PlotType" : "Triangle"
    },
    {
        "firstName": "atharva",
        "lastName": "khatkar",
        "age": 40,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 5000,
        "AmountPaid" : 2500,
        "PlotType" : "Square"
    },
    {
        "firstName": "ashish",
        "lastName": "khatavkar",
        "age": 45,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 6000,
        "AmountPaid" : 3000,
        "PlotType" : "Rectangle"
    },
    {
        "firstName": "shantanu",
        "lastName": "bagade",
        "age": 50,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 7000,
        "AmountPaid" : 3500,
        "PlotType" : "Circle"
    },
    {
        "firstName": "akash",
        "lastName": "ganachari",
        "age": 55,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 8000,
        "AmountPaid" : 4000,
        "PlotType" : "Triangle"
    },
    {
        "firstName": "sagar",
        "lastName": "kuldharan",
        "age": 60,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 9000,
        "AmountPaid" : 4500,
        "PlotType" : "Square"
    },
    {
        "firstName": "sagar",
        "lastName": "kubetkar",
        "age": 60,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 9000,
        "AmountPaid" : 4500,
        "PlotType" : "Square"
    },
    {
        "firstName": "sagar",
        "lastName": "kulkarni",
        "age": 60,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 9000,
        "AmountPaid" : 4500,
        "PlotType" : "Square"
    },

]

def home(request):
    return render(request, 'home.html')

def data(request):
    if request.method == 'POST':
        queryName = request.POST.get('query')
        queryName = queryName.lower()
        if queryName:
            datalist = []
            for i in datavar:
                if i['firstName'] == queryName or i['lastName'] == queryName:
                    datalist.append(i)
            return render(request, 'data.html', {'data': datalist})
    return render(request ,'data.html')


def getInvoice(request):
    if request.method == "GET":
        # Extract data from the POST request
        data = {
            "firstName": request.GET.get("firstName"),
            "lastName": request.GET.get("lastName"),
            "age": request.GET.get("age"),
            "address": request.GET.get("address"),
            "city": request.GET.get("city"),
            "state": request.GET.get("state"),
            "zipcode": request.GET.get("zipcode"),
            "phone": request.GET.get("phone"),
            "TotalBill": request.GET.get("TotalBill"),
            "AmountPaid": request.GET.get("AmountPaid"),
            "PlotType": request.GET.get("PlotType"),
        }
    
        return render(request, 'invoice.html', data)
    
    return HttpResponse("Hello Nigga")



def printInvoice(request):
    if request.method == "GET" :
        # Extract data from the POST request
        data = {
            "firstName": request.GET.get('firstName'),
            "lastName": request.GET.get("lastName"),
            "age": request.GET.get("age"),
            "address": request.GET.get("address"),
            "city": request.GET.get("city"),
            "state": request.GET.get("state"),
            "zipcode": request.GET.get("zipcode"),
            "phone": request.GET.get("phone"),
            "TotalBill": request.GET.get("TotalBill"),
            "AmountPaid": request.GET.get("AmountPaid"),
            "PlotType": request.GET.get("PlotType"),
        }

        # Path to your Word template
        template_path = "C:/Users/Pratham/Desktop/Client2/env/project/templates/document.docx"

        # Load and replace placeholders in the Word document
        document = Document(template_path)
        for paragraph in document.paragraphs:
            for key, value in data.items():
                if f"{{{{ {key} }}}}" in paragraph.text:
                    paragraph.text = paragraph.text.replace(f"{{{{ {key} }}}}", str(value))

        # Save the modified document to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_docx:
            document.save(tmp_docx.name)
            tmp_docx.close()

            # Convert the Word document to PDF
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
                tmp_pdf.close()
                convert(tmp_docx.name, tmp_pdf.name)

                # Read the PDF file into memory
                with open(tmp_pdf.name, "rb") as pdf_file:
                    pdf_data = pdf_file.read()

                # Remove temporary files
                os.remove(tmp_docx.name)
                os.remove(tmp_pdf.name)

                # Return the PDF file as a downloadable response
                response = HttpResponse(pdf_data, content_type="application/pdf")
                response["Content-Disposition"] = f'attachment; filename="Invoice_{data["firstName"]}_{data["lastName"]}.pdf"'

                return response

    return HttpResponse("Invalid request")