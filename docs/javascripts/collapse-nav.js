/* Collapse all sidebar nav sections on initial load for MkDocs Material */
(function () {
  function collapseNav() {
    try {
      var sidebar = document.querySelector(".md-sidebar .md-nav");
      if (!sidebar) return;
      var toggles = sidebar.querySelectorAll("input.md-nav__toggle");
      toggles.forEach(function (toggle) {
        if (toggle.checked) toggle.checked = false;
      });
    } catch (e) {
      /* no-op */
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", collapseNav);
  } else {
    collapseNav();
  }

  /* Re-apply on client-side navigations (instant loading) */
  document.addEventListener("DOMContentLoaded", function () {
    var observer = new MutationObserver(function () {
      collapseNav();
    });
    observer.observe(document.body, { childList: true, subtree: true });
  });
})();


