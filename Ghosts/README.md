The GhostPost Machine™ is a website where people can anonymously post Boasts or Roasts of whatever they want. Like most services, there is a character limit: 280 characters. We are deliberately not dealing with logins, as that is outside the scope of the project (and beyond our time constraints). 

A front end is necessary to make this work, though it doesn't have to be pretty -- invest as much time as you want into it.

Back end:

One model to represent both boasts and roasts
Boolean to tell whether it's a boast or a roast
Charfield to put the content of the post in
integer field for up votes
integer field for down votes
datetimefield for submission time
Front end: 

Homepage that displays boasts and roasts, sorted by time submitted
buttons to filter the content by either boasts or roasts, sorted by time submitted
upvote and downvote buttons for each boast and roast
when clicked, these buttons affect the numbers on the relevant post appropriately
ability to sort content based on number of votes
page to submit a boast or a roast
 