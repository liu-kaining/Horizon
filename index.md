---
layout: default
title: Horizon
---

# Horizon

{% assign stats = site.data.stats %}

<div id="lang-zh" class="lang-section" markdown="1">

<div class="hz-home-hero" markdown="1">

每天自动帮你把“值得看”的信息挑出来：抓取 → 去重 → AI 评分 → 总结，生成中英双语速递。

</div>

<div class="hz-home-grid">
  <section class="hz-card">
    <h2>每日速递 <a class="rss-icon" href="{{ '/feed-zh.xml' | relative_url }}" aria-label="订阅中文"><svg viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M128.081 415.959c0 35.369-28.672 64.041-64.041 64.041S0 451.328 0 415.959s28.672-64.041 64.041-64.041 64.04 28.673 64.04 64.041zm175.66 47.25c-8.354-154.6-132.185-278.587-286.95-286.95C7.656 175.765 0 183.105 0 192.253v48.069c0 8.415 6.49 15.472 14.887 16.018 111.832 7.284 201.473 96.702 208.772 208.772.547 8.397 7.604 14.887 16.018 14.887h48.069c9.149.001 16.489-7.655 15.995-16.79zm144.249.288C439.596 229.677 251.465 40.445 16.503 32.01 7.473 31.686 0 38.981 0 48.016v48.068c0 8.625 6.835 15.645 15.453 15.999 191.179 7.839 344.627 161.316 352.465 352.465.353 8.618 7.373 15.453 15.999 15.453h48.068c9.034-.001 16.329-7.474 16.005-16.504z"/></svg></a></h2>
    <p class="hz-card-sub">直接看今天发生了什么（点日期进入）。</p>

    <div class="hz-search">
      <input id="hz-search-input-zh" class="hz-search-input" type="search" placeholder="搜：关键词 或 #标签（例：agent / OpenAI / #RAG）" autocomplete="off" />
      <p class="hz-search-hint">从历史速递里查你关心的主题；支持多个词，#标签可叠加筛选。</p>
      <div id="hz-search-results-zh" class="hz-search-results"></div>
    </div>

    <ul>
      {% assign zh_posts = site.posts | where: "lang", "zh" %}
      {% for post in zh_posts limit:20 %}
        <li><a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }}</a></li>
      {% else %}
        <li><em>暂无内容</em></li>
      {% endfor %}
    </ul>
  </section>

  <aside class="hz-card">
    <h2>覆盖情况</h2>
    <p class="hz-card-sub">一眼看“抓了多少、留下多少、最近更新”。</p>
    <div class="hz-stats">
      <div class="hz-stat">
        <span class="k">累计入选（重点）</span>
        <span class="v">{{ stats.total_articles | default: 0 }}</span>
      </div>
      <div class="hz-stat">
        <span class="k">累计抓取（全部）</span>
        <span class="v">{{ stats.total_fetched | default: 0 }}</span>
      </div>
      <div class="hz-stat">
        <span class="k">中文速递（累计）</span>
        <span class="v">{{ stats.total_digests_zh | default: zh_posts.size }}</span>
      </div>
      <div class="hz-stat">
        <span class="k">最近更新</span>
        <span class="v">{{ stats.last_digest_date | default: (zh_posts.first.date | date: "%Y-%m-%d") }}</span>
      </div>
    </div>

    {% if stats.total_articles == 0 and stats.total_fetched == 0 and zh_posts.size > 0 %}
    <p class="hz-card-sub">统计会在下一次 GitHub Actions 运行后自动更新（当前为占位数据）。</p>
    {% endif %}

    <div class="hz-home-links">
      <h3>怎么配置/扩展</h3>
      <ul>
        <li><a href="{{ '/configuration' | relative_url }}">配置指南</a></li>
        <li><a href="{{ '/scrapers' | relative_url }}">信息源采集器</a></li>
        <li><a href="{{ '/scoring' | relative_url }}">评分系统</a></li>
      </ul>
    </div>
  </aside>
</div>

</div>

<div id="lang-en" class="lang-section" markdown="1">

<div class="hz-home-hero" markdown="1">

Horizon picks what matters: fetch → dedupe → AI score → summarize, published as bilingual daily digests.

</div>

<div class="hz-home-grid">
  <section class="hz-card">
    <h2>Daily Digest <a class="rss-icon" href="{{ '/feed-en.xml' | relative_url }}" aria-label="Subscribe English"><svg viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M128.081 415.959c0 35.369-28.672 64.041-64.041 64.041S0 451.328 0 415.959s28.672-64.041 64.041-64.041 64.04 28.673 64.04 64.041zm175.66 47.25c-8.354-154.6-132.185-278.587-286.95-286.95C7.656 175.765 0 183.105 0 192.253v48.069c0 8.415 6.49 15.472 14.887 16.018 111.832 7.284 201.473 96.702 208.772 208.772.547 8.397 7.604 14.887 16.018 14.887h48.069c9.149.001 16.489-7.655 15.995-16.79zm144.249.288C439.596 229.677 251.465 40.445 16.503 32.01 7.473 31.686 0 38.981 0 48.016v48.068c0 8.625 6.835 15.645 15.453 15.999 191.179 7.839 344.627 161.316 352.465 352.465.353 8.618 7.373 15.453 15.999 15.453h48.068c9.034-.001 16.329-7.474 16.005-16.504z"/></svg></a></h2>
    <p class="hz-card-sub">Read what matters today (click a date).</p>

    <div class="hz-search">
      <input id="hz-search-input-en" class="hz-search-input" type="search" placeholder="Search keyword or #tag (e.g. agent / OpenAI / #RAG)" autocomplete="off" />
      <p class="hz-search-hint">Search across historical digests; combine keywords and #tags.</p>
      <div id="hz-search-results-en" class="hz-search-results"></div>
    </div>

    <ul>
      {% assign en_posts = site.posts | where: "lang", "en" %}
      {% for post in en_posts limit:20 %}
        <li><a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }}</a></li>
      {% else %}
        <li><em>No posts yet</em></li>
      {% endfor %}
    </ul>
  </section>

  <aside class="hz-card">
    <h2>Coverage</h2>
    <p class="hz-card-sub">At a glance: fetched, selected, and latest update.</p>
    <div class="hz-stats">
      <div class="hz-stat">
        <span class="k">Selected (important)</span>
        <span class="v">{{ stats.total_articles | default: 0 }}</span>
      </div>
      <div class="hz-stat">
        <span class="k">Fetched items</span>
        <span class="v">{{ stats.total_fetched | default: 0 }}</span>
      </div>
      <div class="hz-stat">
        <span class="k">Digests (EN)</span>
        <span class="v">{{ stats.total_digests_en | default: en_posts.size }}</span>
      </div>
      <div class="hz-stat">
        <span class="k">Latest</span>
        <span class="v">{{ stats.last_digest_date | default: (en_posts.first.date | date: "%Y-%m-%d") }}</span>
      </div>
    </div>

    {% if stats.total_articles == 0 and stats.total_fetched == 0 and en_posts.size > 0 %}
    <p class="hz-card-sub">Stats will update after the next GitHub Actions run (placeholder values for now).</p>
    {% endif %}

    <div class="hz-home-links">
      <h3>Configure / extend</h3>
      <ul>
        <li><a href="{{ '/configuration' | relative_url }}">Configuration Guide</a></li>
        <li><a href="{{ '/scrapers' | relative_url }}">Source Scrapers</a></li>
        <li><a href="{{ '/scoring' | relative_url }}">Scoring System</a></li>
      </ul>
    </div>
  </aside>
</div>

</div>
