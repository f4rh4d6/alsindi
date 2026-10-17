/* ============================================================
   THE SURVEY — Portfolio Data Store
   Single source of truth for site content & photography catalog.
   ============================================================ */

const DEFAULT_SITE_DATA = {
  "identity": {
    "name": "Alsindi",
    "role": "Landscape Photographer",
    "location": "Hamburg ",
    "instagram": "@itsalsindi",
    "instagramUrl": "https://instagram.com/itsalsindi",
    "email": "f.alsindi98@gmail.com",
    "phone": "+1 (555) 014-2833",
    "copyrightYear": "2026"
  },
  "home": {
    "eyebrow": "Architecture & Landscape \u2014 Survey 2026",
    "heroTitle": "Built\nWorlds,\nContested\nGround",
    "heroLede": "Photographs of structures that shape public life \u2014 from historic spires and modern corporate facades to the crowd barriers that partition our city squares.",
    "heroImage": "assets/images/04-hamburg-rathaus-barriers.jpg",
    "heroPlateTitle": "Hamburg Rathaus, Barrier Study",
    "heroPlateMeta": "Canon EOS \u00b7 50mm \u00b7 f/4.5 \u2014 2026",
    "featuredNote": "Survey Plate N\u00b001 / Public Space & Civic Boundaries"
  },
  "statement": {
    "eyebrow": "Artist Statement",
    "quote": "Every photograph is a decision about what deserves to be looked at. I choose the places where policy becomes concrete \u2014 and where public ground is quietly negotiated.",
    "quoteSource": "Field Notes, 2026",
    "paragraphs": [
      "I photograph the architecture of everyday life \u2014 the estates, overpasses, and quiet horizons that frame how we actually live. Each image is a small act of attention: a record of what the built world says about the people who move through it.",
      "Landscape, for me, is never empty. Every square, field, and shoreline carries the trace of a decision \u2014 a barrier, a zoning code, a planned perimeter. These photographs ask you to look at the ground beneath the view."
    ]
  },
  "about": {
    "eyebrow": "About the Photographer",
    "heading": "Alsindi",
    "portraitImage": "assets/images/portrait.svg",
    "portraitCaption": "Self, in the field \u2014 2025",
    "bioParagraphs": [
      "I'm an architectural and landscape photographer documenting built environments and their social consequences \u2014 the places where civic history meets contemporary boundaries.",
      "Working between digital systems and medium-format film, I print on heavy cotton rag paper. My work focuses on how public spaces are managed: from municipal squares guarded by crowd barriers to the layered skylines where Gothic spires compete with modern commercial towers.",
      "My photographs have been exhibited internationally and shared daily with a dedicated Instagram community, where followers contribute coordinates and historical context on contested urban sites."
    ],
    "gear": "Canon EOS R System \u00b7 Mamiya 7II \u00b7 35mm & 50mm Prime Lenses \u00b7 Hahnem\u00fchle Photo Rag 308gsm",
    "philosophy": "The camera is not an instrument of decoration; it is a survey tool. We measure the space we allow each other.",
    "stats": [
      {
        "value": "10",
        "label": "Years in the field"
      },
      {
        "value": "140+",
        "label": "Sites documented"
      },
      {
        "value": "52k",
        "label": "Instagram community"
      },
      {
        "value": "18",
        "label": "Exhibitions & Catalogs"
      }
    ]
  },
  "commentary": {
    "eyebrow": "Critical Context & Social Commentary",
    "title": "Structures of Division & Assembly",
    "quote": "Architecture is politics frozen into stone, mortar, and municipal setback lines.",
    "quoteAuthor": "A. Ford",
    "quoteSource": "On Public Space & Civic Perimeters",
    "essay": [
      {
        "subhead": "The Rathaus Barrier: Civic Space Partitioned",
        "text": "In front of the ornate neo-Renaissance facade of the Hamburg Rathaus, temporary galvanized steel barriers with reflective hazard markings control civilian movement. The juxtaposition is stark: opulent civic authority behind modular crowd control. The barrier is not an anomaly; it is the modern interface between the citizen and the state."
      },
      {
        "subhead": "Spires & Capital: The Skyline Survey",
        "text": "The blackened spire of St. Nikolai \u2014 left in ruins as an anti-war memorial \u2014 rises alongside modern corporate glass headquarters. In one frame, centuries of urban trauma, municipal renewal, and corporate dominance sit shoulder-to-shoulder under a cold northern sky."
      },
      {
        "subhead": "The Daily Survey on Instagram",
        "text": "A significant part of my practice lives on Instagram (@alsindi). Rather than treating social media as a commercial shop window, I run the feed as an open field notebook. Followers contribute coordinates, historical context on threatened landmarks, and firsthand accounts of living in the spaces I document."
      }
    ]
  },
  "contact": {
    "eyebrow": "Inquiries & Commissions",
    "title": "Let's Build Something",
    "lede": "Available for architectural documentation, editorial assignments, exhibition loans, and fine art print acquisitions worldwide.",
    "channels": [
      {
        "label": "Email",
        "value": "hello@alsindi.photo",
        "href": "mailto:hello@alsindi.photo",
        "note": "Editorial & Commission briefs"
      },
      {
        "label": "Instagram",
        "value": "@alsindi",
        "href": "https://instagram.com/alsindi",
        "note": "Daily field dispatches & DM"
      },
      {
        "label": "Phone",
        "value": "+1 (555) 014-2833",
        "href": "tel:+15550142833",
        "note": "Studio desk (Pacific Time)"
      },
      {
        "label": "Studio",
        "value": "Portland & Hamburg",
        "href": "https://maps.google.com/?q=Hamburg+Germany",
        "note": "European & US Field Base"
      }
    ]
  },
  "photos": [
    {
      "id": "01",
      "num": "N\u00b001",
      "title": "Hamburg Rathaus, Barrier Study",
      "year": "2026",
      "category": "commentary",
      "caption": "Galvanized crowd barriers with reflective hazard markings stand guard before the historic Hamburg City Hall.",
      "image": "assets/images/04-hamburg-rathaus-barriers.jpg",
      "meta": "Canon EOS \u00b7 50mm \u00b7 f/4.5 \u00b7 ISO 100"
    },
    {
      "id": "02",
      "num": "N\u00b002",
      "title": "St. Nikolai Spire & Urban Ridge",
      "year": "2026",
      "category": "architecture",
      "caption": "The blackened Gothic memorial spire rises above brick commercial blocks and corporate glass towers.",
      "image": "assets/images/01-hamburg-spire.jpg",
      "meta": "Canon EOS \u00b7 70mm \u00b7 f/5.6 \u00b7 1/500s"
    },
    {
      "id": "03",
      "num": "N\u00b003",
      "title": "Hamburg Skyline at High Noon",
      "year": "2026",
      "category": "architecture",
      "caption": "Layered rooftops and municipal spires under a clear Baltic sky \u2014 an architectural chronology.",
      "image": "assets/images/02-hamburg-skyline.jpg",
      "meta": "Canon EOS \u00b7 50mm \u00b7 f/8 \u00b7 1/320s"
    },
    {
      "id": "04",
      "num": "N\u00b004",
      "title": "Rooftop Horizons & Brick Facades",
      "year": "2026",
      "category": "architecture",
      "caption": "Terraces, mechanical shafts, and brick window grids in dialogue with historic church towers.",
      "image": "assets/images/03-hamburg-rooftops.jpg",
      "meta": "Canon EOS \u00b7 50mm \u00b7 f/6.3 \u00b7 1/400s"
    },
    {
      "id": "05",
      "num": "N\u00b005",
      "title": "Housing Block, East Quadrant",
      "year": "2024",
      "category": "architecture",
      "caption": "East quadrant of a 1970s estate, where 214 flats face a single wind direction.",
      "image": "assets/images/01-housing-block.svg",
      "meta": "Mamiya 7II \u00b7 80mm \u00b7 Tri-X 400"
    },
    {
      "id": "06",
      "num": "N\u00b006",
      "title": "Horizon Line, Low Tide",
      "year": "2023",
      "category": "landscape",
      "caption": "A single orange seam marks the tide line on a flat, industrial coast.",
      "image": "assets/images/02-horizon-line.svg",
      "meta": "35mm \u00b7 f/11 \u00b7 1/125s"
    },
    {
      "id": "07",
      "num": "N\u00b007",
      "title": "Scaffold Study, Site 9",
      "year": "2025",
      "category": "commentary",
      "caption": "A building wrapped in its own scaffolding \u2014 progress suspended mid-gesture.",
      "image": "assets/images/03-scaffold.svg",
      "meta": "Medium Format Digital \u00b7 50mm"
    },
    {
      "id": "08",
      "num": "N\u00b008",
      "title": "Viaduct over the A42",
      "year": "2022",
      "category": "architecture",
      "caption": "Six arches, one orange vehicle \u2014 the infrastructure that routes our days.",
      "image": "assets/images/04-viaduct.svg",
      "meta": "Mamiya 7II \u00b7 43mm \u00b7 f/8"
    },
    {
      "id": "09",
      "num": "N\u00b009",
      "title": "Field Curves, November",
      "year": "2024",
      "category": "landscape",
      "caption": "Plowing lines that follow the contour of the hill \u2014 and the boundary the planner drew.",
      "image": "assets/images/05-field-curves.svg",
      "meta": "35mm \u00b7 Tri-X 400 \u00b7 f/5.6"
    },
    {
      "id": "10",
      "num": "N\u00b010",
      "title": "Facade, Morning Light",
      "year": "2023",
      "category": "architecture",
      "caption": "A grid of windows, a grid of lives \u2014 the facade as a social diagram.",
      "image": "assets/images/06-facade-morning.svg",
      "meta": "Medium Format Digital \u00b7 90mm"
    },
    {
      "id": "11",
      "num": "N\u00b011",
      "title": "Coast, Low Tide",
      "year": "2024",
      "category": "landscape",
      "caption": "Two figures on a wide beach, the tide gone out to a hard orange horizon.",
      "image": "assets/images/08-coast.svg",
      "meta": "Mamiya 7II \u00b7 80mm \u00b7 f/11"
    },
    {
      "id": "12",
      "num": "N\u00b012",
      "title": "Perimeter",
      "year": "2024",
      "category": "commentary",
      "caption": "A chain-link survey of the boundary \u2014 what is kept in, what is kept out.",
      "image": "assets/images/12-perimeter.svg",
      "meta": "Mamiya 7II \u00b7 43mm \u00b7 f/16"
    }
  ]
};

function getSiteData() {
  return DEFAULT_SITE_DATA;
}
