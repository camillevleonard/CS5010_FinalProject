import pandas as pd
import plotly.express as px
from plotly.offline import plot

#Req Data
data = pd.read_csv("../DataInput/MainData.csv")

def topState (numStates = 5, measure = 'Rate', gender = 'Both', drugType = 'All', 
              startYear = 2000, endYear = 2017, save = False):
    arguments = locals()
    validate = validateMe(arguments)
    
    if validate[0] == False:
        # This prints the validation message
        return(validate[1])
    else:
        print ("proceed with top state function")

        drugLookup = {
            'All': 561,
            'Opioid': 562,
            'Cocaine': 563,
            'Amphetamine': 564,
            }
        
            
        filterData = data[data.metric_name.eq(measure) & 
                             data.sex_name.eq(gender) &
                             (data.year <= endYear) &
                             (data.year >= startYear) &
                             data.cause_id.eq(drugLookup[drugType])]
        
        avgData = filterData.groupby(['location_name', 'sex_name', 'age_name', 'cause_name',
                                      'metric_name'])['val'].mean().reset_index()
        
        topEntries = avgData.nlargest(numStates, ['val'])
        
        if save:
            topEntries.to_csv('topEntries.csv')
            print("The .csv has been saved to the current directory")
            return(topEntries)
        else:
            return(topEntries)

def bottomState (numStates = 5, measure = 'Rate', gender = 'Both', drugType = 'All', 
              startYear = 2000, endYear = 2017, save = False):
    
    arguments = locals()
    validate = validateMe(arguments)
    
    if validate[0] == False:
        # This prints the validation message
        return(validate[1])
    else:
        print ("proceed with bottom state function")
    

        drugLookup = {
            'All': 561,
            'Opioid': 562,
            'Cocaine': 563,
            'Amphetamine': 564,
            }
        
            
        filterData = data[data.metric_name.eq(measure) & 
                             data.sex_name.eq(gender) &
                             (data.year <= endYear) &
                             (data.year >= startYear) &
                             data.cause_id.eq(drugLookup[drugType])]
        
        avgData = filterData.groupby(['location_name', 'sex_name', 'age_name', 'cause_name',
                                      'metric_name'])['val'].mean().reset_index()
        
        bottomEntries = avgData.nsmallest(numStates, ['val'])
        
        if save:
            bottomEntries.to_csv('bottomEntries.csv')
            print("The .csv has been saved to the current directory")
            return(bottomEntries)
        else:
            return(bottomEntries)


def stateHeatMap (year, measure = 'Rate', gender = 'Both', drugType = 'All'):
    
    arguments = locals()
    validate = validateMe(arguments)
    
    if validate[0] == False:
        # This prints the validation message
        return(validate[1])
    else:
        print ("proceed with stateHeatMap function")

        states = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
            }
    
        stateAbb = pd.DataFrame.from_dict(states, orient='index', columns=['location_name'])
        stateAbb['stateAbb'] = stateAbb.index
    
        withState = pd.merge(data, stateAbb, 'left')
    
        drugLookup = {
            'All': 561,
            'Opioid': 562,
            'Cocaine': 563,
            'Amphetamine': 564,
            }
        
        filterData = withState[withState.metric_name.eq(measure) & 
                               withState.sex_name.eq(gender) &
                               withState.year.eq(year) &
                               data.cause_id.eq(drugLookup[drugType])]
        
        fig = px.choropleth(locations=filterData.stateAbb, locationmode='USA-states', 
                            color=filterData.val, scope='usa', color_continuous_scale = 'sunsetdark')
        plot(fig, config={'displayModeBar': False})

##Query 4

def stateBarChart (state, measure = 'Rate', startYear = 2000, endYear = 2017, gender = 'Both'):
    arguments = locals()
    validate = validateMe(arguments)
    
    if validate[0] == False:
        # This prints the validation message
        return(validate[1])
    else:
        # print ("proceed with State Bar Chart function")
    
        filterData = data[data.location_name.eq(state) &
                          data.metric_name.eq(measure) &
                          data.sex_name.eq(gender) &
                          (data.year <= endYear) &
                          (data.year >= startYear) &
                          data.cause_id.isin([561, 562, 563, 564])].sort_values(by=['year'])
        
        if (endYear - startYear) > 0:
            fig = px.line(filterData, x='year', y='val', color='cause_name', 
                      title = 'Drug Related Deaths in ' + state + ' (' + measure + ')')
            plot(fig, config={'displayModeBar': False})
        else:
            fig = px.bar(filterData, x='cause_name', y='val', 
                         title = 'Drug Related Deaths in ' + state + ' (' + measure + ')')
            plot(fig, config={'displayModeBar': False})
        
    
###Allows one year
### Parameters: state, rate v number, start_year, end_year, gender
### Return: barchart for single year, line chart for time period greater than 1
        
