# Improve to Target Command

**Purpose**: Automated iterative improvement of plugins or prompts until a defined quality score is reached. Combines plugin generation (or uses an existing plugin), review analysis, and intelligent step-by-step improvement in an autonomous loop.

**Trigger**: The user wants to create a high-quality plugin or prompt without manual iteration work.

## Workflow Overview

The command executes an intelligent improvement cycle consisting of four main phases that repeat until the quality target is reached or termination criteria apply.

Phase one is initialization. If the user describes a plugin idea, the initial plugin is first created via the generate-plugin workflow. If the user already has an existing plugin, it is used as the starting point. In both cases, a baseline review is performed to determine the current quality status.

Phase two is strategic planning. The Review Orchestrator has already created a prioritized roadmap with critical fixes, major improvements, and optimizations. Each phase has an estimated impact rating. The system now calculates which fixes should be addressed in the current iteration based on the difference between the current score and target score.

Phase three is focused implementation. The system does not work through all issues simultaneously but concentrates on a manageable amount of prioritized changes. For each change, the affected file is loaded, the specific modification is made, and the file is saved. Old versions are kept as backups for possible rollbacks.

Phase four is validation and decision. After each implementation phase, a complete re-review is performed. The system compares the new score with the previous one. If the target score is reached, the loop terminates successfully. If significant progress was made but the target is not yet reached, the next iteration starts. If no progress or even regression is detected, the rollback logic kicks in.

## Parameters

```
/improve-to-target [input] --target-score=X.X [OPTIONS]
```

**Required Parameters**:
- `[input]`: Plugin description (for new plugins) or path to existing plugin
- `--target-score=X.X`: Desired minimum score (0.0-10.0)

**Optional Parameters**:
- `--max-iterations=N`: Maximum number of iterations (Default: 5)
- `--dry-run`: Preview mode, shows planned changes without execution
- `--aggressiveness=N`: Change strategy (1=conservative, 2=moderate, 3=aggressive, Default: 2)
- `--focus=DIMENSION`: Focus on specific dimension (pe, sec, fs, cot, req, arch, code, tech)
- `--min-improvement=X.X`: Minimum score improvement per iteration (Default: 0.3)
- `--profile=PROFILE`: Review profile (quick, standard, comprehensive, code-focused, Default: standard)
- `--interactive`: Asks after each iteration whether to continue
- `--preserve-sections=SECTIONS`: Sections that must not be changed (comma-separated)

## Detailed Workflow

### Phase 1: Initialization

**Step 1.1: Input Processing**

If input is a plugin description, delegate to generate-plugin command. This executes the complete generation workflow including questions and structure planning. The resulting plugin is used as baseline.

If input is an existing plugin, load all files into the working context. Create a complete inventory of all files with their current content. This inventory serves as the basis for change tracking and rollbacks.

**Step 1.2: Baseline Review**

Delegate to the Review Orchestrator with the specified profile. The orchestrator executes all relevant evaluators and delivers a comprehensive report with overall score, dimensional scores, prioritized issue list, and roadmap.

Extract the critical information from the review report. The baseline score is documented as the starting point. The delta to the target is calculated. The prioritized roadmap is converted into a structured action list.

**Step 1.3: Feasibility Check**

Before the loop starts, perform a feasibility check. If the baseline score is already above the target, congratulate the user and terminate successfully without iteration. If the delta between baseline and target is greater than four points, warn that this may require many iterations and possibly recommend a lower target for the first run.

Calculate an estimated number of required iterations based on the roadmap. If Phase 1 critical fixes bring +1.5 points, Phase 2 +0.8 points, and Phase 3 +0.4 points, and the delta is 2.0 points, then an estimate of two iterations is given. Inform the user about this estimate.

**Output Format for Initialization**:
```markdown
# Initialization Complete

**Baseline Score**: [X.X/10]
**Target Score**: [Y.Y/10]
**Delta**: [Z.Z] points

**Estimated Iterations**: [N] (Maximum: [max-iterations])

**Roadmap Summary**:
- Phase 1 (Critical): [N] issues, estimated impact +[X.X] points
- Phase 2 (Major): [N] issues, estimated impact +[X.X] points
- Phase 3 (Optimizations): [N] issues, estimated impact +[X.X] points

**Starting automated improvement loop...**
```

