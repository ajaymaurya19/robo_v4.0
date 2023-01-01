int x;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  while (!Serial.available());
  nvidia send data servo angle 
  #send data to nvidia wheels+ ultrosonic+ 
  x = Serial.readString().toInt();
  Serial.print(x + 1);
}