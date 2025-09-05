// masonry_gallery.js

// --- State ---
const likedImages = new Set();
const masonryGrid = document.getElementById("masonryGrid");
let itemsPerLoad = 6;
let currentIndex = 0;
let isLoading = false;
let msnry;

// --- Create card ---
function createImageElement(image) {
  const div = document.createElement("div");
  div.className = "masonry-item";
  div.innerHTML = `
    <a href="/image-detail/?id=${image.id}">
      <img src="${image.src}" alt="${image.alt}" loading="lazy">
      ${image.price > 0 ? `<div class="price-banner">$${image.price}</div>` : ""}
      ${image.description ? `<div class="image-description">${image.description}</div>` : ""}
      <div class="image-overlay">
        <div class="overlay-content">
          <div class="photographer">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="7" r="4"></circle>
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
            </svg>
            <span>${image.photographer}</span>
          </div>
          <div class="image-actions">
            <button class="action-btn like-btn" data-id="${image.id}">
              <i class="fa-regular fa-heart"></i>
            </button>
            <button class="action-btn download-btn" data-id="${image.id}">
              <i class="fa-solid fa-download"></i>
            </button>
          </div>
        </div>
      </div>
    </a>
  `;
  return div;
}

// --- Load images ---
function loadImages() {
  if (isLoading) return;
  if (currentIndex >= sampleImages.length) return;

  isLoading = true;
  showLoader();

  setTimeout(() => {
    const nextBatch = sampleImages.slice(currentIndex, currentIndex + itemsPerLoad);
    const elements = [];

    nextBatch.forEach((img) => {
      const el = createImageElement(img);
      masonryGrid.appendChild(el);
      elements.push(el);
    });

    // Wait for images to load before appending to Masonry
    imagesLoaded(elements, function() {
      msnry.appended(elements);
      msnry.layout();

      // Re-bind actions
      document.querySelectorAll(".like-btn").forEach((btn) => {
        btn.onclick = (e) => {
          e.stopPropagation();
          const id = +btn.dataset.id;
          toggleLike(id);
        };
      });
      document.querySelectorAll(".download-btn").forEach((btn) => {
        btn.onclick = (e) => {
          e.stopPropagation();
          alert(`Downloading image ${btn.dataset.id}...`);
        };
      });

      currentIndex += itemsPerLoad;
      hideLoader();
      isLoading = false;
    });

  }, 800); // fake delay
}

// --- Like toggle ---
function toggleLike(id) {
  likedImages.has(id) ? likedImages.delete(id) : likedImages.add(id);
  masonryGrid.innerHTML = "";
  currentIndex = 0;

  msnry.destroy();
  msnry = new Masonry(masonryGrid, {
    itemSelector: ".masonry-item",
    columnWidth: ".masonry-item",
    percentPosition: true,
    gutter: 16,
  });

  loadImages();
}

// --- Loader ---
function showLoader() { document.getElementById("loader").style.display = "flex"; }
function hideLoader() { document.getElementById("loader").style.display = "none"; }

// --- Infinite scroll ---
window.addEventListener("scroll", () => {
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 200) {
    loadImages();
  }
});

// --- Init ---
document.addEventListener("DOMContentLoaded", () => {
  msnry = new Masonry(masonryGrid, {
    itemSelector: ".masonry-item",
    columnWidth: ".masonry-item",
    percentPosition: true,
    gutter: 16,
  });

  loadImages();
});
