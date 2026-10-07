# SITE_STYLE_GUIDE

更新日期：2026-10-07（Asia/Shanghai）

用途：保存 plastocyanin 主站及 SpinFront 当前已确认的版式、品牌与交互规则，作为跨对话和后续维护的格式备份。实际实现仍以各仓库 main 分支中的模板与 CSS 为准；如本文件与最新代码冲突，先检查是否为未同步改动，再更新本文件。

## 1. 共用视觉语言

主色：
- 深蓝灰：`#203139`
- 链接 / 强调蓝：`#355c7d`
- 金色：`#b68c37`
- 暖白 / 米白背景：`#f6f6f3` 附近
- 分隔线使用浅灰，不使用高对比粗边框作为常规内容分隔。

字体只保留两类角色：
- Georgia / serif：品牌、项目名、栏目名，以及 SpinFront 的杂志化标题与日期数字。
- sans-serif：正文、中文内容标题、分类标签、筛选、导航和一般界面文字。

主页精选项目中的 SpinPlot、SpinFront、NMR Experiment Library 使用 Georgia。中文笔记标题、“精选项目”“笔记与调研”、SOFTWARE / DIGEST / REFERENCE 等分类与正文保持 sans-serif。SpinFront 日历组件允许日期和焦点标题使用 serif，但不再引入第三套字体体系。

## 2. 品牌与标题链接反馈

所有已有语义链接的标题和品牌文字使用同一交互规则：
- 默认：深蓝灰。
- hover / active / keyboard focus：主体文字变为 `#355c7d`，显示细下划线。
- 下划线偏移约 `.18em`，保持文字可读。
- 所有作为品牌显示的 `plastocyanin.` 中，字母 `o` 与末尾圆点统一使用金色；其他字母保持深蓝灰。品牌 hover / active / focus 时，金色 `o` 与圆点继续保持金色。
- 不为普通不可点击标题增加无意义的自链接。
- 键盘 focus 必须可见。

适用范围包括：
- plastocyanin.（品牌中的 `o` 与末尾圆点为金色）
- Notebook / Workshop / SpinFront
- 主站项目标题与笔记标题
- SpinFront Latest Issue 标题与归档结果标题
- SpinFront 日报大标题和页尾品牌链接

## 3. 主站页头与栏目品牌

主站保留 Φ 风格个人图标及 favicon。主站资源位于 `assets/images/imasen_phi_logo/`。

Notebook / Workshop 使用两行栏目品牌：
- plastocyanin. 为第一行，其中 `o` 与末尾圆点均为金色。
- 第二行为栏目名；当前已确认金色字母分布沿用仓库现有实现。
- 图标和 plastocyanin 返回主站；栏目名返回栏目首页。
- 品牌文字使用 Georgia。

SpinPlot 继续使用其独立的紧凑深色单行页头，不强制改成主站浅色栏目页头。
主站首页品牌：
- Hero 中的大号 `plastocyanin.` 作为主页链接，使用与其他品牌相同的 hover / active / focus 反馈。
- `About plastocyanin.` 中的 plastocyanin 词组使用品牌格式：Georgia，金色 `o` 与金色圆点，并链接主页。


## 4. 主站页尾

使用默认布局的页面统一采用与 SpinFront 日报相近的左右双栏结构。

左栏：
- 第一行始终为 `plastocyanin.`，链接主站。
- Workshop 页面：显示 `Workshop` + `Projects / Tools`。
- Notebook 页面：显示 `Notebook` + `Notes / Research`。
- About / CV 页面：显示 `About / CV` + `Profile / CV`。
- 主页面：显示 `hyphoon` + `Personal website`。

右栏：
- 第一行统一为：`© YYYY wuhaifeng@ustc.edu.cn. All rights reserved.`
- 第二行按页面内容采用相应声明：
  - Workshop：本站项目说明与文字内容版权归作者所有，未经许可不得复制、转载或用于商业用途。
  - Notebook：本站笔记与文字内容版权归作者所有，未经许可不得复制、转载或用于商业用途。
  - About / CV：本站个人资料与文字内容版权归作者所有，未经许可不得复制、转载或用于商业用途。
  - 主页及一般页面：本站内容版权归作者所有，未经许可不得复制、转载或用于商业用途。

桌面端左右平衡，右栏右对齐；移动端上下堆叠并左对齐。

Notebook 的 Just the Docs 阅读器仍使用其侧栏版权结构，不再额外增加底部页尾。

## 5. 主站首页 SpinFront 日历组件

首页 SpinFront 组件保留内部滚动浏览，不取消滚动交互。

当前规则：
- 组件配色统一为深蓝灰 + 金色 + 暖白，不再使用独立绿色强调体系。
- 左侧按月显示已有日报日期；默认选择 Asia/Shanghai 当日，当日无日报时选最新一期。
- 右侧条目保留内部滚动、Daily Epigraph、滚动定位与焦点判断。
- 普通 / 邻近 / 当前条目透明度约为 `0.72 / 0.88 / 1`。
- 不再用 scale 缩放聚焦条目。
- 编号采用金色 `01 /` 形式。
- 条目标题链接到对应完整日报条目，而不是直接跳论文原始来源。
- 右上角“进入日报主页”固定链接到 `/spinfront/`。

## 6. SpinFront 日报主页

正式入口：`/spinfront/`。

