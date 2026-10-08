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

## 电子—电子距离文档格式（2026-10-05）

原报告的 H2 章标题、H3 小节及 H4 子节保留原层级与编号；短标题用于页面 H1 和侧栏。科学内容组件保留着重框、警告、案例卡片、等宽序列块、SVG 时间轴、回波轮廓与图例。专用样式由 `assets/jtd/distance-content.css` 维护；生成时不得丢弃组件样式或删除编号。

电子—电子距离报告目录以原文视觉结构为准：左侧四个部分为主目录，展开各章；摘要与报告范围、缩写与术语、参考文献为独立入口。右侧固定显示当前章全部编号小节及下级标题，随滚动标记当前位置。不可再用17章平铺或将章内小节放到左侧替代原有分组。H4正文标题18px，正文16px。


## 2026-10-07 首页 SpinFront 日历组件

首页 About plastocyanin 区块下方保留 SpinFront 日历组件。左侧按月显示已发布日报日期，点击日期后右侧切换对应日报；默认选择 Asia/Shanghai 当日，若当日尚无日报则显示最新一期。右侧条目继续使用内部滚动浏览，保留 Daily Epigraph、滚动定位与当前条目聚焦，不取消滚动交互。

组件视觉统一到主站及 SpinFront 杂志版的深蓝灰、金色与暖白体系，不再使用独立绿色强调色。滚动焦点仅调整透明度，不再缩放条目；普通、邻近、当前条目的透明度依次为 0.72、0.88、1。条目编号采用金色“01 /”形式。标题改为链接到对应完整日报条目，而不是直接跳原始来源；右上角“进入日报主页”固定链接至 `/spinfront/`。组件运行时继续读取 `/spinfront/search-index.json` 与 `/spinfront/taxonomy/taxonomy.json`，SpinFront 新日报发布后无需重新构建主站即可进入日历。Daily Epigraph 继续读取 `/assets/data/epigraphs.json` 并按 Asia/Shanghai 日期稳定轮换。

## 2026-10-07 SpinFront 杂志化视觉体系

SpinFront 正式采用 editorial magazine 视觉作为日报与归档主页的统一基准。正式入口保持 `/spinfront/`，独立源码仓库为 `imasenHF/spinfront`。

完整日报使用杂志内页结构：顶部仅保留 `plastocyanin.` 与 Daily Archive；大号 `SpinFront` 为日报主页链接，其中字母 o 使用主站金色；右侧使用日期封面块。正文采用大号编号、衬线标题、细分隔线、技术评注金色左线及右侧分类标签。桌面端右侧显示分类标签，移动端改在标题下显示，避免重复。DOI 显示完整字符串并链接到 doi.org；来源及替代来源保留链接。检索说明默认折叠，页尾 SpinFront 返回日报主页，并提供相邻日报导航。

`/spinfront/` 由数据库式首页调整为“Magazine Front Page + Archive”：首屏展示最新一期与前四条内容，搜索、日历、主题和高级筛选下移到 Explore the Archive。检索结果取消独立白色圆角卡片，采用与日报一致的编号、衬线标题、细分隔线和金色技术评注。日历仍保留原有日期定位功能，选中日期使用深蓝灰底、白字与金色标记；最近一期和全部日期为常用操作，日期范围与最近7天/本月收纳到 DATE RANGE 折叠区。


### 2026-10-07 SpinFront 归档滚动与交互修订

SpinFront 日报主页归档区改为单一页面纵向滚动：左侧 sidebar 不再使用 sticky、固定视口高度或独立滚动条，日期与主题筛选随页面正常滚动，避免在结果区底部出现左栏被视口裁切的视觉问题。日报主页首屏大号 SpinFront 标题与日报内页一致，作为返回 `/spinfront/` 的链接，字母 o 保持金色。归档结果中的“技术评注”默认展开，同时保留手动折叠能力。


### 2026-10-07 统一标题与品牌链接反馈

主站与 SpinFront 统一可点击标题和品牌文字的交互：默认保持深蓝灰；hover、active 或键盘 focus 时主体文字转为蓝色并显示细下划线，金色圆点或子项目名称中的金色字母保持金色。该规则用于项目/笔记等已有标题链接、SpinFront 最新一期与归档结果标题，以及 plastocyanin、Notebook、Workshop、SpinFront 品牌链接。

主站页尾加入 linked brand 层级：plastocyanin 返回主页；Notebook/Workshop 页面额外显示对应栏目链接。SpinFront 日报主页与日报内页页尾均显示 plastocyanin 与 SpinFront 两级品牌链接，分别返回主站和日报主页。仅对已有语义链接的标题应用交互，不为普通不可点击标题增加无意义的自链接。


### 2026-10-07 首页字体角色收敛

主页及栏目页字体角色收敛为两类：Georgia/serif 用于品牌与项目名称，sans-serif 用于正文、中文内容标题、分类标签和界面元素。主页精选项目中的 SpinPlot、SpinFront、NMR Experiment Library 等项目名统一使用 Georgia 系列；“精选项目”“笔记与调研”、笔记标题、SOFTWARE/DIGEST/REFERENCE 等分类与正文继续使用 sans-serif。SpinFront 日历组件保留自身 editorial 排版：日期/焦点标题可使用衬线，普通列表与摘要仍按组件现有规则显示，不再额外引入第三套字体体系。


