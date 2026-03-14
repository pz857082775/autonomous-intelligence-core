# 模块 11：全平台软件/界面自动操作

## 能力概述
自动调用电脑任意软件，自动操作任意界面。支持点击、输入、拖拽、截图识别、文本提取、文件上传下载、快捷键执行。

---

## 软件支持

### 系统工具
| 软件类型 | 操作方式 | 工具 |
|----------|----------|------|
| 文件管理器 | 浏览、创建、删除、移动 | `exec` + 系统命令 |
| 终端 | 命令执行 | `exec` |
| 文本编辑器 | 打开、编辑、保存 | `exec` + 文件操作 |
| 系统设置 | 配置修改 | `exec` + 配置文件 |

### 办公软件
| 软件类型 | 操作方式 | 工具 |
|----------|----------|------|
| Word | 文档创建、编辑 | `docx` skill |
| Excel | 表格处理 | `xlsx` skill |
| PDF | 阅读、编辑 | `pdf` skill |
| PPT | 演示文稿 | `pptx` skill |

### 浏览器
| 操作类型 | 工具 | 说明 |
|----------|------|------|
| 导航 | `browser navigate` | 打开/跳转 URL |
| 点击 | `browser act click` | 点击元素 |
| 输入 | `browser act type` | 填写表单 |
| 截图 | `browser snapshot` | 获取页面状态 |
| 下载 | `browser act waitForDownload` | 下载文件 |
| 上传 | `browser upload` | 上传文件 |

### 设计工具
| 软件类型 | 操作方式 | 工具 |
|----------|----------|------|
| 图片编辑 | 调用 API 或脚本 | `canvas` + 脚本 |
| 视频处理 | 调用 FFmpeg 等 | `exec` |

---

## 界面操作能力

### 基础操作
| 操作 | 工具/方法 | 说明 |
|------|----------|------|
| 点击 | `browser act click` | 点击按钮、链接 |
| 双击 | `browser act doubleClick` | 双击打开 |
| 右键 | `browser act button:right` | 右键菜单 |
| 输入 | `browser act type` | 文本输入 |
| 清空 | `browser act fill` | 清空并填充 |
| 选择 | `browser act select` | 下拉选择 |
| 悬停 | `browser act hover` | 鼠标悬停 |

### 高级操作
| 操作 | 工具/方法 | 说明 |
|------|----------|------|
| 拖拽 | `browser act drag` | 拖放元素 |
| 截图 | `browser screenshot` | 页面截图 |
| 滚动 | `browser act evaluate` | 执行 JS 滚动 |
| 快捷键 | `browser act press` | 键盘快捷键 |
| 等待 | `browser act wait` | 等待元素/时间 |

### 文件操作
| 操作 | 工具/方法 | 说明 |
|------|----------|------|
| 上传 | `browser upload` | 上传文件到网页 |
| 下载 | `browser act waitForDownload` | 从网页下载 |
| 读取 | `read` | 读取本地文件 |
| 写入 | `write` | 写入本地文件 |
| 编辑 | `edit` | 编辑本地文件 |

---

## 界面识别

### 元素定位
| 定位方式 | 说明 | 优先级 |
|----------|------|--------|
| Aria 标签 | `refs="aria"` | 最高（最稳定） |
| Role + Name | `refs="role"` | 高 |
| CSS 选择器 | 自定义选择器 | 中 |
| XPath | 路径定位 | 低 |
| 图像识别 | 截图匹配 | 备选 |

### 元素状态检测
| 状态 | 检测方式 |
|------|----------|
| 可见性 | 元素是否在视口内 |
| 可点击性 | 是否被遮挡/禁用 |
| 文本内容 | 提取元素文本 |
| 属性值 | 读取元素属性 |

### 界面变化适应
```
检测到界面变化
  ↓
重新扫描页面结构
  ↓
更新元素映射
  ↓
验证操作可用
  ↓
继续执行或报告
```

---

## 跨平台适配

### Windows 适配
| 适配项 | 说明 |
|--------|------|
| 路径格式 | 使用反斜杠 `\` |
| 命令行 | PowerShell/CMD |
| 快捷键 | Ctrl 为主 |
| 文件关联 | Windows 注册表 |

### macOS 适配
| 适配项 | 说明 |
|--------|------|
| 路径格式 | 使用正斜杠 `/` |
| 命令行 | Bash/Zsh |
| 快捷键 | Cmd 为主 |
| 应用启动 | `open` 命令 |

### Linux 适配
| 适配项 | 说明 |
|--------|------|
| 路径格式 | 使用正斜杠 `/` |
| 命令行 | Bash |
| 快捷键 | Ctrl 为主 |
| 应用启动 | 桌面环境相关 |

---

## 操作脚本

使用 `scripts/ui_automator.py` 管理界面操作：

```bash
# 打开应用
python scripts/ui_automator.py launch --app chrome --url "https://example.com"

# 执行点击
python scripts/ui_automator.py click --selector "#button-id"

# 执行输入
python scripts/ui_automator.py type --selector "#input-id" --text "内容"

# 截图识别
python scripts/ui_automator.py snapshot --output temp/snapshot.json

# 文件上传
python scripts/ui_automator.py upload --selector "#file-input" --file path/to/file
```

---

## 操作日志

### 日志格式
```markdown
## UI 操作记录 [UI-YYYYMMDD-XXX]

时间：YYYY-MM-DD HH:MM:SS
操作类型：[click/type/navigate/etc]
目标元素：[选择器/描述]
操作结果：成功/失败
耗时：X 秒
截图：temp/screenshots/XXX.png
```

---

## 相关模块
- ← [04-execution.md](04-execution.md) 接收执行指令
- → [08-memory.md](08-memory.md) 界面布局存入记忆
