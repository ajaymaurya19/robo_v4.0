//#include <ArduinoJson.h>
//#######################################
//#######################################
// GPIO mappings for Arduino Mega 2560
//#######################################
int m2_EL_Start_Stop=13;  //EL
int m2_Signal_hall=12;   // Signal - Hall sensor
int m2_ZF_Direction=11;  // ZF
int m2_VR_speed=10;    //VR

int m1_EL_Start_Stop=4;  //EL
int m1_Signal_hall=3;   // Signal - Hall sensor
int m1_ZF_Direction=2;  // ZF
int m1_VR_speed=5;    //VR

int CH1=8;
int CH3=9;  

const uint8_t ECHO_PIN = 6;
const uint8_t TRIGGER_PIN = 7;

const int sensorTimeout = 17493;


const float wheel_dimeter = 16.5;
const float wheel_circumference = 51.81;
float dis_l = 0.0F;
float dis_r = 0.0F;

//#######################################
int posl=0;int posr=0;int steps=0;int speed1=0;
int prevleft = 0; int countleft = 0;
int prevright = 0; int countright = 0;
int clicks_per_rotation = 100;
String direction1;
//#######################################


uint16_t echo(bool isCM) {
  long echoDuration;
  long distance;

  digitalWrite(TRIGGER_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(5);
  digitalWrite(TRIGGER_PIN, LOW);

  echoDuration = pulseIn(ECHO_PIN, HIGH, sensorTimeout); // Returns microseconds
  //echoDuration = pulseIn(ECHO_PIN, HIGH); // Returns microseconds

    distance = echoDuration / 29 / 2; // 29.15 microseconds per cm
  //delay(1);
  return distance;
}


void plus_left() {
  posl++; //count steps
  Serial.println(posl);
    
}
void plus_right() {
  posr++; //count steps
  Serial.println(posr);
    /*if(posr>=steps){
    wheelStop();
    posr=0;*/
  }
}


int readChannel(int channelInput, int minLimit, int maxLimit, int defaultValue){
  int ch = pulseIn(channelInput, HIGH, 30000);
  if (ch < 100) return defaultValue;
  return map(ch, 1000, 2000, minLimit, maxLimit);
}

void setup() {

// put your setup code here, to run once:
Serial.begin(115200);

//wheel 1 - Setup pin mode
pinMode(m1_EL_Start_Stop, OUTPUT);//stop/start - EL
pinMode(m1_Signal_hall, INPUT);   //plus       - Signal  
pinMode(m1_ZF_Direction, OUTPUT); //direction  - ZF

pinMode(m2_EL_Start_Stop, OUTPUT);//stop/start - EL
pinMode(m2_Signal_hall, INPUT);   //plus       - Signal  
pinMode(m2_ZF_Direction, OUTPUT); //direction  - ZF
digitalWrite(m1_EL_Start_Stop,LOW);
digitalWrite(m2_EL_Start_Stop,LOW);

pinMode(TRIGGER_PIN, OUTPUT);
pinMode(ECHO_PIN, INPUT);

pinMode(CH1, INPUT);
pinMode(CH3, INPUT);
    //Hall sensor detection - Count steps
    attachInterrupt(digitalPinToInterrupt(m1_Signal_hall), plus_left, CHANGE);
    attachInterrupt(digitalPinToInterrupt(m2_Signal_hall), plus_right, CHANGE);
}


void wheelStop(){
  digitalWrite(m1_EL_Start_Stop,LOW);
  digitalWrite(m2_EL_Start_Stop,LOW);
}

void wheelMoveForward(){
      analogWrite(m1_VR_speed, speed1);
      analogWrite(m2_VR_speed, speed1);

      digitalWrite(m1_ZF_Direction,LOW);
      digitalWrite(m2_ZF_Direction,HIGH);

      digitalWrite(m1_EL_Start_Stop,HIGH);
      digitalWrite(m2_EL_Start_Stop,HIGH);
}

