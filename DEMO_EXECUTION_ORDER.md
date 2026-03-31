# Demo execution order

## Recommended order for the live demo

Run the files in exactly this order:

```bash
python demo/01_failure_case_without_repair.py
python demo/02_success_case_with_auto_repair.py
python demo/03_success_case_clean_manifest.py
python demo/04_demo_summary.py
```

For a single-command demo:

```bash
python run_demo_all.py
```

## Why this order works well

### Step 01 — Failure case without repair
- Purpose: immediately shows the audience that the system can detect unsafe manifests.
- Visible outcome: deployment is **blocked**.
- Demo value: creates strong contrast for the next step.

### Step 02 — Success case with auto-repair
- Purpose: shows the neuro-symbolic repair loop.
- Visible outcome: the **same risky manifest** is repaired and then deployed successfully.
- Demo value: clearly demonstrates improvement from failure to success.

### Step 03 — Success case with clean manifest
- Purpose: shows that already-compliant workloads pass directly.
- Visible outcome: deployment is **allowed** without repair.
- Demo value: proves the system does not over-correct clean inputs.

### Step 04 — Comparative summary
- Purpose: ends the demo with a crisp comparison table.
- Visible outcome: markdown and JSON summary generated in `demo_outputs/`.

## Demo deliverables produced automatically

After running the demo, these files are generated in `demo_outputs/`:
- `01_failure_case_without_repair.json`
- `02_success_case_with_auto_repair.json`
- `03_success_case_clean_manifest.json`
- `demo_execution_summary.md`
- `demo_execution_summary.json`

## Suggested talking points
- “Here is the unsafe manifest. The system finds multiple violations and blocks deployment.”
- “Now I enable the repair loop. The same manifest is corrected automatically and passes verification.”
- “Finally, here is a compliant manifest that passes directly, showing the pipeline behaves correctly in success cases too.”
