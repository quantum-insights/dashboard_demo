from django.shortcuts import render
from demo.models import Demo
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from demo.load_invoice import DataLoader
# Create your views here.

def index(request):

    try:
        dl= DataLoader()
        dl.load_data()
    except Exception as e:
        print(e)

    qs= Demo.objects.all()
    demo_data= [
        {
            'demo': x.name,
            'start': x.start_date,
            'end': x.end_date,
            'responsible': x.responsible.username
        } for x in qs
    ]

    df = pd.DataFrame(demo_data)

    fig = px.timeline(
        df, x_start= 'start', x_end= 'end', y= 'demo', color= 'responsible'
    )

    fig.update_yaxes(autorange= 'reversed')
    gantt_plot= plot(fig, output_type= 'div')
    context = {'plot_div': gantt_plot}

    return render(request, 'index.html', context)
