console.log("Script loaded");

const themes = ["space", "sea", "forest", "sunset", "mountains", "garden"];

let audioEnabled = false;
let displayedNotes = []; // Array of current notes shown (max 5)
let history = [];

const container = document.getElementById("notes-container");
const addBtn = document.getElementById("addAffirmation");
const backBtn = document.getElementById("backAffirmation");
const themeSelector = document.getElementById("themeSelector");
const toggleAudioBtn = document.getElementById("toggleAudio");
const themeAudio = document.getElementById("themeAudio");
const emptyMsg = document.getElementById("emptyMessage");

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

  const theme = themeSelector?.value || "space";

  displayedNotes.forEach((noteText, i) => {
    const note = createStickyNote(noteText, i, theme);
    container.appendChild(note);
  });
}


// Create sticky note element
function createStickyNote(content, index, theme) {
  const noteDiv = document.createElement("div");
  noteDiv.className = `sticky-note theme-${theme}`;
  noteDiv.innerHTML = `<p>${content}</p>`;

  // Random rotation and offsets for stacking effect
  const rotation = Math.random() * 12 - 6; // -6 to +6 deg
  const offsetX = Math.random() * 10 - 5;  // -5px to +5px
  const offsetY = Math.random() * 10 - 5;  // -5px to +5px

  noteDiv.style.transform = `rotate(${rotation}deg) translate(${offsetX}px, ${offsetY}px)`;
  noteDiv.style.zIndex = 40 - index; // top note on top

  return noteDiv;
}

// Show a random note
function showRandomNote() {
  if (notes.length === 0) return;

  const available = notes.filter(a => !displayedNotes.includes(a));
  const nextNote = available.length > 0 
    ? available[Math.floor(Math.random() * available.length)]
    : notes[Math.floor(Math.random() * notes.length)];

  // Add current notes to history
  if (displayedNotes.length > 0) {
    history.push([...displayedNotes]);
  }

  displayedNotes.unshift(nextNote);

  if (displayedNotes.length > 5) displayedNotes.pop(); // max 5
  renderNotes();

  // Animate top note
  const topNote = container.firstElementChild;
  if (topNote) {
    topNote.classList.add("new-note");
    setTimeout(() => topNote.classList.remove("new-note"), 300);
  }
}

// Go back to previous note
function goBack() {
  if (history.length === 0) return;

  displayedNotes = history.pop();
  renderNotes();
}

// Theme & audio handling
themeSelector?.addEventListener("change", () => {
  document.body.className = `theme-${themeSelector.value}`;
  renderNotes();

  if (audioEnabled) {
    themeAudio.src = `audio/${themeSelector.value}.mp3`;
    themeAudio.play();
  }
});

toggleAudioBtn?.addEventListener("click", () => {
  audioEnabled = !audioEnabled;

  if (audioEnabled) {
    themeAudio.src = `audio/${themeSelector.value}.mp3`;
    themeAudio.play();
  } else {
    themeAudio.pause();
  }
});

// Buttons
addBtn?.addEventListener("click", showRandomNote);
backBtn?.addEventListener("click", goBack);

// Initial page load
document.addEventListener("DOMContentLoaded", () => {
  if (notes.length > 0) {
    const randomIndex = Math.floor(Math.random() * notes.length);
    displayedNotes.push(notes[randomIndex]); // first note
    renderNotes();
  }
});


// Form submission handling
const form = document.getElementById('quoteForm');
const popup = document.getElementById('popup');

form.addEventListener('submit', async (e) => {
    e.preventDefault(); // prevent normal submission

    const formData = new FormData(form);

    try {
        const response = await fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        });

        const data = await response.json();

        if (response.ok) {
            showPopup(data.message);
            form.reset(); // ready for next quote
        } else {
            showPopup(Object.values(data.errors).join(' '), true);
        }

    } catch (error) {
        console.error('Error submitting quote:', error);
        showPopup('An unexpected error occurred.', true);
    }
});

// Function to show popup
function showPopup(message, isError = false) {
    popup.textContent = message;
    popup.style.background = isError ? '#ffcccc' : '#fffae6';
    popup.style.borderColor = isError ? '#ff0000' : '#ffd700';
    popup.classList.remove('hidden');

    setTimeout(() => popup.classList.add('hidden'), 3000);
}