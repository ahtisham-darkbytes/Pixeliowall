document.addEventListener("DOMContentLoaded", () => {
  const masonryGrid = document.getElementById("masonryGrid");

  const msnry = new Masonry(masonryGrid, {
    itemSelector: ".masonry-item",
    columnWidth: ".masonry-item",
    percentPosition: true,
    gutter: 16,
  });

  // Wait for images to load before layout
  imagesLoaded(masonryGrid, function () {
    msnry.layout();
  });

  // Bind download buttons (like buttons are handled inline)
  document.querySelectorAll(".download-btn").forEach((btn) => {
    btn.onclick = (e) => {
      e.stopPropagation();
      // Download functionality can be added here later
      console.log(`Downloading image ${btn.dataset.id}...`);
    };
  });
});
