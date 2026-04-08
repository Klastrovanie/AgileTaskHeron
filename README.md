# AgileTaskHeron
Automated Agile Task Force Optimization using Heterogeneous Graphs

AgileTaskHeron is an intelligent graph engine that automatically **prioritizes tasks** and creates optimal **Task-Skill-Person bundles** for Agile teams.

By modeling **Tasks**, **Required Skills**, and **Human Resources** (including past experience) in a single heterogeneous graph, it delivers:

- Task priority ranking using **PageRank**
- Natural team bundles using **Louvain community detection**
- Ready-to-use Agile sprint recommendations

Built with GPU acceleration (RAPIDS cuGraph + cuDF) for high performance.

---

### ✨ Key Features
- Task-centric priority calculation (PageRank)
- Automatic discovery of meaningful Task-Skill-Person bundles (Louvain)
- Weight-based importance control (HR team’s subjective judgment supported)
- GPU-accelerated computation
- Easy-to-use Jupyter Notebook demo

---

### 🚀 Quick Start

# 1. Create environment
```bash
conda env create -f environment.yml
conda activate rapids
```

# 2. Run example
```bash  
python agile_task_bundle.py
```

### How to Use

1. Prepare your edges DataFrame with src, dst, edge_type, and weight
2. Call analyze_task_bundle(edges)
3. Get Agile priority order + recommended bundles instantly

Weight Guidelines
- Range: 0.1 ~ 1.0 (0 is not allowed)  
- 1.0 = critically important  
- 0.1 = slightly related

The weight is subjective — HR or Agile teams should assign values based on real business importance, past performance, and strategic priority.

### Key Advantages

Unlike deep learning-based team recommendation systems that require extensive historical data, long training periods, and periodic retraining whenever the organization changes, AgileTaskHeron is completely <b>training-free.</b>

It is designed to work instantly using only your existing data:

- <b>Leverages existing knowledge</b>: Team leaders’ performance reviews, past project evaluations, and domain expertise can be directly converted into edge weights.
- <b>Instant Task Force creation</b>: As soon as a new task appears, the system can immediately generate optimized Task-Skill-Person bundles and priorities — no retraining needed.
- <b>Truly Task-Oriented</b>: It explicitly calculates which tasks are most important and in what order they should be executed, rather than simply matching people to skills.
- <b>High flexibility</b>: Users have full control to define and adjust edge weights based on business priorities, strategic importance, or real-world experience.

This makes AgileTaskHeron particularly powerful for HR teams and Agile organizations that want fast, practical, and explainable results without the complexity and maintenance overhead of deep learning models.


## License

AGPL v3 — free for research and non-commercial use.  
Commercial use requires a separate agreement.

For commercial licensing: leave a message on [Discussions](../../discussions)

## Copyright

Copyright © 2026 Klastrovanie Co., Ltd. All rights reserved.
