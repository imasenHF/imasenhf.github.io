# SITE_CONTEXT

更新日期：2026-10-09（Asia/Shanghai）
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
| Workshop | `/projects/` | 展示独立工具、参考资料及信息整理项目；当前由 `_projects/` 管理八个项目入口 |
| Notebook | `/notes/` | 技术调研和学习笔记；已公开 W 波段 EPR、X 波段医学 EPR、电子—电子距离测定三份分章文档 |
| About / CV | `/about/` | 当前仅有公开身份与联系方式，完整公开 CV 尚未建立 |
| Interests | 尚无正式栏目 | 待有可公开内容后再增加入口 |

首页精选项目由项目元数据决定；Notebook 的学习和技术调研不在 Workshop 重复登记。Workshop 中四个 Web 项目链接到独立网页，四个历史软件项目直接链接 GitHub 仓库。详情及维护文档参见 [PROJECT_INDEX.md](PROJECT_INDEX.md)。

## 3. 技术、内容与部署

- 主站使用 **Jekyll + GitHub Pages**。主要文件：`_config.yml`、`Gemfile`、`_layouts/default.html`、`index.html`、`assets/css/`、`assets/js/`。2026-10-08 对应 `5699b72` 的 [Pages 运行 37791293149](https://github.com/imasenHF/imasenhf.github.io/actions/runs/37791293149) 显示成功；其后的提交须核对各自构建与发布结果。
- Workshop 项目元数据：`_projects/*.md`；分类：`_data/project-types.yml`；列表入口：`projects/index.html`。新增或调整展示项目时，同时核对这些文件与 `PROJECT_INDEX.md`。
- Notebook 正文以 `_note_sources/<slug>.html` 为单一编辑来源；执行 `python scripts/build-note-docs.py <slug>` 生成 `_notes/` 与 `notes/<slug>/` 下的文档页面、目录及搜索数据。不得直接改生成页面。共享模板变更后重新生成受影响文档。写作和版式要求参见 [docs/NOTE_TEMPLATE.md](docs/NOTE_TEMPLATE.md)。
- Note 页面采用 Just the Docs 分章布局，保留公式、相位表、SVG 时间轴、标题层级、中文检索及移动端导航。默认主题 mist；其他主题与具体实现以现有模板为准。正式三份笔记路径为 `/notes/w-band-epr/`、`/notes/x-band-epr-medical/`、`/notes/electron-electron-distance/`。
- 网站的正式 Web 项目入口为 `/spinfront/`、`/spinplot/`、`/nmr-atlas/` 与 `/nmrexp/`。对应仓库独立构建、发布，主站只维护入口或必要的首页嵌入组件。
- 旧 `/SpinFront/`、`/SpinPlot/`、`/NMR_EXP/` 等大小写路径保留兼容跳转；迁移应保留适用的查询参数、锚点和深层路径。静态跳转不等同于服务器 301。新网页路径使用小写，文件资产名遵循真实大小写。
- 主站 `CNAME` 为 `plastocyanin.org`。独立子项目不新增相同 CNAME，以免争用域名。Cloudflare、Pages 设置以及线上 HTTP 访问应与构建结果分开核对；一次成功的 Actions 运行不等于所有浏览器功能已验收。

## 4. 品牌与设计分工

跨站共用品牌、色彩、字体角色、链接反馈、主页及共享页头/页尾规则，以 [docs/SITE_STYLE_GUIDE.md](docs/SITE_STYLE_GUIDE.md) 为准。主站实际样式由现有 CSS 和模板确定。

项目专属风格和功能规范保存在各自仓库：SpinFront 的 `docs/STYLE_GUIDE.md`、NMR Atlas 的 `NMR_ATLAS_CONTEXT.md`、SpinPlot 的 `PROJECT_CONTEXT.md`、`docs/STYLE_GUIDE.md` 与 `docs/ARCHITECTURE.md`；Notebook 依 `docs/NOTE_TEMPLATE.md`。共用规范只写一次，独立项目保留确有差异的实现。不因局部内容修改重新设计品牌或恢复废止布局。

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
- SpinPlot 模块化临时预览：`/previews/spinplot-modularization/` 为独立子仓库预览分支的构建快照（`27c64bb`），供交互检查；正式 `/spinplot/` 仍由原独立仓库发布。临时页面不属于正式导航，测试结束后需清理；后续预览版本不会自动同步此快照。
- NMR Atlas：持续核对核种参数、化学位移来源、筛选和移动端操作；具体当前约束以该仓库文档为准。
- Notebook 和 Interests：依据实际完成的文章增加内容，保留参考资料来源及适用范围。
- 维护工作：重要修改同步相关记录；Git 版本历史保存过往过程，本文件不再持续追加已经废止的草稿和决定。

维护本文件时保留当前有效内容，不为每次提交追加状态段落。若需追溯旧设计或修改过程，使用 Git 历史。
