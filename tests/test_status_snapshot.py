import copy,unittest,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"analysis"))
from status_incidents import load_events,build_item_table,summarise,merge_events
class StatusSnapshotTests(unittest.TestCase):
 def setUp(self):
  self.events=load_events()
 def test_row_count(self):self.assertEqual(len(self.events),88)
 def test_item_count(self):self.assertEqual(len(build_item_table(self.events)),25)
 def test_dedup(self):self.assertEqual(merge_events(self.events,self.events),self.events)
 def test_money_movement(self):
  s=summarise(build_item_table(copy.deepcopy(self.events)),self.events)
  self.assertEqual((s["money_movement_incidents"],s["money_movement"]["resolved"],s["money_movement"]["median_minutes_to_resolution"]),(6,5,63))
 def test_public_gap(self):
  s=summarise(build_item_table(copy.deepcopy(self.events)),self.events)
  self.assertEqual(s["longest_gap_money_movement"]["minutes"],315)
 def test_not_customer_wait(self):
  self.assertIn("not problem start",summarise(build_item_table(copy.deepcopy(self.events)),self.events)["method_note"])
if __name__=="__main__":unittest.main()
