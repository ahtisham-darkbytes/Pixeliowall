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

  // Bind like/download buttons
  document.querySelectorAll(".like-btn").forEach((btn) => {
    btn.onclick = (e) => {
      e.stopPropagation();
      alert(`Liked image ${btn.dataset.id}`);
    };
  });

  document.querySelectorAll(".download-btn").forEach((btn) => {
    btn.onclick = (e) => {
      e.stopPropagation();
      alert(`Downloading image ${btn.dataset.id}...`);
    };
  });
});
