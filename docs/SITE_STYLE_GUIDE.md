# SITE_STYLE_GUIDE

更新日期：2026-10-08（Asia/Shanghai）

适用范围：plastocyanin 主站视觉规范及各独立 Web 项目共同采用的品牌规则。子项目特有的页面、控件、模板及钉钉通知版式保存在各自仓库；本文件不复制全部子项目样式。实际 CSS、HTML 与构建结果用于确认已实施状态。

## 1. 共用品牌

- 正式品牌为 `plastocyanin.`；采用 Georgia / serif。
- 深蓝灰 `#203139` 为默认主体文字；链接与交互蓝 `#355c7d`；品牌金色 `#b68c37`；背景使用接近 `#f6f6f3` 的暖白。页面具体色值以实际样式和图形资源为准。
- 品牌文字中的字母 `o` 与末尾圆点均为金色，其余字母默认深蓝灰。
- 既有语义链接在 hover、active、keyboard focus 时，主体文字显示蓝色并出现细下划线；品牌金色部分保留金色；键盘焦点可见。普通不可点击标题不额外制造自链接。
- 统一字体角色：Georgia / serif 用于网站品牌、项目/栏目名称及 SpinFront 杂志标题和日期；sans-serif 用于正文、中文技术标题、分类标签、筛选与常规界面。不强制将所有中英混排文本设置为 Georgia。
- Φ 风格个人图标使用已确认资源 `assets/images/imasen_phi_logo/`，包括金色 I、闭合蓝色倾斜轨道、金色圆点与 EPR 波形。不要重新设计或用相似临摹替换。

## 2. 主站页头、栏目与首页

- 主站导航：Home / Workshop / Notebook / About / CV；显示内容依据实际栏目。
- 页头分隔线与 `.header-inner.container` 内容宽度一致，不贯穿整个浏览器窗口。
- Notebook / Workshop 使用两行品牌：第一行为 `plastocyanin.`、第二行为栏目名，配合原有图标；图标和主品牌返回首页，栏目名进入各自列表页。Notebook 和 Workshop 已确认的金色字母分布沿用仓库现有 `assets/css/section-brand.css`。
- 首页 Hero 的 `plastocyanin.` 是主站链接；About plastocyanin 一节内的同名词组也使用品牌规则并链接主页。
- 首页科学示意图位于 `assets/images/plastocyanin/`，由 `scripts/build_plastocyanin_visual.py` 生成。当前选定 K 方案：EPR 示意谱金黄色 `#F0BE32`、内线宽 3.5、单侧白色描边 3、总外宽 9.5；谱线位于蛋白结构下半部前景，无坐标轴。示意图不用于定量分析。
- 首页 SpinFront 日历为主站专用组件：左侧月历、右侧内部滚动日报条目；保留 Daily Epigraph、日期定位、焦点透明度约 0.72 / 0.88 / 1、金色编号及标题通向完整日报的链接。右上角进入 `/spinfront/`。当前显示的分类标签须可点击并进入相应 SpinFront 筛选；不取消组件内部滚动。此处的具体交互实现位于 `assets/js/home-spinfront.js` 与主站样式。

## 3. 主站共享页尾

- 分隔线为 2px 深蓝灰。桌面端品牌与版权内容相对分隔线各内缩 40px，移动端 20px；不同页面可保留自身容器宽度。
- 桌面端使用左右双栏、右侧右对齐；移动端上下堆叠、文字左对齐。
- 左栏第一行固定为 `plastocyanin.`（返回首页），第二行按页面为 `Workshop`、`Notebook`、`About / CV` 或主页的 `hyphoon`；第三行描述分别为 `Projects / Tools`、`Notes / Research`、`Profile / CV` 或 `Personal website`。
- 右栏第一行：`© YYYY wuhaifeng@ustc.edu.cn. All rights reserved.`；第二行按项目说明、笔记、个人资料或一般网页内容使用对应版权声明。
- Notebook 的 Just the Docs 阅读页使用自身的版权区域，不重复加入主站双栏页尾。

## 4. 各项目专用规范的归属

| 范围 | 正式规范位置 | 适用边界 |
| --- | --- | --- |
| 主站共享导航、品牌、首页、页尾 | 本文件 + `_layouts/default.html`、`assets/css/style.css`、`assets/css/section-brand.css` | 主站已实现样式为准；跨站视觉调整需检查各受影响项目 |
| Notebook 分章文档、公式、主题、搜索 | [docs/NOTE_TEMPLATE.md](NOTE_TEMPLATE.md) + `assets/jtd/` | 采用 Just the Docs；不恢复纸张阅读器或任意比例缩放 |
| SpinFront 日报主页、单期日报、归档、标签与钉钉消息 | [SpinFront docs/STYLE_GUIDE.md](https://github.com/imasenHF/spinfront/blob/main/docs/STYLE_GUIDE.md) | 独立使用 editorial magazine 版式；不恢复圆角卡片数据库式首页或独立滚动 sidebar |
| SpinPlot 软件界面 | [SpinPlot README](https://github.com/imasenHF/spinplot/blob/main/README.md)、[架构](https://github.com/imasenHF/spinplot/blob/main/docs/ARCHITECTURE.md) 及实际应用文件 | 保留独立紧凑单行、深蓝渐变页头；不强制套用主站双行品牌 |
| NMR Atlas 周期表、配色与专用交互 | [NMR_ATLAS_CONTEXT.md](https://github.com/imasenHF/nmr-atlas/blob/main/NMR_ATLAS_CONTEXT.md) | 品牌链接沿用主站蓝灰/金色，周期表配色由独立工具自身管理 |
| NMR Experiment Library 教材阅读器 | [nmrexp README](https://github.com/imasenHF/nmrexp/blob/main/README.md) 与阅读器样式 | 保持现有教材阅读功能；不将主站页面样式直接覆盖第三方资料页面 |

## 5. 维护和验收

- 共用视觉决定修改本文件；SpinFront、NMR Atlas 等专属版式变化更新各自仓库的专用记录。项目之间有联动时核对所有实际受影响页面，但不机械复制同一段规范。
- 对模板或 CSS 的变更，至少检查主站桌面/手机页头、页尾、链接、键盘焦点及受影响的首页组件；对外部项目进行对应页面检查。
- 修改 Notebook 主题与排版，遵循 `docs/NOTE_TEMPLATE.md`，重建受影响的源文档并检查公式、目录和搜索。
- 记录仅保留已确认且仍有效的设计规则；实验性草稿、弃用风格和设计过程由 Git 历史保留。
