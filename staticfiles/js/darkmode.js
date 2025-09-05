document.addEventListener("DOMContentLoaded", () => {
  const buttons = [
    document.getElementById("darkModeBtn"),
    document.getElementById("darkModeBtnMobile")
  ].filter(Boolean);

  const storageKey = "darkMode";

  const enableDarkMode = (save = true) => {
    document.body.classList.add("dark-mode");
    if (save) localStorage.setItem(storageKey, "enabled");
  };

  const disableDarkMode = (save = true) => {
    document.body.classList.remove("dark-mode");
    if (save) localStorage.setItem(storageKey, "disabled");
  };

  // Initialize
  const saved = localStorage.getItem(storageKey);
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

  if (saved === "enabled") enableDarkMode(false);
  else if (saved === "disabled") disableDarkMode(false);
  else if (prefersDark) enableDarkMode(false);
  else disableDarkMode(false);

  // Attach click to both buttons
  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      document.body.classList.contains("dark-mode") ? disableDarkMode(true) : enableDarkMode(true);
    });
  });
});
