Part 2 agonised me - I originally tried some lowest-common-multiple type thing
to avoid getting to the point where after a delay of N ps, all the scanners are
back in the top position and we're basically just looping. Clearly got this
wrong as it was stopping after ~42,000

I basically gave up until Kinnison told me his solution took a minute to run
with optimised Rust and the answer was in the region of 4 million ps - I
trusted my code, changed the maximum value to something in the region of 100
million, and let it run free (under "nice -n 19" because it made my laptop
crawl). After 3 minutes, I had an answer in the same sort of region :)
