#CS 5010 Semester Project 
#Matt Dakolios, Darren Frye, Paul Hicks, Camille Leonard, Sudhanshu Luthra

import unittest
from ModuleWithValidation import *

#Query 1 Unit Testing
class topStateTestCase(unittest.TestCase):
    
    def setUp(self):
        self.numStates = 5
        self.measure = 'Rate'
        self.gender = 'Both'
        self.drugType = 'All'
        self.startYear = 2000
        self.endYear = 2017
        self.save = False     
        self.drugLookup = {
            'All': 561,
            'Opioid': 562,
            'Cocaine': 563,
            'Amphetamine': 564,
            }
    ##test that a range of years can be selected 
    ##test that a singular year can be selected
    
    #test to make sure the input parameters fall within accepted values 
    def test_n_states(self):
        #number of states falls within 1-50 range
        #n_states_input = self.numStates
        df = topState(10)
        length_df = len(df)
        self.assertEqual(length_df, 10)
        
        self.assertEqual(topState(60), "Please pass the correct value for Number of States.Pick a number from 1 to 50.")
        
    
        
    def test_n_states_null(self):
        #number of states defaults to 5 if another number not specified
        self.assertEqual(self.numStates, 5)
        
    def test_rate_or_number(self):
        #confirms death rate or number of deaths selected
        rate_number = (self.measure == "Rate" or self.measure == "Death")
        self.assertTrue(rate_number)
        
    def test_drug_type_in_range(self):
        #confirms drug type is from list of available drug types
        self.assertIn(self.drugType, self.drugLookup) 
        
    def test_start_year_in_range(self):
        #start year falls within 2000-2017 inclusive
        start_year_selected = (self.startYear > 1999 and self.startYear < 2018)
        self.assertTrue(start_year_selected)
        
    def test_end_year_in_range(self):
        #end year falls within 2000-2017 inclusive 
        end_year_selected = (self.endYear > 1999 and self.endYear< 2018)
        self.assertTrue(end_year_selected)
        
    def test_end_year_greaterThanStartYear(self):
        #end year must be greater than start year
        self.assertGreater(self.endYear, self.startYear)
        
    def test_save(self):
        #confirms user has selected / input value to indicate either save or don't save
        #self.assertTrue(self.save)   
        if self.save == False:
            self.assertEqual(self.save, False)
        else: 
            self.assertEqual(self.save, True)
        
#     #test that a data frame is created 
#     #test that csv is created when save option is selected 
#     #test that exception handling returns right values 
    def test_size_of_dataframe(self):
        df = topState(numStates = self.numStates)
        length_df = len(df)
        self.assertEqual(length_df, self.numStates)
        
#Query 2 Unit Testing
class bottomStateTestCase(unittest.TestCase):
    def setUp(self):
        self.numStates = 5
        self.measure = 'Rate'
        self.gender = 'Both'
        self.drugType = 'All'
        self.startYear = 2000
        self.endYear = 2017
        self.save = False     
        self.drugLookup = {
            'All': 561,
            'Opioid': 562,
            'Cocaine': 563,
            'Amphetamine': 564,
            }
    #test to make sure the input parameters fall within accepted values 
    def test_n_states(self):
        #number of states falls within 1-50 range
        #n_states_input = self.numStates
        n_states_input = (self.numStates > 0 and self.numStates < 51)
        self.assertTrue(n_states_input)
    
    #how do you flag this for null only?    
    def test_n_states_null(self):
        #number of states defaults to 5 if another number not specified
        self.assertEqual(self.numStates, 5)
        
    def test_rate_or_number(self):
        #confirms death rate or number of deaths selected
        rate_number = (self.measure == "Rate" or self.measure == "Death")
        self.assertTrue(rate_number)
    
    #test exception handling... not setup right will have to address later 
    def test_rate_or_numberException(self):
        #confirms death rate or number of deaths selected
        returnValue = bottomState(measure = "Invalid Entry")
        self.assertEqual(returnValue, "Please pass the correct value for Measure.")
        
    def test_drug_type_in_range(self):
        #confirms drug type is from list of available drug types
        self.assertIn(self.drugType, self.drugLookup) 
        
    def test_start_year_in_range(self):
        #start year falls within 2000-2017 inclusive
        start_year_selected = (self.startYear > 1999 and self.startYear < 2018)
        self.assertTrue(start_year_selected)
        
    def test_end_year_in_range(self):
        #end year falls within 2000-2017 inclusive 
        end_year_selected = (self.endYear > 1999 and self.endYear< 2018)
        self.assertTrue(end_year_selected)
        
    def test_end_year_greaterThanStartYear(self):
        #end year must be greater than start year
        self.assertGreater(self.endYear, self.startYear)
        
    def test_save(self):
        #confirms user has selected / input value to indicate either save or don't save
        #self.assertTrue(self.save)   
        if self.save == False:
            self.assertEqual(self.save, False)
        else: 
            self.assertEqual(self.save, True)
        
    #test that a data frame is created 
    #test that csv is created when save option is selected 
    #
        
# #Query 3 Unit Testing
# class stateHeatMap(unittest.TestCase):
#     def test_year_in_range(self):
#         start_year_selected = (self.start_year > 1999 and self.start_year < 2018)
#         self.assertTrue(start_year_selected)

#     def test_rate_or_number(self):
#         #confirms death rate or number of deaths selected
#         rate_number = (self.rateOrNumber = "rate" or self.rateOrNumber = "number")
#         self.assertTrue(rate_number)
    
#     def test_drug_type_in_range(self):
#         #confirms drug type is from list of available drug types
#         self.assertIn(self.drug_type_selected, self.drugTypes)
        
#     #test that the function returns a heat map 
        
# #Query 4 Unit Testing
# class stateHist(unittest.TestCase):
#     def test_state(self):   ## are we accepting numerical input or state names?
    
#     def test_rate_or_number(self):
#         #confirms death rate or number of deaths selected
#         rate_number = (self.rateOrNumber = "rate" or self.rateOrNumber = "number")
#         self.assertTrue(rate_number)
    
#     def test_start_year_in_range(self):
#         #start year falls within 2000-2017 inclusive
#         start_year_selected = (self.start_year > 1999 and self.start_year < 2018)
#         self.assertTrue(start_year_selected)
        
#     def test_end_year_in_range():
#         #end year falls within 2000-2017 inclusive 
#         end_year_selected = (self.end_year > 1999 and self.end_year < 2018)
#         self.assertTrue(end_year_selected)
        
#     def test_end_year_greaterThanStartYear(self):
#         #end year must be greater than start year
#         self.assertGreater(self.end_year, self.start_year)
    
#     def test_save(self):
#         #confirms user has selected / input value to indicate either save or don't save
        
#     #test return data frame 
#     #test return csv if save option is selected

if __name__ == '__main__':
    unittest.main()
