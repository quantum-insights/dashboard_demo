from .models import Invoice
import pandas as pd


class DataLoader():

    def load_data(self):

        print('Starting Data Loading...')

        file_path = '/Users/paul/PycharmProjects/customer_data/customer_shopping_data.csv'

        try:
            df= pd.read_csv(file_path)
        except Exception as e:
            print('e')
        print('File Found...')
        df.invoice_date = pd.to_datetime(df.invoice_date)

        print('DF Columns: \n', df.head())



        ls_invoices= []

        for index, (row, index, row) in enumerate(df.iterrows()):

            if index >= 100:
                break

            #print('Created Object ', index)

            invoice = Invoice(
                invoice_no = row['invoice_no'],
                customer_id= row['customer_id'],
                gender= row['gender'],
                age= row['age'],
                category = row['category'],
                quantity = row['quantity'],
                price = row['price'],
                payment_method= row['payment_method'],
                invoice_date= row['invoice_date'],
                shopping_mall= row['shopping_mall'])


            ls_invoices.append(invoice)

        Invoice.objects.bulk_create(ls_invoices)

        print('Data Loaded successfully!')




