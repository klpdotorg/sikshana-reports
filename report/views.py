from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Sum
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie

from report.models import *
import report

# Create your views here.

@csrf_exempt
def main(request):
    if request.method == 'GET':
        topframe={'district':[],'block':[],'cluster':[],'school_id':[],'school_name':[],'clas':[],'total_students':[],'math_above_average':[],'math_average':[],'math_minimum':[],'math_below_minimum':[],'kannada_above_Average':[],'kannada_average':[],'kannada_minimum':[],'kannada_below_minimum':[]}
        topframe['district']=[row.district for row in schools_master.objects.all().distinct('district')]
        topframe['block']=['|'.join([row.district,row.block]) for row in schools_master.objects.all().distinct('district','block')]
        topframe['cluster']=['|'.join([row.block,row.cluster]) for row in schools_master.objects.all().distinct('block','cluster')]
        topframe['school_name']=['|'.join([row.cluster,row.school_name]) for row in schools_master.objects.all().distinct('cluster','school_name')]
        topframe['school_id']=[row.school_id for row in schools_master.objects.all().distinct('school_id')]
        topframe['clas']=[row.clas for row in schools_master.objects.all().distinct('clas')]
        topframe['math']=['overall','math_above_average','math_average','math_minimum','math_below_minimum']
        topframe['kannada']=['overall','kannada_above_average','kannada_average','kannada_minimum','kannada_below_minimum']
        return render(request,'index.html',topframe)
    elif request.method == 'POST':
        parent={'school':'cluster','cluster':'block','block':'district','district':'state','state':'state'}
        typ=request.POST['type']
        if typ != 'All District':
            clas=request.POST['clas']
            name_child=str(request.POST[typ])
        else:
            typ = 'state'
            clas='7'
            name_child='all'        
        try:
            name_parent=str(request.POST[parent[typ]])
        except:
            name_parent='all'
        table_child = getattr(report.models,str(typ+'_aggregation'))
        table_parent = getattr(report.models,str(parent[typ]+'_aggregation'))
        data_child=[]
        data_parent=[]
        data=[]
        if name_child not in ['District','Block','Cluster','School']:
            for row in table_child.objects.all().filter(name=name_child, clas=clas):
                data_child.append('|'.join(['math','math_above_average',"%.2f" % (row.math_above_average*100/float(row.total))]))
                data_child.append('|'.join(['math','math_average',"%.2f" % (row.math_average*100/float(row.total))]))
                data_child.append('|'.join(['math','math_minimum',"%.2f" % (row.math_minimum*100/float(row.total))]))
                data_child.append('|'.join(['math','math_below_minimum',"%.2f" % (row.math_below_minimum*100/float(row.total))]))
                data_child.append('|'.join(['kannada','kannada_above_average',"%.2f" % (row.kannada_above_average*100/float(row.total))]))
                data_child.append('|'.join(['kannada','kannada_average',"%.2f" % (row.kannada_average*100/float(row.total))]))
                data_child.append('|'.join(['kannada','kannada_minimum',"%.2f" % (row.kannada_minimum*100/float(row.total))]))
                data_child.append('|'.join(['kannada','kannada_below_minimum',"%.2f" % (row.kannada_below_minimum*100/float(row.total))]))
                data_child.append('|'.join(['total',str(row.total),'']))
                data_child.append('|'.join(['kannada','overall',"%.2f" % ((row.kannada_above_average+row.kannada_average+row.kannada_minimum)*100/float(row.total))]))
                data_child.append('|'.join(['math','overall',"%.2f" % ((row.math_above_average+row.math_average+row.math_minimum)*100/float(row.total))]))
            for row in table_parent.objects.all().filter(name=name_parent, clas=clas):
                data_parent.append('|'.join(['math','math_above_average',"%.2f" % (row.math_above_average*100/float(row.total))]))
                data_parent.append('|'.join(['math','math_average',"%.2f" % (row.math_average*100/float(row.total))]))
                data_parent.append('|'.join(['math','math_minimum',"%.2f" % (row.math_minimum*100/float(row.total))]))
                data_parent.append('|'.join(['math','math_below_minimum',"%.2f" % (row.math_below_minimum*100/float(row.total))]))
                data_parent.append('|'.join(['kannada','kannada_above_average',"%.2f" % (row.kannada_above_average*100/float(row.total))]))
                data_parent.append('|'.join(['kannada','kannada_average',"%.2f" % (row.kannada_average*100/float(row.total))]))
                data_parent.append('|'.join(['kannada','kannada_minimum',"%.2f" % (row.kannada_minimum*100/float(row.total))]))
                data_parent.append('|'.join(['kannada','kannada_below_minimum',"%.2f" % (row.kannada_below_minimum*100/float(row.total))]))
                data_parent.append('|'.join(['total',str(row.total),'']))
                data_parent.append('|'.join(['kannada','overall',"%.2f" % ((row.kannada_above_average+row.kannada_average+row.kannada_minimum)*100/float(row.total))]))
                data_parent.append('|'.join(['math','overall',"%.2f" % ((row.math_above_average+row.math_average+row.math_minimum)*100/float(row.total))]))
            data=[data_child,data_parent]
            print data
        return HttpResponse(json.dumps(data), content_type="application/json")

def about(request):
    return render(request,'about.html')