# Motion Notes · ECE 470

52 课、12 个模块、9 类交互实验。中文直觉 + 关键公式 + 必要例子，整合两份 Midterm Study Guide。页面支持日夜主题、低干扰粒子、目录搜索、考试范围筛选、进度导入导出。

## 直接使用

打开 `dist/index.html` 即可本地阅读。脚本、数学字体和课程均随项目提供，无需联网获取 CDN。学习进度仅存当前浏览器；不同站点地址、设备或浏览器不会自动同步，切换前可导出进度。下载文档在部分浏览器会直接显示文本，可另存为。

## GitHub Pages 部署

1. 新建自己的 GitHub 仓库，将本项目内容提交到仓库根目录（不是再套一层目录）。包括 `.github/workflows/pages.yml`、`content/`、`scripts/` 与 `dist/`。若拖拽上传漏掉隐藏目录，可在 GitHub 的 Add file → Create new file 中以 `.github/workflows/pages.yml` 为文件名创建，并粘贴本项目同名文件内容。
2. 仓库 Settings → Pages → Build and deployment → Source 选择 **GitHub Actions**。
3. Actions → Deploy course to Pages → Run workflow；之后每次向 main 推送都会自动构建部署。如果你的默认分支不是 main，修改 workflow 的 branches。
4. 工作流完成后，在 Pages 设置或该次 deployment 中打开实际生成的网站地址。

工作流只发布 dist，不发布课程源文件和制作脚本；网站用相对路径，支持项目子路径。已包含 workflow_dispatch，因此手动运行入口在 workflow 文件进入默认分支后可用。

参考：[GitHub 官方自定义 Pages 工作流文档](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)。页面要求与权限可能随平台调整，以官方说明为准。

## 修改课程

- 每课正文：`content/l01.md` 到 `content/l52.md`，LaTeX 用 `$...$` 和 `$$...$$`。
- 课程顺序、标题、模块、来源：`content/manifest.json`。已有 ID 不要变更，避免破坏进度。
- 界面：`dist/index.html`、`dist/style.css`；交互与路由：`dist/app.js`。
- 执行 `python scripts/build.py`，再执行 `node scripts/check.cjs` 检查公式语法。
- 本地服务：`python -m http.server 8000 --directory dist`，浏览器打开终端对应地址。
- 不要直接修改 dist/course.js；它是从 Markdown 构建出的文件。

`UPDATE_COURSE_PROMPT.md` 是给后续 AI 的完整更新指令。`COURSE_MAP.md` 是原资料知识点对应表。

## 内容范围与约定

数学与物理说明依据用户提供的两份 Study Guide，并补充推导桥梁与短例。原 PDF 没有在本次制作中重新访问；不声称重新核验原课件。保留课程特有 DH 顺序、twist/wrench 参考点和奇异性适用条件。删去代码合集、API 使用参考和输入错误排查。交互是教学模型：2R 连杆长度各 1 m；二维图或投影不能代替一般三维求解器。

## 依赖

KaTeX 0.16.11（MIT）、Marked 12.0.2（MIT），版本固定并存于 dist/vendor。许可证见 THIRD_PARTY_LICENSES.txt。没有分析追踪或外部 API，没有登录或数据库。
