import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"analysis"))
from decision_engine import decide,analyze
CASES=json.loads((ROOT/"data"/"decision_cases.json").read_text())
class DecisionTests(unittest.TestCase):
 def test_routes(self):
  self.assertEqual([decide(c)["route"] for c in CASES],["COMMUNICATION_GAP","DATA_QUALITY","EXPECTED_HOLD","POLICY_REVIEW","MONITOR","POLICY_REVIEW"])
 def test_no_mutation(self):
  before=copy.deepcopy(CASES);analyze(CASES);self.assertEqual(CASES,before)
 def test_duplicate_ids(self):
  with self.assertRaises(ValueError):analyze([CASES[0],CASES[0]])
 def test_no_source(self):
  x=copy.deepcopy(CASES[0]);x["events"]=x["events"][1:];self.assertEqual(decide(x)["route"],"DATA_QUALITY")
 def test_unknown_state(self):
  x=copy.deepcopy(CASES[0]);x["events"][0]["status"]="released"; 
  with self.assertRaises(ValueError):decide(x)
 def test_unknown_hold_category(self):
  x=copy.deepcopy(CASES[0]);x["hold_category"]="unknown"
  with self.assertRaises(ValueError):decide(x)
 def test_messaging_threshold_boundary(self):
  x=copy.deepcopy(CASES[0]);x["repeat_contacts_7d"]=1;self.assertEqual(decide(x)["route"],"MONITOR")
 def test_policy_precedes_communication(self):
  self.assertEqual(decide(CASES[5])["route"],"POLICY_REVIEW")
 def test_report_matches_fixture(self):
  expected=analyze(CASES)
  actual=json.loads((ROOT/"data"/"decision_report.json").read_text())
  self.assertEqual(expected,actual)
if __name__=="__main__":unittest.main()
