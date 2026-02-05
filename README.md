# Robotic Handwriting via SVG-to-Motion Pipeline (Dobot)
An end-to-end robotic handwriting system that converts SVG vector strokes into physical brushstrokes via computer vision, geometric path planning, and real-world robot control.
## Overview
This project implements an end-to-end robotic handwriting system that enables a Dobot robotic arm to write characters and full poems by converting SVG vector strokes into physical pen motions.<br>
The system bridges computer graphics, geometric path planning, and real-world robot control, transforming abstract vector representations into precise, repeatable handwriting on paper.
## Key Features
* ✍️ SVG-based character input (vector strokes)
* 🔁 Stroke-preserving path extraction and normalization
* 🖊 Pen-up / pen-down modeling via Z-axis control
* 🧩 Hierarchical control: stroke → character → poem
* 🧭 Deterministic queued motion execution
* 📐 Human-robot interaction of alignment correction for real-world paper handling
## System Pipeline
```text
FULL PIPELINE: SVG → Robot Handwriting (Dobot)

 ┌──────────────────────────────────────────────────────────────────┐
 │  0) INPUT ASSETS                                                  │
 │                                                                  │
 │   Character / glyph stored as SVG (vector strokes)                │
 │   e.g. "一.svg" , "春.svg" , ...                                  │
 └───────────────┬──────────────────────────────────────────────────┘
                 │
                 ▼
 ┌──────────────────────────────────────────────────────────────────┐
 │  1) SVG PARSING + NORMALIZATION                                   │
 │  Script: read.py                                                  │
 │                                                                  │
 │   - Reads SVG line-by-line                                        │
 │   - Extracts polyline points from points="x,y x,y ..."            │
 │   - Finds an origin (org_x, org_y)                                │
 │   - Normalizes & scales: (x-org_x)/450 , (y-org_y)/450            │
 │   - Inserts stroke separators: "s\n"                              │
 │                                                                  │
 │  Output: per-character stroke file                                │
 │   char/<CHAR>.txt                                                 │
 │   Format:                                                        │
 │     s                                                            │
 │     x y                                                          │
 │     x y                                                          │
 │     ...                                                          │
 │     s                                                            │
 │     ...                                                          │
 └───────────────┬──────────────────────────────────────────────────┘
                 │
                 ▼
 ┌──────────────────────────────────────────────────────────────────┐
 │  2) STROKE-LEVEL EXECUTION (Single Character)                      │
 │  Script: write_1.py                                               │
 │                                                                  │
 │   Input: one stroke block from <CHAR>.txt                         │
 │                                                                  │
 │   Robot actions (for each stroke):                                │
 │     1) PEN UP:  move to first (x0,y0) at safe Z                    │
 │     2) PEN DOWN: lower to writing depth (deepth / depth)           │
 │     3) DRAW:    follow all points (xi,yi) at constant Z            │
 │     4) PEN UP:  raise to safe Z                                    │
 │                                                                  │
 │   Uses:                                                           │
 │     - Dobot DLL via DobotDllType (ctypes bindings)                 │
 │     - queued motion commands + wait for completion                 │
 └───────────────┬──────────────────────────────────────────────────┘
                 │
                 ▼
 ┌──────────────────────────────────────────────────────────────────┐
 │  3) POEM / PAGE-LEVEL ORCHESTRATION (Multiple Characters)          │
 │  Script: model_4.py                                               │
 │                                                                  │
 │   Input: full poem typed by user (characters separated by spaces) │
 │                                                                  │
 │   Layout engine:                                                  │
 │     - Iterates a 4×7 grid (columns×rows)                           │
 │     - For each character:                                         │
 │         loads char/<CHAR>.txt                                     │
 │         iterates strokes ("s\n" separators)                        │
 │         executes strokes via PTP commands                          │
 │                                                                  │
 │   Real-world handling:                                             │
 │     - Paper reposition prompts                                    │
 │     - Alignment correction from point.txt (getdy())                │
 └───────────────┬──────────────────────────────────────────────────┘
                 │
                 ▼
 ┌──────────────────────────────────────────────────────────────────┐
 │  4) ROBOT CONTROL LAYER                                            │
 │  Library: DobotDllType + DobotDll.dll                              │
 │                                                                  │
 │   - ConnectDobot / DisconnectDobot                                 │
 │   - SetPTP*Params (speed/accel)                                    │
 │   - SetPTPCmd / SetPTPWithLCmd (Cartesian moves)                   │
 │   - Queued command execution + status polling                      │
 │                                                                  │
 │  Physical result: Dobot arm moves a pen over paper to write glyphs │
 └──────────────────────────────────────────────────────────────────┘


OPTIONAL RELATED SCRIPT (Manual demo / quick test):
 ┌──────────────────────────────────────────────────────────────────┐
 │ trial.py                                                          │
 │  - Connect, move to preset points                                 │
 │  - Conditional motion based on user input                          │
 │  - Useful for workspace checks and quick motion tests              │
 └──────────────────────────────────────────────────────────────────┘
```
## Repository Structure
```graphql
Image-to-Trajectory_Robot_Controller/
├── README.md
├── LICENSE
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── controller/
│   │   ├── __init__.py
│   │   ├── dobot_controller.py
│   │   ├── motion_commands.py
│   │   └── safety_checks.py
│   │
│   ├── communication/
│   │   ├── __init__.py
│   │   ├── serial_interface.py
│   │   └── protocol.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       └── logger.py
│
├── examples/
│   ├── basic_motion.py
│   ├── pick_and_place.py
│   ├── trajectory_demo.py
│   └── calibration_example.py
│
├── config/
│   ├── default.yaml
│   └── hardware.yaml
│
├── tests/
│   ├── test_connection.py
│   ├── test_motion.py
│   └── test_safety.py
│
└── scripts/
    ├── run_demo.sh
    └── connect_robot.py
```
## How It Works
1. SVG Parsing
* Characters are represented as SVG files composed of stroke polylines.
* read.py extracts stroke points, normalizes coordinates, and inserts stroke separators.
2. Stroke Execution
* write_1.py executes one character at a time:
 * Move to stroke start (pen up)
 * Lower pen (pen down)
 * Trace stroke points
 * Lift pen (pen up)
3. Poem Layout
* model_4.py arranges characters in a grid (e.g. 4×7 layout).
* Each character is written sequentially.
* Manual alignment correction compensates for paper movement.

## Technologies Used
* **Hardware**: Dobot robotic arm
* **Language**: Python (ctypes DLL bindings)
* **Robot Control**: Dobot SDK (PTP Cartesian motion)
* **Geometry**: SVG stroke extraction & normalization

## Example Use Cases
* Robotic handwriting and calligraphy demos
* Human–robot interaction experiments
* Vector-to-motion research

## One-Line Summary
An end-to-end system that converts SVG character strokes into precise robotic handwriting using a Dobot manipulator.
