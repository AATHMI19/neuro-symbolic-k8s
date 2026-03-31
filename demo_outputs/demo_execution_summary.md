# Demo Execution Summary

| Step | Scenario | Manifest | Violations / Before→After | Risk | Decision | Deployment |
|---|---|---|---|---:|---|---|
| 01_failure_case_without_repair | Failure path | frontend-risky | 4 | 100 | BLOCK | Blocked |
| 02_success_case_with_auto_repair | Success path after repair | frontend-risky | 4 -> 0 | 100 -> 0 | PASS | Allowed |
| 03_success_case_clean_manifest | Direct success path | payments-compliant | 0 | 0 | PASS | Allowed |

## Demo speaking flow
1. Run Step 01 to show a visible blocked deployment failure.
2. Run Step 02 to show auto-repair turning the same risky manifest into a compliant deployment.
3. Run Step 03 to show a clean manifest passing directly without repair.
4. Use this summary table to close the demo with both failure and success visibility.
