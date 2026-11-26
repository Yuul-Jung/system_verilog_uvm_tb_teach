/*
 * 교육용 HTML 공통 동작 — 유지보수용 원본 (STANDARD 4·10.3·10.4)
 * 페이지 본문은 바꾸지 않고 탐색·이전/다음·모바일 메뉴·코드 복사만 덧붙인다.
 * 입력: 페이지의 window.COURSE (tools/guide/build_guides.py가 실제 존재하는 장만 넣음),
 *       body[data-chapter], main section[id] > h2.
 * 이관 원본과 구문 트리(acorn AST)가 같음을 확인함.
 */
(async () => {
  "use strict";
  // (추가) 긴 신호명·파일명을 가진 표는 모바일에서 표 안에서만 스크롤한다.
  document.querySelectorAll("main table").forEach((table) => {
    if (table.parentElement.classList.contains("table-wrap")) return;
    const wrapper = document.createElement("div");
    wrapper.className = "table-wrap";
    wrapper.tabIndex = 0;
    wrapper.setAttribute("role", "region");
    wrapper.setAttribute("aria-label", "표 가로 스크롤");
    table.before(wrapper);
    wrapper.append(table);
  });
  // (변경) 과정 목차는 course.json을 우선 사용한다. 오프라인에서도 현재 발행본을 탐색할 수 있도록 스냅샷을 보존한다.
  const fallback = window.COURSE || {
  "title": "RTL · SystemVerilog · UVM 교수용 해설서",
  "short_title": "SV UVM TEACH",
  "home_label": "전체 교수용 해설서",
  "chapters": [
    {
      "id": "ch01",
      "number": 1,
      "title": "테스트벤치의 첫 실행",
      "file": "ch01_teacher_v02.html"
    },
    {
      "id": "ch02",
      "number": 2,
      "title": "Clock·Reset·이벤트",
      "file": "ch02_teacher_v01.html"
    },
    {
      "id": "ch03",
      "number": 3,
      "title": "반복 자극과 작업 분리",
      "file": "ch03_teacher_v01.html"
    }
  ]
};
  let data = fallback;
  if (location.protocol === "https:" || location.protocol === "http:") {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 2500);
    try {
      const response = await fetch("course.json", { cache: "no-cache", signal: controller.signal });
      if (!response.ok) throw new Error("course.json HTTP " + response.status);
      const manifest = await response.json();
      if (!Array.isArray(manifest.chapters) || manifest.chapters.length < 1 || manifest.chapters.length > 24 ||
          !manifest.chapters.every((ch, i) =>
            ch.number === i + 1 && ch.id === "ch" + String(i + 1).padStart(2, "0") &&
            typeof ch.title === "string" &&
            /^ch[0-9]{2}_[a-z0-9_]+$/.test(ch.slug) &&
            /^v[0-9]+$/.test(ch.version))) throw new Error("Invalid course manifest");
      data = { ...fallback, chapters: manifest.chapters.map(ch => ({
        id: ch.id, number: ch.number, title: ch.title,
        file: ch.slug + "_" + ch.version + ".html"
      })) };
    } catch (_) {
      // 네트워크 또는 매니페스트 오류 시 검증된 발행 스냅샷을 사용한다.
    } finally {
      clearTimeout(timer);
    }
  }
  const nav = document.getElementById("course-nav");
  if (!nav) return;
  const current = document.body.dataset.chapter || "";
  const pageNames = data.chapters || [];
  // (추가) 6부 × 4장의 상하 체계: 각 장은 오직 한 부에 소속된다.
  // 이 과정의 교육과정(CURRICULUM.md)과 명칭·범위를 일치시킨다.
  const parts = [
    { number: 1, start: 1, end: 4, title: "Verilog 테스트벤치 기초" },
    { number: 2, start: 5, end: 8, title: "SystemVerilog 문법" },
    { number: 3, start: 9, end: 12, title: "자동 검증·속성·커버리지" },
    { number: 4, start: 13, end: 16, title: "인터페이스·연산기 검증" },
    { number: 5, start: 17, end: 20, title: "UVM 검증 환경" },
    { number: 6, start: 21, end: 24, title: "실무 회귀 검증" },
  ];
  const partOf = (ch) => parts.find((part) => {
    const number = Number(ch?.number);
    return Number.isFinite(number) &&
      number >= part.start && number <= part.end;
  }) || null;
  const activeChapter = pageNames.find((ch) => ch.id === current) || null;
  const currentPart = partOf(activeChapter);
  // 1. 좌측 탐색 (STANDARD 4.1 — 기준: ai-agent-engineering)
  //    과정 머리글 → 전체 학습 안내서(INDEX) → 접이식 '전체 장 바로가기' → 현재 쪽 세부 목차
  const el = (tag, cls, text) => {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined) e.textContent = text;
    return e;
  };
  const numText = (n) => String(n).padStart(2, "0");
  const mainCount = pageNames.filter((ch) => !String(ch.number).includes(".")).length;
  const header = el("div", "course-nav-header");
  header.append(el("span", "", data.short_title || data.title), el("span", "", mainCount + " CHAPTERS"));
  nav.append(header);
  const home = el("a", "course-nav-home", "⌂  " + (data.home_label || "전체 학습 안내서"));
  home.href = "index.html";
  if (!current || !pageNames.some((ch) => ch.id === current)) home.setAttribute("aria-current", "page");
  nav.append(home);
  // (추가) PART를 상위 제목으로 한 번만 표시한다.
  // INDEX에서는 현재 부가 없으므로 전체 과정이라는 단일 제목을 표시한다.
  const partHeader = el("h2", "course-part-heading");
  partHeader.append(
    el("span", "course-part-code", currentPart
      ? "PART " + numText(currentPart.number) : "ALL 6 PARTS"),
    el("span", "course-part-name", currentPart
      ? currentPart.title : "전체 교육과정")
  );
  nav.append(partHeader);
  const box = el("details", "course-chapters");
  box.open = true;
  box.append(el("summary", "", currentPart
    ? "장 목록 · " + pageNames.filter((ch) =>
        partOf(ch)?.number === currentPart.number).length + "장"
    : "전체 장 바로가기"));
  const chLinks = el("div", "course-ch-links");
  let currentChapter = null;
  let activeChapterLink = null;
  // 보조 장(07.1·12.3 등)은 같은 본 장을 보고 있을 때만 펼쳐 목록을 짧게 유지
  const baseOf = (n) => String(n).split(".")[0];
  const curBase = baseOf(pageNames.find((ch) => ch.id === current)?.number ?? "");
  pageNames.forEach((ch) => {
    // (변경) 개별 장에서는 해당 PART의 장들만 보여 준다.
    if (currentPart && partOf(ch)?.number !== currentPart.number) return;
    if (String(ch.number).includes(".") && baseOf(ch.number) !== curBase) return;
    const a = el("a", "course-ch-link");
    a.href = ch.file;
    a.append(el("span", "course-ch-num", numText(ch.number)), el("span", "", ch.title));
    if (ch.id === current) {
      a.setAttribute("aria-current", "page");
      currentChapter = ch;
      activeChapterLink = a;
    }
    chLinks.append(a);
  });
  box.append(chLinks);
  nav.append(box);

  // 2. 현재 쪽 세부 목차: 절 제목(h2)을 번호·제목으로 나눠 표시하고, 화면에 보이는 절을 강조
  const sections = [...document.querySelectorAll("main section[id]")];
  if (sections.length) {
    const sub = el("ol", currentChapter
      ? "toc-sections course-nested-sections" : "toc-sections");
    if (currentChapter && activeChapterLink) {
      // (변경) SECTION은 현재 CHAPTER의 바로 아래에 들여써 표시한다.
      const heading = el("div", "course-toc-heading", "제" + numText(currentChapter.number) + "장 세부 목차");
      activeChapterLink.after(heading, sub);
    } else {
      // INDEX에는 장이 없으므로 INDEX 자체의 절 목차를 표시한다.
      nav.append(el("div", "course-toc-heading", "INDEX 목차"));
      nav.append(sub);
    }
    sections.forEach((sec) => {
      const li = el("li"),
        a = el("a");
      const h2 = sec.querySelector("h2");
      const num = h2?.querySelector(".num")?.textContent.trim() || "";
      let text = h2?.textContent.trim().replace(/\s+/g, " ") || sec.id;
      if (num && text.startsWith(num)) text = text.slice(num.length).trim();
      a.href = "#" + sec.id;
      a.append(el("span", "n", num || "·"), el("span", "", text));
      li.append(a);
      sub.append(li);
    });
    const items = [...sub.querySelectorAll("a")];
    const mark = (id) =>
      items.forEach((x) => {
        const on = x.getAttribute("href") === "#" + id;
        x.classList.toggle("active", on);
        if (on) x.setAttribute("aria-current", "location");
        else x.removeAttribute("aria-current");
      });
    let ticking = false;
    const sync = () => {
      ticking = false;
      const limit = Math.min(180, innerHeight * 0.28);
      let best = sections[0];
      sections.forEach((x) => {
        if (x.getBoundingClientRect().top <= limit) best = x;
      });
      mark(best.id);
    };
    addEventListener("scroll", () => {
      if (!ticking) {
        ticking = true;
        requestAnimationFrame(sync);
      }
    }, { passive: true });
    sync();
  }

  // 3. 본문 끝 이전/다음 장 링크 (처음·마지막 장은 전체 목차로)
  const idx = pageNames.findIndex((ch) => ch.id === current);
  const links = document.getElementById("chapter-links");
  if (links && idx >= 0) {
    const prev = pageNames[idx - 1],
      next = pageNames[idx + 1];
    const add = (ch, label) => {
      let a = document.createElement("a");
      a.href = ch?.file || "index.html";
      a.textContent = label + (ch ? " · " + ch.title : " · 전체 목차");
      links.append(a);
    };
    add(prev, "← 이전");
    add(next, "다음 →");
  }

  // 4. 모바일 서랍 메뉴: 버튼·덮개 클릭, 링크 선택, Escape 키로 닫기
  const toggle = document.getElementById("mobile-menu"),
    shade = document.getElementById("shade");
  const close = () => {
    nav.classList.remove("open");
    shade?.classList.remove("open");
    toggle?.setAttribute("aria-expanded", "false");
  };
  toggle?.addEventListener("click", () => {
    let open = !nav.classList.contains("open");
    nav.classList.toggle("open", open);
    shade?.classList.toggle("open", open);
    toggle.setAttribute("aria-expanded", String(open));
  });
  shade?.addEventListener("click", close);
  nav.addEventListener("click", (e) => {
    if (e.target.closest("a")) close();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") close();
  });

  // 5. 코드 박스 복사 버튼: pre의 소스 텍스트만 복사 (제목 줄 제외)
  document.querySelectorAll(".codeblock").forEach((block) => {
    const pre = block.querySelector("pre");
    if (!pre) return;
    const bar = block.querySelector(".codebar");
    if (!bar) return;
    const b = document.createElement("button");
    b.type = "button";
    b.textContent = "복사";
    b.setAttribute("aria-label", "코드 복사");
    b.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(pre.textContent);
        b.textContent = "복사 완료";
        setTimeout(() => (b.textContent = "복사"), 1200);
      } catch {
        b.textContent = "복사 실패";
      }
    });
    bar.append(b);
  });
})();
