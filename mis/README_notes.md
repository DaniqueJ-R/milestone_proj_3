Forgot about page for wireframe, added after- no need. scrapped
Make new wireframe for log in

Lnks 
How to use react - https://www.youtube.com/watch?v=SqcY0GlETPk (check/ didnt do it)

Scrapped ideas - 
report section
about us section
stickers
Likes?

Bugs encounteres - 

Overall
installing gunicorn, summernote and heroku

Heroku
Deployment to Heroku - ffix

JAVA
Function allowing notes to flip -fix
function to then change colour of note and background at the same time - fix
Connecting notes to display on sticky - fix


Python
updated names and had to wipe db to reformat change - fix
Getting Static code to read correctly in django - fix

Password done page to show if password is in the system, but shwing email is not in system for all email - still

CSS

HTML

Spoke to Mentre and now changing it to where user has to log in to crate note so they can delete/edit tthemself
Now that thats changign, might lookk into liking notes?

Trouble with Log in set up, taking me straight to log in but not findgin tempate - fixed by adding quote/login.html to url

Add {% blocktrans %} and {% trans 'Register:' %} - translation for text to user language- later on if possible

Decided to change function of badword Json so db can be updated anytime with new banned words

Added audio, but sometimes js does not catch which file to play and logs error - fixed?

Drop down not fully working, reloading page and showing new note but not filtering as it should. 

MAking sidebr be notmal nav bar, I figured out its the display flex in the body thats making it stay to the side like that, ave to remove that when mobile szed and it should work? Nav bar keeps taking up sidebar space - fixed

Not fixed - Superuser dashbord not showing "No pending notes" Message but normal user dashbod shoing it. BEfore code was only showing "no pending notes" but not showing the notes tat wre pending. Not all normal sers see "no pending"

Updating to debug false causing trouble, not reading static files -  Fixed by deleting static collect files, turning to true, remove server then run collect againi

Bug - not fixed? - Added collaps to each theme on mobile navbar, but once theme selected, nav not closed properly so you have to press it again to correct it. Removed from dropdown as it was clashing with JS, and Decided that Users may want tto go through more than one theme at once, and may be annoying to always reoopn.+

Notified that if music is playing the change theme option does not show, and you cannot shange the theme until the music is paused. 

Main background and notes load on inital loading of page then flicks to uersonalized theme afer a sec9

Testing shows tat user can create new accout with same email - fix?

Save changes not taking you back to main page?