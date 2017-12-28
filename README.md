# code-snippets
This repository gathers diverse tiny challenges I encountered on YouTube, Facebook, Twitter or other social media

## 0001 - Micmaths 9-digit Enigma

Mickaël Launay alias Micmaths is a French 250K-subscriber YouTuber. As his channel is now 10 years old, he decided to organize a YouTube Live in November 2017. During this live, he challenged us with an enigma: find the only solution to `42 x _ _ _ = _ _ _ _` so that each `_` is a digit and digits from 1 to 9 should appear only once in the equation. Here's the link: https://www.youtube.com/watch?v=vYa930zDtz4&t=13m
- Finding the solution to this enigma was actually pretty easy because as 2 and 4 are already taken, we naively try out `42 * 135` then `42 * 136` then `42 * 137` and finally we find after 4 attempts that `42 * 138` is the solution, without actually thinking about the problem in detail. I still decided to implement a naive implementation of the solution to this enigma by also looking for other starting numbers than just `42`
- Note: I'm aware that my solution is pretty naive as it doesn't apply basic mathematics rules like multiples (e.g. if 2 is taken and is the last digit of the first number then there is no point in multiplying that first number by a second number that ends with 6, because `2 * 6 = 12` (same ending digit)
