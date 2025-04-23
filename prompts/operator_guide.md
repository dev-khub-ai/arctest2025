# Operator Guide: Interacting with the Puzzle Solving Agent

## Purpose

This guide is for human operators or orchestration agents to consistently manage task-solving sessions with the Puzzle Solving Agent, following the multi-task, cumulative knowledge-building strategy.

The goal is to maintain clarity, repeatability, and progressive learning across hundreds or thousands of tasks.

## Operator Responsibilities

As the operator, you are responsible for:
- Supplying new tasks (training pairs and test inputs).
- Ensuring the agent works through training data fully before moving to test inputs.
- Requesting rule explanations and outputs at each critical step.
- Maintaining the Knowledge Base (KB), including storing rules, grid outputs, and versioning metadata.
- Spot-checking outputs against ground truth (if available).
- Escalating unresolved tasks for deeper review or refinement.

## Standard Workflow (Per Task)

1. Start Task
   - Provide task ID and full training pairs (inputs and outputs).
   - Provide test inputs (input grids only).

2. Request Training Pair Analysis
   - Ask the agent to analyze all training pairs.
   - Confirm detection of objects, candidate programs, and any patterns.

3. Request Rule Formulation
   - Have the agent summarize the general rule.
   - Ensure the rule covers all training examples.

4. Request Training Verification
   - Ask the agent to apply the rule to training inputs and compare inferred outputs to provided outputs.
   - Confirm correctness.

5. Request Test Inference
   - After successful training verification, request application of the rule to test inputs.
   - Confirm outputs are displayed cleanly.

6. Request Rule Export
   - Have the agent export the final rule in:
     - Plain text or Markdown
     - YAML (optional, structured format for KB)

7. Log Metadata
   - Record metadata (see versioning template below).
   - Include rule version, date, task ID, and any improvements.

8. Archive
   - Store task artifacts (rules, inputs, outputs, explanations) in the KB folder for future retrieval.

9. Cumulative Update (Optional)
   - If rule is generalizable, update the family rulebook.
   - Update task index and pattern library.

## Recommended Artifacts to Save (Per Task)

- Task training and test inputs
- Inferred rule (text and YAML)
- Training pair verification (inputs and outputs)
- Test predictions
- Operator notes (optional)
- Versioning metadata (using template below)

## Checklist (Quick Reference)

- [ ] Provided task inputs and outputs.
- [ ] Agent analyzed training pairs.
- [ ] Agent explained rule clearly.
- [ ] Rule verified on training pairs.
- [ ] Rule applied to test inputs.
- [ ] Agent exported rule and outputs.
- [ ] Metadata logged.
- [ ] Artifacts archived to KB.

---

# Versioning Metadata Template

Use this template to track the evolution of task solutions and rule definitions.

Save this alongside each task's artifacts (for example, as "metadata.yaml" or "metadata.json").

```yaml
task_id: task88
date_solved: 2025-04-10
solver_version: v1.0.0
rule_version: v1.2
operator: "Casey"  # or name of automated agent
status: "solved"  # solved, in-progress, needs-review
rule_summary: "Palette-driven stamping with global palette scan, offset based template stamping."
programs_detected:
  - program:
      c1: 1
      c2: 0
      description: "Background fill using object template stamped at all empty positions."
  - program:
      c1: 2
      c2: 0
      description: "Overlay vertical stripes based on palette value 2."
generalized: true  # whether this rule applies to other tasks
pattern_family: "Template Stamping"
artifacts:
  rule_markdown: "final-rule.md"
  rule_yaml: "final-rule.yaml"
  training_verification: "training-outputs.md"
  test_predictions: "test-outputs.md"
  operator_notes: "notes.md"
related_tasks:
  - task245
  - task311
notes: |
  Rule fully verified. Matches ground truth outputs exactly.
  Promoted rule to general template for Template Stamping family.
```

## Optional: Add Auto-Indexing

You can maintain a central index of tasks by collecting these metadata files.

Example auto-generated global index:

```yaml
tasks:
  - task_id: task88
    status: solved
    pattern_family: Template Stamping
    rule_version: v1.2
    generalized: true
  - task_id: task245
    status: solved
    pattern_family: Template Stamping
    rule_version: v1.1
    generalized: true
```

---

# Summary

With this Operator Guide and Versioning Metadata Template, you will:
- Maintain a clean, repeatable workflow.
- Avoid manual errors and copy-paste waste.
- Build a cumulative, reusable Knowledge Base.
- Track rule evolution clearly over time.
- Prepare for automation and future integration with agents or LLMs.

---

Would you like me to now also prepare:
- A directory structure template for your Knowledge Base (so you can immediately scaffold your system)?
- A draft of an auto-indexing Python script that reads these metadata files and builds an up-to-date index automatically?
- A blueprint for zero-manual automation, describing how to run this whole workflow seamlessly with tooling?
