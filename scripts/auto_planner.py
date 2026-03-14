#!/usr/bin/env python3
"""
AIC 自动计划模块
自动拆解复杂任务为可执行子步骤，生成执行计划
"""

import json
import yaml
from datetime import datetime
from pathlib import Path

class AutoPlanner:
    def __init__(self):
        self.plan_template = {
            "task_name": "",
            "created_at": "",
            "goal": "",
            "steps": [],
            "resources": {},
            "risks": [],
            "progress": {
                "current_step": 0,
                "completed": 0,
                "total": 0
            }
        }
    
    def decompose_task(self, task_description, max_depth=3):
        """拆解任务为子步骤"""
        # 简化实现，实际需集成 LLM
        steps = [
            {
                "id": 1,
                "description": f"Step 1: Analyze {task_description}",
                "tool": "thinking",
                "estimated_time": 30,
                "dependencies": [],
                "status": "pending"
            },
            {
                "id": 2,
                "description": f"Step 2: Plan execution for {task_description}",
                "tool": "planning",
                "estimated_time": 60,
                "dependencies": [1],
                "status": "pending"
            },
            {
                "id": 3,
                "description": f"Step 3: Execute plan for {task_description}",
                "tool": "execution",
                "estimated_time": 300,
                "dependencies": [2],
                "status": "pending"
            }
        ]
        return steps
    
    def create_plan(self, task_name, task_description, output_path=None):
        """创建执行计划"""
        plan = self.plan_template.copy()
        plan["task_name"] = task_name
        plan["created_at"] = datetime.now().isoformat()
        plan["goal"] = task_description
        plan["steps"] = self.decompose_task(task_description)
        plan["progress"]["total"] = len(plan["steps"])
        
        if output_path:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w') as f:
                yaml.dump(plan, f, default_flow_style=False, allow_unicode=True)
            print(f"Plan created: {output_path}")
        
        return plan
    
    def update_step(self, plan_path, step_id, status, result=None):
        """更新步骤状态"""
        with open(plan_path, 'r') as f:
            plan = yaml.safe_load(f)
        
        for step in plan["steps"]:
            if step["id"] == step_id:
                step["status"] = status
                if result:
                    step["result"] = result
                if status == "completed":
                    plan["progress"]["completed"] += 1
                break
        
        with open(plan_path, 'w') as f:
            yaml.dump(plan, f, default_flow_style=False, allow_unicode=True)
        
        print(f"Step {step_id} updated to {status}")
    
    def replan(self, plan_path, reason):
        """重新规划"""
        with open(plan_path, 'r') as f:
            plan = yaml.safe_load(f)
        
        # 记录重新规划原因
        if "replans" not in plan:
            plan["replans"] = []
        plan["replans"].append({
            "timestamp": datetime.now().isoformat(),
            "reason": reason
        })
        
        # 重新拆解未完成的任务
        remaining_steps = [s for s in plan["steps"] if s["status"] == "pending"]
        # 简化：重新生成步骤
        plan["steps"] = self.decompose_task(plan["goal"])
        plan["progress"]["completed"] = 0
        
        with open(plan_path, 'w') as f:
            yaml.dump(plan, f, default_flow_style=False, allow_unicode=True)
        
        print(f"Plan replanned due to: {reason}")

if __name__ == "__main__":
    import sys
    
    planner = AutoPlanner()
    
    if len(sys.argv) < 2:
        print("Usage: python auto_planner.py <command> [args]")
        print("Commands: create, update, replan")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "create":
        task_name = sys.argv[2] if len(sys.argv) > 2 else "Untitled"
        task_desc = sys.argv[3] if len(sys.argv) > 3 else "No description"
        output = sys.argv[4] if len(sys.argv) > 4 else "temp/task-plan.yaml"
        planner.create_plan(task_name, task_desc, output)
    
    elif command == "update":
        plan_path = sys.argv[2]
        step_id = int(sys.argv[3])
        status = sys.argv[4]
        planner.update_step(plan_path, step_id, status)
    
    elif command == "replan":
        plan_path = sys.argv[2]
        reason = sys.argv[3] if len(sys.argv) > 3 else "Unknown"
        planner.replan(plan_path, reason)
    
    else:
        print(f"Unknown command: {command}")
