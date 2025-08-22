console.log("Script loaded");

const themes = ["space", "sea", "forest", "sunset"];

let audioEnabled = false;
let displayedNotes = []; // Array of current notes shown (max 5)
let history = [];
let notes = []; // Global notes array
let currentTheme = "space"; // default

const container = document.getElementById("notes-container");
const addBtn = document.getElementById("addAffirmation");
const backBtn = document.getElementById("backAffirmation");
const themeSelector = document.getElementById("themeSelector");
const toggleAudioMobile = document.getElementById("toggleAudioMobile");
const toggleAudioSidebar = document.getElementById("toggleAudioSidebar");
const themeAudio = document.querySelectorAll("dropdown-content");
const emptyMsg = document.getElementById("emptyMessage");

// Load notes from server
async function loadNotes() {
  try {
    const response = await fetch("/notes-json/");
    notes = await response.json(); // Assign to global notes array
    console.log("Notes loaded:", notes);

    // Initialize first displayed note
    if (notes.length > 0) {
      const randomIndex = Math.floor(Math.random() * notes.length);
      displayedNotes.push(notes[randomIndex]);
      renderNotes();
    }
  } catch (error) {
    console.error("Error fetching notes:", error);
    notes = [];
  }
}

// // Initial page load
document.addEventListener("DOMContentLoaded", () => {
  // Load notes
  loadNotes();

  // Get the saved theme from localStorage
  const savedTheme = localStorage.getItem("selectedTheme") || "space"; 
  currentTheme = savedTheme; // update global tracker

  // Apply it to the body
  document.body.className = `theme-${currentTheme}`;

  // Mark the correct theme link as selected if it exists
  const link = document.querySelector(`#themeSelector a[data-value="${currentTheme}"]`);
  if (link) link.classList.add("selected");

  // Update audio source if audio is enabled
  themeAudio.src = `/static/audio/${currentTheme}.mp3`;
  if (audioEnabled) themeAudio.play();

// Apply theme to cards and buttons
  applyThemeToCards(currentTheme);

  console.log("Initial theme applied:", currentTheme);
});


// Render all displayed notes
function renderNotes() {
  container.innerHTML = "";

  if (emptyMsg) {
    if (displayedNotes.length === 0) {
      emptyMsg.classList.remove("hidden");
    } else {
      emptyMsg.classList.add("hidden");
    }
  }

  const selectedLink = document.querySelector(".dropdown-content a.selected");
  const theme = selectedLink
    ? selectedLink.getAttribute("data-value")
    : "space"; // default

  displayedNotes.forEach((noteText, i) => {
    const note = createStickyNote(noteText, i, theme);
    container.appendChild(note);
  });
}

// Create sticky note element
function createStickyNote(noteObj, index, theme) {
  const noteDiv = document.createElement("div");
  noteDiv.className = `sticky-note theme-${theme}`;
  noteDiv.innerHTML = `
        <p class="note-content">${noteObj.content}</p>
        <p class="note-author">— ${noteObj.name}</p>
    `;

  const rotation = Math.random() * 12 - 6;
  const offsetX = Math.random() * 10 - 5;
  const offsetY = Math.random() * 10 - 5;

  noteDiv.style.transform = `rotate(${rotation}deg) translate(${offsetX}px, ${offsetY}px)`;
  noteDiv.style.zIndex = 40 - index;

  return noteDiv;
}

// Show a random note
function showRandomNote() {
  console.log("Showing random note now");
  if (notes.length === 0) return;

  const available = notes.filter((a) => !displayedNotes.includes(a));
  const nextNote =
    available.length > 0
      ? available[Math.floor(Math.random() * available.length)]
      : notes[Math.floor(Math.random() * notes.length)];

  if (displayedNotes.length > 0) {
    history.push([...displayedNotes]);
  }

  displayedNotes.unshift(nextNote);

  if (displayedNotes.length > 5) displayedNotes.pop();
  renderNotes();

  const topNote = container.firstElementChild;
  if (topNote) {
    topNote.classList.add("new-note");
    setTimeout(() => topNote.classList.remove("new-note"), 300);
  }
  console.log("Random note shown:", nextNote);
}

// Go back to previous note
function goBack() {
  if (history.length === 0) return;

  displayedNotes = history.pop();
  renderNotes();
}

