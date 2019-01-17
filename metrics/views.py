from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
import json
import pandas as pd


def homepage(request):
    the_data = pd.read_csv('static/tester_data/fortune1000.csv')
    #group data by deparment
    sector = the_data.groupby('Sector').sum()
    group_list = sector['Revenue']
    result =  group_list.to_json(orient='columns')





    '''
    render homepage template
    '''
    args_to_template = {
            "result": json.loads(result)

    }
    return render(request, 'metrics/homepage.html', args_to_template)


def load_data():
    sector = pd.read_csv('static/tester_data/fortune1000.csv')
    df = sector.groupby('Sector' )['Revenue','Profits','Employees'].sum()
    df_as_json = df.to_dict()
    total_revenue = sector['Revenue'].sum()
    total_profits = sector['Profits'].sum()
    total_empt = sector['Employees'].sum()
    total_sectors= sector['Sector'].nunique()
    total_companies= sector['Company'].nunique()
    total_industries= sector['Industry'].nunique()
    new_obj ={
            "total_sectors": total_sectors,
            "total_companies":total_companies,
            "total_industries":total_industries,
            "total_revenue":total_revenue,
            "total_profits":total_profits,
            "total_empt":total_empt,
    }
    for item in df_as_json:
        new_obj[item] = []
        for key,value in df_as_json[item].items():
            result = {
                    'label':key,
                    "value":value,

            }
            new_obj[item].append(result)
            # new_obj[item]['labels'].append(key)
            # new_obj[item]['values'].append(value)

        #pprint(key)


    return new_obj


class homepageData(APIView):
    authentication_classes = []
    permission_classes = []
    #get python Response

    def get(self, request, format=None):

        the_data = load_data()
        data =  the_data
        return Response(data)





