# Take A Breath

![Website Mockup](documents/read-me/)

[Live Website](https://take-a-breath-a26c57655e5e.herokuapp.com/)  
[GitHub Repository](https://github.com/DaniqueJ-R/milestone_proj_3)

---

## About

Take A Breath is a minimalist, full-stack web application built to spread kindness and positivity online. Inspired by the concept of a message in a bottle, it allows users to submit short, anonymous motivational quotes or kind messages. When someone visits the site, they receive a randomly selected note written by another user. The project is designed with accessibility and user experience in mind, offering a calm, focused space where people can pause, reflect, and feel supported—no accounts or logins needed. All messages are stored in a secure database and can be added or removed via a simple, user-friendly interface.

---

## Table of Contents

- [User Experience](#user-experience)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
- [Features](#features)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)

---

## User Experience

### Strategy

This site is aimed at overall internet users seeking comforting and motivational quotes, and in turn would like to contribute to the positive pile of affirmations. The primary goals are to:

- Anyone is able to view notes at any time on the site
- atmosphere of site is changeable to allow for a more calming experience
- Logged in users are able to add, edit, and delete their own notes

**User Stories:**

- As a user, I want to be notified if my message contains harmful language and be prevented from submitting it, so the platform stays safe and positive.
- As a user, I want to log in so that I can edit and delete my own notes, ensuring I stay in control of my content.
- As a logged-in user, I want to be able to write and save a new note, so that I can express my thoughts and keep track of them.
- As a user, I want to click back and next buttons to flip through quotes so I can explore multiple uplifting messages at my own pace.
- As a user, I want to change the site’s theme to match calming environments (space, sea, forest, etc.) so I can choose the mood that helps me feel relaxed. 
- As a user, I want my quote to appear on a sticky note design so the messages feel personal, warm, and handwritten.
- As a user, I want the background white noise to match the theme I select, so the visuals and audio work together to create a relaxing atmosphere.
- As a user, I want new notes to stack on top of each other like real sticky notes, so the experience feels visually tactile and comforting.
- As a user, I want to include my name or have it show "Anonymous" if I leave it blank, so I can choose my level of visibility.
- As a user, I want to post a quote to a specific category whenever I want, so that I can share affirmations and organize them by mood.
- As a user, I want to filter messages by emotional categories like stress or grief, so I can read messages that match how I feel.
- As a user, I want to decorate my sticky note with cute stickers by dragging and dropping them, so I can add a personal, expressive touch.
- As a user, I want to like notes that resonate with me, so I can express appreciation and help highlight notes that others may also enjoy.

### Primary Strategic Aims

- A safe and supportive online space – Create a calm, minimalist environment where users can share and receive positive, anonymous notes without fear of negativity or harmful content.

- Increase engagement and return visits – Encourage users to keep interacting with the platform by offering a refreshing experience each time they visit, with new random motivational notes.

- Provide an alternative solution for wellbeing – Offer a simple, digital alternative to social media feeds by focusing solely on kindness and positivity, helping users pause, reflect, and boost their mood.

---

## Scope

### In-Scope Features

- Responsive homepage with eligable affirmations
- Navigation menu linking to all other main pages 
- interactive atmosphere changer with matching white noise
- Log in page with data protection
- Sign up page for new members
- CRUD for logged in users and their custom notes
- Note moderation for certain language
- Interactive interface for all screen size
- Social media integration

### Out-of-Scope Features

- Mood filter to seperate note types
- Report button under notes section
- About us Page with contact form
- Interacive stickers added to notes when written
- Like button for each note on homepage
- Pictures section to view photos of animals, relaxing sceens, etc

### Scrapped Features

- Users creating notes when not logged in

---

## Structure

- **Homepage:** Sticky Notes design, all approved quotes displayed, back and forth buttons, 'Pick a note' and 'Write a note' headers
- **Write Note Page:** Detailed explination how section works, Sticy Note design continued, reset and submit buttons, pop-up to inform if note auto or manually approved
- **My Notes Page:** all users notes, Pending and Approved sections, Edit and Delete Button for every note. 
- **Global Elements:** Consistent nav menu and sidebar menu for mobile and desktop respecivly, audio toggle, footer with licence, and social links

---

## Skeleton

Wireframes were designed for mobile, tablet, and desktop responsiveness.

- Homepage Wireframes - 
[Desktop,](documents/read-me/desktop-1-homepage.png)
[Tablet,](documents/read-me/tablet-1-homepage.png)
[Phone](documents/read-me/phone-1-homepage.png)
- Writing Page Wireframes - 
[Desktop,](documents/read-me/desktop-2-writing.png)
[Tablet,](documents/read-me/tablet-2-writing.png)
[Phone](documents/read-me/phone-2-writing.png)
- My Notes Wireframes - 
[Desktop,](documents/read-me/desktop-3-dashboard.png)
[Tablet,](documents/read-me/tablet-3-dashboard.png)
[Phone](documents/read-me/phone-3-dashboard.png)

Responsive breakpoints considered:
- <576px - Phone
- ≥576px - Tablet and desktop

---

## Surface

### Visual Design

- Custom matching colourscheem for Sea (Blue Tones), Sunset(Orange-Purple Tones), Cosmic (purple Tones), and Forest(Green Tones)  or calming color palette
- Accessible typography for overall site
- Curved hadwritten typography for notes displayed
- Simple, welcoming layout

### Color Scheme

Colors picked via tools like IMAGECOLORPICKER and contrast-tested for accessibility.

### Media

- All images and audio include alt tags
- Colour themes inspured by [Coolors](https://coolors.co/)
- Audio embedded from sources like [Freesound](https://freesound.org/)
- Logo sourced from free platform [Creative Fabrica](https://www.creativefabrica.com/product/take-a-deep-breath-retro-svg/)

---

## Features

### Universal Features

#### Navigation Menu
Responsive nav bar for mobile and matching Sidebar for tablet and desktop. Contains the following:
- Site logo
- Log in / Sign up (if not logged in)
- My Notes (only if loogged in)
- Pick notes
- Write Notes
- Pictures (disabled)
- Atmosphere Changer
- Audio Toggle
- Social Media 

#### Footer
Contains copyright for site including year. 

#### Metadata
Optimized meta titles and descriptions for better SEO.

#### Confirmation Page
Displays a success message after form submission.

### Page-Specific Features

#### FAQ Accordion
Compact collapsible sections with common user questions.

#### Inquiry/Booking Form
Fields: Full name, email, phone, reason, date, message

---

## Testing

### Code Validation

- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://jigsaw.w3.org/css-validator/)

### Browser Testing

Tested across major browsers to ensure consistency:
- Navigation
- Fonts
- Form functionality
- Responsiveness

### Device Testing

Tested on:
- Desktop
- Tablet
- Mobile

### Accessibility

- Tested using [WAVE](https://wave.webaim.org/)
- Resolved contrast issues and heading structure

### User Stories

Each user story tested to ensure functionality matches expectations.

### Performance

Lighthouse used to improve image sizes, font loading, and rendering.

---

## Bugs

### Fixed

- Resized large images to improve performance
- Corrected nav-menu dropdown alignment
- Fixed font overflow in pricing table
- Re-aligned class sections using Bootstrap
- Resolved carousel size issue
- Fixed accordion tabs opening simultaneously
- Adjusted social media icon placement and responsiveness

### Remaining

- Nav-menu on smaller devices does not collapse after link click (to be fixed)

---

## Deployment

### Live Site

Deployed using GitHub Pages:

1. Go to repository Settings > Pages
2. Set source to `main` branch
3. Save and visit the generated link

[Live Website Link](https://your-deployment-link.com)

### How to Fork & Clone

1. Set up Git and GitHub authentication
2. Visit [Original Repo](https://github.com/your-username/your-repo-name)
3. Click "Fork"
4. In your new fork, click "Code" > Clone with HTTPS or SSH
5. Run `git clone <URL>` in your terminal

More info: [GitHub Docs - Fork a Repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

---

## Credits

- **Images:** [Freepik](https://freepik.com)
- **Wireframes:** [Balsamiq](https://balsamiq.com/wireframes)
- **Video:** [InVideo](https://ai.invideo.io/)
- **Tools Used:** HTML5, CSS3, Bootstrap, JavaScript, Chrome DevTools, Git, GitHub
ing
