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


## License

AGPL v3 — free for research and non-commercial use.  
Commercial use requires a separate agreement.

For commercial licensing: leave a message on [Discussions](../../discussions)

## Copyright

Copyright © 2026 Klastrovanie Co., Ltd. All rights reserved.