### Phase 2: Strategic Planning (per iteration)

**Step 2.1: Iteration Context Analysis**

At the beginning of each iteration, the current state is analyzed. What is the current score? How large is the remaining delta to the target? Which issues have already been fixed? Which are still open? Were there new issues that arose in the previous iteration?

**Step 2.2: Action Selection Strategy**

The number and type of issues addressed in this iteration depends on the aggressiveness parameter.

With conservative strategy (aggressiveness=1), only the highest-priority issue category is addressed. If critical issues exist, only these. If no critical issues remain, only the top three major issues. Maximum five changes per iteration. The goal is minimal risk with safe, incremental improvements.

With moderate strategy (aggressiveness=2, the default), all critical issues plus the top five major issues are addressed. Maximum ten changes per iteration. This is the balance between speed and safety.

With aggressive strategy (aggressiveness=3), all critical issues, all major issues, and relevant minor issues are addressed. Maximum fifteen changes per iteration. Structural refactorings are also allowed. The goal is fast convergence to the target, with higher risk for side effects.

**Step 2.3: Focus Dimension Filtering**

If the focus parameter is set, only issues from this dimension are addressed. This is useful when the user knows that, for example, only security problems need to be fixed, but prompt engineering and architecture are already good. The other dimensions are skipped in this case.

**Step 2.4: Preserve Sections Handling**

If preserve-sections is specified, these sections are excluded from any changes. This is critical when the user has already manually perfected certain parts. For example, preserve-sections=role,capabilities would mean that the role and capabilities tags may never be changed.

**Output Format for Planning**:
```markdown
## Iteration [N]/[max-iterations]

**Current Score**: [X.X/10]
**Target Score**: [Y.Y/10]
**Remaining Delta**: [Z.Z] points

**Planned Actions for this Iteration**:

### Critical Fixes ([N] actions)
1. **[Issue Title]** (File: [filename], Line: [X])
   - Current Problem: [Description]
   - Planned Fix: [Specific action]
   - Estimated Impact: +[X.X] points
   - Risk: [Low|Medium|High]

2. [Additional critical fixes...]

### Major Improvements ([N] actions)
[Similar structure]

**Total Estimated Impact**: +[X.X] points (would bring score to ~[predicted score])
**Estimated Time**: [X] minutes
**Risk Assessment**: [Low|Medium|High]

[If dry-run mode:]
**DRY RUN MODE**: No changes will be made. Review planned actions above.

[If interactive mode:]
**Proceed with these changes?** [Y/N]
```

### Phase 3: Focused Implementation

**Step 3.1: Backup Creation**

Before each change, a complete backup of the current plugin state is created. This is done by copying all files to a versioned backup directory. The format is backup-iteration-N-timestamp. This allows complete rollbacks if the iteration fails.

**Step 3.2: Sequential Change Application**

The planned changes are processed sequentially, not in parallel. This allows better error handling and makes it easier to understand which change had which effect.

For each change, the following process runs. First, load the affected file into the context. Second, identify the exact location of the change by line number or pattern matching. Third, make the change considering the context and preserve-sections constraints. Fourth, validate that the change is syntactically correct - for Markdown, check that tags are closed; for code, that it compiles. Fifth, save the modified file.

**Step 3.3: Change Documentation**

Each change made is documented in a change log. This includes which file was changed, which lines were affected, what the old version was and what the new version is, which issue was fixed thereby, and what the expected impact is. This change log is essential for debugging if something goes wrong.

**Step 3.4: Incremental Validation**

After every third of the planned changes, a quick validation is performed. This includes syntactic checks - are all files still valid? Are expected files still found? Are there new obvious errors? If problems are detected, the implementation stops and a rollback to the last good state occurs.

**Output Format for Implementation**:
```markdown
### Implementation Progress

[V] 1/10: Fixed missing action verb in SKILL.md line 45
    Before: "You should analyze the requirements"
    After: "Analyze the requirements"

[V] 2/10: Added security constraint in generate-plugin.md
    Added: <constraints> block with CWE-89, CWE-78 checks

[?] 3/10: Reordering few-shot examples by complexity...
    Calculating complexity scores...
    Reordering from [3,1,4,2] to [1,2,3,4]

[V] Incremental validation (3/10 completed): PASSED

[?] 4/10: [Next action...]
```

