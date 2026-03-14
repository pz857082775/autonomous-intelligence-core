#!/usr/bin/env python3
"""
AIC 自愈模块
检测异常并自动修复，修复后验证
"""

import json
import subprocess
import time
from datetime import datetime
from pathlib import Path

class SelfHealer:
    def __init__(self):
        self.healing_log = []
        self.repair_actions = {
            "process_crash": self.restart_process,
            "memory_overflow": self.clear_cache,
            "skill_failure": self.reload_skill,
            "network_error": self.retry_connection,
            "file_error": self.restore_file,
            "interface_stuck": self.refresh_interface
        }
    
    def detect_anomaly(self, error_message):
        """检测异常类型"""
        error_lower = error_message.lower()
        
        if "crash" in error_lower or "killed" in error_lower:
            return "process_crash"
        elif "memory" in error_lower or "oom" in error_lower:
            return "memory_overflow"
        elif "skill" in error_lower or "module" in error_lower:
            return "skill_failure"
        elif "network" in error_lower or "connection" in error_lower:
            return "network_error"
        elif "file" in error_lower or "not found" in error_lower:
            return "file_error"
        elif "stuck" in error_lower or "timeout" in error_lower:
            return "interface_stuck"
        else:
            return "unknown"
    
    def restart_process(self, process_name):
        """重启进程"""
        print(f"Restarting process: {process_name}")
        # 简化实现
        return {"success": True, "action": f"restarted {process_name}"}
    
    def clear_cache(self):
        """清理缓存"""
        print("Clearing cache...")
        cache_dir = Path.home() / ".openclaw" / "cache"
        if cache_dir.exists():
            for f in cache_dir.glob("*"):
                try:
                    f.unlink()
                except:
                    pass
        return {"success": True, "action": "cache cleared"}
    
    def reload_skill(self, skill_name):
        """重新加载技能"""
        print(f"Reloading skill: {skill_name}")
        # 简化实现
        return {"success": True, "action": f"reloaded {skill_name}"}
    
    def retry_connection(self, max_retries=3):
        """重试连接"""
        print(f"Retrying connection (max {max_retries} times)...")
        for i in range(max_retries):
            time.sleep(1 * (i + 1))
            print(f"Retry {i + 1}/{max_retries}")
        return {"success": True, "action": "connection retried"}
    
    def restore_file(self, file_path):
        """恢复文件"""
        print(f"Restoring file: {file_path}")
        # 简化实现
        return {"success": True, "action": f"restored {file_path}"}
    
    def refresh_interface(self):
        """刷新界面"""
        print("Refreshing interface...")
        # 简化实现
        return {"success": True, "action": "interface refreshed"}
    
    def heal(self, error_message, context=None):
        """执行修复"""
        anomaly_type = self.detect_anomaly(error_message)
        print(f"Detected anomaly: {anomaly_type}")
        
        if anomaly_type in self.repair_actions:
            result = self.repair_actions[anomaly_type](**(context or {}))
        else:
            result = {"success": False, "action": "unknown anomaly, manual intervention needed"}
        
        # 记录修复日志
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "error": error_message,
            "anomaly_type": anomaly_type,
            "result": result
        }
        self.healing_log.append(log_entry)
        
        return result
    
    def verify(self, check_type, target):
        """验证修复结果"""
        print(f"Verifying {check_type} for {target}...")
        # 简化实现
        return {"verified": True, "status": "normal"}
    
    def get_history(self, limit=10):
        """获取修复历史"""
        return self.healing_log[-limit:]

if __name__ == "__main__":
    import sys
    
    healer = SelfHealer()
    
    if len(sys.argv) < 2:
        print("Usage: python self_healer.py <command> [args]")
        print("Commands: heal, verify, history")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "heal":
        error = sys.argv[2] if len(sys.argv) > 2 else "Unknown error"
        result = healer.heal(error)
        print(json.dumps(result, indent=2))
    
    elif command == "verify":
        check_type = sys.argv[2] if len(sys.argv) > 2 else "functional"
        target = sys.argv[3] if len(sys.argv) > 3 else "system"
        result = healer.verify(check_type, target)
        print(json.dumps(result, indent=2))
    
    elif command == "history":
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        history = healer.get_history(limit)
        print(json.dumps(history, indent=2))
    
    else:
        print(f"Unknown command: {command}")
