from django.shortcuts import render

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

]

def home(request):
    return render(request, 'home.html')

def data(request):
    queryName = request.POST.get('query')
    queryName = queryName.lower()
    if queryName:
        datalist = []
        for i in datavar:
            if i['firstName'] == queryName or i['lastName'] == queryName:
                datalist.append(i)
        return render(request, 'data.html', {'data': datalist})
    return render(request ,'data.html')