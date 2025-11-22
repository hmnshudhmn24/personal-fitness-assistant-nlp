from src import dataset_preprocessing
import json
def test_csv_to_jsonl(tmp_path):
    csv = tmp_path / 'd.csv'
    csv.write_text('age,level,goal,time,output\n25,beginner,weight_loss,30,Test plan\n')
    out = tmp_path / 'out.jsonl'
    dataset_preprocessing.csv_to_jsonl(str(csv), str(out))
    data = out.read_text().strip().splitlines()
    obj = json.loads(data[0])
    assert 'input' in obj and 'target' in obj
