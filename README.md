# plastocyanin

hyphoon 的个人空间。当前为未提交的 Jekyll 重设计草稿。

## 本地预览

```sh
bundle install
bundle exec jekyll serve
```

打开 http://localhost:4000/。普通 Python 静态服务器不能编译 Liquid 模板。

## 内容维护

- 项目在 `_projects/`：title、summary、kind、link、featured、order。
- 笔记在 `_notes/`：title、summary、category、tags、featured、order、published_at。
- 首页精选按 order 排列，Notes 全部列表按 published_at 倒序排列。
- 三份报告的发布日期未确认，暂为空；真实发布时填写 YYYY-MM-DD。
- 新笔记可以使用 Markdown。已有复杂报告保留 HTML，样式限定在正文内。
- SpinFront 当前只有入口页，尚未导入期刊摘要归档。
- About / CV 当前只有联系信息，未编写履历。

## 发布前

运行 `bundle exec jekyll build`。发布环境必须编译 Jekyll，部署 `_site/`；不要直接上传模板源码。现有 NMR_EXP 与 SpinPlot 独立项目地址保持不变。此轮未提交、推送或部署。

## 科学视觉资源

`assets/images/plastocyanin/plastocyanin-composition.svg` 由 `scripts/build_plastocyanin_visual.py` 生成。数据来源为同目录 CSV，4096 点、275–350 mT；使用统一线性幅度缩放，不做逐峰放大或平滑。结构采用原 config6.png。当前首页使用结构在前、谱线在后的叠层构图，图内无坐标轴，交叠处存在视觉遮挡。更新数据后运行该脚本再构建 Jekyll。

## 首页 K 款确认

用户选定 K：黄色 #F0BE32 内线宽 3.5、白色单侧描边 3（总外宽 9.5），谱线位于结构下半部前景，无坐标轴。此前背景谱线与后景叠层方案废止。用户已授权修改后直接提交并推送，取代此前暂不提交要求。

## Notes 共用阅读模板

用于长篇调研、学习笔记、实验方法及计算记录。新文章使用 `_notes/` 内的 Markdown 或 HTML，指定 `layout: note`；元数据统一展示，首页与列表读取同一来源。阅读界面提供 Home、自动目录、页内搜索、主题、缩放、图表与打印样式，不包含教材页码或扫描页功能。

完整写作字段、功能限制与检查方法见 [docs/NOTE_TEMPLATE.md](docs/NOTE_TEMPLATE.md)。W 波段 EPR 报告是首个迁移样例。

Notes 模板沿用 NMR_EXP 阅读器的主题和侧栏比例；Home 图标与页内搜索同列于侧栏顶部，正文按 H2 小节生成独立纸张与 Notes 页码。W 波段调研用作完整样例。使用说明见 [Notes 模板文档](docs/NOTE_TEMPLATE.md)。
