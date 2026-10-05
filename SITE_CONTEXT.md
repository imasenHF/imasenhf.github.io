# SITE_CONTEXT

检查日期：2026-10-03（Asia/Shanghai）
检查基准：main，a5d1157a275d49c980536100fec7b71b7512df3d。
依据：仓库完整目录、README.md、index.html、CNAME、assets/css/style.css、GitHub Pages 工作流及线上首页响应。以下区分检查事实和用户明确要求。

## 基本信息与有效要求

网站：https://plastocyanin.org
主站仓库：https://github.com/imasenHF/imasenhf.github.io
公开署名：hyphoon
公开联系邮箱：wuhaifeng@ustc.edu.cn
GitHub 用户名、仓库名、实际 URL 和参考文献作者保留准确值。

网站持续记录项目、学习笔记、技术文章、个人经历与兴趣。当前专业范围包括 NMR、EPR、化学、科学计算；允许 ACG、奥特曼及其他兴趣内容。全部内容使用主站，不再使用 mr 子域隔离专业内容。分类依据实际内容建立。

## 已检查的仓库与页面

公开仓库，默认分支 main。根目录原有 CNAME、README.md、index.html、favicon.ico 和 assets/。
assets/css/style.css 为独立样式表；assets/images/imasen_phi_logo/ 包含 SVG、PNG、ICO 和 ico.ipynb。根目录及图标目录各有一份 favicon.ico。
完整目录中未发现 AGENTS.md、package.json、依赖锁文件、Gemfile、_config.yml、.nojekyll 或 .github/workflows/。

网站源页面只有 index.html，文档语言为 en。当前导航为 Research → /#research、Projects → /#projects、About → /#about；另有 /#main-content 跳转入口。
首页包含介绍、磁共振介绍、项目列表、About 与页脚。项目列表显示 NMR Experiments、Magnetic Resonance Simulation 和 Future projects，均无项目链接；页面状态文字不能证明项目实现状态。
首页两处链接指向 https://mr.plastocyanin.org；其可用性未检查。
主站内未发现 /NMR_EXP/、SpinFront、SpinPlot、Notes、Interests 或独立 CV 页面。
首页 canonical 与 Open Graph URL 均为 https://plastocyanin.org/。
本地图片及 CSS 使用相对路径，站点标识链接使用 /；头像来自 GitHub 外部地址。仅有更新页脚年份的内联 JavaScript。
CSS 包含 860px、640px 响应式断点、键盘焦点样式及减少动画设置；本次未进行浏览器视觉验收。

## 构建与部署检查

源文件可直接由静态 HTTP 服务读取；仓库未定义项目构建命令或前端依赖。
README 给出的本地预览命令为 python -m http.server 8000。
README 说明 GitHub Pages 使用 main 分支根目录；该描述尚未通过 Pages 设置接口独立确认。
GitHub 动态工作流 pages build and deployment（dynamic/pages/pages-build-deployment）运行 36348127218 对应检查基准提交，结果 success。
工作流 build 中明确包含 Build with Jekyll，deploy 中包含 Deploy to GitHub Pages，均成功。完成时间为 2026-09-28 04:29:13（Asia/Shanghai）。这属于托管端构建步骤，仓库没有自定义 Jekyll 配置。
CNAME 内容为 plastocyanin.org。
2026-10-03 线上 https://plastocyanin.org/ 返回 HTTP 200，响应服务器为 GitHub.com；本次未逐字比对线上内容与源文件。
DNS、Cloudflare 设置、HTTPS 强制设置及 Pages 设置页面未检查。

## 已明确但尚未实施的页面要求

默认入口为 Home、Projects、Notes、About / CV；Interests 有公开内容后再显示。这些是目标要求，当前导航尚未符合。
首页包含已确认的网站介绍、名称缘由、精选项目、精选 Notes；不单设近期更新，不放个人履历。
项目页说明用途、实际功能、状态、示例、限制与代码入口。笔记保留背景、参数、来源和适用范围。CV 使用经过选择的公开经历并关联项目。
保留有效 URL；/NMR_EXP/ 为用户明确要求保留的路径，其当前部署状态待检查。
不预设更换框架。独立仓库需有独立运行、发布或维护周期等实际理由。
优先考虑正文、公式、代码、谱图和移动端阅读，减少重复卡片、装饰模块与空页面。

## 内容与记录维护规则

中文优先。区分文献、实验、计算和个人判断，参考文献提供真实出处及 DOI 或链接。
缺失事实标记待补；不得将建议路径、年份、功能或成果写成事实。客户及内部材料按公开范围筛选和匿名处理。
内容交付同时给出标题、栏目、标签和文件位置。局部修订只改指定范围。
SITE_CONTEXT.md 维护网站规则与状态；PROJECT_INDEX.md 维护项目；CV_RECORDS.md 仅维护适合公开仓库的经历。信息尽量只维护一处。
重要任务同步更新有关记录。仓库更新后须另行同步 ChatGPT 项目源；本次未同步项目源。
提交、推送和部署遵循具体任务授权。本次只建立三份记录，不改页面、样式、资源或部署配置。

