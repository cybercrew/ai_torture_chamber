#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
#include <Servo.h>
Servo xaxis;
Servo yaxis;
void setup() 
{
  xaxis.attach(5);
  yaxis.attach(6);
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(1,1);
}
  

void loop()
{
  if(Serial.available())
  {
    String epic = Serial.readString();
    Serial.println(epic);
    if(epic[0]=='X')
    {
      epic.replace("X","");
      int xco = epic.toInt();
      Serial.println(xco);
      int x = map(xco, 0, 640, 0, 180);
      xaxis.write(x);
    }
    if(epic[0]=='Y')
    {
      epic.replace("Y","");
      int yco = epic.toInt();
      Serial.println(yco);
      int y = map(yco, 0, 480, 0, 120);
      yaxis.write(y);
    }
    
    //
    //
    delay(20);
    //xaxis.write(x);
  }
} 
