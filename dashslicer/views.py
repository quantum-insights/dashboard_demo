from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from demo.models import Demo, Invoice
import pandas as pd
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objs as go
from demo.load_invoice import DataLoader
# Create your views here.

def dash(request):

    context= {
        'text': 'Some random text from the slicer'
    }

    return render(request, 'index.html', context)
