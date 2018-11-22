# Projectile Solver
Solves physics projectile questions

# Usage
If you have a problem where you have an object being launched from a certain height at a certain angle at a certain velocity, this will preform an analysis on the movement. [If you need help, click here](#Documentation)

# Installation
open a terminal and type the following: <br>
[***REPLACE THE BOLDED TEXT WITH THE MOST RECENT VERSION***](#Versions)<br>
<pre>
curl https://codeload.github.com/Djsurry/projectile-solver/zip/v<b>1.0</b> --output projectile.zip<br>
unzip projectile.zip <br>
cd projectile-solver-<b>1.0</b> <br>
sudo ./setup
</pre>
***You might have to enter your password here***

# Documentation
## Inputs
The program asks for 3 inputs; `height`, `angle`, and `initial velocity`.
 1. Height
  - A number, in meters
  - The height at which the ball is being launched from
 2. Angle
  - a number, in degrees
  - the angle the ball is being launched from
 3. inital velocity
  - a number, in m/s

## Options
 1. Range
  - the total distance the projectile goes, along the x, in m
 2. Total time
  - the time it takes the ball to hit the ground, in s
 3. X and Y at specific time
  - Asks for an input, which is a time value in seconds. Must be within the range of possible times
  - Prints the X and Y at that time, in s
 4. X or Y at cooresponding distance
  - finds x at a specific y or y at a specific x
  - asks whether you want to find x from y or y from x
  - asks for a distance, in meters, must be in range
  - prints the other distance, in meters, of the other variable
 5. Maximum height
  - the max height the projectile reaches, in m
 6. Speed on impact with ground
  - prints the speed on impact with ground, in m/s
 7. Velocity on impact with ground
  - Prints velocity on impact with ground, in m with offset in degrees 


# Versions

[1.1](https://github.com/Djsurry/projectile-solver/releases/tag/v1.1)

[1.0](https://github.com/Djsurry/projectile-solver/releases/tag/v1.0)

[0.2](https://github.com/Djsurry/projectile-solver/releases/tag/v0.2)

[0.1](https://github.com/Djsurry/projectile-solver/releases/tag/v0.1)