### 2026-10-07 全站页尾双栏统一

使用默认布局的主站页面页尾统一改为与 SpinFront 日报相近的双栏结构：左栏显示 plastocyanin 品牌，Notebook/Workshop 页面附对应栏目品牌链接；右栏显示版权、公开联系邮箱及 Email/GitHub 入口并右对齐。移动端自动改为上下堆叠。品牌链接继续使用统一的蓝色 hover/focus + 细下划线反馈，金色圆点或栏目金色字母保持金色。Note 阅读器仍保留其侧栏版权结构，不额外插入页面页尾。


### 2026-10-07 页尾内容平衡修订

SpinFront 日报主页页尾与日报内页统一为左右双栏：左侧显示 plastocyanin、SpinFront 与栏目说明，右侧显示“© 年份 wuhaifeng@ustc.edu.cn. All rights reserved.”及日报版权声明。

主站默认布局页尾同步采用相同结构。左栏固定显示 plastocyanin，并按页面显示对应二级品牌与简短说明：Workshop / Projects / Tools，Notebook / Notes / Research，About / CV / Profile / CV；主页显示 hyphoon / Personal website。右栏统一使用公开邮箱版权格式，第二行声明按页面类型分别使用项目说明、笔记内容、个人资料或一般站点内容的版权表述。移动端继续改为上下排列。


### 2026-10-07 plastocyanin 品牌字形统一

所有作为品牌显示的 `plastocyanin.` 统一采用 Georgia/serif，字母 `o` 与末尾圆点使用金色 `#b68c37`，其余字母保持深蓝灰。该规则适用于主站页头、栏目页头、主站页尾、SpinFront 日报主页页头/页尾及完整日报页头/页尾；hover、active、keyboard focus 时主体文字变蓝并显示细下划线，金色 `o` 与圆点保持金色。

主站首页 Hero 的大号 `plastocyanin.` 改为主页链接；“About plastocyanin.”中的 plastocyanin 词组改为品牌格式并链接主页。此规则补充并覆盖此前只要求品牌末尾圆点为金色的旧描述。仓库格式备份位于 `docs/SITE_STYLE_GUIDE.md`，SpinFront 专属备份位于 `imasenHF/spinfront/docs/STYLE_GUIDE.md`。


### 2026-10-07 SpinFront 日报元数据与分类标签

完整日报条目将来源与 DOI 合并为同一条元数据：先显示原始来源及替代来源，有 DOI 时在其后显示完整 DOI 并链接 doi.org；无 DOI 时不显示 DOI。日报条目中的 taxonomy 分类标签改为可点击链接，进入 `/spinfront/` 对应筛选结果。可链接维度包括谱学方向、实验类型、方法、应用、仪器部件及信息类型；时间范围等非 taxonomy 字段保持普通文本。


### 2026-10-07 页尾几何与 SpinFront 品牌反馈修订

主站共享页尾与 SpinFront 日报页尾统一分隔线和文字相对位置：分隔线使用 2px 深蓝灰；允许不同页面沿用各自天然容器宽度，但桌面端品牌与版权内容相对分隔线左右各内缩 40px，移动端内缩 20px。SpinFront 日报主页页尾采用相同内缩规则。

SpinFront 日报主页此前标题 hover 仅出现下划线但未稳定变色，原因是主页样式使用了未定义的 `--blue` 变量。已在 `assets/home.css` 明确定义 `--blue:#355c7d`，并对顶部 `plastocyanin.` 与大号 `SpinFront` 增加显式 hover / active / focus 颜色规则；主体变蓝，品牌金色 o 与圆点保持金色。


### 2026-10-07 主站页头分割线宽度

主站页头底部分割线从全浏览器宽度改为实际内容容器宽度：`.site-header` 不再绘制 border，改由 `.header-inner.container` 绘制 1px 浅灰分割线。这样不同屏幕上分割线随主站内容宽度变化，与 SpinFront 主页按内容宽度收束的页头处理一致。


### 2026-10-08 NMR Atlas Workshop 关联

NMR Atlas 作为独立 Web 工具，仓库为 `imasenHF/nmr-atlas`，正式入口使用 `/nmr-atlas/`。主站 Workshop 新增 `_projects/nmr-atlas.md`，归类为 reference / Reference Tool，点击后直接进入 NMR Atlas，不建立主站重复项目正文页。

NMR Atlas 当前不设置为首页 featured 项目，仅出现在 Workshop 全部项目列表。其功能与视觉细节由独立仓库 `NMR_ATLAS_CONTEXT.md` 维护。


### 2026-10-08 SpinFront 分类标签跨视图检索

SpinFront 的 taxonomy 分类标签统一为“显示即能检索”。完整日报、SpinFront 日报主页检索结果及主站首页 SpinFront 日历组件中，只要某个标签实际显示，就必须可点击并进入 `/spinfront/` 对应筛选结果。链接格式使用 `?view=all&<dimension>=<tag>#explore`，维度来自 `taxonomy/taxonomy.json`，不按标签名称猜测。日报主页中的信息类型、方向、实验类型、方法、应用、仪器部件及“更多标签”均采用该链接；主站日历组件保持有限标签展示数量，但实际显示的标签全部可点击。时间范围、来源、发布日期等非 taxonomy 字段不作为分类链接。
