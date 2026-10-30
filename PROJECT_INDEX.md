# PROJECT_INDEX

更新日期：2026-10-30（Asia/Shanghai）

本文件是 plastocyanin 所有公开子项目的统一索引，负责用途、入口、仓库、发布形式、有效状态和进一步阅读位置。具体功能以独立仓库最新代码与 README 为准；构建成功与线上实际交互验收须区分。

## 1. 主站与独立 Web 项目

| 项目 | 用途 | 仓库及详细记录 | 公开入口 | 发布形式与当前状态 |
| --- | --- | --- | --- | --- |
| plastocyanin | 个人网站、Workshop、Notebook、About / CV | [主站仓库](https://github.com/imasenHF/imasenhf.github.io) · [SITE_CONTEXT](SITE_CONTEXT.md) · [视觉规范](docs/SITE_STYLE_GUIDE.md) | <https://plastocyanin.org/> | Jekyll / GitHub Pages；2026-10-08 对应主站提交的发布流程成功 |
| SpinFront | NMR/EPR 日报、检索、分类与日期归档 | [仓库](https://github.com/imasenHF/spinfront) · [README](https://github.com/imasenHF/spinfront/blob/main/README.md) · [日报任务](https://github.com/imasenHF/spinfront/blob/main/docs/DAILY_TASK_PROMPT.md) · [专用风格](https://github.com/imasenHF/spinfront/blob/main/docs/STYLE_GUIDE.md) | <https://plastocyanin.org/spinfront/> | Python 标准库构建静态站 / GitHub Actions Pages；2026-10-08 最近检查的构建发布成功；每日内容另行提交 |
| SpinPlot | CW EPR 一维/二维谱处理、绘图、扫描特征与功率拟合 | [仓库](https://github.com/imasenHF/spinplot) · [README](https://github.com/imasenHF/spinplot/blob/main/README.md) · [预览项目记录](https://github.com/imasenHF/spinplot/blob/main/PROJECT_CONTEXT.md) · [预览开发上下文](https://github.com/imasenHF/spinplot/blob/main/docs/DEVELOPMENT_CONTEXT.md) · [二维技术说明](https://github.com/imasenHF/spinplot/blob/main/docs/TWO_DIMENSIONAL.md) · [架构优化规划](https://github.com/imasenHF/spinplot/blob/main/docs/ARCHITECTURE_IMPROVEMENT_PLAN.md) | 正式 <https://plastocyanin.org/spinplot/> · [独立预览](https://plastocyanin.org/previews/spinplot-modularization/)（页面标记 `0.10.0-dev`，品牌名链接返回正式版） | 正式入口来自 `main`，PR #1/#2 均已合并；正式版本 0.10.0，Pages [41005910687](https://github.com/imasenHF/spinplot/actions/runs/41005910687) 部署成功，GitHub Release [v0.10.0](https://github.com/imasenHF/spinplot/releases/tag/v0.10.0) 已发布。隔离预览包括 Contour/3D、三种坐标显示、Auto Z、右侧投影按每条磁场谱提取峰峰线宽，Variable scan 单 Measurement、双特征双 Y 轴、独立功率拟合与数学公式，按点排除拟合、测量范围默认约束、衍生曲线独立样式及 CSV。2026-10-30 修复 Heatmap 数据列空白、普通热图冗余 Scan style；Variable scan 改为 34 px 符号样式列且列表等高，非功率扫描自动折叠拟合；统一排除点与公式括号样式，Linear Y/Top/Right/Z 刻度不自动采用科学计数法。完整回归 [40923593424](https://github.com/imasenHF/spinplot/actions/runs/40923593424) 成功；独立预览 Pages [40924052918](https://github.com/imasenHF/imasenhf.github.io/actions/runs/40924052918) 发布、公开 Chromium [40923593239](https://github.com/imasenHF/spinplot/actions/runs/40923593239) 验收成功。Variable scan 派生曲线已支持鼠标拖拽及 Alt+↑/↓ 更改实际绘制 Z-order；源矩阵固定、样式列同步，排序随项目配置保存并用于绘图/导出。完整回归 [40929024040](https://github.com/imasenHF/spinplot/actions/runs/40929024040) 成功，独立预览 Pages [40929364489](https://github.com/imasenHF/imasenhf.github.io/actions/runs/40929364489) 与公开 Chromium [40929024041](https://github.com/imasenHF/spinplot/actions/runs/40929024041) 验收成功。**阶段 B（正式版 0.10.0）**：PR #2 已合并 `emptyProjectionSpace`，每子图可选 none/top/right/both；无投影子图可占用同行上投影、同列右投影预留区或两者，投影显隐及色标、标题、g 轴、图例边距保持独立。适用于 1D、2D 和 Variable scan，默认 none。完整回归 [41005667591](https://github.com/imasenHF/spinplot/actions/runs/41005667591)、独立预览 Pages [41005533960](https://github.com/imasenHF/imasenhf.github.io/actions/runs/41005533960)、公开 HTTP [41005667562](https://github.com/imasenHF/spinplot/actions/runs/41005667562)、公开 Chromium [41005667590](https://github.com/imasenHF/spinplot/actions/runs/41005667590)、正式 Pages [41006773145](https://github.com/imasenHF/spinplot/actions/runs/41006773145)、生产 HTTP 检查 [41006826196](https://github.com/imasenHF/spinplot/actions/runs/41006826196) 和发布工作流 [41006841041](https://github.com/imasenHF/spinplot/actions/runs/41006841041) 均成功。正式入口和独立预览均为 0.10.0；GitHub Release [v0.10.0](https://github.com/imasenHF/spinplot/releases/tag/v0.10.0) 已发布。真实复杂谱线科学验证仍需独立进行。 当前 PDF 导出使用 svg2pdf.js + jsPDF 将共享 SVG 场景转换为矢量路径与文本对象；不嵌入整页栅格图像。中文字体嵌入及 Acrobat/Edge/Firefox 实际阅读器验收待完成。
| NMR Atlas | NMR 周期表、核种比较、磁场/频率换算、溶剂及杂质参考 | [仓库](https://github.com/imasenHF/nmr-atlas) · [README](https://github.com/imasenHF/nmr-atlas/blob/main/README.md) · [当前约束](https://github.com/imasenHF/nmr-atlas/blob/main/NMR_ATLAS_CONTEXT.md) | <https://plastocyanin.org/nmr-atlas/> | 静态 JavaScript / GitHub Actions Pages；2026-10-08 最近检查的发布成功；Workshop 已列入 |
| NMR Experiment Library | 三套 NMR 实验教材的双语阅读、跨教材检索及原页对照 | [仓库](https://github.com/imasenHF/nmrexp) · [README](https://github.com/imasenHF/nmrexp/blob/main/README.md) | <https://plastocyanin.org/nmrexp/> | 静态 HTML / GitHub Pages；2026-10-06 最近检查的发布成功；保持现有资料范围，不加入个人原创实验笔记 |
| Countdown Studio | PowerPoint 倒计时动画生成、内容边界裁剪、透明 GIF 与离线 MP4 导出 | [仓库](https://github.com/imasenHF/countdown-studio) · [README](https://github.com/imasenHF/countdown-studio/blob/main/README.md) · [项目状态](https://github.com/imasenHF/countdown-studio/blob/main/docs/PROJECT_CONTEXT.md) · [界面规范](https://github.com/imasenHF/countdown-studio/blob/main/docs/STYLE_GUIDE.md) | <https://plastocyanin.org/countdown-studio/> | 单文件 HTML / GitHub Actions Pages；自动裁剪透明留白；浏览器导出和 PowerPoint 播放兼容性仍待实测 |

## 2. 源码与程序包项目

这些项目作为历史工具直接从 Workshop 链接 GitHub 首页，不新增主站 `/projects/<slug>/` 正文页，当前均不列入首页精选。

| 项目 | 用途 | 仓库及说明 | 公开形式与维护范围 |
| --- | --- | --- | --- |
| EasyCurling | XYZ 分子或晶体单元重复、刚性/渐进弯曲和模型构建 | [仓库与 README](https://github.com/imasenHF/easycurling) | Python 启动脚本与 Windows CPython 3.12 x64 编译扩展（核心可移植源码未在仓库公开）；Windows 发布包已有 [v1.1.0](https://github.com/imasenHF/easycurling/releases/tag/v1.1.0)；结构用于后续计算前需检查几何合理性 |
| Mconvert | 通过 Multiwfn 进行结构/波函数文件转换，生成 Gaussian、ORCA 输入模板 | [仓库与 README](https://github.com/imasenHF/mconvert) | Bash 脚本；依赖本地 Multiwfn 及菜单接口；按兼容性需要维护 |
| DNA Builder | 通过固定模板构建 ssDNA / dsDNA 的 XYZ 几何结构 | [仓库与 README](https://github.com/imasenHF/dna-builder) | Python / NumPy / SciPy 源码；几何拼接不包含结构优化；历史 2023 v1.0 逻辑保留 |
| Computational Chemistry Tools | Gaussian、ORCA、CP2K、Multiwfn 工作流的批处理、提取、转换、输入和可视化脚本 | [仓库与 README](https://github.com/imasenHF/compchem-tools) · [脚本索引](https://github.com/imasenHF/compchem-tools/blob/main/docs/SCRIPT_INDEX.md) | 按用途分类的 Bash/Python 源码；各脚本依赖与参数单独确认 |

## 3. 项目分类与展示

- Workshop 路径为 `/projects/`，使用 `_projects/*.md` 管理摘要、类型、展示顺序、`featured` 和正式链接；分类表为 `_data/project-types.yml`。
- SpinPlot、SpinFront、NMR Atlas、NMR Experiment Library 与 Countdown Studio 保留各自独立网页。主站只负责入口与已明确的首页组件，不复制子项目完整说明。
- EasyCurling、Mconvert、DNA Builder、Computational Chemistry Tools 点击后直接进入 GitHub 仓库；各 README 负责依赖、使用方法、限制与源码入口。
- Notebook 技术调研按 `_note_sources/` 和 `docs/NOTE_TEMPLATE.md` 维护，不在 Workshop 重复建立项目条目。CV 仅从已确认的 `CV_RECORDS.md` 选择公开经历。
- 本索引只记录重要项目发布状态，不随 SpinFront 每日增刊、依赖更新或普通脚本提交反复改变版本快照。项目入口、功能范围、维护仓库、发布方式或重要完成状态发生变化时更新。
