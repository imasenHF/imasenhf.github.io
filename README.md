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

运行 `bundle exec jekyll build`。发布环境必须编译 Jekyll，部署 `_site/`；不要直接上传模板源码。独立项目正式入口为 /nmrexp/ 与 /spinplot/。此轮未提交、推送或部署。

## 科学视觉资源

`assets/images/plastocyanin/plastocyanin-composition.svg` 由 `scripts/build_plastocyanin_visual.py` 生成。数据来源为同目录 CSV，4096 点、275–350 mT；使用统一线性幅度缩放，不做逐峰放大或平滑。结构采用原 config6.png。当前首页使用结构在前、谱线在后的叠层构图，图内无坐标轴，交叠处存在视觉遮挡。更新数据后运行该脚本再构建 Jekyll。

## 首页 K 款确认

用户选定 K：黄色 #F0BE32 内线宽 3.5、白色单侧描边 3（总外宽 9.5），谱线位于结构下半部前景，无坐标轴。此前背景谱线与后景叠层方案废止。用户已授权修改后直接提交并推送，取代此前暂不提交要求。

## Notes 文档模板

三篇技术调研采用 Just the Docs 原生文档布局、分章页面、中文及英文跨页搜索与主题切换。默认配色与主页一致；ICO 返回主页，文档标题返回文档首页，每页包含 Back to top 和版权信息。使用原生响应式布局，不提供手动阅读比例或纸张分页。

正文唯一编辑来源在 `_note_sources/`，运行 `python scripts/build-note-docs.py <slug>` 生成 `_notes/` 文档主页、`notes/<slug>/` 子页及索引。修改正文后重新生成，不手工编辑生成页面。官方资源与 MIT 许可位于 `assets/jtd/`。

用途、写作原则、元数据、公式与表格规范、发布检查见 [Notes 写作与版式规范](docs/NOTE_TEMPLATE.md)。

## URL 约定
新增网页路径使用小写，项目显示名保持原样。项目入口为 /nmrexp/、/spinplot/、/spinfront/。旧大写根入口和深层页面通过静态兼容页跳转，查询参数和锚点保留。下载资产、代码文件按实际文件名引用，不统一转换文件名大小写。EasyCurling 源码位于 https://github.com/imasenHF/easycurling 。
