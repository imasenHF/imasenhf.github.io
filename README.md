# plastocyanin

hyphoon 的个人网站，收录科研工具、NMR/EPR 笔记与调研，并提供独立项目入口。

[访问网站](https://plastocyanin.org/) · [Notebook](https://plastocyanin.org/notes/) · [Workshop](https://plastocyanin.org/projects/)

## 阅读与项目入口

| 栏目或项目 | 内容 | 地址 |
|---|---|---|
| Notebook | 谱学笔记与技术调研，支持分章阅读和文档内检索 | [/notes/](https://plastocyanin.org/notes/) |
| SpinPlot | 浏览器端 CW EPR 数据处理与作图 | [/spinplot/](https://plastocyanin.org/spinplot/) |
| SpinFront | NMR/EPR 日报、日期归档与标签检索 | [/spinfront/](https://plastocyanin.org/spinfront/) |
| NMR Experiment Library | 按教材与章节组织的 NMR 实验参考资料 | [/nmrexp/](https://plastocyanin.org/nmrexp/) |

独立项目分别维护于 [spinplot](https://github.com/imasenHF/spinplot)、[spinfront](https://github.com/imasenHF/spinfront) 和 [nmrexp](https://github.com/imasenHF/nmrexp)。本仓库维护主站和 Notebook。

## 本地预览

需要 Ruby、Bundler 与 Jekyll 依赖：

```sh
bundle install
bundle exec jekyll serve
```

访问 http://localhost:4000/。发布前运行 `bundle exec jekyll build`；构建结果位于 `_site/`。普通静态服务器不会编译 Liquid 模板。

## 内容维护

- `_projects/` 保存项目标题、摘要、类型、链接及展示顺序。
- `_notes/` 保存笔记元数据和文档入口。笔记列表按 `published_at` 排序；未确认的发布日期留空。
- `_note_sources/` 是技术调研正文的编辑来源。运行 `python scripts/build-note-docs.py <slug>` 生成文档首页、分章页面和搜索索引。
- Notes 的标题层级、编号、公式、强调框与主题配色见 [写作与版式规范](docs/NOTE_TEMPLATE.md)。

生成的文档页面应通过源文件修改后重新构建。页面介绍与操作提示使用简洁、具体的表述；功能说明以当前实现为准。

## 发布与资源

主站使用 Jekyll 和 GitHub Pages。网页路径使用小写；旧大写项目入口通过兼容页跳转，保留查询参数与锚点。

首页结构与 EPR 示意谱图由 `scripts/build_plastocyanin_visual.py` 生成，输入位于 `assets/images/plastocyanin/`。示意谱图省略坐标轴，不作为定量分析图使用。

Just the Docs 资源及其 MIT 许可位于 `assets/jtd/`。网站笔记的引用与转载要求见各文档页脚；第三方资源的权利归各自权利人。

## 联系

wuhaifeng@ustc.edu.cn
