#include <Adafruit_NeoPixel.h>




#define PIN 6

Adafruit_NeoPixel neo = Adafruit_NeoPixel(120, PIN, NEO_GRB + NEO_KHZ800);




void setup() {

  // put your setup code here, to run once:
  pinMode(2, INPUT);
  neo.begin();
  neo.show();

}
void loop() {
  if(digitalRead(2)==HIGH){
    colorWipe(neo.Color(200,200,200),1);
  }
  else if(digitalRead(2)==LOW){
    colorWipe(neo.Color(0,0,0),1);
  }
}
void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<neo.numPixels(); i++) {
      neo.setPixelColor(i, c);
      neo.show();
      delay(wait);
  }
}
