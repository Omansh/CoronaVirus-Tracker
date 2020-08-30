from django.shortcuts import render



def home(request):
    import json
    import requests

    api_request = requests.get("https://api.covid19api.com/world/total")


    try:
        api=json.loads(api_request.content)


    except Exception as e:
        api="Error..."

    Info = ['TotalConfirmed','TotalDeaths','TotalRecovered']

    values = [api['TotalConfirmed'],api['TotalDeaths'],api['TotalRecovered']]
    #TotalConfirmed = api['TotalConfirmed']
    #TotalDeaths = api['TotalDeaths']
    #TotalRecovered = api['TotalRecovered']




    return render(request, 'caselookup/home.html', {'api':api,
                                         'Info':Info,
                                         'values':values,
                                         'title' : 'Home',
                                        })




def CountrywiseStats(request):
    import json
    import requests

    if request.method == "POST":
        country = request.POST['country']
        api_request = requests.get("https://covid-19.dataflowkit.com/v1/"+ country +"")

        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api = "Error..."


        Active_Cases = api['Active Cases_text']
        Country = api['Country_text']
        Last_Checked = api['Last Update']
        New_Cases = api['New Cases_text']
        New_Deaths = api['New Deaths_text']
        Total_Cases = api['Total Cases_text']
        Total_Deaths = api['Total Deaths_text']
        Total_Recovered = api['Total Recovered_text']

        labels = ['Active_Cases','New_Cases','New_Deaths','Total_Cases','Total_Deaths','Total_Recovered']

        label_values = [api['Active Cases_text'],api['New Cases_text'],api['New Deaths_text'],api['Total Cases_text'],api['Total Deaths_text'],api['Total Recovered_text']]

        return render(request, 'caselookup/countrywisecases.html', {'api':api,
                                                         'Active_Cases':Active_Cases,
                                                         'Country':Country,
                                                         'Last_Checked':Last_Checked,
                                                         'New_Cases':New_Cases,
                                                         'New_Deaths':New_Deaths,
                                                         'Total_Cases':Total_Cases,
                                                         'Total_Deaths':Total_Deaths,
                                                         'Total_Recovered':Total_Recovered,
                                                         'labels' : labels,
                                                         'label_values' : label_values,

                                                         })
    else:

        api_request = requests.get("https://covid-19.dataflowkit.com/v1/:country")

        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api = "Error..."


        Active_Cases = api['Active Cases_text']
        Country = api['Country_text']
        Last_Checked = api['Last Update']
        New_Cases = api['New Cases_text']
        New_Deaths = api['New Deaths_text']
        Total_Cases = api['Total Cases_text']
        Total_Deaths = api['Total Deaths_text']
        Total_Recovered = api['Total Recovered_text']

        labels = ['Active_Cases','New_Cases','New_Deaths','Total_Cases','Total_Deaths','Total_Recovered']

        label_values = [api['Active Cases_text'],api['New Cases_text'],api['New Deaths_text'],api['Total Cases_text'],api['Total Deaths_text'],api['Total Recovered_text']]

        return render(request, 'caselookup/countrywisecases.html', {'api':api,
                                                         'Active_Cases':Active_Cases,
                                                         'Country':Country,
                                                         'Last_Checked':Last_Checked,
                                                         'New_Cases':New_Cases,
                                                         'New_Deaths':New_Deaths,
                                                         'Total_Cases':Total_Cases,
                                                         'Total_Deaths':Total_Deaths,
                                                         'Total_Recovered':Total_Recovered,
                                                         'labels' : labels,
                                                         'label_values' : label_values,

                                                         })

def statewisecases(request):
    import json
    import requests

    statewisecases_api_url = requests.get("https://covid-india-cases.herokuapp.com/states/")

    try:
        statewisecases_api_data = json.loads(statewisecases_api_url.content)

    except Exception as e:

        statewisecases_api_data = "Error..."


    states = []
    deaths = []
    noOfCases = []
    cured = []

    i=0
    while i<len(statewisecases_api_data):
        states.append(statewisecases_api_data[i]['state'])
        deaths.append(statewisecases_api_data[i]['deaths'])
        noOfCases.append(statewisecases_api_data[i]['noOfCases'])
        cured.append(statewisecases_api_data[i]['cured'])
        i+=1




    return render(request, 'caselookup/statewisecases.html', {'statewisecases_api_data' : statewisecases_api_data, 
                                                    'states' : states,
                                                    'deaths' : deaths,
                                                    'noOfCases' : noOfCases,
                                                    'cured' : cured,

                                                    })



def casestimeline(request):

    import requests
    import json

    cases_timeline_api_url = requests.get("https://api.covid19india.org/data.json")

    try:
        case_timeline_data = json.loads(cases_timeline_api_url.content)

    except Exception as e:
        case_timeline_data = "Error..."

    dates = []
    cases_reported_each_day = []

    i=0
    while i<len(case_timeline_data['cases_time_series']):
        dates.append(case_timeline_data['cases_time_series'][i]['date'])
        cases_reported_each_day.append(case_timeline_data['cases_time_series'][i]['totalconfirmed'])
        i+=7








    return render(request, 'caselookup/casestimeline.html', {'case_timeline_data':case_timeline_data,
                                                  'dates':dates,
                                                  'cases_reported_each_day':cases_reported_each_day
                                                  })