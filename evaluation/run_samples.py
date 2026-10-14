import json
import time
from evaluation.samples import SAMPLES
from main import generate_description
from generator.llm_client import LLMError, DEFAULT_MODEL
from generator.prompt_builder import PROMPT_TEMPLATE

OUTPUT_FILE = "evaluation/results_v3.md"
RUNS_PER_SAMPLE = 2

def run_evaluation():
    print(f"Starting evaluation runner. Writing results to {OUTPUT_FILE}...")

    # Initialize or reset the markdown report with front matter
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Property Description LLM Evaluation Report\n\n")
        f.write(f"Model: {DEFAULT_MODEL}. Each sample runs {RUNS_PER_SAMPLE} times.\n\n")
        f.write("## Prompt template used\n\n```\n" + PROMPT_TEMPLATE + "\n```\n\n")

    # Iterate through each defined scenario
    for index, sample in enumerate(SAMPLES, 1):
        label = sample.get("label", f"Sample {index}")
        raw_data = sample.get("data", {})

        print(f"Processing evaluation [{index}/{len(SAMPLES)}]: '{label}'...")

        # Format the input metadata neatly for the markdown file
        formatted_input = json.dumps(raw_data, indent=2)

        # Append section header and raw data payload
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(f"## {index}. {label}\n\n")
            f.write("### Test Input Data\n")
            f.write(f"```json\n{formatted_input}\n```\n\n")
            f.write("### Execution Outputs\n\n")

        # Run the pipeline several times to monitor consistency
        for run_id in range(1, RUNS_PER_SAMPLE + 1):
            start = time.perf_counter()                  # start the stopwatch
            try:
                output_text = generate_description(raw_data)
            except ValueError as e:
                output_text = f"INPUT VALIDATION ERROR: {e}"
            except LLMError as e:
                output_text = f"LLM ERROR: {e}"
            except Exception as e:
                output_text = f"UNEXPECTED ERROR: {e}"
            seconds = time.perf_counter() - start        # elapsed time, in seconds

            with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                f.write(f"#### Run {run_id} ({seconds:.1f}s)\n{output_text}\n\n---\n\n")

    print(f"Evaluation complete! Review the final artifacts inside: '{OUTPUT_FILE}'")

if __name__ == "__main__":
    run_evaluation()