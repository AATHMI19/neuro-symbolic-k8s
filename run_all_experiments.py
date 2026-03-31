
import importlib

modules=[
"experiments.dataset.manifest_dataset",
"experiments.dataset.cluster_setup",
"experiments.baseline.llm_only_generation",
"experiments.baseline.schema_validation",
"experiments.baseline.policy_validation_only",
"experiments.proposed.neuro_symbolic_pipeline",
"experiments.effectiveness.detection_accuracy",
"experiments.effectiveness.repair_convergence",
"experiments.effectiveness.minimal_change",
"experiments.effectiveness.incremental_verification",
"experiments.performance.latency_vs_manifest_size",
"experiments.performance.policy_scaling",
"experiments.performance.cicd_throughput",
"experiments.security.compound_violations",
"experiments.security.adversarial_prompts",
"experiments.security.policy_conflicts",
"experiments.governance.certificate_integrity",
"experiments.governance.audit_log_test",
"experiments.deployment.canary_deployment",
"experiments.deployment.runtime_drift_detection",
"experiments.ablation.no_repair_loop",
"experiments.ablation.no_incremental_verification",
"experiments.ablation.no_runtime_monitor"
]

for m in modules:
    mod=importlib.import_module(m)
    print("\nRunning",m)
    mod.run()
