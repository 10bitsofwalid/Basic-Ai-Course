# Basic AI & Python Programming Lab Repository

This repository contains problem-solving scripts, Object-Oriented Programming (OOP) exercises, search algorithms, and rule-based expert systems developed for AI and Python fundamentals.

---

## 📁 Repository Structure

### Root Directory: Problem-Solving & AI Algorithms
| File | Topic / Description | Concepts Used |
| :--- | :--- | :--- |
| [`Problem01.py`](Problem01.py) | Temperature Suitability Checker | Conditionals (`if`, `elif`, `else`) |
| [`Problem02.py`](Problem02.py) | Variable Input and Reassignment | I/O, String variables |
| [`Problem03.py`](Problem03.py) | Student Grading System | Relational operators, range validation |
| [`Problem04.py`](Problem04.py) | Interactive State Space Navigation | State tracking, loop control, battery threshold |
| [`Problem05.py`](Problem05.py) | Linear State Sequential Path Finder | List indexing, forward transitions, slicing |
| [`Problem06.py`](Problem06.py) | Breadth-First Search (BFS) Pathfinding | BFS graph search, adjacency dictionary, queue |
| [`Problem07.py`](Problem07.py) | Multi-Route Sub-Path Finder | Dictionary search, sub-path slicing |
| [`Problem08.py`](Problem08.py) | Disaster Response Decision System | Rule-based decision system, multi-level triage |
| [`Problem09.py`](Problem09.py) | Student Database & Record Search | OOP (Classes, objects), list search |
| [`Problem10.py`](Problem10.py) | Weather Condition Classifier | OOP, class methods, constructor (`__init__`) |
| [`Problem11.py`](Problem11.py) | Electricity Bill Calculation | OOP, tier classification, boundary handling |
| [`Problem12.py`](Problem12.py) | Electricity Bill with Area Verification | OOP, input validation, membership checking |
| [`Problem13.py`](Problem13.py) | Multi-Zone Customer Registry & Billing | OOP, customer validation, two-level check |
| [`Problem14.py`](Problem14.py) | Two-Factor Service Area & Customer Billing | OOP, defensive inputs, customer sets |
| [`Problem15.py`](Problem15.py) | Security Expert System with Forward Reasoning | OOP, propositional inference, rule firing |
| [`Problem16.py`](Problem16.py) | Smart Hospital Forward Chaining Engine | Knowledge base, subset matching, fixed-point inference |
| [`Problem17.py`](Problem17.py) | Hospital Expert System (Pre-seeded Facts) | Propositional rules, iterative deduction |
| [`Problem18.py`](Problem18.py) | Full Clinical Decision Support System | Interactive forward chaining, clinical decision rules |

### `python basic/` Directory: Core Python & OOP Exercises
| File | Topic / Description | Concepts Used |
| :--- | :--- | :--- |
| [`python basic/OOP01.py`](python%20basic/OOP01.py) | Student Record Database | Classes, instances, search loops, case-insensitivity |
| [`python basic/problemSolve01.py`](python%20basic/problemSolve01.py) | Electricity Billing with Area & Customer Verification | Composite lists, membership checking, usage tiers |
| [`python basic/problemSolve02.py`](python%20basic/problemSolve02.py) | Product Inventory Valuation | Multi-instance OOP, total value computation, categorization |

---

## 🛠️ Summary of Fixes Applied Across Codes

1. **Syntax & Constructor Fixes**:
   - Fixed `Weather._init_` to standard `Weather.__init__` in `Problem10.py`.
2. **Scope & Indentation Corrections**:
   - Extracted user interaction code out of class bodies (`Problem12.py`).
   - Fixed un-indented methods (`forward_chaining` and `display_results`) in `Problem16.py` and `Problem17.py`.
   - Fixed premature while-loop termination in `Problem17.py`.
3. **Undefined Variable & Unbound Reference Fixes**:
   - Added missing input for `bill_unit` in `Problem13.py`.
   - Prevented execution of billing when customer or area is invalid (`Problem12.py`, `Problem13.py`).
4. **Logic & Algorithmic Corrections**:
   - Fixed truthiness check on string `infrastructure_damage` in `Problem08.py` to compare with `"high"`.
   - Resolved boundary gap at unit `500` across `Problem11.py`, `Problem12.py`, `Problem13.py`, `Problem14.py`, and `problemSolve01.py`.
   - Fixed `Student` search bug in `Problem09.py` where `else:` was inside the loop printing "No student available" on every non-matching item.
   - Normalized customer lists to lowercase in `problemSolve01.py` so capitalization differences don't fail verification.
5. **Step-by-Step Documentation**:
   - Added numbered step comments throughout every file (`# Step 1: ...`, `# Step 2: ...`) explaining data structures, algorithms, and decision flows.

