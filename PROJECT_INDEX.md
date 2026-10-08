# PROJECT_INDEX

更新日期：2026-10-07（Asia/Shanghai）

本文件记录当前项目用途、仓库、公开入口、状态和后续维护方式。网站实际实现仍以各仓库 main 分支为准。

| 项目 | 用途 | 仓库 | 公开入口 | 当前状态 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| plastocyanin 主站 | 个人项目、笔记、经历与兴趣的统一入口 | imasenHF/imasenhf.github.io | https://plastocyanin.org/ | Jekyll 主站；Workshop、Notebook、About / CV 已建立 | 随实际内容维护 |
| SpinPlot | 浏览器端 CW EPR 数据处理与作图工具 | imasenHF/spinplot | https://plastocyanin.org/spinplot/ | 独立 Web 工具，主站提供入口 | 按仓库规划继续维护 |
| SpinFront | NMR / EPR 信息整理与日报归档 | imasenHF/spinfront | https://plastocyanin.org/spinfront/ | 独立站点，持续更新 | 按日报规则维护 |
| NMR Atlas | 交互式 NMR 核素周期表、核种比较、氘代溶剂残余峰与常见杂质跨溶剂参考 | imasenHF/nmr-atlas | https://plastocyanin.org/nmr-atlas/ | 独立静态 Web 工具；Workshop 提供入口 | 按 NMR_ATLAS_CONTEXT.md 继续维护 |
| NMR Experiment Library | NMR 实验教材阅读与检索资料库 | imasenHF/nmrexp | https://plastocyanin.org/nmrexp/ | 独立参考资料库；不加入自有实验理解 | 保持现有资料范围 |
| EasyCurling | 分子或晶体单元重复、弯曲建模 | imasenHF/easycurling | https://github.com/imasenHF/easycurling | 历史工具项目；Workshop 直接链接仓库，不建立独立项目页 | 仅在需要时维护 README、源码或 release |
| Mconvert | 基于 Multiwfn 的结构/波函数文件转换与输入模板生成 | imasenHF/mconvert | https://github.com/imasenHF/mconvert | 历史工具项目；README 记录安装与用法 | 仅在需要时修正兼容性 |
| DNA Builder | 基于固定模板生成 ssDNA / dsDNA XYZ 几何结构 | imasenHF/dna-builder | https://github.com/imasenHF/dna-builder | 历史工具项目；保留 2023 年 v1.0 几何逻辑并更新公开联系信息 | 仅在需要时维护说明或源码 |
| Computational Chemistry Tools | Gaussian、ORCA、CP2K、Multiwfn 等工作流的小型 Bash/Python 工具集合 | imasenHF/compchem-tools | https://github.com/imasenHF/compchem-tools | 历史脚本集合；已按用途分类并补充脚本索引 | 仅在发现明确问题时修正 |

## Workshop 入口规则

SpinPlot、SpinFront、NMR Atlas 与 NMR Experiment Library 保留现有正式网页入口。

EasyCurling、Mconvert、DNA Builder 与 Computational Chemistry Tools 作为历史项目展示。Workshop 只保留项目名称、类型和简短摘要，点击后直接进入对应 GitHub 仓库首页，不建立 `/projects/<slug>/` 项目介绍页。仓库 README 负责说明安装、依赖、基本用法和限制。

上述四个历史项目当前均设置为 `featured: false`，不占用首页精选项目位置。

## 内容分区

调研和学习记录进入 Notebook，不在 Workshop 重复建立项目。Interests 随实际公开内容增加。适合公开的个人贡献与项目成果另在 `CV_RECORDS.md` 维护。
