# PROJECT_INDEX

更新日期：2026-10-08（Asia/Shanghai）

本文件是 plastocyanin 所有公开子项目的统一索引，负责用途、入口、仓库、发布形式、有效状态和进一步阅读位置。具体功能以独立仓库最新代码与 README 为准；构建成功与线上实际交互验收须区分。

## 1. 主站与独立 Web 项目

| 项目 | 用途 | 仓库及详细记录 | 公开入口 | 发布形式与当前状态 |
| --- | --- | --- | --- | --- |
| plastocyanin | 个人网站、Workshop、Notebook、About / CV | [主站仓库](https://github.com/imasenHF/imasenhf.github.io) · [SITE_CONTEXT](SITE_CONTEXT.md) · [视觉规范](docs/SITE_STYLE_GUIDE.md) | <https://plastocyanin.org/> | Jekyll / GitHub Pages；2026-10-08 对应主站提交的发布流程成功 |
| SpinFront | NMR/EPR 日报、检索、分类与日期归档 | [仓库](https://github.com/imasenHF/spinfront) · [README](https://github.com/imasenHF/spinfront/blob/main/README.md) · [日报任务](https://github.com/imasenHF/spinfront/blob/main/docs/DAILY_TASK_PROMPT.md) · [专用风格](https://github.com/imasenHF/spinfront/blob/main/docs/STYLE_GUIDE.md) | <https://plastocyanin.org/spinfront/> | Python 标准库构建静态站 / GitHub Actions Pages；2026-10-08 最近检查的构建发布成功；每日内容另行提交 |
| SpinPlot | CW EPR 一维/二维谱处理、绘图与导出 | [仓库](https://github.com/imasenHF/spinplot) · [README](https://github.com/imasenHF/spinplot/blob/main/README.md) · [项目状态](https://github.com/imasenHF/spinplot/blob/main/PROJECT_CONTEXT.md) · [专用风格](https://github.com/imasenHF/spinplot/blob/main/docs/STYLE_GUIDE.md) · [架构](https://github.com/imasenHF/spinplot/blob/main/docs/ARCHITECTURE.md) · [二维说明](https://github.com/imasenHF/spinplot/blob/main/docs/TWO_DIMENSIONAL.md) · [版本记录](https://github.com/imasenHF/spinplot/blob/main/CHANGELOG.md) | <https://plastocyanin.org/spinplot/> | Vite / TypeScript / GitHub Actions Pages；检查时应用版本 0.9.2，2026-10-08 发布成功；数值与兼容性仍需专项检查 |
| NMR Atlas | NMR 周期表、核种比较、磁场/频率换算、溶剂及杂质参考 | [仓库](https://github.com/imasenHF/nmr-atlas) · [README](https://github.com/imasenHF/nmr-atlas/blob/main/README.md) · [当前约束](https://github.com/imasenHF/nmr-atlas/blob/main/NMR_ATLAS_CONTEXT.md) | <https://plastocyanin.org/nmr-atlas/> | 静态 JavaScript / GitHub Actions Pages；2026-10-08 最近检查的发布成功；Workshop 已列入 |
| NMR Experiment Library | 三套 NMR 实验教材的双语阅读、跨教材检索及原页对照 | [仓库](https://github.com/imasenHF/nmrexp) · [README](https://github.com/imasenHF/nmrexp/blob/main/README.md) | <https://plastocyanin.org/nmrexp/> | 静态 HTML / GitHub Pages；2026-10-06 最近检查的发布成功；保持现有资料范围，不加入个人原创实验笔记 |

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
- SpinPlot、SpinFront、NMR Atlas、NMR Experiment Library 保留各自独立网页。主站只负责入口与已明确的首页组件，不复制子项目完整说明。
- EasyCurling、Mconvert、DNA Builder、Computational Chemistry Tools 点击后直接进入 GitHub 仓库；各 README 负责依赖、使用方法、限制与源码入口。
- Notebook 技术调研按 `_note_sources/` 和 `docs/NOTE_TEMPLATE.md` 维护，不在 Workshop 重复建立项目条目。CV 仅从已确认的 `CV_RECORDS.md` 选择公开经历。
- 本索引只记录重要项目发布状态，不随 SpinFront 每日增刊、依赖更新或普通脚本提交反复改变版本快照。项目入口、功能范围、维护仓库、发布方式或重要完成状态发生变化时更新。
