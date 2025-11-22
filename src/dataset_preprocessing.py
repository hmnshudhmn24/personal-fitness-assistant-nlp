import argparse, csv, json
from pathlib import Path

def csv_to_jsonl(input_csv: str, output_jsonl: str):
    p_in = Path(input_csv)
    p_out = Path(output_jsonl)
    p_out.parent.mkdir(parents=True, exist_ok=True)
    with p_in.open(encoding='utf-8') as fin, p_out.open('w', encoding='utf-8') as fout:
        reader = csv.DictReader(fin)
        for row in reader:
            age = (row.get('age') or '').strip()
            level = (row.get('level') or '').strip()
            goal = (row.get('goal') or '').strip()
            time = (row.get('time') or '').strip()
            out = (row.get('output') or '').strip()
            if not age or not level or not goal or not time or not out:
                continue
            inp = f"age: {age} | level: {level} | goal: {goal} | time: {time}"
            fout.write(json.dumps({'input': inp, 'target': out}, ensure_ascii=False) + '\n')
    print(f'Wrote processed data to {p_out}')

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    csv_to_jsonl(args.input, args.output)
