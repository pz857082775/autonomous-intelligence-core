#!/usr/bin/env python3
"""
AIC 记忆管理模块
管理长期记忆和短期记忆的存储、检索、更新
"""

import json
import re
from datetime import datetime
from pathlib import Path

class MemoryManager:
    def __init__(self, workspace_path=None):
        if workspace_path is None:
            workspace_path = Path.home() / "openclaw" / "workspace"
        self.workspace = Path(workspace_path)
        self.memory_file = self.workspace / "MEMORY.md"
        self.memory_dir = self.workspace / "memory"
        self.temp_dir = self.workspace / "temp"
        
        # 确保目录存在
        self.memory_dir.mkdir(parents=True, exist_ok=True)
        self.temp_dir.mkdir(parents=True, exist_ok=True)
    
    def get_daily_file(self, date=None):
        """获取每日记忆文件"""
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        return self.memory_dir / f"{date}.md"
    
    def write_memory(self, content, memory_type="daily", date=None):
        """写入记忆"""
        if memory_type == "daily":
            file_path = self.get_daily_file(date)
        elif memory_type == "long-term":
            file_path = self.memory_file
        elif memory_type == "temp":
            file_path = self.temp_dir / "current-task.md"
        else:
            file_path = self.get_daily_file(date)
        
        # 追加内容
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f"\n{content}\n")
        
        print(f"Memory written to: {file_path}")
        return file_path
    
    def search_memory(self, query, max_results=10):
        """搜索记忆（简化实现）"""
        results = []
        
        # 搜索每日记忆
        for file_path in self.memory_dir.glob("*.md"):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if query.lower() in content.lower():
                    results.append({
                        "path": str(file_path),
                        "snippet": content[:200] + "..."
                    })
        
        # 搜索长期记忆
        if self.memory_file.exists():
            with open(self.memory_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if query.lower() in content.lower():
                    results.append({
                        "path": str(self.memory_file),
                        "snippet": content[:200] + "..."
                    })
        
        return results[:max_results]
    
    def get_memory(self, path, from_line=None, lines=None):
        """读取记忆片段"""
        file_path = Path(path)
        if not file_path.exists():
            return {"error": "File not found"}
        
        with open(file_path, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
        
        if from_line is not None:
            start = from_line - 1
            end = start + lines if lines else len(all_lines)
            selected_lines = all_lines[start:end]
        else:
            selected_lines = all_lines
        
        return {
            "path": str(file_path),
            "content": "".join(selected_lines)
        }
    
    def compact_memory(self, archive_older_than=30):
        """整理记忆，归档旧文件"""
        today = datetime.now()
        archived = []
        
        for file_path in self.memory_dir.glob("*.md"):
            # 解析文件名日期
            match = re.match(r"(\d{4}-\d{2}-\d{2})\.md", file_path.name)
            if match:
                file_date = datetime.strptime(match.group(1), "%Y-%m-%d")
                days_old = (today - file_date).days
                
                if days_old > archive_older_than:
                    # 移动到归档目录
                    archive_dir = self.memory_dir / "archive"
                    archive_dir.mkdir(exist_ok=True)
                    new_path = archive_dir / file_path.name
                    file_path.rename(new_path)
                    archived.append(str(file_path.name))
        
        return {"archived": archived}
    
    def export_memory(self, output_path):
        """导出记忆"""
        export_data = {
            "exported_at": datetime.now().isoformat(),
            "long_term": "",
            "daily": []
        }
        
        # 导出长期记忆
        if self.memory_file.exists():
            with open(self.memory_file, 'r', encoding='utf-8') as f:
                export_data["long_term"] = f.read()
        
        # 导出每日记忆
        for file_path in sorted(self.memory_dir.glob("*.md")):
            with open(file_path, 'r', encoding='utf-8') as f:
                export_data["daily"].append({
                    "date": file_path.stem,
                    "content": f.read()
                })
        
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)
        
        print(f"Memory exported to: {output_path}")
        return output_path

if __name__ == "__main__":
    import sys
    
    manager = MemoryManager()
    
    if len(sys.argv) < 2:
        print("Usage: python memory_manager.py <command> [args]")
        print("Commands: write, search, get, compact, export")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "write":
        content = sys.argv[2] if len(sys.argv) > 2 else ""
        memory_type = sys.argv[3] if len(sys.argv) > 3 else "daily"
        manager.write_memory(content, memory_type)
    
    elif command == "search":
        query = sys.argv[2] if len(sys.argv) > 2 else ""
        results = manager.search_memory(query)
        print(json.dumps(results, indent=2, ensure_ascii=False))
    
    elif command == "get":
        path = sys.argv[2] if len(sys.argv) > 2 else ""
        result = manager.get_memory(path)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    elif command == "compact":
        days = int(sys.argv[2]) if len(sys.argv) > 2 else 30
        result = manager.compact_memory(days)
        print(json.dumps(result, indent=2))
    
    elif command == "export":
        output = sys.argv[2] if len(sys.argv) > 2 else "temp/memory-export.json"
        manager.export_memory(output)
    
    else:
        print(f"Unknown command: {command}")