## 待完成与待补

页面及 README 的署名仍使用旧信息；后续按 hyphoon 更新，本次保留原文件。
首页旧 mr 链接与当前主站规划不一致，后续另行处理。
目标导航、项目入口、近期更新和 CV 入口尚未实施，具体 URL 待确定。
NMR_EXP 外部仓库、/NMR_EXP/ 实际发布状态及来源说明待检查，详见 PROJECT_INDEX.md。
Pages 实际发布源、DNS 与 HTTPS 设置待补；本次新记录提交对应的部署结果需后续查看。
教育、工作、研究、论文及项目贡献的公开材料待补，详见 CV_RECORDS.md。

## 检查来源

- https://github.com/imasenHF/imasenhf.github.io/tree/a5d1157a275d49c980536100fec7b71b7512df3d
- https://github.com/imasenHF/imasenhf.github.io/actions/runs/36348127218
- https://plastocyanin.org/

## 2026-10-04 本地重设计草稿

用户授权开始设计，明确暂不提交。本地增加 Jekyll 布局、projects/notes 集合与索引、About 联系页、SpinFront 入口页；保留 NMR_EXP 和 SpinPlot 路径。三份已完成报告仅纳入本地预览，发布日期为空。引用原句来源链接核对为 Wikipedia Metalloprotein 的 Plastocyanin 段落。采用米白、灰蓝、金色的阅读型布局，使用用户选定 config6 和原 SVG 谱线。尚未提交、推送或部署；上述旧站检查描述是改版前快照。

### 结构与谱线构图修订

用户指出原谱线与结构融合效果欠佳，授权使用现有数据重新设计。改用统一 SVG 画布，结构偏左，谱线横贯下部；CSV 的 4096 点以统一线性比例重绘，磁场轴 275–350 mT。未改变结构图片与谱线峰形、相对幅度。原图与原 SVG 保留。此次修改仍为未提交草稿。

### 结构与谱线叠层修订（替代上一版并排构图）

用户明确要求融合更紧密且不出现横坐标。已移除轴线、刻度、单位、背景色块和图内标签；谱线作为后景穿过结构下部，结构作为前景在交叠处遮挡谱线，主峰保留于右侧。统一 SVG 画布从 640×630 缩短为 640×460。CSV 全部 4096 点仍采用统一线性映射，结构原图未改，显示遮挡不代表删除数据。图外保留 EPR 示意模拟说明。构图导出图已查看；未提交或部署。

### 方案一效果预览

用户否定前版叠层效果，要求提供方案一效果。已改为独立蛋白结构加整个介绍区下部的浅灰蓝谱线背景，无坐标轴。谱线源于 CSV，统一缩放；前景正文与结构维持原内容。已输出完整图文设计效果 intro-option1.png（SVG 排版导出，并非浏览器截图），更新本地首页 HTML/CSS 与预览。该方案待用户审阅，不记为最终确认。Jekyll 构建通过，仍未提交、推送、部署。

## 首页 K 款确认

用户选定 K：黄色 #F0BE32 内线宽 3.5、白色单侧描边 3（总外宽 9.5），谱线位于结构下半部前景，无坐标轴。此前背景谱线与后景叠层方案废止。用户已授权修改后直接提交并推送，取代此前暂不提交要求。

## Notes 阅读模板确认与实施

用户全部通过新阅读模板方案，授权保存到主仓库。新增 note 布局及工具栏、专用 CSS/JS、元数据与标签、自动 H2/H3 目录、Home、页内搜索、主题、80%–160% 缩放及打印样式。删除 W 波段报告的旧目录与重复标题，保留正文内容，作为首个迁移样例。另外两份报告暂保留原布局。格式文档见 docs/NOTE_TEMPLATE.md。构建与功能检查结果以本轮实测为准，不将浏览器视觉验收自动记为完成。

## 2026-10-04 Notes 阅读模板修订

用户确认恢复 NMR_EXP 阅读器视觉基线：侧栏自动比例、滑杆设置图标与主题圆点、章节树和纸张标题头；Home 图标与搜索输入框在侧栏顶部同行。保留标签/元数据和全文搜索。H2 开始独立纸张，H3 不拆页，页码为“第 N 页”，允许 data-page-break 手动分隔。W 波段报告为验收样例，不修改主页。

本轮检查通过：Jekyll 构建、JS 语法、W 波段 9 个 H2 对应 9 张独立纸张、无空封面、标题元数据、目录折叠、全文搜索与清除、比例缩放与主题按钮。移动节点前后正文/表格/公式文本一致。真实浏览器视觉、外部 MathJax/Mermaid 渲染和打印仍待验收。

## 2026-10-04 字体与小节标题头修订

对照 NMR_EXP/200-and-more-nmr-experiments-html/experiments/1.html：基础正文 14 px、H3 17 px、H4 15 px（随阅读比例缩放），中文与英文统一衬线字体序列。每个 H2 移至所在纸张的浅色标题头，保持原 ID 和目录链接；首张纸同时保留文章标题与元数据。清除旧报告 H1 的黑色下边框及页头边线。此记录覆盖上一版仅首张纸有标题头的实现。

