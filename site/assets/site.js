document.querySelectorAll(".top-nav a").forEach((link) => {
  if (link.href === window.location.href) {
    link.style.background = "rgba(224, 194, 122, 0.14)";
  }
});
