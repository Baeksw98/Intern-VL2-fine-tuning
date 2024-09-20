import json
import os
import glob

def convert_to_internvl2_format(input_file, output_file, image_dir, dataset_type, is_test=False):
    converted_data = []
    image_files = {os.path.splitext(os.path.basename(f))[0]: f for f in glob.glob(os.path.join(image_dir, 'P*.jpg'))}
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read().strip()
        if content.startswith('[') and content.endswith(']'):
            data = json.loads(content)
        else:
            data = [json.loads(line) for line in content.splitlines() if line.strip()]
    
    idx = 0
    for item in data:
        image_id = item['input']['id']
        if image_id not in image_files:
            print(f"Warning: Image file for {image_id} not found in {dataset_type} dataset.")
            continue
        
        image_path = image_files[image_id]
        
        human_input = f"<image>\n{item['input']['ocr_info'][0]['words']}\n이미지에 대해 정확히 설명해주세요."
        
        if not is_test and 'output' in item:
            for output in item['output']:
                conversations = [
                    {"from": "human", "value": human_input},
                    {"from": "gpt", "value": output}
                ]
                
                converted_item = {
                    "id": idx,
                    "image": image_path,
                    "width": item['input']['image_width'],
                    "height": item['input']['image_height'],
                    "conversations": conversations
                }
                converted_data.append(converted_item)
                idx += 1
        else:
            # For test data or if no output is available
            conversations = [{"from": "human", "value": human_input}]
            converted_item = {
                "id": idx,
                "image": image_path,
                "width": item['input']['image_width'],
                "height": item['input']['image_height'],
                "conversations": conversations
            }
            converted_data.append(converted_item)
            idx += 1

    # Write the converted data to the output file in JSONL format
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in converted_data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')

# Directory paths
base_dir = '/data/swbaek/Projects/Korean_IC_Competition/data'
image_dir = os.path.join(base_dir, 'nikluge-gips-2023_image')
input_json_dir = os.path.join(base_dir, 'nikluge-gips-2023_JSONL')
output_json_dir = '/data/swbaek/Projects/Korean_IC_Competition/Intern-VL2-fine-tuning/data'

# Ensure output directory exists
os.makedirs(output_json_dir, exist_ok=True)

# Process train, dev, and test data
datasets = [
    ('nikluge-gips-2023-train.jsonl', 'nikluge-gips-2023-internvl2-train.jsonl', 'train', False),
    ('nikluge-gips-2023-dev.jsonl', 'nikluge-gips-2023-internvl2-dev.jsonl', 'dev', False),
    ('nikluge-gips-2023-test.jsonl', 'nikluge-gips-2023-internvl2-test.jsonl', 'test', True)
]

for input_file, output_file, dataset_type, is_test in datasets:
    input_path = os.path.join(input_json_dir, input_file)
    output_path = os.path.join(output_json_dir, output_file)
    
    convert_to_internvl2_format(input_path, output_path, image_dir, dataset_type, is_test)
    print(f"Conversion complete for {input_file}. Output saved to {output_file}.")

print("All conversions completed.")