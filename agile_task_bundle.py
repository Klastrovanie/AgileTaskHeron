# agile_task_bundle.py
import cudf
import cugraph
import pandas as pd
from typing import Dict, List

def analyze_task_bundle(edges: cudf.DataFrame) -> Dict:

    G = cugraph.Graph()
    G.from_cudf_edgelist(
        edges,
        source='src',
        destination='dst',
        edge_attr='weight'
    )

    pagerank_scores = cugraph.pagerank(G)

    workgroup, _ = cugraph.louvain(G)
    workgroup = workgroup.merge(pagerank_scores, on='vertex', how='left')

    result = {
        "priority_bundles": [],
        "pagerank_scores": pagerank_scores.to_pandas(),
        "graph_stats": {
            "nodes": G.number_of_nodes(),
            "edges": G.number_of_edges()
        }
    }

    partition_labels = workgroup['partition'].unique().to_arrow().to_pylist()
    for part in sorted(partition_labels):
        group = workgroup[workgroup['partition'] == part]
        
        tasks = group[group['vertex'].str.startswith('Task')]['vertex'].to_pandas().tolist()
        if not tasks:
            continue
        task_name = tasks[0]
        
        skills = group[group['vertex'].str.startswith('Skill')]['vertex'].to_pandas().tolist()
        people = group[group['vertex'].str.startswith('Person')]['vertex'].to_pandas().tolist()
        
        task_score = float(group[group['vertex'] == task_name]['pagerank'].iloc[0])
        
        result["priority_bundles"].append({
            "priority": len(result["priority_bundles"]) + 1,
            "task": task_name,
            "score": round(task_score, 4),
            "required_skills": skills,
            "available_people": people,
            "bundle_size": len(group)
        })

    return result


# ====================== Example ======================
if __name__ == "__main__":
    edges = cudf.DataFrame({
        'src': ['Person1', 'Person2', 'Task1', 'Person1', 'Task1', 'Task2', 'Person2', 'Person3', 'Person3'],
        'dst': ['Task1', 'Task2', 'Task2', 'Skill1', 'Skill1', 'Skill2', 'Skill2', 'Task1', 'Skill1'],
        'edge_type': ['Assigned_To', 'Completed', 'Depends_On', 'Has_Skill', 'Requires_Skill', 'Requires_Skill', 'Has_Skill', 'Completed', 'Has_Skill'],
        'weight': [1.0, 0.8, 0.5, 0.7, 0.6, 0.6, 0.6, 0.2, 0.2]
    })

    result = analyze_task_bundle(edges)
    print("=== Agile Task Bundle 결과 ===")
    for bundle in result["priority_bundles"]:
        print(f"{bundle['priority']} Ranking ─ {bundle['task']} (importance {bundle['score']})")
        print(f"   • Required Skills : {bundle['required_skills']}")
        print(f"   • Human resources : {bundle['available_people']}")