function renderImageDetail() {
  console.log("renderImageDetail called"); // check if script runs

  const params = new URLSearchParams(window.location.search);
  const id = parseInt(params.get("id"));
  const container = document.getElementById("imageDetail");
  const loader = document.getElementById("loader");

  if (!window.sampleImages || !container) {
    console.error("sampleImages not loaded or container missing");
    return;
  }

  const image = sampleImages.find(img => img.id == id);

  if (image) {
    const isFree = image.price === 0;

    container.innerHTML = `
      <div class="detail-card">
        <div class="detail-image">
          <img src="${image.src}" alt="${image.alt}">
        </div>
        <div class="detail-info">
          <h2>${image.alt}</h2>
          <p><strong>Photographer:</strong> ${image.photographer}</p>
          <p><strong>Price:</strong> ${isFree ? "Free" : "$" + image.price}</p>
          <p class="detail-desc">${image.description}</p>
          <div class="detail-actions">
            ${
              isFree
                ? `<button class="btn-action download-btn"><i class="fa-solid fa-download"></i> Download</button>`
                : `<button class="btn-action download-btn"><i class="fa-solid fa-cart-shopping"></i> Buy Now</button>`
            }
            <button class="btn-action favorite-btn" data-id="${image.id}">
              <i class="fa-regular fa-heart"></i> Add to Favorites
            </button>
          </div>
        </div>
      </div>
    `;
  } else {
    container.innerHTML = "<p>Image not found</p>";
  }

  if (loader) loader.style.display = "none";
  container.style.display = "block";
}

// Wait until sampleImages is loaded
const waitForSampleImages = setInterval(() => {
  if (window.sampleImages) {
    clearInterval(waitForSampleImages);
    renderImageDetail();
  }
}, 50);
