// Mobile Menu
document.addEventListener("DOMContentLoaded", function () {
  const mobileMenuBtn = document.getElementById("mobileMenuBtn");
  const mobileMenu = document.getElementById("mobileMenu");

  if (mobileMenuBtn && mobileMenu) {
    function toggleMobileMenu() {
      mobileMenu.classList.toggle("active");
      mobileMenuBtn.classList.toggle("active");
      document.body.classList.toggle("no-scroll");
    }

    // Open/close with button
    mobileMenuBtn.addEventListener("click", toggleMobileMenu);

    // Close on nav link click
    document.querySelectorAll(".mobile-nav .nav-link").forEach((link) => {
      link.addEventListener("click", () => {
        mobileMenu.classList.remove("active");
        mobileMenuBtn.classList.remove("active");
        document.body.classList.remove("no-scroll");
      });
    });

    // Close on outside click
    document.addEventListener("click", (event) => {
      if (
        mobileMenu.classList.contains("active") &&
        !mobileMenu.contains(event.target) &&
        !mobileMenuBtn.contains(event.target)
      ) {
        toggleMobileMenu();
      }
    });
  }
});