没有 H3 子目录的 H2 使用普通链接行，移除展开箭头和空子列表；全目录无子节时隐藏展开/收起全部控件。

## 2026-10-04 23:26 — 本轮已确认并实施的规则

目录 H2 基础 13 px/650，H3 基础 12 px/400，编号显示“第 1 章”；正文 H3 自动 1.1、1.2 编号，与目录一致，已有数字前缀去重。H3 加粗、主题色序号和细浅色下边线。桌面左右页边距为纸宽 12.1%，上下接近 Word A4 2.54 cm 的比例；手机 24 px，打印 2.54 cm。删除每纸页码。顶部文档标题左侧使用现有 favicon.ico；Home 无边框、无常态底色。表格按内容宽度布局，长单元格换行，超宽表局部滚动。

统一版权位于侧栏目录最下方，邮箱为 mailto 链接：© 2026 Hyphoon wuhaifeng@ustc.edu.cn. All rights reserved. 引用请注明作者与来源；转载、改编或商业使用请事先联系作者。

默认从 _config.yml 的 note_copyright 读取，文章可用同名完整对象覆盖 year/author/email/notice。不再生成其他声明版本。W 波段正文末尾的旧版权已删除。此段覆盖前文页码及较小边距设置。


## 2026-10-05 阅读器截图修订
ICO 跨顶部标题和分类两行居中；目录 H2 和章序号均为常规字重。纸张标题头顶部留白桌面 28 px、手机 24 px，左右边距保持既定比例。公式不生成横向滚动条：行内公式整体换行，超出正文宽度时按实际宽度缩放；文字箭头流程按节点换行。自然宽度表格在正文内居中，超宽表仍局部滚动。

默认主题为 mist，界面名称保留“雾蓝”。首次访问与无有效主题记录时使用 mist；读者主动选择其他主题后保留其选择。


## 2026-10-05 URL 小写迁移
SpinFront 主入口改为 /spinfront/，旧 /SpinFront/ 保留兼容跳转，保留查询参数与锚点。NMR_EXP 与 SpinPlot 独立仓库改名待 GitHub 管理登录完成；在新地址部署前，主站仍指向有效旧地址。规划路径 /nmr_exp/、/spinplot/，项目显示名称不变。


用户已手动将独立仓库改名为 nmrexp、spinplot、easycurling。正式地址使用 /nmrexp/、/spinplot/、/spinfront/；主站元数据与项目索引同步更新。EasyCurling 是 Python/Windows 软件仓库，没有网页入口，源码和下载链接使用 github.com/imasenHF/easycurling，发布资产文件名仍按实际大小写保留。旧 /NMR_EXP/、/SpinPlot/、/SpinFront/ 根入口保留静态跳转，404 兼容脚本处理旧前缀的深层页面，保留查询参数与锚点；GitHub Pages 静态兼容页不等于服务器 301。


## 2026-10-05 导航与项目分类
Notes 侧栏 Home 返回 /notes/，顶部 ICO 返回 /。首页介绍原文不变，在“正在学的东西，”后主动断行，手机自然换行。Projects 按 _data/project-types.yml 的分类和顺序分组；项目用 project_type 标注，未知类别显示于其他项目。专题调研条目用 note 指向 Notes slug，标题、摘要、URL 从原笔记读取，正文只维护一份。首页精选项目保持原有三个入口。


## 2026-10-05 Projects 与 Notes 分区修订
三份调研只在 Notes 展示，不在 Projects 重复设置入口。Projects 保留软件开发、参考资料、信息整理三类，后续按独立项目的实际类型扩展。此规则覆盖此前将调研笔记列入专题调研项目的安排。


## 2026-10-05 首页介绍自然换行
取消首页介绍中的强制换行，保留原文和当前可用宽度。所有屏幕尺寸均按容器宽度自动换行，此规则覆盖前文按语义主动断行的安排。后续用户提出调整时，先评估合理性及与既定规划的关系，再实施已授权修改。


## 2026-10-05 Notes 正式发布规范
Notes 采用 Just the Docs 原生响应式文档格式及主页蓝灰暖白主题，不恢复纸张或阅读比例调节。W 波段标题为“W 波段 EPR：原理与应用”，副标题为“高场效应、应用体系与实验条件”。三篇调研的原文统一维护于 `_note_sources/`，生成器输出正式主页、子页面、搜索与旧锚点映射。写作与版式要求以 `docs/NOTE_TEMPLATE.md` 为准，覆盖旧阅读器说明。

## 栏目标识（2026-10-05）

显示名称使用 Notebook 与 Workshop，URL 保留 `/notes/` 与 `/projects/`。栏目列表页与子页采用主页 Georgia 字体的双行标识，ICO 为 48 px 跨两行，`plastocyanin` 25 px，栏目名 16 px 居中。Notebook 采用已选 F，Workshop 采用已选 A：字母 o 使用主页圆点金色 #b68c37，其余字母 #203139。ICO 与主标题返回主页，副标题返回栏目列表；文档目录首页与面包屑继续返回文档首页。
