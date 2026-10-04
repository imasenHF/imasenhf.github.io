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