void wheelMoveBackward(){
      analogWrite(m1_VR_speed, speed1);
      analogWrite(m2_VR_speed, speed1);

      digitalWrite(m1_ZF_Direction,HIGH);
      digitalWrite(m2_ZF_Direction,LOW);

      digitalWrite(m1_EL_Start_Stop,HIGH);
      digitalWrite(m2_EL_Start_Stop,HIGH);
}
void wheelMoveleft(){
      analogWrite(m1_VR_speed, speed1);
      analogWrite(m2_VR_speed, speed1);

      digitalWrite(m1_ZF_Direction,HIGH);
      digitalWrite(m2_ZF_Direction,HIGH);
   
      digitalWrite(m1_EL_Start_Stop,LOW);
      digitalWrite(m2_EL_Start_Stop,HIGH);
}
void wheelMoveright(){
      analogWrite(m1_VR_speed, speed1);
      analogWrite(m2_VR_speed, speed1);
 
      digitalWrite(m1_ZF_Direction,LOW);
      digitalWrite(m2_ZF_Direction,LOW);

      digitalWrite(m1_EL_Start_Stop,HIGH);
      digitalWrite(m2_EL_Start_Stop,LOW);
}
int ch1Value, ch3Value;
int map_ch1, map_ch3;
void loop() {
    uint16_t distanceCM = echo(true); // Report in cm = true.
    ch1Value = readChannel(CH1, -100, 100, 0);
    ch3Value = readChannel(CH3, -100, 100, 0);
    //map_ch1 = map(ch1Value, -100, 100, 0, 255);
    //map_ch3 = map(ch3Value, -100, 100, 0, 255);

    dis_l += ((countleft - prevleft) / (clicks_per_rotation) * wheel_circumference);
    dis_r += ((countright - prevright) / (clicks_per_rotation) * wheel_circumference);
    
    
    Serial.print("Distance: ");
    Serial.print(distanceCM);
    Serial.print("cm");
    Serial.print(", CH1: ");
    Serial.print(ch1Value);
    Serial.print(", CH3: ");
    Serial.print(ch3Value);
  if (distanceCM > 10) {
        if ((ch1Value >= 0 && ch1Value < 5 ) && (ch3Value <= 0 && ch3Value > -5 ))
        { 
          Serial.println("Stop");
          wheelStop();  
       }
      else if (ch1Value < 0 && ch3Value <= -5 )
        { 
          map_ch1 = map(ch1Value, -100, 0, 0, 255);
          map_ch3 = map(ch3Value, -100, -5, 0, 255);
          speed1 = 100;
          Serial.print("left");
          analogWrite(m1_VR_speed, map_ch1);
          analogWrite(m2_VR_speed, map_ch3);

          digitalWrite(m1_ZF_Direction,HIGH);
          digitalWrite(m2_ZF_Direction,HIGH);
   
          digitalWrite(m1_EL_Start_Stop,HIGH);
          digitalWrite(m2_EL_Start_Stop,HIGH);
          //wheelMoveleft();  
       }

       else if (ch1Value = 0 && ch3Value <= -5 )
        { 
          map_ch1 = map(ch1Value, -100, 0, 0, 255);
          map_ch3 = map(ch3Value, -100, -5, 0, 255);
          speed1 = 100;
          Serial.print("roll left");
          analogWrite(m1_VR_speed, map_ch1);
          analogWrite(m2_VR_speed, map_ch3);

          digitalWrite(m1_ZF_Direction,HIGH);
          digitalWrite(m2_ZF_Direction,HIGH);
   
          digitalWrite(m1_EL_Start_Stop,HIGH);
          digitalWrite(m2_EL_Start_Stop,HIGH);
          //wheelMoveleft();  
       }
     else if (ch1Value < 0 && ch3Value >= 5){
          map_ch1 = map(ch1Value, -100, 0, 0, 255);
          map_ch3 = map(ch3Value, 5, 100, 0, 255);
          Serial.print("right");
          analogWrite(m1_VR_speed, map_ch1);
          analogWrite(m2_VR_speed, map_ch3);
     
          digitalWrite(m1_ZF_Direction,LOW);
          digitalWrite(m2_ZF_Direction,LOW);
    
          digitalWrite(m1_EL_Start_Stop,HIGH);
          digitalWrite(m2_EL_Start_Stop,HIGH);
          //wheelMoveright();
       }

      else if (ch1Value = 0 && ch3Value >= 5){
          map_ch1 = map(ch1Value, -100, 0, 0, 255);
          map_ch3 = map(ch3Value, 5, 100, 0, 255);
          Serial.print("roll right");
          analogWrite(m1_VR_speed, map_ch1);
          analogWrite(m2_VR_speed, map_ch3);
     
          digitalWrite(m1_ZF_Direction,LOW);
          digitalWrite(m2_ZF_Direction,LOW);
    
          digitalWrite(m1_EL_Start_Stop,HIGH);
          digitalWrite(m2_EL_Start_Stop,HIGH);
          
         // wheelMoveright();
       }
     else if (ch1Value < 0 && (ch3Value > -5 && ch3Value < 5 )){
          map_ch1 = map(ch1Value, -100,0, 0, 255);
          //map_ch3 = map(ch3Value, -5, 5, 0, 255);
          Serial.print("Forward");
          analogWrite(m1_VR_speed, map_ch1);
          analogWrite(m2_VR_speed, map_ch1);
    
          digitalWrite(m1_ZF_Direction,LOW);
          digitalWrite(m2_ZF_Direction,HIGH);
    
          digitalWrite(m1_EL_Start_Stop,HIGH);
          digitalWrite(m2_EL_Start_Stop,HIGH);
         // wheelMoveForward();
       }
   
     else if (ch1Value >= 5 ){
          map_ch1 = map(ch1Value, 0, 100, 0, 255);
          //map_ch3 = map(ch3Value, -100, 100, 0, 255);
          Serial.print("Backward");
          analogWrite(m1_VR_speed, map_ch1);
          analogWrite(m2_VR_speed, map_ch1);
    
          digitalWrite(m1_ZF_Direction,HIGH);
          digitalWrite(m2_ZF_Direction,LOW);
    
          digitalWrite(m1_EL_Start_Stop,HIGH);
          digitalWrite(m2_EL_Start_Stop,HIGH);
          //wheelMoveBackward();
       }
       
     else
       {
        Serial.print("Stop");
        wheelStop();
       }
       }
    Serial.print(", Speed of motor 1:");
    Serial.print(map_ch1);
    Serial.print(". Speed of motor 2:");
    Serial.println(map_ch3);
     
        delay(50);

       prevleft = countleft;
       prevright = countright;

}
