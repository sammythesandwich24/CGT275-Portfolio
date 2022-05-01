PImage img;
PShape starship;

float easing = 0.05;
float offset = 0;

void setup() {
 size(800, 800);
 img = loadImage("UnionGateway.png");
 starship = loadShape("TawadeS_Starship.svg");
}
void draw() {
  image(img, 0, 0);
  float targetOffset = map(mouseY, 0, height, -40, 40);
  offset += (targetOffset - offset) * easing;
  shape(starship, 85 + offset, 65);
}
