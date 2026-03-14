# 模块 09：自动调用（技能/资源调度）

## 能力概述
自动识别当前任务需要的子技能/工具/软件，一键调用。支持跨技能链式调用，调用失败自动重试/切换替代方案。

---

## 调用识别

### 技能匹配
```
任务需求分析
  ↓
提取关键动作（动词）
  ↓
匹配技能描述（description）
  ↓
选择最优技能
  ↓
验证技能可用
```

### 匹配规则
| 规则 | 说明 | 优先级 |
|------|------|--------|
| 精确匹配 | 技能名/描述完全匹配需求 | 最高 |
| 语义匹配 | 技能描述语义相似 | 高 |
| 功能匹配 | 技能能完成所需功能 | 中 |
| 近似匹配 | 技能可部分满足需求 | 低 |

### 技能选择矩阵
| 任务类型 | 首选技能 | 备选技能 |
|----------|----------|----------|
| PDF 处理 | `pdf` | `pdf-text-extractor` |
| Word 处理 | `docx` | - |
| Excel 处理 | `xlsx` | - |
| 网页搜索 | `cn-web-search` | `web_fetch` |
| 浏览器操作 | `agent-browser` | `browser` |
| 天气查询 | `weather` | - |
| 财经数据 | `finance-data` | - |

---

## 调用方式

### 1. 技能调用
```bash
# 通过 sessions_spawn 调用子技能
python scripts/skill_invoker.py spawn --skill skill-name --task "任务描述"

# 通过 sessions_send 发送消息
python scripts/skill_invoker.py send --session session-key --message "指令"
```

### 2. 工具调用
```bash
# 调用 OpenClaw 工具
python scripts/tool_invoker.py call --tool exec --command "ls -la"

# 链式调用
python scripts/tool_invoker.py chain --steps "exec,read,write"
```

### 3. 软件调用
```bash
# 启动软件
python scripts/app_invoker.py launch --app app-name

# 执行软件操作
python scripts/app_invoker.py action --app app-name --action "click" --target "按钮"
```

### 4. API 调用
```bash
# 调用外部 API
python scripts/api_invoker.py call --endpoint url --method POST --data json-data
```

---

## 调用规则

### 最优匹配原则
1. **功能匹配度最高**：选择最能完成任务的技能
2. **响应速度最快**：选择执行最快的方案
3. **资源占用最低**：选择最省资源的方案
4. **稳定性最好**：选择最可靠的方案

### 调用优先级
```
1. 本地技能（已安装）
2. 远程技能（可快速安装）
3. 工具调用（exec/browser 等）
4. 外部 API
5. 人工协助（最后手段）
```

---

## 链式调用

### 调用链结构
```
任务：处理 PDF 并提取文字

调用链：
1. pdf-text-extractor → 提取文本
   ↓
2. memory_manager → 存储结果
   ↓
3. copywriting → 润色文本
   ↓
4. docx → 生成文档
```

### 调用链配置
```yaml
chain:
  name: pdf-process-chain
  steps:
    - skill: pdf-text-extractor
      input: "${file_path}"
      output: "${extracted_text}"
    - skill: memory_manager
      input: "${extracted_text}"
      output: "${memory_id}"
    - skill: copywriting
      input: "${extracted_text}"
      output: "${polished_text}"
    - skill: docx
      input: "${polished_text}"
      output: "${output_file}"
```

### 数据传递
```
步骤 1 输出 → 步骤 2 输入
  ↓
格式转换（如需要）
  ↓
验证数据完整性
  ↓
传递到下一步
```

---

## 调用失败处理

### 失败类型
| 失败类型 | 原因 | 处理策略 |
|----------|------|----------|
| 技能不存在 | 未安装 | 安装技能或切换替代 |
| 技能加载失败 | 依赖缺失 | 安装依赖或跳过 |
| 调用超时 | 执行过慢 | 重试或切换 |
| 执行错误 | 逻辑错误 | 分析错误，重试或报告 |
| 结果无效 | 输出不符合预期 | 验证失败，重试 |

### 自动重试
```bash
# 配置重试
python scripts/skill_invoker.py call --skill skill-name --retry 3 --backoff exponential

# 重试策略：
# - 第 1 次失败：等待 1 秒重试
# - 第 2 次失败：等待 2 秒重试
# - 第 3 次失败：等待 4 秒重试
# - 第 4 次失败：切换替代方案
```

### 替代方案切换
```
主技能失败
  ↓
查找备选技能列表
  ↓
选择最优备选
  ↓
执行备选方案
  ↓
记录主技能失败原因
```

---

## 调用日志

### 日志格式
```markdown
## 调用记录 [INV-YYYYMMDD-XXX]

时间：YYYY-MM-DD HH:MM:SS
调用类型：[技能/工具/软件/API]
调用对象：[名称]
输入参数：{...}
执行结果：成功/失败
输出结果：{...}
耗时：X 秒
重试次数：X
```

---

## 调用脚本

使用 `scripts/skill_invoker.py` 管理调用：

```bash
# 调用技能
python scripts/skill_invoker.py spawn --skill skill-name --task "任务"

# 链式调用
python scripts/skill_invoker.py chain --config chain-config.yaml

# 查看调用历史
python scripts/skill_invoker.py history --limit 20

# 查看技能状态
python scripts/skill_invoker.py status --skill skill-name
```

---

## 相关模块
- ← [03-planning.md](03-planning.md) 接收计划中的技能需求
- → [04-execution.md](04-execution.md) 执行调用
- → [10-coordination.md](10-coordination.md) 协调多调用