### Phase 4: Validation and Decision

**Step 4.1: Comprehensive Re-Review**

After completing all planned changes, a complete review is performed. This again happens through delegation to the Review Orchestrator with the same profile as the baseline review. It is important that exactly the same evaluators with the same parameters are used to make the scores comparable.

The re-review delivers a new overall score, new dimensional scores, and an updated issue list. Some issues have been fixed, others may still be open, and in rare cases new issues may have arisen.

**Step 4.2: Progress Analysis**

Now the progress is quantitatively analyzed. The score improvement is calculated as new score minus old score. The improvement rate is calculated as score improvement divided by estimated impact of the changes made. A rate near 1 means the changes had exactly the expected effect. A rate above 1 means they were even better than expected. A rate below 0.5 means they had less effect than hoped.

Critical is also the check for regression. If dimensional scores in non-focused dimensions have dropped, this could be a sign that the changes had unintended side effects. If the overall score has dropped despite fixes made, something has definitely gone wrong.

**Step 4.3: Decision Logic**

Based on the progress analysis, the system makes one of five possible decisions.

Decision one is Success - Target Reached. If the new score is greater than or equal to the target score, the goal was successfully achieved. The loop terminates with success status. The final plugin is saved in the output directory. A summary report is generated with baseline score, final score, number of iterations, changes made, and final dimensional scores.

Decision two is Continue - Good Progress. If the score has increased significantly - at least min-improvement points - and the target is not yet reached and max-iterations is not yet reached, a new iteration starts. The roadmap is recalculated based on the remaining issues.

Decision three is Rollback and Retry. If the score has not increased or has even fallen, a rollback to the backup before this iteration is performed. The system tries an alternative approach with different changes or lower aggressiveness level. Maximum two rollbacks per loop are allowed.

Decision four is Plateau Detection - Human Intervention Needed. If over two consecutive iterations the improvement was below min-improvement, the system has reached a plateau. Further automatic iteration is unlikely to help. The loop stops and informs the user that manual intervention is needed. A detailed report on the remaining issues is provided.

Decision five is Max Iterations Reached - Partial Success. If max-iterations is reached but the target is not yet, the loop terminates with partial success. The plugin is better than at the beginning, but has not fully reached the goal. The user gets the option to either accept the current result, lower the target score, or increase max-iterations and continue.

**Output Format for Validation**:
```markdown
## Iteration [N] Complete

**Previous Score**: [X.X/10]
**New Score**: [Y.Y/10]
**Improvement**: +[Z.Z] points ([W]% of estimated impact)

### Score Changes by Dimension
| Dimension | Before | After | Change |
|-----------|--------|-------|--------|
| Prompt Engineering | [X.X] | [Y.Y] | +[Z.Z] |
| Security | [X.X] | [Y.Y] | +[Z.Z] |
| [etc.] | | | |

**Issues Resolved**: [N]
**Issues Remaining**: [N]
**New Issues Introduced**: [N]

**Decision**: [Success|Continue|Rollback|Plateau|MaxIterations]

[If Continue:]
**Preparing Iteration [N+1]...**

[If Success:]
**TARGET SCORE REACHED!**
Final plugin saved to: [path]

[If Plateau:]
**PLATEAU DETECTED**
Automatic improvement has stalled. Manual review recommended.
See detailed report below for remaining issues.

[If MaxIterations:]
**MAX ITERATIONS REACHED**
Current score [X.X] is below target [Y.Y] but significant progress made.
Options:
A) Accept current result
B) Continue with [N] more iterations
C) Lower target score to [realistic value]
```

## Safety Mechanisms

The system implements several critical safety mechanisms to avoid catastrophic errors.

**Iteration Limit**: Maximum five iterations by default, configurable up to maximum ten. Prevents endless loops on unsolvable problems.

**Rollback Capability**: Each iteration has a complete backup. On regression, automatic rollback occurs. Maximum two rollbacks per session.

**Progress Threshold**: If two consecutive iterations bring less than min-improvement improvement, the loop stops. Prevents inefficient iteration at plateau.

