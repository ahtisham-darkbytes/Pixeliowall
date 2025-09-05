// Images -- sample data
const sampleImages = [
  {
    id: 1,
    src: "/static/images/travel.webp",
    photographer: "John Doe",
    alt: "Mountain landscape",
    price: 10,
    description:
      "A breathtaking mountain landscape with peaks bathed in sunlight, perfect for adventure and nature lovers.",
  },
  {
    id: 2,
    src: "/static/images/7.webp",
    photographer: "Jane Smith",
    alt: "Nature scene",
    price: 0,
    description:
      "A peaceful nature scene with lush greenery, evoking calm and tranquility.",
  },
  {
    id: 3,
    src: "/static/images/8.webp",
    photographer: "Mike Johnson",
    alt: "Ocean waves",
    price: 5,
    description:
      "Gentle ocean waves rolling onto the shore under a bright, clear sky.",
  },
  {
    id: 4,
    src: "/static/images/9.webp",
    photographer: "Sarah Wilson",
    alt: "Forest trees",
    price: 0,
    description:
      "A dense forest with towering trees, showcasing the beauty and serenity of nature.",
  },
  {
    id: 5,
    src: "/static/images/5.webp",
    photographer: "David Brown",
    alt: "Sunset sky",
    price: 10,
    description:
      "A vivid sunset sky painting the horizon with warm, mesmerizing colors.",
  },
  {
    id: 6,
    src: "/static/images/22.webp",
    photographer: "Emma Davis",
    alt: "Coffee cup",
    price: 0,
    description:
      "A cozy coffee cup scene, perfect for calm mornings and quiet moments.",
  },
  {
    id: 7,
    src: "/static/images/ocean-waves.webp",
    photographer: "Alex Miller",
    alt: "Street photography",
    price: 0,
    description:
      "Street photography capturing candid moments of daily life in the city.",
  },
  {
    id: 8,
    src: "/static/images/flowers-bloom.webp",
    photographer: "Lisa Garcia",
    alt: "Flowers bloom",
    price: 0,
    description:
      "Bright flowers in full bloom, celebrating the beauty and vibrancy of nature.",
  },
  {
    id: 9,
    src: "/static/images/portrait-woman.webp",
    photographer: "Nina Rodriguez",
    alt: "Portrait woman",
    price: 6,
    description:
      "A striking portrait of a woman with a captivating expression.",
  },
  {
    id: 10,
    src: "/static/images/abstract-composition.webp",
    photographer: "Tom Anderson",
    alt: "Abstract art",
    price: 0,
    description:
      "A colorful abstract art composition full of creativity and imagination.",
  },
  {
    id: 11,
    src: "/static/images/beach-sunset.webp",
    photographer: "Chris Taylor",
    alt: "Beach sunset",
    price: 0,
    description:
      "A tranquil beach sunset with soft waves reflecting the golden sky.",
  },
  {
    id: 12,
    src: "/static/images/urban-night.webp",
    photographer: "Maya Patel",
    alt: "Urban night",
    price: 9,
    description:
      "A vibrant cityscape at night, full of lights and urban energy.",
  },
  {
    id: 13,
    src: "/static/images/chess.webp",
    photographer: "Alex Haules",
    alt: "Chess board",
    price: 0,
    description:
      "A detailed chessboard ready for a strategic and thoughtful game.",
  },
  {
    id: 14,
    src: "/static/images/cat.webp",
    photographer: "Efrem Efre",
    alt: "Cat",
    price: 0,
    description: "A charming cat captured in a playful and curious pose.",
  },
  {
    id: 15,
    src: "/static/images/girl.webp",
    photographer: "Efrem Efre",
    alt: "Girl portrait",
    price: 0,
    description:
      "A portrait of a young girl with expressive eyes and personality.",
  },
  {
    id: 16,
    src: "/static/images/bird.webp",
    photographer: "Efrem Efre",
    alt: "Bird",
    price: 0,
    description:
      "A bird perched gracefully, highlighting the beauty of wildlife.",
  },
  {
    id: 17,
    src: "/static/images/light_baloon.webp",
    photographer: "Efrem Efre",
    alt: "Light balloon",
    price: 0,
    description:
      "A glowing light balloon floating in the evening, creating a magical atmosphere.",
  },
  {
    id: 18,
    src: "/static/images/nursery.webp",
    photographer: "Efrem Efre",
    alt: "Nursery",
    price: 0,
    description:
      "A colorful nursery filled with playful elements and a warm, inviting ambiance.",
  },
  {
    id: 19,
    src: "/static/images/parrot.webp",
    photographer: "Efrem Efre",
    alt: "Parrot",
    price: 0,
    description:
      "A vibrant parrot perched gracefully, showcasing its vivid feathers.",
  },
  {
    id: 20,
    src: "/static/images/station.webp",
    photographer: "Efrem Efre",
    alt: "Station",
    price: 0,
    description:
      "A busy station capturing the hustle and bustle of daily commuters.",
  },
  {
    id: 21,
    src: "/static/images/tree.webp",
    photographer: "Efrem Efre",
    alt: "Tree",
    price: 0,
    description: "A solitary tree standing tall in a peaceful, open landscape.",
  },
  {
    id: 22,
    src: "/static/images/tram.webp",
    photographer: "Efrem Efre",
    alt: "Tram",
    price: 0,
    description:
      "A tram moving through city streets, illustrating the rhythm of urban life.",
  },
  {
    id: 23,
    src: "/static/images/art.webp",
    photographer: "Efrem Efre",
    alt: "Art",
    price: 0,
    description:
      "A piece of artwork highlighting creativity, colors, and artistic expression.",
  },
  {
    id: 24,
    src: "/static/images/group.webp",
    photographer: "Efrem Efre",
    alt: "Group",
    price: 0,
    description:
      "A group of people enjoying time together, full of joy and connection.",
  },
  {
    id: 25,
    src: "/static/images/food2.webp",
    photographer: "Efrem Efre",
    alt: "Food",
    price: 0,
    description:
      "A delicious meal presented beautifully, appealing to the senses.",
  },
  {
    id: 26,
    src: "/static/images/travel2.webp",
    photographer: "Efrem Efre",
    alt: "Travel",
    price: 0,
    description:
      "An inspiring travel scene capturing adventure and exploration.",
  },
  {
    id: 27,
    src: "/static/images/water.webp",
    photographer: "Efrem Efre",
    alt: "Water",
    price: 0,
    description:
      "Calm, clear water reflecting its surroundings, evoking serenity and balance.",
  },
  {
    id: 28,
    src: "/static/images/nature.webp",
    photographer: "Efrem Efre",
    alt: "Nature",
    price: 40,
    description:
      "A scenic nature view showcasing unspoiled landscapes and natural beauty.",
  },
  {
    id: 29,
    src: "/static/images/food1.webp",
    photographer: "Efrem Efre",
    alt: "Food",
    price: 0,
    description:
      "A visually appealing dish, perfectly plated and ready to enjoy.",
  },
  {
    id: 30,
    src: "/static/images/technology.webp",
    photographer: "Efrem Efre",
    alt: "Technology",
    price: 0,
    description:
      "A technology-themed image representing innovation and modern progress.",
  },
  {
    id: 31,
    src: "/static/images/desert.webp",
    photographer: "Alice M",
    alt: "Technology",
    price: 5,
    description: "A nature-themed image representing desrt and progress.",
  },
  {
    id: 32,
    src: "/static/images/greece.webp",
    photographer: "Frank Muller",
    alt: "Technology",
    price: 50,
    description: "A nature inspied pictured featuring greece",
  },
];
