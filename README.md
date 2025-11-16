## 基于Django的博客系统

基于Django框架的博客网站，毕业设计、课程设计、网站设计。<font color="red">联系微信：YCK2050</font>

### 1、技术版本

- Python==3.10
- Django==4.2.6
- Bootstrap==5.2
- Jquery==3.6.3

### 2、功能要点

- `article`（文章管理）
- `category`（分类管理）
- `comment`（评论管理）
- `userprofile`（用户管理）
- `password_reset`（密码重置）

### 3、技术要点

 ✔ Django ORM 模型定义
 ✔ 富文本内容（可能集成 markdown）
 ✔ 文件上传（若有封面图片）
 ✔ 分页 Pagination
 ✔ CreateView / UpdateView 基于函数或类视图
 ✔ slug / id 文章详情页映射
 ✔ 登录用户才能发布（使用 login_required）

 ✔ 评论展示（按时间排序）
 ✔ 可能包含楼中楼回复

 ✔ Django 内置用户扩展（OneToOne）
 ✔ 注册、登录、退出
 ✔ 修改个人资料（头像、简介）
 ✔ Django Auth 完整套件

### 4、总结分析

本博客系统基于 Python 3.10 与 Django Web 框架开发，采用 MTV 架构模式，将业务逻辑、数据模型与模板渲染有效分离，结构清晰、扩展性强。整个项目共划分为多个功能模块，包括文章系统、分类系统、评论系统、用户系统以及密码找回模块，各模块之间通过 Django 的 URL 分发、模型关联与模板继承机制进行协作，整体架构合理规范。

在技术实现上，项目充分利用了 Django 提供的 ORM、Admin 后台、Auth 用户系统、表单验证、模板系统等核心特性，实现了从文章发布、分类归档、评论交互到用户登录与权限控制的一整套博客业务逻辑。同时，系统通过 ModelForm 与分页、文件上传、登录限制、中间件等技术增强了实际功能的实用性与安全性。

数据库设计方面，文章、评论、分类、用户之间采用一对多与多对一关系建模，数据结构清晰，可维护性强。前端基于 Django Template 实现页面展示，并保持模板复用，提升开发效率。

总体来看，该项目完整实现了一个轻量级博客的核心功能，代码结构规范，模块划分清晰，符合 Django 开发标准，具有良好的学习与扩展价值，例如可以进一步加入标签系统、Markdown 编辑器、前后端分离等功能。

### 5、功能展示

#### 博客列表

![screencapture-127-0-0-1-8000-2025-11-16-15_55_40](https://raw.githubusercontent.com/rongdisun/learn/main/img/screencapture-127-0-0-1-8000-2025-11-16-15_55_40.png)

#### 博客详情

![screencapture-127-0-0-1-8000-article-detail-8-2025-11-16-15_56_17](https://raw.githubusercontent.com/rongdisun/learn/main/img/screencapture-127-0-0-1-8000-article-detail-8-2025-11-16-15_56_17.png)

#### 搜索博客

![screencapture-127-0-0-1-8000-search-article-2025-11-16-15_58_39](https://raw.githubusercontent.com/rongdisun/learn/main/img/screencapture-127-0-0-1-8000-search-article-2025-11-16-15_58_39.png)

#### 发布博客

![screencapture-127-0-0-1-8000-publish-article-2025-11-16-15_57_57](https://raw.githubusercontent.com/rongdisun/learn/main/img/screencapture-127-0-0-1-8000-publish-article-2025-11-16-15_57_57.png)

#### 数据分析

![screencapture-127-0-0-1-8000-data-analysis-chart-view-2025-11-16-15_56_34](https://raw.githubusercontent.com/rongdisun/learn/main/img/screencapture-127-0-0-1-8000-data-analysis-chart-view-2025-11-16-15_56_34.png)

#### 个人信息

![Snipaste_2025-11-16_15-59-28](https://raw.githubusercontent.com/rongdisun/learn/main/img/Snipaste_2025-11-16_15-59-28.png)

#### 修改密码

![Snipaste_2025-11-16_15-59-39](https://raw.githubusercontent.com/rongdisun/learn/main/img/Snipaste_2025-11-16_15-59-39.png)

#### 后台管理页面

![image-20251116174735643](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20251116174735643.png)

### 获取源码

![image-20251116175139656](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20251116175139656.png)