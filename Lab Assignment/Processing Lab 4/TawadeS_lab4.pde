PShape starship;

float easing = 0.05;
float offset = 0;

void setup() {
 size(800, 800);
 starship = loadShape("TawadeS_Starship.svg");
}
void draw() {
  float targetOffset = map(mouseY, 0, height, -40, 40);
  offset += (targetOffset - offset) * easing;
  shape(starship, 85 + offset, 65);
}
