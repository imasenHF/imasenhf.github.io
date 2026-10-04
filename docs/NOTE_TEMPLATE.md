# Notes 阅读模板

用于个人学习笔记、技术调研、实验方法和计算记录。采用纸张式正文、文章目录、页内搜索与阅读设置。模板是主站共享组件，不复制 NMR 资料库的章节、PDF 页码、原书页码或扫描页映射。

## 新建文章

在 `_notes/` 新建 `.md` 或 `.html`，使用 `layout: note`。Markdown 在构建时转为 HTML，正文静态输出，不依赖浏览器注入。复杂图表可保留 HTML。正文从 H2 开始，文章 H1 由模板生成。

```yaml
---
layout: note
title: 文章标题
summary: 简短摘要
category: 磁共振
tags: [EPR, W-band]
published_at: null
updated_at: null
featured: false
order: 1
math: true
---
```

标题为必填，建议填写摘要、分类与标签。日期确认后填 YYYY-MM-DD，空日期不显示。featured/order 用于首页精选。math 为 true 时加载 MathJax；外部 CDN 不可达时数学表达式保留源码。附件可选：`attachments: [{title: 数据文件, url: /assets/notes/example/data.csv}]`。正文参考文献由作者编写，模板不补写来源。

图片与附件放在 `assets/notes/<文章名>/`；路径使用 `relative_url`。复杂 HTML 内有 Liquid 冲突时局部使用 raw/endraw，勿将需要解析的资源 URL 包在 raw 内。

## 阅读功能

侧栏顶部同行放 Home 图标和搜索输入框；Home 返回主站。H2/H3 自动生成折叠章节目录，已有标题 ID 保留，缺失 ID 按出现顺序生成；需长期引用的章节建议显式固定 ID。子节可收起；手机使用目录抽屉。

页内搜索匹配当前正文的普通文本，保留大小写原文，高亮、计数、上一项/下一项、清除。Ctrl/Cmd+K 聚焦搜索框，Enter 下一项，Shift+Enter 上一项，Esc 关闭目录抽屉与设置面板。公式、代码、Mermaid 以及跨 HTML 元素边界的短语不参与完整匹配；正文搜索清除后不更改链接与图表。分类与摘要在文章头部显示；标签链接打开 Notes 列表并应用查询。

主题有 mist/sage/sand/mauve/gray，默认 mist。自动适应或 80%–160% 手动缩放，设置仅存于本浏览器 Notes 专用键。缩放沿用 NMR_EXP 的侧栏宽度、纸张宽度、字体和页边距比例，保留浏览器原生缩放。谱图图片颜色不随主题改变。代码复制需要 HTTPS 与浏览器剪贴板权限，失败时提示选中文本。

真实纸张按 H2 小节分页，H3 保留在所属小节；每张纸有独立阴影、间隔及右下角“第 N 页”。正文高度随内容变化，不按固定高度切段。需要额外分隔时插入 `<div data-page-break></div>`。有引言时首张纸包含标题与引言，否则标题放在首个 H2 小节的纸张顶部。分页通过移动现有 DOM 节点实现，保留链接、表格、公式和引用。打印隐藏工具栏、目录和操作按钮，保留标题、元数据和正文，并按纸张分隔；过长小节可能占多张实体打印页。关闭 JS 后正文与元数据仍可阅读，目录、搜索、主题等增强功能不可用。

## 文件职责

- `_layouts/note.html`：静态正文与元数据。
- `_includes/note-toolbar.html`：Home、搜索、显示设置。
- `assets/css/note-reader-base.css`：复用 NMR_EXP/reader-template/shared/reader.css 的阅读器基础样式，保留主题、原始几何比例与显示设置。
- `assets/css/note-reader.css`：Notes 元数据、侧栏 Home/搜索、独立纸张及打印适配。
- `assets/js/note-reader.js`：目录、搜索、阅读设置和键盘操作。
- `_notes/w-band-epr.html`：首个完整迁移样例；另外两份报告暂保留原布局。

## 检查

运行 `bundle exec jekyll build` 和 `node --check assets/js/note-reader.js`。检查静态正文、单一 H1、元数据与标签、链接、公式、目录和搜索。浏览器需检查 390 px 手机布局、宽表格滚动、80%/160% 缩放、主题、脚注、深链接和打印。Mermaid/MathJax 渲染依赖相应库加载成功。未通过浏览器验收前不将视觉检查记为完成。

## 本轮验证记录

W 波段样例已通过 Jekyll 构建、JS 语法检查和 DOM 功能检查：静态正文、单一 H1、标签路径、目录、表格滚动容器、搜索翻页与清除后正文一致、主题和缩放、目录抽屉 Esc 关闭目录抽屉与设置面板。DOM 检查不等同于真实浏览器视觉检查；390 px 布局、MathJax/Mermaid 实际渲染和打印分页仍待浏览器验收。

## 2026-10-04 修订

恢复 NMR_EXP 的阅读视觉：原有自动缩放和侧栏宽度、滑杆设置图标及主题色按钮、折叠章节树、浅色纸张标题头。Home 与输入式全文搜索位于侧栏顶部同行。H2 分纸、H3 随节，取消原书/PDF 标识。W 波段作为格式样例，其他报告暂不迁移。

本轮检查通过：Jekyll 构建、JS 语法、W 波段 9 个 H2 对应 9 张独立纸张、无空封面、标题元数据、目录折叠、全文搜索与清除、比例缩放与主题按钮。移动节点前后正文/表格/公式文本一致。真实浏览器视觉、外部 MathJax/Mermaid 渲染和打印仍待验收。
