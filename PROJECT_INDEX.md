# PROJECT_INDEX

检查日期：2026-10-04（Asia/Shanghai）
主站检查基准见 SITE_CONTEXT.md。这里只记录主站检查结果及用户明确的项目范围；除下述 SpinPlot 更新外，未读取其他项目仓库或代码；首页文案不作为功能完成的证明。

| 项目 | 用途与来源 | 已确认仓库 | 网页入口 | 当前状态 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| plastocyanin 主站 | 个人项目、笔记、经历与兴趣的统一入口；用户明确定位 | imasenHF/imasenhf.github.io | https://plastocyanin.org/ | 单页静态站；当前页面结构与部署见 SITE_CONTEXT.md | 按当前要求另行制定页面维护任务 |
| NMR_EXP | 实验参考资料库；用户明确要求 | 待补，本次未检查外部仓库 | /nmrexp/ 为必须保留的路径，当前可用性待检查 | 主站无对应目录；首页 NMR Experiments 条目没有链接，显示 In preparation；资料库实际状态待检查 | 检查实际仓库与发布入口，确认资料来源、个人贡献及说明 |
| SpinFront | NMR/EPR 信息整理与每日简报项目 | imasenHF/spinfront | https://plastocyanin.org/spinfront/ | 已独立构建和发布；日报采用 editorial magazine 版式，主页提供最新一期、搜索、刊期日历、主题筛选和完整归档；主站首页日历组件运行时读取 SpinFront 索引 | 持续维护日报内容、标签体系与归档交互；后续改动保持主站、日报主页和日报内页视觉一致 |
| SpinPlot | 浏览器端 CW EPR 数据处理与作图软件 | imasenHF/spinplot | https://plastocyanin.org/spinplot/ 直接打开软件；旧 /spinplot/legacy/ 跳转首页 | 当前版本 0.2.2（首次公开 0.1.0）；新增仅缩小预览、Clear config 与手动行列布局；ΔB 工具关闭保留标记，独立 Clear ΔB 清除标记并支持 Undo；Ctrl＋左键拖动平移 Y，Shift＋左键拖动平移 X。部署成功，在线布局应用与配置复位已检查。使用 MAJOR.MINOR.PATCH 版本规则；package.json 管理应用版本，项目文件格式版本独立。Vite 构建，算法和界面尚未模块化；完整数据操作未验收，PDF 中文字体仍有限制 | 按该仓库 docs/ARCHITECTURE.md 迁移模块；主站 /projects/spinplot/ 介绍页尚未建立 |
| 其他小项目 | 用户已有工具及小项目，逐项整理 | 待补 | 待补 | 名称、数量、完成程度及公开范围待补 | 逐项确认用途、运行方式、本人贡献及公开价值 |

## 现有页面条目的解释

首页 Magnetic Resonance Simulation 显示 In development，文案提及独立代码库；本次未找到仓库地址或实现材料，不登记为已确认独立项目，也不将其等同于 SpinPlot。
首页 Future projects 显示 Open，为占位条目，不代表已存在的项目。
NMR Experiments 与 NMR_EXP 的具体对应关系待检查。

## 项目整理规则

项目页需依据最新代码和说明记录用途、实际功能、运行方式、状态、示例、限制及代码入口。
NMR_EXP 的内容来源与个人贡献应准确说明，不将参考资料全部写为本人作品。
SpinFront 栏目、内容格式与归档方式依据现有规范和实际输出确定。
仓库分工依据独立运行、发布及维护周期决定，未确认的地址与路径标记待补。
适合公开的个人贡献与项目成果写入 CV_RECORDS.md，日期和结果需有明确材料。
Notes 是学习笔记与技术记录的内容栏目，Interests 是兴趣内容栏目；具体分类随实际公开内容增加。

## 本地首页重设计草稿（2026-10-04，未提交）

首页项目元数据位于 `_projects/`，顺序为 SpinPlot、SpinFront、NMR Experiment Library。SpinFront 仅创建本地入口介绍，尚未导入归档；三份报告进入本地 Notes，尚未发布。项目既有源记录不据此改为已部署。

## 首页 K 款确认

用户选定 K：黄色 #F0BE32 内线宽 3.5、白色单侧描边 3（总外宽 9.5），谱线位于结构下半部前景，无坐标轴。此前背景谱线与后景叠层方案废止。用户已授权修改后直接提交并推送，取代此前暂不提交要求。


## 2026-10-05 当前仓库与 URL

| 项目 | 源码仓库 | 正式网页入口 |
|---|---|---|
| NMR Experiment Library | https://github.com/imasenHF/nmrexp | /nmrexp/ |
| SpinPlot | https://github.com/imasenHF/spinplot | /spinplot/ |
| SpinFront | https://github.com/imasenHF/spinfront | /spinfront/ |
| EasyCurling | https://github.com/imasenHF/easycurling | Python/Windows 软件，无网页入口 |

此表覆盖早期路径记录。


## 2026-10-05 Projects 与 Notes 分区修订
三份调研只在 Notes 展示，不在 Projects 重复设置入口。Projects 保留软件开发、参考资料、信息整理三类，后续按独立项目的实际类型扩展。此规则覆盖此前将调研笔记列入专题调研项目的安排。
