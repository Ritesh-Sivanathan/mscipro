// Create a canvas element
const canvas = document.createElement('canvas');
canvas.width = 800;
canvas.height = 600;
document.body.appendChild(canvas);
const ctx = canvas.getContext('2d');

// Define the Ball class
class Ball {
  constructor(x, y, radius, mass) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.mass = mass;
    this.vx = 0; // velocity along the x-axis
    this.vy = 0; // velocity along the y-axis
    this.ax = 0; // acceleration along the x-axis
    this.ay = 0; // acceleration along the y-axis
  }

  update() {
    // Apply gravity
    this.ay = 0.5; // acceleration due to gravity

    // Update velocity
    this.vx += this.ax;
    this.vy += this.ay;

    // Update position
    this.x += this.vx;
    this.y += this.vy;

    // Check for collision with the ground
    if (this.y + this.radius >= canvas.height) {
      this.y = canvas.height - this.radius;
      this.vy *= -0.8; // reverse velocity and apply some restitution
    }
  }

  draw() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.closePath();
    ctx.fillStyle = 'red';
    ctx.fill();
  }
}

// Create an array to hold the balls
const balls = [];

// Create some balls
balls.push(new Ball(100, 100, 20, 1));
balls.push(new Ball(200, 100, 30, 2));
balls.push(new Ball(300, 100, 40, 3));

// Animation loop
function animate() {
  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Update and draw each ball
  balls.forEach(ball => {
    ball.update();
    ball.draw();
  });

  // Request the next animation frame
  requestAnimationFrame(animate);
}

// Start the animation loop
animate();