// Theme & audio handling
document.querySelectorAll("#themeSelector a").forEach((a) => {
  a.addEventListener("click", (e) => {
    e.preventDefault();

    // Remove 'selected' from any other link
    document
      .querySelectorAll("#themeSelector a")
      .forEach((link) => link.classList.remove("selected"));

    // Add 'selected' to the clicked link
    a.classList.add("selected");

    const value = a.getAttribute("data-value");
    currentTheme = value; // update global tracker
    document.body.className = `theme-${value}`;
    console.log("Theme changed to:", currentTheme);

    // Store in localStorage
    localStorage.setItem("selectedTheme", value);

    // Update notes
    if (document.getElementById("notes-container")) {
  renderNotes();
}

    // Update cards
    applyThemeToCards(value);
    console.log("Cards theme updated:", value);

    // Update audio source if audio is enabled
    if (audioEnabled) {
      themeAudio.src = `/static/audio/${value}.mp3`;
      themeAudio.play();
      console.log("Audio source updated:", themeAudio.src);
    } else {
      console.log("Audio is disabled, not updating source");
      themeAudio.pause();
    }
  });
});

// Apply theme to body, cards, and buttons
function applyThemeToCards(theme) {
  // Cards
  document.querySelectorAll(".note-card").forEach(card => {
    card.classList.remove("theme-space", "theme-sea", "theme-forest", "theme-sunset");
    card.classList.add(`theme-${theme}`);
  });

  // Buttons
  document.querySelectorAll(".btn-theme").forEach(btn => {
    btn.classList.remove(
      "btn-theme-space",
      "btn-theme-sea",
      "btn-theme-forest",
      "btn-theme-sunset"
    );
    btn.classList.add(`btn-theme-${theme}`);
  });

    // Write-page background
const bg = document.getElementById("sticky-note-writing");
if (bg) {
  bg.classList.remove("theme-space", "theme-sea", "theme-forest", "theme-sunset");
  bg.classList.add(`theme-${theme}`);
}
}


// Toggle audio on/off
[toggleAudioMobile, toggleAudioSidebar].forEach((el) => {
  el?.addEventListener("click", () => {
  audioEnabled = !audioEnabled;

  if (audioEnabled) {
    themeAudio.src = `/static/audio/${currentTheme}.mp3`;
    themeAudio.play();
    toggleAudioMobile.innerHTML = '<i class="fa-solid fa-volume-high"></i>';
    toggleAudioSidebar.innerHTML = '<i class="fa-solid fa-volume-high"></i>';
    console.log("Audio enabled:", themeAudio.src);
  } else {
    themeAudio.pause();
    toggleAudioMobile.innerHTML = '<i class="fa-solid fa-volume-xmark"></i>';
    toggleAudioSidebar.innerHTML = '<i class="fa-solid fa-volume-xmark"></i>';
    console.log("Audio disabled");
  }
});
});

// Buttons
addBtn?.addEventListener("click", () => {
  console.log("Add button clicked");
  showRandomNote();
});
backBtn?.addEventListener("click", () => {
  console.log("Back button clicked");
  goBack();
});

// Form submission handling
if (document.getElementById("quoteForm")) {
  const form = document.getElementById("quoteForm");
  const popup = document.getElementById("popup");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form);

    try {
      const response = await fetch(form.action, {
        method: "POST",
        body: formData,
        headers: { "X-Requested-With": "XMLHttpRequest" },
      });

      const data = await response.json();

      if (response.ok) {
        showPopup(data.message);
        form.reset();
      } else {
        showPopup(Object.values(data.errors).join(" "), true);
      }
    } catch (error) {
      console.error("Error submitting quote:", error);
      showPopup("An unexpected error occurred.", true);
    }
  });
}

// Function to show popup
function showPopup(message, isError = false) {
  popup.textContent = message;
  popup.style.background = isError ? "#ffcccc" : "#fffae6";
  popup.style.borderColor = isError ? "#ff0000" : "#ffd700";
  popup.classList.remove("hidden");

  setTimeout(() => popup.classList.add("hidden"), 3000);
}

// Dropdown functionality
document.querySelectorAll(".dropdown-header").forEach((header) => {
  header.addEventListener("click", () => {
    const content = header.nextElementSibling;
    content.classList.toggle("open");
  });
});
