# SITE_CONTEXT

更新日期：2026-10-30（Asia/Shanghai）
状态依据：主仓库 `main` 的实际代码与项目记录、子项目 README 和 GitHub Actions 核对。本文记录当前已确认决定；新的提交、部署与浏览器状态需分别检查。

## 1. 网站身份与定位

- 网站：<https://plastocyanin.org/>
- 主仓库：<https://github.com/imasenHF/imasenhf.github.io>
- 公开署名：hyphoon
- 公开联系邮箱：wuhaifeng@ustc.edu.cn
- GitHub 用户名、仓库名称、引用文献作者及真实 URL 保留准确值。

plastocyanin 用于记录个人项目、学习笔记、技术文章、经历和兴趣。当前内容以 NMR、EPR、化学与科学计算为主，不限制未来主题。专业内容和个人兴趣共用主站；不恢复 `mr.plastocyanin.org` 的独立分区。栏目依据实际公开内容增加，不提前建立空栏目。

## 2. 当前网站结构

主站当前导航为 **Home、Workshop、Notebook、About / CV**。

| 栏目 | 正式路径 | 当前内容与职责 |
| --- | --- | --- |
| Home | `/` | 个人介绍、plastocyanin 命名缘由与科学示意图、SpinFront 日历、精选项目和笔记 |
| Workshop | `/projects/` | 展示独立工具、参考资料及信息整理项目；当前由 `_projects/` 管理九个项目入口 |
| Notebook | `/notes/` | 技术调研和学习笔记；已公开 W 波段 EPR、X 波段医学 EPR、电子—电子距离测定三份分章文档 |
| About / CV | `/about/` | 当前仅有公开身份与联系方式，完整公开 CV 尚未建立 |
| Interests | 尚无正式栏目 | 待有可公开内容后再增加入口 |

首页精选项目由项目元数据决定；Notebook 的学习和技术调研不在 Workshop 重复登记。Workshop 中五个 Web 项目链接到独立网页，四个历史软件项目直接链接 GitHub 仓库。详情及维护文档参见 [PROJECT_INDEX.md](PROJECT_INDEX.md)。

## 3. 技术、内容与部署

