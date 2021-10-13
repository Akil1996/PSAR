from django.http.response import JsonResponse
from django.shortcuts import render
from .detailedreport import dreport_main
from .plreport import plreport_main
from .reportgeneration import report_generation_main
# Create your views here.

def backtest_home(request):
    return render(request, "backtesthome.html", {})

def plreport_home(request):
    return render(request, "plreporthome.html", {})

def backtest_result(request):
    if request.method == "GET":
        stockName = (request.GET.get('stockName'))
        fund = int(request.GET.get('fund'))
        psarStart = (request.GET.get('psarStart'))
        psarIncrement = float(request.GET.get('psarIncrement'))
        psarMaxvalue = float(request.GET.get('psarMaxvalue'))
        timeFrame = (request.GET.get('timeFrame'))
        fromDate = (request.GET.get('fromDate'))
        toDate = (request.GET.get('toDate'))
        result_df = dreport_main(stockName, psarStart, psarIncrement, psarMaxvalue, timeFrame, fromDate, toDate)
        pl_df = plreport_main(stockName, psarStart, psarIncrement, psarMaxvalue, timeFrame, fromDate, toDate, fund)
        # report_dic = report_generation_main(pl_df, fund, fromDate, toDate)
        # print(result_df)
        # print("##############################")
        # print(pl_df)
        # print("##############################")
        # print(report_dic)
        # context = {
        #         "result" :result_df,
        #         "pl_df" : pl_df,
        #         "report_dic": report_dic,
        #     }
        context = {
            "result" :result_df,
            "pl_df" : pl_df,
            "s": 's'
        }
        return JsonResponse(context)   
    

    

