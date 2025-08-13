console.log("Script loaded");

document.addEventListener("DOMContentLoaded", () => {
  // const affirmations = [
  //   "You are enough.",
  //   "You are strong.",
  //   "This too shall pass.",
  //   "Peace begins with you.",
  //   "Your potential is endless."
  // ];

  const themes = ["space", "sea", "forest", "sunset", "mountains", "garden"];

  let audioEnabled = false;
  let displayedNotes = []; // Array of current notes shown (max 5)

  const container = document.getElementById("notes-container");
  const addBtn = document.getElementById("addAffirmation");
  const backBtn = document.getElementById("backAffirmation");
  const themeSelector = document.getElementById("themeSelector");
  const toggleAudioBtn = document.getElementById("toggleAudio");
  const themeAudio = document.getElementById("themeAudio");
  const emptyMsg = document.getElementById("emptyMessage");

  // Create a sticky note element
  function createStickyNote(text, index, theme) {
    const note = document.createElement("div");
    note.className = `sticky-note theme-${theme}`;

    // Rotation and offsets like React example
    const rotation = ((index * 3) % 12) - 6;
    const offsetX = ((index * 2) % 8) - 4;
    const offsetY = ((index * 1.5) % 6) - 3;

    note.style.setProperty("--rotation", `${rotation}deg`);
    note.style.setProperty("--offsetX", `${offsetX}px`);
    note.style.setProperty("--offsetY", `${offsetY}px`);

    note.style.transform = `rotate(${rotation}deg) translate(${offsetX}px, ${offsetY}px)`;
    note.style.zIndex = 40 - index; // top note on top
    note.textContent = text;

    return note;
  }

  // Render all displayed notes (up to 5)
  function renderNotes() {
    container.innerHTML = "";

  if (emptyMsg) {
  if (displayedNotes.length === 0) {
    emptyMsg.classList.remove("hidden");
  } else {
    emptyMsg.classList.add("hidden");
  }
}

    const theme = themeSelector.value || "space";

    displayedNotes.forEach((noteText, i) => {
      const note = createStickyNote(noteText, i, theme);
      container.appendChild(note);
    });
  }

  // Add a new random affirmation to stack, max 5 notes
  
  //might delete this - all affirmations
  // addBtn.addEventListener("click", () => {
  //   // Pick a random affirmation that isn't currently displayed if possible
  //   let available = affirmations.filter(a => !displayedNotes.includes(a));
  //   let nextAffirmation;

  //   if (available.length === 0) {
  //     // All displayed, just pick random from all
  //     nextAffirmation = affirmations[Math.floor(Math.random() * affirmations.length)];
  //   } else {
  //     nextAffirmation = available[Math.floor(Math.random() * available.length)];
  //   }
  // displayedNotes.unshift(nextAffirmation); // new note on top


  addBtn.addEventListener("click", () => {
  let available = notes.filter(a => !displayedNotes.includes(a));
  let nextNote;

  if (available.length === 0) {
    nextNote = notes[Math.floor(Math.random() * notes.length)];
  } else {
    nextNote = available[Math.floor(Math.random() * available.length)];
  }

    displayedNotes.unshift(nextNote);
   
    // Limit stack to 5
    if (displayedNotes.length > 5) {
      displayedNotes.pop();
    }

    renderNotes();

  // Animation for new note
  // Add animation class to top note
  const topNote = container.firstElementChild;
  if (topNote) {
    topNote.classList.add("new-note");
    setTimeout(() => topNote.classList.remove("new-note"), 300);
  }
});



  // Remove top note on Back button
  backBtn.addEventListener("click", () => {
    if (displayedNotes.length > 0) {
      displayedNotes.shift();
    }
    renderNotes();
  });

  // Theme change updates all notes and body background
  themeSelector.addEventListener("change", () => {
    document.body.className = `theme-${themeSelector.value}`;
    renderNotes();

    if (audioEnabled) {
      themeAudio.src = `audio/${themeSelector.value}.mp3`;
      themeAudio.play();
    }
  });

  // Toggle audio
  toggleAudioBtn.addEventListener("click", () => {
    audioEnabled = !audioEnabled;
    if (audioEnabled) {
      themeAudio.src = `audio/${themeSelector.value}.mp3`;
      themeAudio.play();
    } else {
      themeAudio.pause();
    }
  });

  // Initial render (empty stack)
  renderNotes();
});

// addBtn.addEventListener("click", () => {
//   // Pick a random affirmation that isn't currently displayed if possible
//   let available = affirmations.filter(a => !displayedNotes.includes(a));
//   let nextAffirmation;

//   if (available.length === 0) {
//     nextAffirmation = affirmations[Math.floor(Math.random() * affirmations.length)];
//   } else {
//     nextAffirmation = available[Math.floor(Math.random() * available.length)];
//   }

//   displayedNotes.unshift(nextAffirmation); // new note on top

//   if (displayedNotes.length > 5) {
//     displayedNotes.pop();
//   }

//   renderNotes();

//   // Add animation class to top note
//   const topNote = container.firstElementChild;
//   if (topNote) {
//     topNote.classList.add("new-note");

//     // Remove class after animation completes (300ms)
//     setTimeout(() => {
//       topNote.classList.remove("new-note");
//     }, 300);
//   }
// });