- 主站使用 **Jekyll + GitHub Pages**。主要文件：`_config.yml`、`Gemfile`、`_layouts/default.html`、`index.html`、`assets/css/`、`assets/js/`。2026-10-08 对应 `5699b72` 的 [Pages 运行 37791293149](https://github.com/imasenHF/imasenhf.github.io/actions/runs/37791293149) 显示成功；其后的提交须核对各自构建与发布结果。
- Workshop 项目元数据：`_projects/*.md`；分类：`_data/project-types.yml`；列表入口：`projects/index.html`。新增或调整展示项目时，同时核对这些文件与 `PROJECT_INDEX.md`。
- Notebook 正文以 `_note_sources/<slug>.html` 为单一编辑来源；执行 `python scripts/build-note-docs.py <slug>` 生成 `_notes/` 与 `notes/<slug>/` 下的文档页面、目录及搜索数据。不得直接改生成页面。共享模板变更后重新生成受影响文档。写作和版式要求参见 [docs/NOTE_TEMPLATE.md](docs/NOTE_TEMPLATE.md)。
- Note 页面采用 Just the Docs 分章布局，保留公式、相位表、SVG 时间轴、标题层级、中文检索及移动端导航。默认主题 mist；其他主题与具体实现以现有模板为准。正式三份笔记路径为 `/notes/w-band-epr/`、`/notes/x-band-epr-medical/`、`/notes/electron-electron-distance/`。
- 网站的正式 Web 项目入口为 `/spinfront/`、`/spinplot/`、`/nmr-atlas/`、`/nmrexp/` 与 `/countdown-studio/`。对应仓库独立构建、发布，主站只维护入口或必要的首页嵌入组件。
- 旧 `/SpinFront/`、`/SpinPlot/`、`/NMR_EXP/` 等大小写路径保留兼容跳转；迁移应保留适用的查询参数、锚点和深层路径。静态跳转不等同于服务器 301。新网页路径使用小写，文件资产名遵循真实大小写。
- 主站 `CNAME` 为 `plastocyanin.org`。独立子项目不新增相同 CNAME，以免争用域名。Cloudflare、Pages 设置以及线上 HTTP 访问应与构建结果分开核对；一次成功的 Actions 运行不等于所有浏览器功能已验收。

## 4. 品牌与设计分工

跨站共用品牌、色彩、字体角色、链接反馈、主页及共享页头/页尾规则，以 [docs/SITE_STYLE_GUIDE.md](docs/SITE_STYLE_GUIDE.md) 为准。主站实际样式由现有 CSS 和模板确定。

项目专属风格和功能规范保存在各自仓库：SpinFront 的 `docs/STYLE_GUIDE.md`、NMR Atlas 的 `NMR_ATLAS_CONTEXT.md`、SpinPlot 的 `PROJECT_CONTEXT.md`、`docs/STYLE_GUIDE.md` 与 `docs/ARCHITECTURE.md`；Notebook 依 `docs/NOTE_TEMPLATE.md`。共用规范只写一次，独立项目保留确有差异的实现。不因局部内容修改重新设计品牌或恢复废止布局。

SpinFront 的 Daily Epigraph 已归入 SpinFront 项目本身：唯一正式数据源为 `imasenHF/spinfront/assets/data/epigraphs.json`。完整日报按日报日期稳定映射到固定 epigraph；主站首页 SpinFront 日历读取同一数据源并按当前选中的日报日期显示同一条，不再按访问当天变化。完整日报封面以左下原有空白区容纳 Epigraph，不恢复封面统计行，也不改变桌面端封面高度、日期栏高度或淡色 `SPIN` 水印位置。

## 5. 远程记录的职责

| 文件 | 唯一主要职责 |
| --- | --- |
| [SITE_CONTEXT.md](SITE_CONTEXT.md) | 主站身份、定位、结构、技术与部署方式、已确认规则及当前待办 |
| [PROJECT_INDEX.md](PROJECT_INDEX.md) | 全部独立项目的仓库、入口、用途、状态与对应详细文档 |
| [CV_RECORDS.md](CV_RECORDS.md) | 经确认可公开的经历、贡献及成果；不存客户资料和私人记录 |
| [docs/SITE_STYLE_GUIDE.md](docs/SITE_STYLE_GUIDE.md) | 跨站共用视觉与主站专用视觉；不复制独立子项目整份设计规范 |
| [AGENTS.md](AGENTS.md) | Codex/维护代理的读取顺序、实施边界、记录变更与验收要求 |

GitHub `main` 的最新文件是长期项目记录。ChatGPT 项目指令仅定义处理要求，不复制不断变化的项目状态。回答前按任务读取相关仓库记录；新决定或实际变化时更新对应文件。对普通问答及未采用的建议，不产生无意义提交。新代码和部署检查决定实际状态；文档如有冲突应检查并修正，不把旧文字当作现行事实。

## 6. 目前待处理事项

- 公开 CV：按 `CV_RECORDS.md` 的公开范围核实教育、研究、工作、成果及项目贡献后再编排；当前 About 页面不代替完整 CV。
- SpinFront：每日任务按其仓库 `docs/DAILY_TASK_PROMPT.md` 执行；自动检索、JSON 提交、Pages 发布和钉钉通知分别核对。当前钉钉工作流由外部 Cloudflare Worker 调度并经 GitHub `workflow_dispatch` 触发；实际 Worker Cron、群收件及配置须单独确认。不得公开 Webhook/Secret。
- SpinPlot：持续核对二维数据、坐标单位、作图/导出和项目保存兼容性；页面与构建成功不能代替数值检查。
- SpinPlot 模块化临时预览：<https://plastocyanin.org/previews/spinplot-modularization/>，源分支 `imasenHF/spinplot` 的 `preview/modularization-phase1-20261009`；PR #1 已于 2026-10-30 合并至正式 `main`（merge commit `163a539c59964271f75055663c82db2974785478`），正式 Pages 部署 [41001804341](https://github.com/imasenHF/spinplot/actions/runs/41001804341) 成功。预览具有 Contour、可旋转 3D、Linear/Log10（跨零 SymLog）/Scientific、可见区域 Auto Z，以及 Variable scan 双特征与独立幅度/线宽模型。**阶段 A（2026-10-29）**：右侧投影从每一条磁场谱直接提取峰峰线宽（单位跟随磁场轴），支持同时显示峰峰幅度和线宽；Variable scan 的 Statistic 与 Signal feature 合并为单个 Measurement，旧配置兼容。拟合模型通过 MathML 展示，求解器说明移入问号帮助；排除点改成按轨迹可勾选列表，保留原始值并在图上单独标记，默认参数搜索范围等于有效测量功率范围。Current data 右列独立控制各衍生曲线线型/符号，重复 Scan style 在直接二维来源下隐藏；默认实测点线与拟合虚线区分，图例默认外置。**2026-10-30 七项界面修复：** 普通二维 Heatmap 源数据列表占满单列，移除无效的 Scan style 与右侧空白；Variable scan 使用 34 px 图形符号样式列，与数据列逐行等高；切换非功率扫描自动折叠功率拟合，不再将未校准 dB 误标为 mW；Exclude points 使用无额外边框的折叠样式；MathML 括号禁止随分式放大。Linear 模式下 Y、顶部/右侧投影及 Z 色标强制使用十进制刻度，Scientific 必须由用户明确选择。完整数值/构建/Chromium/旧版对照 [40923593424](https://github.com/imasenHF/spinplot/actions/runs/40923593424) 通过；更新后的独立静态资源已由主站 Pages [40924052918](https://github.com/imasenHF/imasenhf.github.io/actions/runs/40924052918) 发布，公开 Chromium 浏览器复核 [40923593239](https://github.com/imasenHF/spinplot/actions/runs/40923593239) 重跑成功。**2026-10-30 衍生曲线 Z-order：** 直接二维 Variable scan 的 Current data 下可鼠标拖拽缩进的派生曲线改变实际前后绘制层级（底部最后绘制、覆盖上层）；右侧 Style 与条目同步，Alt+↑/↓ 可键盘调整。原始二维数据行不参与拖动。排序保存在现有子图配置 `scanDerivedOrder`，项目重载、Canvas 绘制和 SVG 等导出保持相同顺序；旧项目未存储时沿用默认值。完整回归 [40929024040](https://github.com/imasenHF/spinplot/actions/runs/40929024040) 成功；预览 Pages [40929364489](https://github.com/imasenHF/imasenhf.github.io/actions/runs/40929364489) 成功，公开 Chromium [40929024041](https://github.com/imasenHF/spinplot/actions/runs/40929024041) 发布后重跑成功。**阶段 B（正式版本 0.10.0，2026-10-30）：** PR #2 已将 `plotFootprint` 的错误显隐语义修正为 `emptyProjectionSpace`，并合并正式 `main`。每个子图可选 `none / top / right / both`；无投影子图可占用同行的上投影预留区、同列的右投影预留区或两者。当前子图显示的投影、色标、标题、g 轴和图例边距保持独立；设置适用于 1D、2D、Variable scan，默认 `none`。正式入口 `/spinplot/` 与独立预览均为 0.10.0。完整回归 [41005667591](https://github.com/imasenHF/spinplot/actions/runs/41005667591)、独立预览 Pages [41005533960](https://github.com/imasenHF/imasenhf.github.io/actions/runs/41005533960)、公开 HTTP [41005667562](https://github.com/imasenHF/spinplot/actions/runs/41005667562)、公开 Chromium [41005667590](https://github.com/imasenHF/spinplot/actions/runs/41005667590)、正式 Pages [41005910687](https://github.com/imasenHF/spinplot/actions/runs/41005910687) 和发布工作流 [41005959883](https://github.com/imasenHF/spinplot/actions/runs/41005959883) 均成功。GitHub Release [v0.10.0](https://github.com/imasenHF/spinplot/releases/tag/v0.10.0) 已发布。真实复杂谱线科学验证仍需独立进行。
- NMR Atlas：持续核对核种参数、化学位移来源、筛选和移动端操作；具体当前约束以该仓库文档为准。
- Notebook 和 Interests：依据实际完成的文章增加内容，保留参考资料来源及适用范围。
- 维护工作：重要修改同步相关记录；Git 版本历史保存过往过程，本文件不再持续追加已经废止的草稿和决定。

维护本文件时保留当前有效内容，不为每次提交追加状态段落。若需追溯旧设计或修改过程，使用 Git 历史。