整体定位为 `Magazine Front Page + Archive`，不是后台式数据库首页。

首屏：
- 顶部显示 plastocyanin.，不在页头额外加入 Φ 图标。
- 大号 `SpinFront` 为日报主页链接；其中字母 o 使用金色。
- 主标题链接反馈与日报内页一致。
- 右侧为 Latest Issue 日期封面块。
- 首屏下方展示最新一期前四条内容。

归档区：
- 搜索、日历、主题和高级筛选放在 `EXPLORE THE ARCHIVE` 下方。
- 搜索结果使用 editorial rows，不恢复独立大圆角白卡。
- 结果采用编号、衬线标题、细分隔线、摘要和金色左线技术评注。
- 技术评注默认展开，仍可手动折叠。
- 左侧筛选栏采用页面正常纵向滚动：不使用 sticky、不限制视口高度、不设独立 scrollbar。
- 日历选中日期使用深蓝灰底、白字、金色标记。
- 最近一期 / 全部日期为一级操作；起止日期、最近7天、本月放入 DATE RANGE。
- “关于归档与数据”和“完整日报归档”位于筛选与结果区之后，保持全宽折叠结构。
- 最后一条结果底部不再额外显示重复分割线。

页尾：
- 左栏：plastocyanin. / SpinFront / NMR / EPR Daily Brief。
- 右栏：`© YYYY wuhaifeng@ustc.edu.cn. All rights reserved.`
- 第二行：`本报告版权归作者所有，未经许可不得复制、转载或用于商业用途。`
- 与日报内页保持相同左右双栏关系。

## 7. SpinFront 完整日报

采用已确认的 D 版 editorial magazine 结构。

页头与封面：
- 顶部只保留 `plastocyanin.` 和 `Daily archive →`。
- `plastocyanin.` 链接主站。
- 大号 `SpinFront` 链接日报主页，字母 o 保持金色。
- 右侧使用深蓝灰日期封面块。
- 首屏保留 NMR / EPR Daily Brief、条数、NMR/EPR 数量和时间范围。

正文：
- 每条使用大号金色编号、Georgia 标题、细分隔线。
- 桌面端分类标签放右侧；移动端右栏隐藏后，在标题下显示标签。
- 摘要为正文色 sans-serif。
- 技术评注使用金色左线。
- 来源与 DOI 合并为同一条元数据：来源及替代来源在前；有 DOI 时在其后追加 `DOI <完整 DOI>` 并链接 `https://doi.org/<doi>`；无 DOI 时完全隐藏 DOI，不显示空值或占位。
- taxonomy 中的真实分类标签均可点击并跳回 `/spinfront/` 的对应筛选结果；谱学方向、实验类型、方法、应用、仪器部件和信息类型都属于可链接分类。时间范围等非 taxonomy 信息保持普通文本。
- 检索范围与筛选说明默认折叠。
- 最后一条正文底部不再额外显示重复分割线。
- 正文后提供 Previous / Next Issue 相邻日报导航。

页尾：
- 左栏：plastocyanin. / SpinFront / NMR / EPR Daily Brief · YYYY-MM-DD。
- 右栏：`© YYYY wuhaifeng@ustc.edu.cn. All rights reserved.`
- 第二行：`本报告版权归作者所有，未经许可不得复制、转载或用于商业用途。`
- plastocyanin. 返回主站，SpinFront 返回日报主页。

## 8. 钉钉日报通知版式

钉钉消息保持紧凑，不使用复杂卡片或多层链接。

当前结构：
```text
SpinFront | YYYY-MM-DD
> NMR / EPR Daily Brief
本期收录 N 条 · NMR X / EPR Y
内容预览
1. ...
2. ...
3. ...
阅读完整日报 →
```

主标题使用略大的 Markdown 标题级别；英文副标题使用引用模块。前三条标题不添加单独可点击链接，仅底部保留完整日报入口。

## 9. 当前实现位置

主站：
- `_layouts/default.html`：共享页头和双栏页尾
- `_includes/section-brand.html`：Notebook / Workshop 品牌
- `assets/css/style.css`：主站视觉、字体角色、标题与页尾链接反馈、首页 SpinFront 组件
- `assets/css/section-brand.css`：栏目品牌样式与交互
- `assets/js/home-spinfront.js`：首页 SpinFront 日历与内部滚动
- `index.html`：主站首页

SpinFront：
- `scripts/build.py`：日报结构、页尾、相邻日报导航、首页最新一期生成
- `templates/home.html`：日报主页骨架
- `templates/issue.html`：单期日报外壳
- `assets/home.css`：日报主页 Magazine Front Page、归档、日历和页尾
- `assets/home.js`：归档筛选、结果与技术评注默认状态
- `assets/style.css`：完整日报 D 版样式

## 10. 修改边界

- 不因局部改动重新设计整套品牌体系。
- 不恢复 SpinFront 旧蓝色渐变卡片首页。
- 不恢复 SpinFront 归档 sidebar 的独立滚动。
- 不取消主站首页 SpinFront 日历组件的内部滚动。
- 不将所有中英混排标题改为 Georgia；中文内容标题仍以 sans-serif 为主。
- 修改模板或共享 CSS 后检查桌面端与移动端。
- 版式改动后同步本文件与 `SITE_CONTEXT.md`；SpinFront 专属规则同步其仓库 `docs/STYLE_GUIDE.md`。
