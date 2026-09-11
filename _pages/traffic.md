---
layout: single
title: "Page View Tracker"
permalink: /traffic/
author_profile: false
---

This page tracks the number of views for each page on this site.

**Total views across tracked pages:** <span id="tracker-total">…</span>

<table id="tracker-table" style="width: 100%; margin-top: 1.5rem;">
    <thead>
        <tr><th style="text-align: left;">Page</th><th style="text-align: right;">Views</th></tr>
    </thead>
    <tbody id="tracker-rows">
        <tr><td colspan="2">Loading…</td></tr>
    </tbody>
</table>

<script>
    (function () {
        var NS = "panyidong.github.io";
        var API = "https://abacus.jasoncameron.dev";
        var PAGES = [
            {% for p in site.html_pages %}{ "url": {{ p.url | jsonify }}, "title": {{ p.title | default: p.url | jsonify }} },{% endfor %}
            {% for p in site.publications %}{ "url": {{ p.url | jsonify }}, "title": {{ p.title | default: p.url | jsonify }} },{% endfor %}
            {% for p in site.talks %}{ "url": {{ p.url | jsonify }}, "title": {{ p.title | default: p.url | jsonify }} },{% endfor %}
            {% for p in site.portfolio %}{ "url": {{ p.url | jsonify }}, "title": {{ p.title | default: p.url | jsonify }} },{% endfor %}
            {% for p in site.posts %}{ "url": {{ p.url | jsonify }}, "title": {{ p.title | default: p.url | jsonify }} },{% endfor %}
        ];
        var BLACKLIST = /404|archive|tag|category|terms|markdown|sitemap|feed|search|non-menu|cv-json|about|\.xml|\.json/;

        function keyFor(url) {
            return url.replace(/[^a-zA-Z0-9-]/g, "") || "home";
        }

        var seen = {}, rows = [];
        PAGES.forEach(function (p) {
            if (BLACKLIST.test(p.url) || seen[p.url] || p.title === p.url) return;
            seen[p.url] = true;
            rows.push(p);
        });

        var tbody = document.getElementById("tracker-rows");
        var totalEl = document.getElementById("tracker-total");
        var total = 0, loaded = 0;
        tbody.innerHTML = "";

        rows.forEach(function (p) {
            var tr = document.createElement("tr");
            var td1 = document.createElement("td");
            var a = document.createElement("a");
            a.href = p.url;
            a.textContent = p.title;
            td1.appendChild(a);
            var td2 = document.createElement("td");
            td2.style.textAlign = "right";
            td2.textContent = "…";
            tr.appendChild(td1);
            tr.appendChild(td2);
            tbody.appendChild(tr);
            p.tr = tr;
            p.cell = td2;
        });

        var i = 0;
        function next() {
            if (i >= rows.length) {
                var sorted = rows.slice().sort(function (a, b) { return (b.value || 0) - (a.value || 0); });
                tbody.innerHTML = "";
                sorted.forEach(function (p) { tbody.appendChild(p.tr); });
                return;
            }
            var p = rows[i]; i += 1;
            fetch(API + "/get/" + NS + "/" + keyFor(p.url), { cache: "no-store" })
                .then(function (r) { return r.ok ? r.json() : { value: 0 }; })
                .then(function (d) {
                    p.value = (typeof d.value === "number" && d.value > 0) ? d.value : 0;
                    p.cell.textContent = p.value.toLocaleString();
                    total += p.value;
                    loaded += 1;
                    if (loaded === rows.length) totalEl.textContent = total.toLocaleString();
                })
                .catch(function () { p.cell.textContent = "n/a"; })
                .finally(function () { setTimeout(next, 450); });
        }
        next();
    })();
</script>