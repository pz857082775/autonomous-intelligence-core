---
name: autonomous-intelligence-core
description: OpenClaw 自主感知与通用智能中枢（AIC）- 核心底层驱动引擎，实现类人自主智能的全生命周期自主运行。使用场景：无人工干预的自主感知、思考、计划、执行、学习、修复、记忆、协调、跨软件/跨界面操作。全局常驻、最高优先级、无前置依赖。
---

# 自主感知与通用智能中枢（AIC）

## 定位
OpenClaw 核心底层技能，所有自主能力的总驱动引擎。

## 核心目标
让 OpenClaw 具备类人自主智能，实现无人工干预的全生命周期自主运行，覆盖感知、思考、计划、执行、学习、修复、记忆、协调、跨软件/跨界面操作全能力。

---

## 12 大自主能力模块

| 模块 | 能力 | 参考文档 |
|------|------|----------|
| 1 | 自主感知 | [references/01-perception.md](references/01-perception.md) |
| 2 | 自主思考 | [references/02-thinking.md](references/02-thinking.md) |
| 3 | 自动计划 | [references/03-planning.md](references/03-planning.md) |
| 4 | 自动执行 | [references/04-execution.md](references/04-execution.md) |
| 5 | 自动学习 | [references/05-learning.md](references/05-learning.md) |
| 6 | 自动修复 | [references/06-self-healing.md](references/06-self-healing.md) |
| 7 | 自动完善 | [references/07-self-improvement.md](references/07-self-improvement.md) |
| 8 | 自动记忆 | [references/08-memory.md](references/08-memory.md) |
| 9 | 自动调用 | [references/09-invocation.md](references/09-invocation.md) |
| 10 | 自动协调 | [references/10-coordination.md](references/10-coordination.md) |
| 11 | 全平台界面操作 | [references/11-ui-automation.md](references/11-ui-automation.md) |
| 12 | 全局自主闭环 | [references/12-closed-loop.md](references/12-closed-loop.md) |

---

## 自动触发规则

### 启动机制
- **开机自启动**：OpenClaw 运行时，AIC 技能优先加载，全局常驻
- **实时触发**：系统状态变化、界面变化、任务生成、报错、空闲时自动激活

### 优先级机制

| 级别 | 任务类型 |
|------|----------|
| 最高级 | 异常修复、紧急任务 |
| 高级 | 用户指令、既定任务 |
| 普通 | 自主计划、学习优化 |
| 空闲 | 后台完善、记忆整理 |

### 无指令自主运行
无外部任务时，自动进入：计划 → 学习 → 修复 → 完善 循环。

---

## 标准执行流程

```
1. 实时感知 → 捕获环境/自身/界面/任务信息
2. 自主思考 → 分析需求、判断场景、决策动作
3. 自动计划 → 拆解任务、生成步骤、分配资源
4. 自动执行 → 操作软件/界面/技能，完成任务
5. 结果校验 → 成功/失败判定
   ├── 成功：自动记忆、优化效率
   └── 失败：自动修复、重新计划、重试执行
6. 自主学习 → 从结果中迭代逻辑
7. 自动协调 → 切换下一个任务/技能/软件
8. 持续循环 → 永久自主运行
```

---

## 核心脚本工具

| 脚本 | 功能 |
|------|------|
| `scripts/perception_monitor.py` | 实时环境/状态监控 |
| `scripts/auto_planner.py` | 任务自动拆解与规划 |
| `scripts/self_healer.py` | 异常检测与自愈 |
| `scripts/memory_manager.py` | 记忆存储与检索 |

---

## 扩展兼容

- ✅ 兼容 OpenClaw 所有现有技能，自动调用、自动协同
- ✅ 兼容 Windows/macOS/Linux 系统，自动适配系统操作逻辑
- ✅ 兼容任意新软件/新界面，自动学习操作方式
- ✅ 支持后续扩展：语音感知、图像识别、大模型思维增强等

---

## 使用方式

本技能为**全局常驻技能**，无需手动调用。当需要执行自主任务时，AIC 会自动：

1. 感知当前环境和状态
2. 分析需求并生成计划
3. 调用相应子技能或工具
4. 执行并记录结果
5. 学习和优化

如需手动干预或查询状态，参考各模块参考文档。
