import json

def validate_jsonl_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            try:
                json_obj = json.loads(line)
                print(f"Line {idx}: Valid JSON")
            except json.JSONDecodeError as e:
                print(f"Line {idx}: JSONDecodeError: {e}")

# Test the function with your file
input_file = '/data/swbaek/Projects/Korean_IC_Competition/Intern-VL2-fine-tuning/data/nikluge-gips-2023-internvl2-train.jsonl'
validate_jsonl_file(input_file)