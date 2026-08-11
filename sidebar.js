/* =========================================================
   StudyplanAI — Shared Sidebar Navigation
   Include on every page with: <script src="sidebar.js"></script>
   Injects a hamburger button + slide-in drawer nav.
   ========================================================= */
(function(){

  const NAV_ITEMS = [
    { icon:"🏠", label:"Home", href:"index.html" },
    { icon:"🚀", label:"Practice", href:"practice.html" },
    { icon:"✨", label:"AI Test Generator", href:"test-generator.html" },
    { icon:"📝", label:"Mock Test", href:"mocktest.html" },
    { icon:"📊", label:"Stats", href:"stats.html" },
    { icon:"🎯", label:"Score Predictor", href:"predictor.html" },
    { icon:"🏆", label:"Leaderboard", href:"leaderboard.html" },
    { icon:"📚", label:"Courses", href:"coming-soon.html?f=Courses", soon:true },
    { icon:"⚔️", label:"Arena", href:"coming-soon.html?f=Arena", soon:true },
    { icon:"👪", label:"Parent's Dashboard", href:"coming-soon.html?f=Parent%27s%20Dashboard", soon:true },
    { icon:"📣", label:"Buzz Board", href:"buzzboard.html" },
    { icon:"🎁", label:"Refer & Earn", href:"refer.html" },
    { icon:"💬", label:"Support", href:"support.html" },
    { icon:"⭐", label:"Membership", href:"studyplanai-membership.html", highlight:true },
  ];

  const styleTag = document.createElement("style");
  styleTag.textContent = `
    .spai-menu-btn{
      position:fixed; top:14px; left:14px; z-index:100;
      width:38px; height:38px; border-radius:10px;
      background:var(--surface,#141b26); border:1px solid var(--line,#28323f);
      display:flex; align-items:center; justify-content:center; cursor:pointer;
    }
    .spai-menu-btn svg{width:19px; height:19px; color:var(--text,#e9edf3);}
    .spai-overlay{
      position:fixed; inset:0; background:rgba(0,0,0,.55); z-index:198;
      opacity:0; pointer-events:none; transition:opacity .2s;
    }
    .spai-overlay.open{opacity:1; pointer-events:auto;}
    .spai-drawer{
      position:fixed; top:0; left:0; bottom:0; width:270px; max-width:82vw; z-index:199;
      background:var(--surface,#141b26); border-right:1px solid var(--line,#28323f);
      transform:translateX(-100%); transition:transform .22s ease; overflow-y:auto;
      font-family:'Inter',system-ui,sans-serif; padding-bottom:24px;
    }
    .spai-drawer.open{transform:translateX(0);}
    .spai-drawer-head{
      padding:20px 18px 16px; border-bottom:1px solid var(--line,#28323f);
      font-family:'Source Serif 4',serif; font-weight:600; font-size:17px; color:var(--text,#e9edf3);
    }
    .spai-drawer-head em{font-style:normal; color:var(--phy,#6b9fdb);}
    .spai-drawer-close{
      position:absolute; top:16px; right:14px; width:28px; height:28px; border-radius:50%;
      background:var(--surface-2,#1c2531); border:1px solid var(--line,#28323f);
      display:flex; align-items:center; justify-content:center; cursor:pointer;
    }
    .spai-drawer-close svg{width:13px; height:13px; color:var(--text-dim,#8d99a8);}
    .spai-nav-list{padding:8px 0;}
    .spai-nav-item{
      display:flex; align-items:center; gap:12px; padding:12px 18px;
      color:var(--text,#e9edf3); font-size:14px; font-weight:500; text-decoration:none;
      border-left:3px solid transparent;
    }
    .spai-nav-item:active{background:var(--surface-2,#1c2531);}
    .spai-nav-item.current{border-left-color:var(--phy,#6b9fdb); background:var(--surface-2,#1c2531);}
    .spai-nav-item .ic{font-size:16px; width:20px; text-align:center; flex-shrink:0;}
    .spai-nav-item .soon-tag{
      margin-left:auto; font-family:'JetBrains Mono',monospace; font-size:9px;
      color:var(--text-faint,#5d6a7a); background:var(--surface-3,#232e3c);
      padding:2px 6px; border-radius:5px; text-transform:uppercase;
    }
    .spai-nav-item.highlight{color:#d99a5c; font-weight:700;}
    body{padding-top:0;}
  `;
  document.head.appendChild(styleTag);

  const currentPage = location.pathname.split("/").pop() || "index.html";

  const itemsHtml = NAV_ITEMS.map(item => {
    const isCurrent = currentPage === item.href.split("?")[0];
    return `<a class="spai-nav-item${isCurrent ? " current" : ""}${item.highlight ? " highlight" : ""}" href="${item.href}">
      <span class="ic">${item.icon}</span><span>${item.label}</span>
      ${item.soon ? '<span class="soon-tag">Soon</span>' : ""}
    </a>`;
  }).join("");

  const drawer = document.createElement("div");
  drawer.className = "spai-drawer";
  drawer.id = "spaiDrawer";
  drawer.innerHTML = `
    <div class="spai-drawer-head">
      Studyplan<em>AI</em>
      <div class="spai-drawer-close" id="spaiClose">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>
      </div>
    </div>
    <div class="spai-nav-list">${itemsHtml}</div>
  `;

  const overlay = document.createElement("div");
  overlay.className = "spai-overlay";
  overlay.id = "spaiOverlay";

  const menuBtn = document.createElement("div");
  menuBtn.className = "spai-menu-btn";
  menuBtn.id = "spaiMenuBtn";
  menuBtn.innerHTML = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg>`;

  document.body.appendChild(overlay);
  document.body.appendChild(drawer);
  document.body.appendChild(menuBtn);

  function openDrawer(){ drawer.classList.add("open"); overlay.classList.add("open"); }
  function closeDrawer(){ drawer.classList.remove("open"); overlay.classList.remove("open"); }

  menuBtn.addEventListener("click", openDrawer);
  overlay.addEventListener("click", closeDrawer);
  document.getElementById("spaiClose").addEventListener("click", closeDrawer);

})();
