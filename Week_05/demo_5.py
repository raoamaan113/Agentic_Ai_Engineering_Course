
from claims_dataset import claims_dataset


def run_model(prompt: str) -> tuple[str, float]:
    start = time.perf_counter()

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        format="json",
        options={"temperature": 0},
    )

    latency_seconds = time.perf_counter() - start
    return response.message.content, latency_seconds


with open("results.jsonl", "w", encoding="utf-8") as output_file:
    for item in claims_dataset:
        for version, prompt_function in [
            ("original", original_prompt),
            ("enhanced", enhanced_prompt),
        ]:
            raw_output, latency = run_model(
                prompt_function(item["claim"])
            )

            record = {
                "id": item["id"],
                "version": version,
                "expected_category": item["expected_category"],
                "required_missing": item["required_missing"],
                "claim": item["claim"],
                "raw_output": raw_output,
                "latency_seconds": round(latency, 3),
            }

            output_file.write(
                json.dumps(record, ensure_ascii=False) + "\n"
            )

            print(
                f"Claim {item['id']} | {version} | "
                f"{latency:.2f}s"
            )
            print(raw_output)
            print("-" * 60)

