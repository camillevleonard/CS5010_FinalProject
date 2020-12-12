#CS 5010 Semester Project 
#Matt Dakolios, Darren Frye, Paul Hicks, Camille Leonard, Sudhanshu Luthra

import unittest
from Module import *

#Query 1 Unit Testing
class topStateTestCase(unittest.TestCase):
    
    def test_n_states_null(self): #validate that the null returns a df with 5 rows
        dfNull = topState()
        lengthNull = len(dfNull)
        self.assertEqual(lengthNull, 5)
        
    def test_n_states(self):
        #number of states falls within 1-50 range
        df = topState(10)
        length_df = len(df)
        self.assertEqual(length_df, 10)
        
    def test_n_states_exception(self): #test exception handling for edge cases of number of states
        self.assertEqual(topState(-1), "Please pass the correct value for Number of States.Pick a number from 1 to 50.")
        self.assertEqual(topState(0), "Please pass the correct value for Number of States.Pick a number from 1 to 50.")
        self.assertEqual(topState(51), "Please pass the correct value for Number of States.Pick a number from 1 to 50.")
        
    def test_measure_exception(self): #test edge cases of measure exception (correct options are "Rate" or "Deaths")
        self.assertEqual(topState(10, " "), "Please pass the correct value for Measure.")
        self.assertEqual(topState(10, "rate"), "Please pass the correct value for Measure.")
        self.assertEqual(topState(10, "test"), "Please pass the correct value for Measure.")
        
    def test_topState_return_df(self): #test that a data frame object is returned by topState
        df_topState = topState()
        self.assertIsInstance(df_topState, object)
    
    def test_gender_exception(self): #test exception handling of edge cases of gender parameter
        self.assertEqual(topState(10, "Rate", "male" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")
        self.assertEqual(topState(10, "Rate", "female" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")
        self.assertEqual(topState(10, "Rate", "both" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")
        self.assertEqual(topState(10, "Rate", "test" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")

    def test_drugType_exception(self): #test exception handling for edge cases of drug type parameter 
        self.assertEqual(topState(10, "Rate", "Both", "Beer"), "Please pass the correct value for DrugType. Options are All, Opioid, Cocaine or Amphetamine") 
        
    def test_startYear_exception(self): #test exception handling for edge cases of startYear parameter
        self.assertEqual(topState(10, "Rate", "Both", "All", 1999), "Please pass the correct value for Start Year. Pick a year from 2000 to 2017.")
        self.assertEqual(topState(10, "Rate", "Both", "All", 2018), "Please pass the correct value for Start Year. Pick a year from 2000 to 2017.")
    
    def test_endYear_exception(self): #test exception handling for edge cases of endYear parameter
        self.assertEqual(topState(10, "Rate", "Both", "All", 2000, 2018), "Please pass the correct value for End Year.Pick a year from 2000 to 2017.")
        self.assertEqual(topState(10, "Rate", "Both", "All", 2005, 2004), "End year cannot be less than Start year. Please correct one of the values") 
        self.assertEqual(topState(10, "Rate", "Both", "All", 2000, 1999), "Please pass the correct value for End Year.Pick a year from 2000 to 2017.")
    
#Query 2 Unit Testing
class bottomStateTestCase(unittest.TestCase):
    
    def test_n_states_null(self):  #test exception handling for edge cases of number of states
        dfNull = bottomState()
        lengthNull = len(dfNull)
        self.assertEqual(lengthNull, 5)
        
    def test_n_states(self): #number of states falls within 1-50 range
        df = bottomState(10)
        length_df = len(df)
        self.assertEqual(length_df, 10)
        
    def test_n_states_exception(self): #test exception handling for edge cases of number of states
        self.assertEqual(bottomState(-1), "Please pass the correct value for Number of States.Pick a number from 1 to 50.")
        self.assertEqual(bottomState(0), "Please pass the correct value for Number of States.Pick a number from 1 to 50.")
        self.assertEqual(bottomState(51), "Please pass the correct value for Number of States.Pick a number from 1 to 50.")
        self.assertEqual(bottomState(60), "Please pass the correct value for Number of States.Pick a number from 1 to 50.")
        
    def test_measure_exception(self): #test edge cases of measure exception (correct options are "Rate" or "Deaths")
        self.assertEqual(bottomState(10, " "), "Please pass the correct value for Measure.")
        self.assertEqual(bottomState(10, "rate"), "Please pass the correct value for Measure.")
        self.assertEqual(bottomState(10, "test"), "Please pass the correct value for Measure.")
        
    def test_bottomState_return_df(self): #test that a data frame object is returned by bottomState
        df_bottomState = bottomState()
        self.assertIsInstance(df_bottomState, object)
    
    def test_gender_exception(self): #test exception handling of edge cases of gender parameter
        self.assertEqual(bottomState(10, "Rate", "male" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")
        self.assertEqual(bottomState(10, "Rate", "female" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")
        self.assertEqual(bottomState(10, "Rate", "both" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")
        self.assertEqual(bottomState(10, "Rate", "test" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")

    def test_drugType_exception(self): #test exception handling for edge cases of drug type parameter 
        self.assertEqual(bottomState(10, "Rate", "Both", "Beer"), "Please pass the correct value for DrugType. Options are All, Opioid, Cocaine or Amphetamine") 
        
    def test_startYear_exception(self): #test exception handling for edge cases of startYear parameter
        self.assertEqual(bottomState(10, "Rate", "Both", "All", 1999), "Please pass the correct value for Start Year. Pick a year from 2000 to 2017.")
        self.assertEqual(bottomState(10, "Rate", "Both", "All", 2018), "Please pass the correct value for Start Year. Pick a year from 2000 to 2017.")
    
    def test_endYear_exception(self): #test exception handling for edge cases of endYear parameter
        self.assertEqual(bottomState(10, "Rate", "Both", "All", 2000, 2018), "Please pass the correct value for End Year.Pick a year from 2000 to 2017.")
        self.assertEqual(bottomState(10, "Rate", "Both", "All", 2005, 2004), "End year cannot be less than Start year. Please correct one of the values") 
        self.assertEqual(bottomState(10, "Rate", "Both", "All", 2000, 1999), "Please pass the correct value for End Year.Pick a year from 2000 to 2017.")
           
#Query 3 Unit Testing
class stateHeatMapTestCase(unittest.TestCase):
    
    def test_measure_exception(self): #test edge cases of measure exception (correct options are "Rate" or "Deaths")
        self.assertEqual(stateHeatMap(2000, " "), "Please pass the correct value for Measure.")
        self.assertEqual(stateHeatMap(2000, "rate"), "Please pass the correct value for Measure.")
        self.assertEqual(stateHeatMap(2000, "test"), "Please pass the correct value for Measure.")      

    def test_gender_exception(self): #test exception handling of edge cases of gender parameter
        self.assertEqual(stateHeatMap(2000, "Rate", "male" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")
        self.assertEqual(stateHeatMap(2000, "Rate", "female" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")
        self.assertEqual(stateHeatMap(2000, "Rate", "both" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")
        self.assertEqual(stateHeatMap(2000, "Rate", "test" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")

    def test_drugType_exception(self): #test exception handling for edge cases of drug type parameter 
        self.assertEqual(stateHeatMap(2000, "Rate", "Both", "Beer"), "Please pass the correct value for DrugType. Options are All, Opioid, Cocaine or Amphetamine") 
        
#Query 4 Unit Testing
class stateBarChartTestCase(unittest.TestCase):
    
    def test_state_exception(self): #test state exception handling, must pass full state name as string
        self.assertEqual(stateBarChart("test"), "Please pass the correct value for State.")
        
    def test_measure_exception(self): #test edge cases of measure exception (correct options are "Rate" or "Deaths")
        self.assertEqual(stateBarChart("Virginia", " "), "Please pass the correct value for Measure.")
        self.assertEqual(stateBarChart("Virginia", "rate"), "Please pass the correct value for Measure.")
        self.assertEqual(stateBarChart("Virginia", "test"), "Please pass the correct value for Measure.")
        
    def test_gender_exception(self): #test exception handling of edge cases of gender parameter
        self.assertEqual(stateBarChart("Virginia", "Rate", 2000, 2001, "male" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")
        self.assertEqual(stateBarChart("Virginia", "Rate", 2000, 2001, "female" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")
        self.assertEqual(stateBarChart("Virginia", "Rate", 2000, 2001, "both" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")
        self.assertEqual(stateBarChart("Virginia", "Rate", 2000, 2001, "test" ), "Please pass the correct value for Gender. Options are : Male, Female or Both")

    def test_startYear_exception(self): #test exception handling for edge cases of startYear parameter
        self.assertEqual(stateBarChart("Virginia", "Rate", 1999, 2001, "Both"), "Please pass the correct value for Start Year. Pick a year from 2000 to 2017.")
        self.assertEqual(stateBarChart("Virginia", "Rate", 2018, 2001, "Both"), "Please pass the correct value for Start Year. Pick a year from 2000 to 2017.")
    
    def test_endYear_exception(self): #test exception handling for edge cases of endYear parameter
        self.assertEqual(stateBarChart("Virginia", "Rate", 2000, 2018, "Both"), "Please pass the correct value for End Year.Pick a year from 2000 to 2017.")
        self.assertEqual(stateBarChart("Virginia", "Rate", 2005, 2004, "Both"), "End year cannot be less than Start year. Please correct one of the values") 
        self.assertEqual(stateBarChart("Virginia", "Rate", 2000, 1999, "Both"), "Please pass the correct value for End Year.Pick a year from 2000 to 2017.")
    

if __name__ == '__main__':
    unittest.main()
    