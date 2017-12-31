# code-snippets
This repository gathers diverse tiny challenges I encountered on YouTube, Facebook, Twitter (or other social media) that I found interesting enough to share

## 0001 - Micmaths 9-digit Enigma

Mickaël Launay alias Micmaths is a French 250K-subscriber YouTuber. As his channel is now 10 years old, he decided to organize a YouTube Live in November 2017. During this live, he challenged us with an enigma: find the only solution to `42 x _ _ _ = _ _ _ _` so that each `_` is a digit and digits from 1 to 9 should appear only once in the equation. Here's the link: https://www.youtube.com/watch?v=vYa930zDtz4&t=13m
- Finding the solution to this enigma was actually pretty easy because as 2 and 4 are already taken, we naively try out `42 * 135` then `42 * 136` then `42 * 137` and finally we find after 4 attempts that `42 * 138` is the solution, without actually thinking about the problem in detail. I still decided to implement a naive implementation of the solution to this enigma by also looking for other starting numbers than just `42`
- Note: I'm aware that my solution is pretty naive as it doesn't apply basic mathematics rules like multiples (e.g. if 2 is taken and is the last digit of the first number then there is no point in multiplying that first number by a second number that ends with 6, because `2 * 6 = 12` (same ending digit))

## 0002 - The perfect city

Codefights is an interesting website with challenges to solve so that recruiters can later connect with you if you get a good score. Once you submit your code, it is tested against several known and unknown tests to check if it handles all possible cases.
On this website I encountered the following challenge under the `Uber Bot` category:
- consider a city that is a perfect infinite square grid, hence each road can be represented as straight lines defined by `x = n` or `y = n` where `n` is an integer
- a car is going from point A to point B and the goal of the challenge is to determine the length of the shortest path between these two points
  - let's say the departure point (A) is `[0.4, 1]` and the destination point (B) is `[0.9, 3]` then the output should be `2.7` as visible on the diagram below
- Note: in the challenge, it was guaranteed that every coordinate is positive. Also, it is easy to notice that in a `[x ; y]` couple of coordinates, at least one of the two coordinates is an integer (otherwise, the car would be off the road)

### Diagram

- A: `[0.4, 1]`
- B: `[0.9, 3]`
- The length of the shortest path, drawn as `#`, is: `2 [y-axis] + 0.6 [corresponding to 1 - 0.4 for A] + 0.1 [corresponding to 1 - 0.9 for B]` = `2.7`

```
 ...                    ...
3 +----B##------+------+
  |      #      |      |
  |      #      |      |
2 +------#------+------+
  |      #      |      |
  |      #      |      |
1 +--A####------+------+
  |      |      |      |
  |      |      |      |
0 +------+------+------+ ...
  0 0.4  1      2      3
```
