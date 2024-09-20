# Intern-VL2 

## Repository Structure
```
# Data resource for training 
data
├── nikluge-gips-2023-train.jsonl       # Training data
├── nikluge-gips-2023-test.jsonl        # Test data
├── nikluge-gips-2023-dev.jsonl         # Development data
├── nikluge-gips-2023-internvl2-train.jsonl  # InternVL2-specific training data
├── nikluge-gips-2023-internvl2-test.jsonl   # InternVL2-specific test data
├── nikluge-gips-2023-internvl2-dev.jsonl    # InternVL2-specific development data
└── convert.py                          # Script to convert data to InternVL2 format

# Code for model fine-tuning and inference
internvl_chat
├── shell
    ├── data
        ├── internvl_finetune_korean.json # Meta file for running fine-tuning script
    ├── scripts
        # Fine-tuning scripts for InternVL2 (1B, 2B, 4B, 8B, 26B, 40B, 76B) 
        ├── internvl2_1b_finetune_full.sh  # Script for InternVL2-1B full fine-tuning
        ├── internvl2_1b_finetune_lora.sh  # Script for InternVL2-1B lora fine-tuning 
        ├── internvl2_2b_finetune_full.sh  # Script for InternVL2-2B full fine-tuning
        ├── internvl2_2b_finetune_lora.sh  # Script for InternVL2-2B lora fine-tuning
        ├── internvl2_4b_finetune_full.sh  # Script for InternVL2-4B full fine-tuning
        ├── internvl2_4b_finetune_lora.sh  # Script for InternVL2-4B lora fine-tuning
        ├── internvl2_8b_finetune_full.sh  # Script for InternVL2-8B full fine-tuning
        ├── internvl2_8b_finetune_lora.sh  # Script for InternVL2-8B lora fine-tuning
        ├── internvl2_26b_finetune_full.sh  # Script for InternVL2-26B full fine-tuning
        ├── internvl2_26b_finetune_lora.sh  # Script for InternVL2-26B lora fine-tuning
        ├── internvl2_40b_finetune_full.sh  # Script for InternVL2-40B full fine-tuning
        ├── internvl2_40b_finetune_lora.sh  # Script for InternVL2-40B lora fine-tuning
        ├── internvl2_76b_finetune_full.sh  # Script for InternVL2-76B full fine-tuning
        ├── internvl2_76b_finetune_lora.sh  # Script for InternVL2-76B lora fine-tuning
├── tools # Tools for running the scripts (Utility functions)
├── zero_stage1_config.json # Configuration file for zero-stage 1
├── zero_stage2_config.json # Configuration file for zero-stage 2
├── zero_stage3_config.json # Configuration file for zero-stage 3
├── zero_stage3_config_34b.json # Configuration file for zero-stage 3 34B
├── zero_stage3_config_70b.json # Configuration file for zero-stage 3 70B
├── zero_stage3_config_100b.json # Configuration file for zero-stage 3 100B


# Inference results
inference
├── qwen_results_V2.jsonl     # Version 2 of inference results
└── qwen_results_V1.jsonl     # Version 1 of inference results


# Main scripts
inference.py                  # Script for running inference
finetune.py                   # Script for fine-tuning
openai_api.py                 # OpenAI-like API implementation

# Additional files
requirements.txt              # Python package requirements
README.md                     # This file

# Output directory for fine-tuned models
outputs
├── ______
└── ______


## Data
### How to Prepare Data
```
{
  "id": 0,
  "image": "/data/swbaek/Projects/Korean_IC_Competition/data/nikluge-gips-2023_image/P00001.jpg",
  "width": 6000,
  "height": 4000,
  "conversations": [
    {
      "from": "human",
      "value": "<image>\n2인승\n이미지에 대해 정확히 설명해주세요."
    },
    {
      "from": "gpt",
      "value": "2인승이라고 적혀 있는 하늘색 테두리 안내판 옆에는 다양한 색깔의 우산들이 띄워져 있다."
    },
    {
      "from": "gpt",
      "value": "다양한 색깔의 우산들이 띄워져 있는 곳 옆에는 2인승이라고 쓰인 하늘색 테두리 안내판이 있다,"
    },
    {
      "from": "gpt",
      "value": "다양한 색깔의 우산이 띄워진 곳 옆에 있는 하늘색 테두리 안내판에는 2인승이라고 적혀 있다."
    },
    {
      "from": "gpt",
      "value": "하늘색 테두리 안내판에는 2인승이라고 적혀 있는데, 그 옆에 띄워져 있는 것은 다양한 색깔의 우산들이다."
    },
    {
      "from": "gpt",
      "value": "안내판은 하늘색 테두리에 2인승이라고 적혀 있으며, 그 옆에 띄워져 있는 것은 다양한 색의 우산들이다."
    }
  ]
},
...
...
```

## Installation
Prerequisites
- Ensure you have Python 3.10 or higher installed.

Setting Up the Environment
1. Clone the Repository (if applicable):

```
git clone <repository-url>
cd Intern-VL2-fine-tuning
```

2. Install Dependencies:
```
pip install -r requirements.txt
```

## How to Run (Training, Inference, Scoring)
# Note: Please change your configurations through modifying the relevant script files in the finetune folder

### Fine-tuning
```
GPUS=8 PER_DEVICE_BATCH_SIZE=2 sh shell/scripts/internvl2_26b_finetune_full.sh
```
- Fine-tuning logs and models will be saved in the output_qwen directory.

### Inference
```
chmod +x finetune/run_inference.sh
./finetune/run_inference.sh
```
- During inference, the output data is saved in jsonl format in the inference directory.

### Evaluation

- Evaluation scripts are provided in the eval_mm directory. Refer to EVALUATION.md for detailed information on how to run evaluations.

## Extra code for tmux
#생성 코드 
tmux new -s TEST 

#리스트 확인 
tmux ls 

#끄지 않고 detach
ctr+b and then d : detach 

#세션 다시 들어가기
tmux attach -t TEST 
 (Ctrl + b) + [ - (scroll)

# 세션 삭제
tmux kill-session -t TEST

## License
MIT License

## Credits
This code was developed by the Sionic AI research team. For any inquiries or further information regarding this code, please reach out to Sangwon Baek at baeksw98@sionic.ai.
To learn more about our company and our vision for the future of AI, please visit our website at https://sionic.ai/.