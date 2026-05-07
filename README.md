# NTU Data Science (SCTP) Pre-Assessment Technical Test Answers

## Overview
- This file contains the answers to all 8 questions in the source (src) folder
- The solutions were done locally on Visual Studio Code 2 and then pushed to my GitHub account

## Files

Each file contains one question. Every solution has two parts: defining a
function (or class) and invoking it with the scenarios specified in the
original assessment.

| File | Topic | What it covers |
|------|-------|----------------|
| `q1.py` | `swap` | variables, type checking, tuple unpacking |
| `q2.py` | `check_divisibility` | operators, modulo, input validation |
| `q3.py` | `string_reverse` | strings, slice notation, immutability |
| `q4.py` | `find_and_replace` | lists, `enumerate`, mutation |
| `q5.py` | `update_dictionary` | dictionaries, key existence checks |
| `q6.py` | `find_first_negative` | `while` loops, manual index counter |
| `q7.py` | `Car` class | classes, `__init__`, `self`, methods |
| `q8.py` | Prompt comparison | written analysis on prompt design |

## Notes on design choices

A few small choices worth flagging:
- In Q1, booleans are rejected before the numeric check, because `bool` is
  a subclass of `int` in Python and would otherwise slip through.
- In Q4 and Q5, the functions modify the input list/dict in place. This is
  the natural reading of the spec.
- In Q6, the `while` loop uses strict `<` against `len(lst)` to avoid the
  off-by-one error, and increments the counter before the next iteration to
  avoid an infinite loop.
- In Q7, `__init__` stores values as instance attributes via `self.x = x`,
  and `describe_car` reads them back. The car is instantiated with keyword
  arguments to keep the call site readable.
- In Q8, the answers are reflected either as comments (#) or with triple quote (''') for longer answers.
