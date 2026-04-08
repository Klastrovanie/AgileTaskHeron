# AgileTaskHeron

**First Public Release:** 2026-04-08  
**Last Updated:** 2026-04-08

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

### What makes AgileTaskHeron unique?

While **PageRank** and **Louvain community detection** are well-known algorithms used in many graph analysis tools, **AgileTaskHeron** is fundamentally different in purpose and design.

**Key differentiators:**

- **Task-centric heterogeneous graph**  
  Most tools analyze general networks (social, knowledge, or organizational graphs).  
  AgileTaskHeron is specifically designed around **Tasks** as the central node, connecting **Required Skills** and **Human Resources** in one unified graph.

- **Task-first priority + natural bundle generation**  
  It doesn’t just find communities or important nodes — it simultaneously calculates **which tasks should be done first** and automatically creates **ready-to-use Task-Skill-Person bundles**.

- **No training required**  
  Unlike deep learning or machine learning-based team recommendation systems, AgileTaskHeron works instantly using only your current data and edge weights. No historical dataset or retraining is needed.

- **Full user control over edges and weights**  
  You define every relationship and importance (weight) yourself. The algorithm respects your domain knowledge and business priorities completely.

- **Built for real Agile / HR workflows**  
  The output is not abstract graph metrics — it directly produces **Agile sprint priority + recommended task forces** that HR and Agile teams can use immediately.

In short, while the underlying algorithms are standard, the **combination, focus on Tasks, and practical Agile application** make AgileTaskHeron unique.

Other tools may use PageRank + Louvain for general network analysis, but none combine them in this specific way to solve **dynamic Agile Task Force formation**.

---

### Key Advantages

Unlike deep learning-based team recommendation systems that require extensive historical data, long training periods, and periodic retraining whenever the organization changes, AgileTaskHeron is completely <b>training-free.</b>

It is designed to work instantly using only your existing data:

- <b>Leverages existing knowledge</b>: Team leaders’ performance reviews, past project evaluations, and domain expertise can be directly converted into edge weights.
- <b>Instant Task Force creation</b>: As soon as a new task appears, the system can immediately generate optimized Task-Skill-Person bundles and priorities — no retraining needed.
- <b>Truly Task-Oriented</b>: It explicitly calculates which tasks are most important and in what order they should be executed, rather than simply matching people to skills.
- <b>High flexibility</b>: Users have full control to define and adjust edge weights based on business priorities, strategic importance, or real-world experience.

This makes AgileTaskHeron particularly powerful for HR teams and Agile organizations that want fast, practical, and explainable results without the complexity and maintenance overhead of deep learning models.

---

### 🚀 Quick Start

#### 1. Create environment
```bash
conda env create -f environment.yml
conda activate rapids
```

#### 2. Run example
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


## Prior Art

To the best of our knowledge, no existing patent covers the specific combination of PageRank-based task priority ranking and Louvain community detection applied to a Task-Skill-Person heterogeneous graph for automated Agile Task Force formation.
Searched across USPTO, EPO, WIPO, KIPRIS, and CNIPA via Google Patents, Espacenet, KIPRIS, and Patentscope. (April 2026)


## License

AGPL v3 — free for research and non-commercial use.  
Commercial use requires a separate agreement.

For commercial licensing: leave a message on [Discussions](../../discussions)


## Pricing

For commercial / closed-source use:

| Users | Annual License |
|-------|---------------|
| up to 50 | $2,000 / year |
| up to 100 | $3,500 / year |
| up to 200 | $4,500 / year |
| Enterprise (unlimited) | Custom quote |

### Why AgileTaskHeron?

| | Jira® Premium | AgileTaskHeron |
|---|---|---|
| Up to 50 users / year | ~$8,724 | $2,000 |
| Up to 100 users / year | ~$17,448 | $3,500 |
| Up to 200 users / year | ~$34,896 | $4,500 |
| Enterprise (unlimited) | Custom | Custom quote |
| Graph-based automatic team formation | ❌ | ✅ |
| Automatic task priority ranking | ❌ | ✅ |
| Data privacy | Atlassian cloud | Your own server |
| Infrastructure | Included | Your own (AWS, on-prem, etc.) |

> Jira® is a registered trademark of Atlassian Corporation.  
> Pricing verified via official Atlassian pricing page, April 2026.


## Copyright

Copyright © 2026 Klastrovanie Co., Ltd. All rights reserved.
