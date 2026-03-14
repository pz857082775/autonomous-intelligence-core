#!/usr/bin/env python3
"""
AIC 感知监控模块
实时监控系统环境、OpenClaw 状态、外部界面、任务环境
"""

import json
import psutil
import time
from datetime import datetime
from pathlib import Path

class PerceptionMonitor:
    def __init__(self):
        self.last_check = {}
        self.changes = []
        
    def check_system(self):
        """检查系统环境"""
        return {
            "timestamp": datetime.now().isoformat(),
            "cpu": {
                "usage": psutil.cpu_percent(interval=1),
                "cores": psutil.cpu_count(),
                "freq": psutil.cpu_freq().current if psutil.cpu_freq() else None
            },
            "memory": {
                "total": psutil.virtual_memory().total,
                "available": psutil.virtual_memory().available,
                "percent": psutil.virtual_memory().percent
            },
            "disk": {
                "total": psutil.disk_usage('/').total,
                "used": psutil.disk_usage('/').used,
                "percent": psutil.disk_usage('/').percent
            },
            "network": {
                "io": psutil.net_io_counters()._asdict()
            }
        }
    
    def check_self(self):
        """检查 OpenClaw 自身状态"""
        # 简化实现，实际需集成 OpenClaw API
        return {
            "timestamp": datetime.now().isoformat(),
            "status": "running",
            "skills_loaded": [],
            "memory_usage": 0,
            "active_tasks": 0
        }
    
    def detect_changes(self, current, category):
        """检测变化"""
        changes = []
        if category in self.last_check:
            last = self.last_check[category]
            # 简单对比实现
            if current != last:
                changes.append(f"{category} changed")
        self.last_check[category] = current
        return changes
    
    def run_monitoring(self):
        """运行监控循环"""
        print("Starting AIC Perception Monitor...")
        while True:
            try:
                # 系统检查
                system_status = self.check_system()
                changes = self.detect_changes(system_status, "system")
                
                # 自身检查
                self_status = self.check_self()
                changes.extend(self.detect_changes(self_status, "self"))
                
                # 输出结果
                result = {
                    "timestamp": datetime.now().isoformat(),
                    "system": system_status,
                    "self": self_status,
                    "changes": changes
                }
                
                print(json.dumps(result, indent=2))
                
                # 休眠 1 秒
                time.sleep(1)
                
            except KeyboardInterrupt:
                print("Monitor stopped.")
                break
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(1)

if __name__ == "__main__":
    monitor = PerceptionMonitor()
    monitor.run_monitoring()