**Preserve Sections**: User-specified sections are never changed. Critical for partially manual plugins.

**Syntax Validation**: After each change, files are checked for syntactic correctness. Invalid changes are discarded.

**Incremental Validation**: After every third of the changes, validation occurs. On problems, the rest of the iteration is aborted.

**Dimensional Balance Check**: If a dimension drops by more than two points while others rise, this is flagged as a red flag. Possibly trade-offs were made that are unfavorable.

**Critical Issue Prevention**: If new critical issues are introduced in an iteration, automatic rollback occurs. Critical issues must never arise through iteration.

## Dry-Run Mode

In dry-run mode, the complete workflow is performed but no actual file changes are made. Instead, a diff is shown for each planned change. This is valuable to understand what the system would do before actually executing it.

The dry-run shows for each change the affected file, the exact location, a before-after diff, and the estimated impact. At the end, a summary is shown with total estimated improvement and risk assessment. The user can then decide whether to start the real run.

## Interactive Mode

In interactive mode, the system asks after each iteration whether to continue. This gives the user complete control. After each iteration, the progress report is displayed. Then it asks: "Continue to next iteration? [Y/N/R]" where Y is yes, N is no, and R is review current state.

If the user chooses R, the complete re-review report is displayed including all dimensional details. The user can then make an informed decision whether another iteration makes sense.

## Example Usage

**Example 1: Create and Perfect a New Plugin**
```
/improve-to-target "A plugin for API documentation generation from code" --target-score=9.0

[System creates initial plugin, baseline score: 6.8/10]
[Iteration 1: Fixes critical issues, score -> 8.2/10]
[Iteration 2: Implements major improvements, score -> 9.1/10]
[Success! Target reached in 2 iterations]
```

**Example 2: Improve Existing Plugin with Focus**
```
/improve-to-target /path/to/my-plugin --target-score=8.5 --focus=security --max-iterations=3

[System reviews existing plugin, baseline score: 7.2/10, Security: 5.1/10]
[Iteration 1: Adds security constraints and examples, Security -> 7.8/10]
[Iteration 2: Implements secure code patterns, Security -> 8.9/10]
[Success! Security dimension above target]
```

**Example 3: Conservative Improvement with Preserved Sections**
```
/improve-to-target /path/to/plugin --target-score=8.0 --aggressiveness=1 --preserve-sections=role,capabilities --interactive

[System shows planned changes for iteration 1]
User reviews and confirms: Y
[Iteration proceeds conservatively, only top issues]
[After iteration: Shows progress, asks to continue]
User: Y
[Continues until target or user stops]
```

## Output Artifacts

At the end of a successful run, the system generates several artifacts that are provided to the user.

The final plugin is saved in the output directory with all improved files. A comprehensive final report is created with baseline vs final score comparison, dimensional score breakdown, complete change log with all changes made, iteration history with score progression, and an executive summary.

A quality certificate is optionally generated that attests that the plugin has reached a specific score and by which criteria it was reviewed. This can be useful for plugin sharing or documentation purposes.

All backups are kept in the backup directory in case the user wants to return to an earlier state. The complete change log is saved as a separate file for audit purposes.

## Error Handling

**File Not Found**: If referenced files disappear during iteration, roll back to the last known good version.

**Syntax Errors After Change**: Automatic revert of the faulty change, log of error details, continue with next change.

**Review Orchestrator Timeout**: If re-review takes longer than thirty minutes, abort with warning. The plugin may be too complex for automatic iteration.

**Unexpected Score Regression**: If score drops by more than 1.0 points, immediate rollback and alternative strategy selection.

**Max Rollbacks Exceeded**: If more than two rollbacks are needed in a run, terminate with error. The problem is probably fundamental and requires manual debugging.

## Constraints

**Maximum Total Execution Time**: Two hours. On exceeding, abort with partial results.

**File Size Limits**: Individual files must not grow beyond five hundred lines during iteration. Larger files require manual splitting.

**Complexity Limit**: If a plugin has over twenty files, recommend manual iteration approach. Automatic iteration becomes too confusing.

**Token Budget**: Maximum fifty thousand tokens per iteration. On exceeding, reduce number of simultaneous changes.
