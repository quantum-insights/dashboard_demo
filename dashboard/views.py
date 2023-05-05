from django.shortcuts import render
from demo.models import Demo, Invoice
import pandas as pd
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objs as go
from demo.load_invoice import DataLoader
# Create your views here.

def index(request):

    #try:
    #    dl= DataLoader()
    #    dl.load_data()
    #except Exception as e:
    #    print(e)

    invoice_objects= Invoice.objects.all()
    invoice_data= [
        {
            'date': x.invoice_date,
            'price': x.price,
            'shopping_mall': x.shopping_mall,
        } for x in invoice_objects
    ]

    df = pd.DataFrame(invoice_data)

    df_daily_revenue= df.groupby('date')['price'].sum().reset_index()

    # index needs to be reseted => plotly express cannot handle shopping mal as index
    df_mall_revenue= df.groupby('shopping_mall')['price'].sum().reset_index()

    print(df_mall_revenue.head())

    fig_line = px.line(
        df_daily_revenue, x= 'date', y= 'price', title= 'Daily Revenue'
    )

    fig_pie= px.pie(df_mall_revenue, values='price', names='shopping_mall', title= 'Revenue per Mall')

    line_plot= plot(fig_line, output_type= 'div')
    pie_plot= plot(fig_pie, output_type= 'div')
    context = {
        'text': 'some random text from plotly',
        'line_div': line_plot,
        'pie_div': pie_plot,
    }

    return render(request, 'index.html', context)
