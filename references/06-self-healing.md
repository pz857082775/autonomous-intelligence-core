# 模块 06：自动修复（自愈能力）

## 能力概述
感知到自身报错、技能失效、软件崩溃、界面卡死时自动修复，修复后自动验证。

---

## 异常检测

### 检测范围
| 检测对象 | 异常类型 | 检测方式 |
|----------|----------|----------|
| 自身运行 | 进程崩溃、内存溢出 | 进程监控 |
| 技能加载 | 技能失效、版本冲突 | 技能检查 |
| 软件状态 | 崩溃、无响应、卡死 | 窗口/API 检测 |
| 界面状态 | 元素丢失、页面错误 | 截图/DOM 检查 |
| 任务执行 | 超时、失败、报错 | 执行日志 |

### 异常分级
| 级别 | 描述 | 响应 |
|------|------|------|
| 致命 | 系统崩溃、数据丢失风险 | 立即修复，必要时回滚 |
| 严重 | 核心功能失效 | 立即修复 |
| 一般 | 非核心功能异常 | 尝试修复，可降级 |
| 轻微 | 性能下降、警告 | 记录，择机处理 |

---

## 修复动作库

### 1. 重启模块
```bash
# 重启 OpenClaw Gateway
openclaw gateway restart

# 重启特定技能
python scripts/skill_manager.py restart --skill skill-name

# 重启浏览器
browser action stop && browser action start
```

### 2. 重置状态
```bash
# 清理临时状态
rm -rf temp/*.tmp

# 重置会话状态
python scripts/state_manager.py reset --session session-id

# 清理缓存
rm -rf ~/.openclaw/cache/*
```

### 3. 回滚操作
```bash
# 文件回滚（使用 trash 恢复）
trash --restore file-path

# Git 回滚
cd workspace && git checkout -- file-path

# 状态回滚
python scripts/state_manager.py rollback --to checkpoint-id
```

### 4. 替换失效逻辑
```bash
# 重新加载技能
python scripts/skill_manager.py reload --skill skill-name

# 更新技能版本
clawhub update skill-name

# 切换备用方案
python scripts/failover.py switch --from skill-a --to skill-b
```

### 5. 重新加载资源
```bash
# 重新加载配置
openclaw config reload

# 重新加载记忆
python scripts/memory_manager.py reload

# 重新初始化环境
python scripts/env_init.py --force
```

---

## 修复流程

```
检测到异常
  ↓
分类异常类型
  ↓
选择修复策略
  ↓
执行修复动作
  ↓
验证修复结果
  ↓
成功 → 继续任务
  ↓
失败 → 升级修复/报告用户
```

---

## 修复策略选择

### 决策树
```
异常类型？
├── 进程崩溃 → 重启进程
├── 内存溢出 → 清理缓存 + 重启
├── 技能失效 → 重新加载技能
├── 网络断开 → 重试连接 → 切换网络
├── 文件丢失 → 从备份恢复 → 重新生成
├── 界面卡死 → 关闭重开 → 切换操作方式
└── 未知异常 → 记录日志 → 报告用户
```

### 修复优先级
1. **最小影响**：优先选择影响最小的修复方式
2. **最快恢复**：在可行方案中选择最快的
3. **最稳方案**：选择成功率最高的方案

---

## 修复验证

### 验证方式
| 验证类型 | 方法 | 判定标准 |
|----------|------|----------|
| 功能验证 | 执行测试操作 | 功能恢复正常 |
| 状态验证 | 检查系统状态 | 指标回到正常范围 |
| 日志验证 | 检查错误日志 | 无新错误产生 |
| 任务验证 | 继续原任务 | 任务可继续执行 |

### 验证脚本
```bash
# 验证修复结果
python scripts/self_healer.py verify --check-type functional --target target-name

# 健康检查
python scripts/self_healer.py health-check
```

---

## 无法修复时的处理

### 生成修复方案
```markdown
## 待修复问题

问题描述：[详细描述]
影响范围：[影响的功能]
尝试过的修复：[已尝试的方法]
失败原因：[为什么失败]

建议方案：
1. [方案 1] - 成功率 X%
2. [方案 2] - 成功率 Y%

需要用户操作：
- [需要用户确认/执行的操作]
```

### 记录待优化项
```markdown
## 待优化记录

问题 ID: HEAL-YYYYMMDD-001
问题类型：[类型]
发生时间：YYYY-MM-DD HH:MM
根本原因：[分析结果]
长期解决方案：[需要开发的修复能力]
优先级：P1/P2/P3
```

---

## 修复脚本

使用 `scripts/self_healer.py` 管理修复：

```bash
# 自动修复
python scripts/self_healer.py auto-fix --error "错误信息"

# 手动触发修复
python scripts/self_healer.py fix --action restart --target target-name

# 查看修复历史
python scripts/self_healer.py history --limit 20

# 生成修复报告
python scripts/self_healer.py report --output temp/healing-report.md
```

---

## 修复日志

### 日志格式
```markdown
## 修复记录 [HEAL-YYYYMMDD-XXX]

时间：YYYY-MM-DD HH:MM:SS
异常类型：[类型]
异常描述：[描述]
修复动作：[执行的修复]
修复结果：成功/失败
验证结果：通过/失败
耗时：X 秒
```

---

## 相关模块
- ← [04-execution.md](04-execution.md) 执行异常触发修复
- → [07-self-improvement.md](07-self-improvement.md) 修复经验用于自我完善
- → [08-memory.md](08-memory.md) 修复记录存入记忆