def validateMe(dictArguments):
    
    returnValue = True
    returnMessage = ''
    
    
    # Setting up dictionary per the list of arguments that will be validated so that we can control the message
    numSate_dict = {
        "name" : "numStates",
        "values" : [],
        "message" : "Please pass the correct value for Number of States.Pick a number from 1 to 50.",
        "comparasion":"maxMin",
        "minVale":1,
        "maxValue":50,
        }    
    measure_dict = {
        "name" : "measure",
        "values" : ["Rate","Death"],
        "message" : "Please pass the correct value for Measure.",
        "comparasion":"static"
        }

    gender_dict = {
     "name" : "gender",
     "values" : ["Male","Female","Both"],
     "message" : "Please pass the correct value for Gender. Options are : Male, Female or Both",
     "comparasion":"static"
    }

    drugType_dict = {
     "name" : "drugType",
     "values" : ["All","Opioid","Cocaine","Amphetamine"],
     "message" : "Please pass the correct value for DrugType. Options are All, Opioid, Cocaine or Amphetamine",
     "comparasion":"static"
    }

    startYear_dict = {
     "name" : "startYear",
     "values" : [],
     "message" : "Please pass the correct value for Start Year. Pick a year from 2000 to 2017.",
     "comparasion":"maxMin",
        "minVale":2000,
        "maxValue":2017,
    }


    endYear_dict = {
     "name" : "endYear",
     "values" : [],
     "message" : "Please pass the correct value for End Year.Pick a year from 2000 to 2017.",
     "comparasion":"maxMin",
        "minVale":2000,
        "maxValue":2017,
    }
    # set up state dictionary so that we can do the validation. Idealy, this should come from sort of DB
    state_dict = {
     "name" : "state",
     "values" : ['Alaska',
                 'Alabama',
                 'Arkansas',
                 'American Samoa',
                 'Arizona',
                 'California',
                 'Colorado',
                 'Connecticut',
                 'District of Columbia',
                 'Delaware',
                 'Florida',
                 'Georgia',
                 'Guam',
                 'Hawaii',
                'Iowa',
                'Idaho',
                 'Illinois',
                'Indiana',
                 'Kansas',
                'Kentucky',
                'Louisiana',
                'Massachusetts',
                'Maryland',
                'Maine',
                'Michigan',
                'Minnesota',
                'Missouri',
                'Northern Mariana Islands',
                'Mississippi',
                'Montana',
                'National',
                'North Carolina',
                'North Dakota',
                'Nebraska',
                'New Hampshire',
                'New Jersey',
                'New Mexico',
                'Nevada',
                'New York',
                'Ohio',
                'Oklahoma',
                'Oregon',
                'Pennsylvania',
                'Puerto Rico',
                'Rhode Island',
                'South Carolina',
                'South Dakota',
                'Tennessee',
                'Texas',
                'Utah',
                'Virginia',
                'Virgin Islands',
                'Vermont',
                'Washington',
                'Wisconsin',
                'West Virginia',
                'Wyoming'],
     
     
     "message" : "Please pass the correct value for State.",
     "comparasion":"static"
    }



    # It could be the case that we don't want to validate all the arguments so setting up dictionary where we can control that . Also, setting up dynamic variables.
    argumentsToBeValidated = {
        "numStates" : numSate_dict,
        "measure"   : measure_dict,
        "gender" : gender_dict,
        "drugType"   : drugType_dict,
        "startYear" : startYear_dict,
        "endYear"   : endYear_dict,
        "state"   : state_dict

        }
    
    # default values for start and end year
    startYearValue = 2000
    endYearValue = 2017 
    
    # loop over only the arguments that are passed in
    for arg in dictArguments:
        # print(dictArguments[arg])
        # check if it matches the key that we are going to validate
        if arg in argumentsToBeValidated.keys():
            
            
            # STORE THE VALUE FOR START YEAR FOR LATER COMPARASION
            if arg == "startYear":
                startYearValue = dictArguments[arg]
            # STORE THE VALUE FOR END YEAR FOR LATER COMPARASION
            if arg == "endYear":
                endYearValue = dictArguments[arg]

            # capture the value that is passed in for the argument
            valueOfTheArgument = dictArguments[arg]
            # print(f"Name of the argument passed in is: {arg} AND Value passed in is: {valueOfTheArgument}")
            # check what kind of comparision we are going to do on the values 
            parameter = argumentsToBeValidated[arg]
            # print(f"parameter is: {parameter}")

            # CHECK STATIC VALUES
            if parameter["comparasion"] =="static":
                if valueOfTheArgument not in parameter["values"]:
                    # print(parameter["message"])
                    returnValue = False
                    returnMessage = parameter["message"]
                    break
                else:

                    pass
                
                
                
            # CHECK MAX MIN VALUES            
            if parameter["comparasion"] =="maxMin":
                if valueOfTheArgument >   parameter["maxValue"] or valueOfTheArgument <   parameter["minVale"]:
                    # print(f"Name of the argument passed in is: {arg} AND Value passed in is: {valueOfTheArgument}")
                    
                    returnValue = False
                    returnMessage = parameter["message"]
                    break
                else:
                    pass


            # OTHER CHECKS
            
            if startYearValue > endYearValue:
                returnValue = False
                returnMessage = "Start year cannot be greater than Start year. Please correct one of the values"
            else:
                pass
            
            if endYearValue < startYearValue:
                returnValue = False
                returnMessage = "End year cannot be less than Start year. Please correct one of the values"
            else:
                pass

    # return the value and a message
    return returnValue, returnMessage
        
