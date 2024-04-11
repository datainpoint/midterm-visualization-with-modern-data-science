import unittest
import importlib
import pandas as pd
import sqlite3

class TestAssignmentThree(unittest.TestCase):
    def test_01(self):
        result_01 = pd.read_sql(asgmt.answer_01, connection)
        self.assertEqual(result_01.shape, (3, 2))
        tables = result_01.iloc[:, 0].values.tolist()
        self.assertIn("candidates", tables)
        self.assertIn("districts", tables)
        self.assertIn("parties", tables)
    def test_02(self):
        result_02 = pd.read_sql(asgmt.answer_02, connection)
        self.assertEqual(result_02.shape, (2, 2))
        vote_tallied_at = result_02.iloc[:, 1].values.astype(str).tolist()
        self.assertIn("2024-01-13 16:30:49", vote_tallied_at)
        self.assertIn("2024-01-13 21:56:59", vote_tallied_at)
    def test_03(self):
        result_03 = pd.read_sql(asgmt.answer_03, connection)
        self.assertEqual(result_03.shape, (2, 4))
        counties = result_03.iloc[:, 0].values.tolist()
        self.assertIn("新竹縣", counties)
        self.assertIn("宜蘭縣", counties)
        towns = result_03.iloc[:, 1].values.tolist()
        self.assertIn("竹北市", towns)
        self.assertIn("大同鄉", towns)
    def test_04(self):
        result_04 = pd.read_sql(asgmt.answer_04, connection)
        self.assertEqual(result_04.shape, (2, 2))
        votes = result_04.iloc[:, 1].values.tolist()
        self.assertIn(158596, votes)
        self.assertIn(136, votes)
    def test_05(self):
        result_05 = pd.read_sql(asgmt.answer_05, connection)
        self.assertEqual(result_05.shape, (2, 4))
        legislator_regions = result_05.iloc[:, 0].values.tolist()
        self.assertIn("新北市第1選舉區", legislator_regions)
        self.assertIn("臺北市第8選舉區", legislator_regions)
        parties = result_05.iloc[:, 1].values.tolist()
        self.assertIn("中國國民黨", parties)
        self.assertIn("興中同盟會", parties)
        candidates = result_05.iloc[:, 2].values.tolist()
        self.assertIn("洪孟楷", candidates)
        self.assertIn("胡之壯", candidates)
    def test_06(self):
        result_06 = pd.read_sql(asgmt.answer_06, connection)
        self.assertEqual(result_06.shape, (15, 4))
        parties = result_06.iloc[:, 1].values.tolist()
        self.assertIn("民主進步黨", parties)
        self.assertIn("中國國民黨", parties)
        names = result_06.iloc[:, 2].values.tolist()
        self.assertIn("林俊憲", names)
        self.assertIn("陳亭妃", names)
        self.assertIn("萬美玲", names)
    def test_07(self):
        result_07 = pd.read_sql(asgmt.answer_07, connection)
        self.assertEqual(result_07.shape, (13, 2))
        parties = result_07.iloc[:, 0].values.tolist()
        self.assertIn("時代力量", parties)
        self.assertIn("小民參政歐巴桑聯盟", parties)
        self.assertNotIn("民主進步黨", parties)
        self.assertNotIn("中國國民黨", parties)
        self.assertNotIn("台灣民眾黨", parties)
    def test_08(self):
        result_08 = pd.read_sql(asgmt.answer_08, connection)
        self.assertEqual(result_08.shape, (66, 3))
        counties = result_08.iloc[:, 0].unique()
        self.assertEqual(counties.size, 22)
        candidates = result_08.iloc[:, 1].unique()
        self.assertEqual(candidates.size, 3)
    def test_09(self):
        result_09 = pd.read_sql(asgmt.answer_09, connection)
        self.assertEqual(result_09.shape, (22, 3))
        counties = result_09.iloc[:, 0].unique()
        self.assertEqual(counties.size, 22)
        candidates = result_09.iloc[:, 1].unique()
        self.assertEqual(candidates.size, 2)
    def test_10(self):
        result_10 = pd.read_sql(asgmt.answer_10, connection)
        self.assertEqual(result_10.shape, (12, 4))
        counties = result_10.iloc[:, 0].unique()
        self.assertEqual(counties.size, 1)
        towns = result_10.iloc[:, 1].unique()
        self.assertEqual(towns.size, 12)
        candidates = result_10.iloc[:, 2].unique()
        self.assertEqual(candidates.size, 2)
        
connection = sqlite3.connect("taiwan_election_2024.db")
asgmt = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentThree)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"You've got {number_of_successes} successes among {number_of_test_runs} questions.")